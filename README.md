# Charlie Image Generator

AI microservice that transforms natural language requests into custom images of my dog Charlie using multi-agent prompt optimization and FLUX.1 model with custom LoRA.

## Architecture

**Multi-agent pipeline:** User request → Prompt refinement → Image generation → Response
- **Root Agent** (Claude Haiku): Orchestrates workflow  
- **Pipeline Agent** (Claude Sonnet): Writer → Reviewer → Refiner
- **Generate Tool**: Calls image generation API with optimized prompt

## Key Features

- Custom LoRA model for consistent character generation
- Request tracking with unique IDs for debugging
- Performance monitoring (20-30s typical generation time)
- Docker containerized with health checks
- Integrates with Apollo messaging app

## Technology Stack

- **Framework**: Google Agent Development Kit (ADK)
- **API**: FastAPI with async support
- **Models**: Claude Haiku (coordination) + Sonnet (prompt engineering)
- **Image Generation**: FLUX.1 with custom LoRA
- **Deployment**: Docker containers

## Performance & Monitoring

The system includes comprehensive request tracking and performance monitoring:

<img width="575" src="https://github.com/user-attachments/assets/61ed86ee-cdb9-4864-8c3a-5a036415216f" />

*Screenshot showing agent communication flow and timing metrics*

Typical request flow: ~20 seconds

## Live Demo
🔗 **Try it**: [helloapollo.chat](https://helloapollo.chat) - Message "Charlie" bot  

## Integration

Designed for Apollo messaging app integration:
- Container-to-container communication
- Real-time WebSocket notifications
- Automatic image upload to R2 storage

## Development Highlights

This project demonstrates:
- **Advanced AI orchestration** using Google's latest ADK framework
- **Production-ready microservice** architecture with proper logging and monitoring
- **Custom model integration** with fal.ai's FLUX pipeline and custom LoRA
- **Multi-agent coordination** for complex prompt engineering tasks

## Results Achieved
Built a multi-agent system that creates rich, optimized prompts and leverages custom LoRA training to generate consistent, high-quality images of Charlie.

**Real Charlie → Generated Charlie:**

<img width="400" src="https://github.com/user-attachments/assets/bc55a36c-d2ef-4ae3-9bb9-bf45aa25ec17" />
<img width="400" src="https://github.com/user-attachments/assets/2b821f43-494f-49c4-b6c0-59f9b5e34d2c" />

**Example Prompts:**
- Input: "Charlie as an astronaut"  
- Generated: "image of a small young chrle, one ear up, light brown nose, light brown eyes, brown fur, wearing a highly detailed white NASA space suit with reflective gold visor raised to show his face, floating weightlessly inside the International Space Station with Earth's blue marble visible through the cupola window behind him, soft ambient lighting from multiple sources creating gentle highlights on his suit and fur, intricate details of control panels and equipment surrounding him, atmospheric depth with bokeh effect on background elements, hyperdetailed fur texture visible around his helmet seal, sense of wonder and exploration, style of Norman Rockwell meets space realism"
