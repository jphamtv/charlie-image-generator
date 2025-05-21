from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from .prompt_pipeline_agent.agent import root_agent as prompt_pipeline_agent
from .tools.generate_image import generate_image

GEMINI_FLASH_MODEL = "gemini-2.0-flash"

prompt_pipeline_tool = AgentTool(
    agent=prompt_pipeline_agent
)

charlie_image_generator = LlmAgent(
    name="charlie_image_generator",
    model=GEMINI_FLASH_MODEL,
    description="Generates images of Charlie the dog based on client requests",
    instruction="""You are the Charlie Image Generator coordinator. Your job is to generate images of Charlie the dog based on user requests.

**Your workflow:**
1. When you receive a user message describing what they want to see with Charlie, call the prompt_pipeline_tool with that message to get a refined prompt
2. Once you have the refined prompt from the pipeline, call the generate_image function with that prompt to create the actual image
3. Return the image URL to the user

**Example user inputs:**
- "Charlie playing in the snow"
- "Charlie wearing a space suit"
- "Charlie in a medieval castle"

Always use both tools in sequence: first the prompt_pipeline_tool, then generate_image.""",
    output_key="image_url",
    tools=[prompt_pipeline_tool, generate_image],
)

root_agent = charlie_image_generator
