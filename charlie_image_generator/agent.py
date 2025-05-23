from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.models.lite_llm import LiteLlm

from .prompt_pipeline_agent.agent import root_agent as prompt_pipeline_agent
from .tools.generate_image import generate_image

GEMINI_FLASH_MODEL = "gemini-2.0-flash"
ANTHROPIC_CLAUDE_HAIKU_MODEL = "claude-3-5-haiku-20241022"

prompt_pipeline_tool = AgentTool(
    agent=prompt_pipeline_agent
)

charlie_image_generator = LlmAgent(
    name="charlie_image_generator",
    # model=GEMINI_FLASH_MODEL,
    model=LiteLlm(model=ANTHROPIC_CLAUDE_HAIKU_MODEL),
    description="Generates images of Charlie the dog based on user requests",
    instruction="""You are the Charlie Image Generator coordinator. Your job is to generate images of Charlie the dog based on user requests.

**Your workflow:**
1. Call the prompt_pipeline_tool with the user's message to get a refined prompt
2. Call the generate_image function with the refined prompt to create the image
3. Return only the `image_url` to the user with no additional text

**Always use both tools in this exact sequence:** prompt_pipeline_tool → generate_image

**Handle any tool errors gracefully** and inform the user if image generation fails.""",
    output_key="image_url",
    tools=[prompt_pipeline_tool, generate_image],
)

root_agent = charlie_image_generator
