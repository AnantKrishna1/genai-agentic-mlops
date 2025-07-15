# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy everything into the container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Start Streamlit app
CMD ["streamlit", "run", "01_ingestion/ui.py", "--server.port=8501", "--server.address=0.0.0.0"]
