# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

#some comments
# Copy the requirements.txt file first to leverage Docker cache
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy all the files from your project to the working directory in the container
COPY app.py .
COPY .env .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
