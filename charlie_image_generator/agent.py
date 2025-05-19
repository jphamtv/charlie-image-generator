
root_agent_model = MODEL_GEMINI_2_0_FLASH

root_agent - Agent(
    name="charlie_image_generator",
    model=root_agent_model,
    description="Main agent. Handles orchestrates sequential workflow",
    instructions="You are the main Image Generator Agent. Send user input to 'prompt_agent'"
    sub_agents=[prompt_agent, image_agent],
    output_key="img_url"    
)