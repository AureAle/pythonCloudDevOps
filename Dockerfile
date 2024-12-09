FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
# Use ENTRYPOINT to define the Python script to run
ENTRYPOINT ["python", "main.py"]

# CMD can be overridden with arguments when running the container
CMD ["Costs"]  # Default argument, can be overridden by passing arguments to docker run

