from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.models.lite_llm import LiteLlm

from .prompt_pipeline_agent.agent import root_agent as prompt_pipeline_agent
from .tools.generate_image import generate_image

GEMINI_FLASH_MODEL = "gemini-2.0-flash"
ANTHROPIC_CLAUDE_HAIKU_MODEL = "claude-3-5-haiku-20241022"

# Wrap the prompt pipeline agent as a tool for the root coordinator
# AgentTool allows one agent to call another agent as a function
prompt_pipeline_tool = AgentTool(
    agent=prompt_pipeline_agent
)

# Root coordinator agent - orchestrates the complete workflow
# Uses Haiku for fast decision-making and tool coordination
charlie_image_generator = LlmAgent(
    name="charlie_image_generator",
    model=LiteLlm(model=ANTHROPIC_CLAUDE_HAIKU_MODEL),
    description="Generates images of Charlie the dog based on user requests",
    instruction="""You are the Charlie Image Generator coordinator. Your job is to generate images of Charlie the dog based on user requests.

**Your workflow:**
1. Call the prompt_pipeline_tool and pass the user's message as-is to get a final_prompt
2. Call the generate_image tool with the final_prompt to create the image
3. Return only the `image_url` to the user with no additional text

**Always use both tools in this exact sequence:** prompt_pipeline_tool → generate_image

**Handle any tool errors gracefully** and inform the user if image generation fails.""",
    output_key="image_url",  # Stores final result in state['image_url']
    tools=[prompt_pipeline_tool, generate_image],  # Available function tools
)

# Export as root_agent for ADK compatibility
# Main entry point for the agent system
root_agent = charlie_image_generator
