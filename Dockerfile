# base image
FROM python:3.13.3

# set working directory inside container
WORKDIR /app

# copy all project files into the container
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# specify the default command to run the app
CMD ["python", "app.py"]