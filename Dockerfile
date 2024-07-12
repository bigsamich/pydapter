# Use the data science notebook as the base image
FROM quay.io/jupyter/datascience-notebook  

# Install the redis package 
RUN pip install redis

# Retain the original entrypoint and command
ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.py"]
