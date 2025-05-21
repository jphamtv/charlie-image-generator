from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from .prompt_pipeline_agent.agent import root_agent as prompt_pipeline_agent
from .tools import generate_image

GEMINI_FLASH_MODEL = "gemini-2.5-flash-preview"

prompt_pipeline_tool = AgentTool(
    agent=prompt_pipeline_agent
    # description="Generates a high-quality prompt for creating images of Charlie",
)

charlie_image_generator = LlmAgent(
    name="charlie_image_generator",
    model=GEMINI_FLASH_MODEL,
    description="Generates images of Charlie the dog based on client requests",
    instruction="""You help coordinate generating images of Charlie the dog based on client requests.
        **Workflow:**
        1. Pass client's input to the prompt_pipeline_tool to generate a prompt.
        2. Take the final prompt and generate an image using the generate_image tool.
        3. Pass the image_url back to the client.
        Process the client's input, generate an appropriate prompt using the prompt_pipeline tool,
        and then generate an image using the generate_charlie_image tool.""",
    output_key="image_url",
    tools=[prompt_pipeline_tool, generate_image],
)

root_agent = charlie_image_generator
