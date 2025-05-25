# Charlie Image Generator

An AI agent system that generates images of Charlie the dog using Google's Agent Development Kit (ADK) and the fal.ai API with a custom LoRA trained on FLUX.1.

## Overview

This project implements a pipeline of specialized agents that work together to:

1. Generate high-quality prompts based on user requests
2. Review and provide feedback on the prompts
3. Refine the prompts based on feedback
4. Generate images using the fal.ai API with a custom LoRA

## Architecture

- **Agent Architecture**: Sequential pipeline with three specialized agents (Writer, Reviewer, Refiner)
- **Implementation Approach**: Uses `AgentTool` for deterministic behavior and control
- **Integration**: Communicates with Apollo via internal Docker networking
- **Models**: Uses Anthropic Claude for agent implementation (Haiku for orchestrating root agent, Sonnet for prompt pipeline agent)
