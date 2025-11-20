# base image
FROM python:3.13.3

# set working directory inside container
WORKDIR /app

# copy all project files into the container
COPY . .

# install dependencies
RUN pip install -r requirements.txt

COPY model.pkl model.pkl
COPY app.py app.py

# specify the default command to run the app
CMD ["python", "app.py", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5500"]