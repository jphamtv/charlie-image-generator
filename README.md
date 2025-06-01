# Charlie Image Generator

AI microservice that transforms natural language requests into custom images of Charlie using multi-agent prompt optimization and FLUX.1 LoRA model.

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
- **Image Generation**: fal.ai FLUX.1 with custom LoRA
- **Deployment**: Docker containers

## Performance & Monitoring

The system includes comprehensive request tracking and performance monitoring:

<img width="575" alt="Screenshot 2025-06-01 at 11 24 30" src="https://github.com/user-attachments/assets/61ed86ee-cdb9-4864-8c3a-5a036415216f" />

*Screenshot showing agent communication flow and timing metrics*

Typical request flow: ~20 seconds

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
