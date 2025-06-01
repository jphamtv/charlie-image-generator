from google.adk.agents import SequentialAgent, LlmAgent
from google.adk.models.lite_llm import LiteLlm

from . import prompt

GEMINI_FLASH_MODEL = "gemini-2.0-flash"
ANTHROPIC_CLAUDE_SONNET_MODEL = "claude-sonnet-4-20250514"

# --- PROMPT ENGINEERING PIPELINE: Writer → Reviewer → Refiner ---
# Each agent has a specialized role in optimizing prompts for Charlie LoRA

# 1. WRITER AGENT - Initial prompt creation
# Transforms user requests into structured prompts following LoRA guidelines
writer_agent = LlmAgent(
    name="prompt_writer",
    model=LiteLlm(model=ANTHROPIC_CLAUDE_SONNET_MODEL),
    instruction=f"""You are an expert Prompt Writer for CHRLE LoRA image generation.
        
        **Task:**
        Transform the user's request into a properly structured prompt following the Prompt Rules.
        
        **Approach:**
        - Extract key elements: action, setting, mood, style from user's message
        - If request is vague, make creative choices that align with user's intent
        - Use the template structure and medium hierarchy from the Prompt Rules
        - Reference the proven examples for inspiration, but create unique variations
        
        **Prompt Rules:**
        {prompt.PROMPT_RULES_WITH_EXAMPLES}
        
        **Output:**
        Generate only the complete prompt. No explanations or additional text.
        """,
    description="Writes initial prompt based on user's message.",
    output_key="initial_prompt",  # Stores result in shared state
)

# 2. REVIEWER AGENT - Quality assurance and technical validation
# Reviews prompts for adherence to LoRA rules and structural completeness
reviewer_agent = LlmAgent(
    name="prompt_reviewer",
    model=LiteLlm(model=ANTHROPIC_CLAUDE_SONNET_MODEL),
    instruction=f"""You are an expert Prompt Reviewer for CHRLE LoRA image generation.
        
        **Task:**
        Review the prompt from 'initial_prompt' for technical adherence to the Prompt Rules and structural completeness.
        
        **Focus Only On:**
        - Missing mandatory elements (chrle trigger word, basic features)
        - Incorrect template structure
        - Technical formatting issues
        - Unclear or contradictory descriptions
        
        **Do NOT flag content based on:**
        - Creative choices (accessories, props, scenarios)
        - Style preferences
        - Artistic interpretation
        - Subject matter (unless technically impossible)
        
        **Prompt Rules:**
        {prompt.PROMPT_RULES_ONLY}
        
        **Output Instructions:**
        If no major technical issues found, output EXACTLY: "No major issues found"
        If technical issues found, output 2-4 specific, actionable bullet points focusing only on technical/structural problems. Do NOT include explanatory text about what's correct.
        """,
    description="Reviews prompt for technical adherence to rules.",
    output_key="review_feedback",  # Stores feedback in shared state
)

# 3. REFINER AGENT - Final optimization and polishing
# Applies reviewer feedback to create the final optimized prompt
refiner_agent = LlmAgent(
    name="prompt_refiner",
    model=LiteLlm(model=ANTHROPIC_CLAUDE_SONNET_MODEL),
    instruction=f"""You are a Prompt Refiner.
        
        **Task:**
        Apply feedback from 'review_feedback' to improve the prompt from 'initial_prompt' while maintaining the original creative concept.
        
        **Process:**
        - If feedback is "No major issues found," return original prompt unchanged
        - Otherwise, apply specific suggestions using the Prompt Rules as reference
        - Preserve the core creative intent and mood
        
        **Prompt Rules:**
        {prompt.PROMPT_RULES_ONLY}
        
        **Output:**
        Only the refined prompt with no additional text.
        """,
    description="Refines prompt based on review comments.",
    output_key="final_prompt",  # Final result stored here
)

# --- SEQUENTIAL PIPELINE ORCHESTRATION ---
# SequentialAgent runs sub-agents in order, sharing state between them
# State flows: initial_prompt → review_feedback → final_prompt
prompt_pipeline_agent = SequentialAgent(
    name="prompt_pipeline_agent",
    sub_agents=[writer_agent, reviewer_agent, refiner_agent],  # Execution order
    description="Executes a sequence of prompt writing, reviewing, and refining.",
    # Final result available in state['final_prompt'] from refiner_agent
)

# Export for ADK tools - must be named 'root_agent' for AgentTool compatibility
root_agent = prompt_pipeline_agent
