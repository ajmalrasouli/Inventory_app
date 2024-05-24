# Inventory Management System 🛒📦

This is a web-based inventory management system built using Django.

## Features ✨

- 👤 Allows users to add, update, and delete products in the inventory.
- 🔐 Provides user authentication and authorization for secure access.
- 📁 Supports pagination for better navigation through product lists.

## Setup 🚀

1. Clone the repository:

```bash
git clone https://github.com/ajmalrasouli/Inventory_app.git
```


# Project Setup

Follow these steps to set up the project environment and run the server.

```
cd .\inventory_management\
```

## Create a Virtual Environment

```sh
python -m venv venv
```

Activate the Virtual Environment
```sh
venv\Scripts\activate
```

Install Dependencies
To install the required dependencies, run:
```sh
pip install -r requirements.txt
```

Usage
Apply Migrations
To apply database migrations, run:
```sh
python manage.py makemigrations
```

```sh
python manage.py migrate
```

Create a Superuser
To create a superuser, run:
```sh
python manage.py createsuperuser
```

Run the Server
To start the development server, run:

```sh
python manage.py runserver
```


1. Access the application at `http://127.0.0.1:8000/`.

## Technologies Used 🛠️

- 🐍 Python
- 🌐 Django
- 🌐 HTML
- 🎨 CSS
- ☕ JavaScript
- 🥾 Bootstrap

## Screenshots 📸
<img width="821" alt="product-list" src="https://github.com/ajmalrasouli/Inventory_app/assets/88502375/e99e105a-4f7c-4bfd-975c-9ba765cfca2e">

<img width="251" alt="profile" src="https://github.com/ajmalrasouli/Inventory_app/assets/88502375/cb1ac8a4-11ba-4897-b9cb-440a171179d9">




## Dockerize the Django Application 🐳

This repository contains a Dockerized Django application for managing inventory. Follow the instructions below to set up and run the application locally using Docker.

## Prerequisites ⚙️

Before you begin, make sure you have the following installed on your system:

- [Docker](https://www.docker.com/) 🐳
- [Docker Compose](https://docs.docker.com/compose/) 🐳

## Clone the Repository

Clone this repository to your local machine using the following command:

```sh
git clone https://github.com/ajmalrasouli/Inventory_app.git
cd Inventory_app
```

### Setup Environment Variables
Create a .env file in the root directory of the project and add the following environment variables:

```plaintext
DJANGO_SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///db.sqlite3
```

Replace your_secret_key with a secret key for your Django application.



#### Step 1: Create a Dockerfile
Create a **Dockerfile** in the root directory of your project with the following content:

```dockerfile
# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . /code/
```


### Step 2: Create a Docker Compose File 📄
Create a **docker-compose.yml** file in the root directory with the following content:


```yml
version: '3.8'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    env_file:
      - .env

```

### Step 3: Build and Run the Docker Container 🏃‍♂️
Build and run the Docker container using the following command:

```sh
docker-compose up --build
```

### Step 4: Apply Migrations and Create a Superuser ⚙️
In a new terminal, run the following commands to apply migrations and create a superuser:

```sh
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```

### Step 5: Access the Application 🌐
Open your web browser and go to **http://localhost:8000** to access the Django application.

## Push Docker Image to Docker Hub 🐳
If you want to push your Docker image to Docker Hub, follow these steps:

1. Build the Docker Image:
   
```sh
docker build -t your-dockerhub-username/inventory_app .

```

2. Log in to Docker Hub:
```sh
docker login
```

3. Push the Docker Image:
```sh
docker push your-dockerhub-username/inventory_app
```

Replace **your-dockerhub-username** with your actual Docker Hub username.


## Repository Overview 📝
**Description**: A Dockerized Django Inventory Application
**Category**: Application
**Full Description**:

This repository contains a Dockerized Django application for managing inventory. The application includes features such as adding, editing, and deleting inventory items, and viewing inventory statistics.

## Features 🌟
- 👤 User authentication and authorization
- 📦 Inventory management (CRUD operations)
- 🌐 Responsive web interface
- 🔌 REST API for integration with other systems



# Setup GitHub Actions workflow for CI/CD 🚀

### Prerequisites ⚙️

- 🐳 Docker
- 🐳 Docker Compose (optional)
- 💻 GitHub account
- 🐳 Docker Hub account



### Docker Setup 🐳

#### Dockerfile
Ensure the following **Dockerfile** is present in the root of your project:

```dockerfile
Copy code
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /code/

# Run the command to start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```
This Dockerfile uses the official Python 3.9 Slim image as the parent image and sets the working directory to /code. It then copies the
requirements.txt file into the container and installs any needed packages. Next, it copies the rest of the application code to the working directory and runs the command
python manage.py runserver 0.0.0.0:8000 to start the Django server.


### GitHub Actions Workflow ⚙️
Ensure the following GitHub Actions workflow is present at **.github/workflows/docker-image.yml**:

```yaml
Copy code
name: Docker Image CI

on:
  push:
    branches:
      - master
  pull_request:
    branches:
      - master

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2

      - name: Cache Docker layers
        uses: actions/cache@v2
        with:
          path: /tmp/.buildx-cache
          key: ${{ runner.os }}-buildx-${{ github.sha }}
          restore-keys: |
            ${{ runner.os }}-buildx-

      - name: Log in to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and push Docker image
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: your-dockerhub-username/inventory_app:latest

      - name: Run tests
        run: |
          docker run --rm your-dockerhub-username/inventory_app:latest python manage.py test
```

### Set Up Docker Hub Secrets 🔑🔐

1. Navigate to the Settings tab in your GitHub repository. ⚙️
2. Select Secrets and variables > Actions. 🔑
3. Click on New repository secret. 🆕
4. Add the following secrets:
   
  * DOCKER_USERNAME: Your Docker Hub username. 👤
  * DOCKER_PASSWORD: Your Docker Hub password. 🔐


### Commit and Push 📤
```sh
Copy code
git add .
git commit -m "Add GitHub Actions workflow for Docker image build and push"
git push origin master
```

### Running the Application 🏃‍♂️

To build and run the Docker container locally:

```sh

docker-compose up --build
```

To access the application, open your browser and navigate to **http://localhost:8000**. 🌐


## Summary 🎯
Following the above steps will set up a GitHub Actions workflow for your inventory_app Django project. This workflow will build your Docker image, run tests, and push the image to Docker Hub every time you push to the master branch or create a pull request targeting the master branch. This setup ensures continuous integration and delivery (CI/CD) for your Dockerized Django application. 🚀



## Contributing 🤝
If you would like to contribute to this project, please follow these steps:

1. Fork the repository. 🍴
2. Create a new branch (**git checkout -b feature-branch**). 🌱
3. Make your changes. ✍️
4. Commit your changes (**git commit -m 'Add some feature'**). 📝
5. Push to the branch (**git push origin feature-branch**). 📤
6. Create a new Pull Request. 🔃




## License 🔒

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.