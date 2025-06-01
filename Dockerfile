FROM python:3.12-slim

# Python optimization for containerized environments
ENV PYTHONDONTWRITEBYTECODE=1 \  
    PYTHONUNBUFFERED=1           

# Security: Create non-root user for application execution
RUN adduser --disabled-password --gecos "" appuser

# Set the working directory in the container
WORKDIR /app

# Copy dependency manifest first for Docker layer caching optimization
# Changes to code won't invalidate the pip install layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY main.py .                           
COPY ./charlie_image_generator ./charlie_image_generator  

# Security: Ensure non-root user owns all application files
RUN chown -R appuser:appuser /app

# Switch to non-root user for runtime security
USER appuser

# Runtime configuration
ENV PORT=8000
EXPOSE 8000

# Start FastAPI server on all interfaces
CMD ["python", "main.py"]
