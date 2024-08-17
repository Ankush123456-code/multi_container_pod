
FROM ubuntu:latest


WORKDIR /app


COPY . .

# Install Python dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean


RUN python3 -m pip install --no-cache-dir -r requirements.txt


# Expose the port that the application listens on.
#EXPOSE 8000

# Run the application.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--timeout-keep-alive","600"]