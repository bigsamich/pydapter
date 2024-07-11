# Use the official Python 3.12 image from Docker Hub as the base image
FROM python:3.12

# Set the working directory inside the container to /app
WORKDIR /app

# Install the redis package 
RUN pip install redis numpy grpcio grpcio-tools

#COPY . .
#COPY ../../GeneralRedisAcnetFrontend/protofiles/reqInfoReading.proto .

#RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. reqInfoReading.proto

# Command to run when the container starts
# This can be changed to the command you need for your application
CMD ["python", "--version"]