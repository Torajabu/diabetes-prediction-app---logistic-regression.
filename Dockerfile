# Use a slim Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files from the host to the container
COPY main.py /app/
COPY frontend.py /app/
COPY models /models/
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Expose the ports for FastAPI and Streamlit
EXPOSE 8000 8501

# Set the command to run FastAPI and Streamlit together
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & streamlit run frontend.py --server.port=8501 --server.enableCORS=false"]
