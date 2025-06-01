# Charlie Image Generator

An AI-powered microservice that generates custom images of Charlie using a multi-agent architecture with Google's Agent Development Kit (ADK) and fal.ai's FLUX.1 model API.

## Overview

Charlie Image Generator transforms natural language requests into high-quality AI-generated images through a multi-agent prompt engineering pipeline. The system uses a custom LoRA (Low-Rank Adaptation) model trained on FLUX.1 model to generate consistent, personalized images of Charlie.

**Key Features:**
- Multi-agent prompt optimization pipeline
- Custom LoRA model for consistent generation of subject's likeness
- FastAPI microservice architecture
- Docker containerized deployment
- Integration with Apollo messaging app - www.helloapollo.chat

## Technology Stack

- **AI Framework**: Google Agent Development Kit (ADK)
- **Language Models**: Anthropic Claude (Haiku for coordination, Sonnet for prompt engineering pipeline)
- **Image Generation**: fal.ai FLUX.1 with custom LoRA
- **API Framework**: FastAPI with async support
- **Deployment**: Docker containers with production logging
- **Integration**: Apollo messaging app via internal networking

## Agentic Architecture

The system implements a hierarchical multi-agent design:

### Root Coordinator Agent
- **Model**: Claude 3.5 Haiku  
- **Role**: Orchestrates the complete workflow
- **Tasks**: Coordinates prompt pipeline agent → uses image generation tool → formats response

### Sequential Prompt Pipeline Agent
- **Model**: Claude Sonnet 4
- **Components**: Writer → Reviewer → Refiner sub agents
- **Purpose**: Transforms user requests into optimized prompts

**Agent Flow:**
1. **Writer Agent**: Converts user request into structured prompt following LoRA guidelines
2. **Reviewer Agent**: Analyzes prompt for technical compliance and completeness  
3. **Refiner Agent**: Applies feedback to optimize prompt quality
4. **Generate Tool**: Calls fal.ai API with custom LoRA model

## Performance & Monitoring

The system includes comprehensive request tracking and performance monitoring:

![Agent Pipeline Logs](./logs-screenshot.png)
*Screenshot showing agent communication flow and timing metrics*

**Monitoring Features:**
- Request ID tracking for debugging
- Agent-to-agent communication logging
- Performance timing (typically 20-30 seconds per image)
- Error handling with detailed diagnostics

## Production Deployment

- **Containerized**: Docker with non-root security
- **Scalable**: FastAPI async architecture  
- **Monitored**: Health checks and log rotation
- **Integrated**: Direct communication with Apollo messaging platform

## Development Highlights

This project demonstrates:
- **Advanced AI orchestration** using Google's latest ADK framework
- **Production-ready microservice** architecture with proper logging and monitoring
- **Custom model integration** with fal.ai's FLUX pipeline and custom LoRA
- **Multi-agent coordination** for complex prompt engineering tasks
- **Container security** best practices with non-root users and minimal attack surface"