FROM python:3.12.3

EXPOSE 5001
#This command will create the working directory for our Python Flask application Docker image
WORKDIR /todo-app-backend

#This command will copy the dependancies and libaries in the requirements.txt to the working directory
COPY ../requirements.txt /todo-app-backend


EXPOSE 5001
#This command will install the dependencies in the requirements.txt to the Docker image
RUN pip install -r requirements.txt --no-cache-dir

#This command will copy the files and source code required to run the application
COPY .. /todo-app-backend

#This command will start the Python Flask application Docker container
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "-p", "5001"]

