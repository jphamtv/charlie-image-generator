from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt_pipeline_agent
from .tools import generate_image

GEMINI_FLASH_MODEL = "gemini-2.5-flash-preview"

prompt_pipeline_tool = AgentTool(
    agent=prompt_pipeline_agent,
    description="Generates a high-quality prompt for creating images of Charlie",
)

charlie_image_generator = LlmAgent(
    name="charlie_image_generator",
    model=GEMINI_FLASH_MODEL,
    description="Generates images of Charlie the dog based on user requests",
    instruction="""You help generate images of Charlie the dog based on user requests.
    Process the user's message, generate an appropriate prompt using the prompt_pipeline tool,
    and then generate an image using the generate_charlie_image tool.""",
    output_key="image_url",
    tools=[prompt_pipeline_tool, generate_image],
)

root_agent = charlie_image_generator
