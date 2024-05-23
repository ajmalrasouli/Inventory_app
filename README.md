# Inventory Management System

This is a web-based inventory management system built using Django.

## Features

- Allows users to add, update, and delete products in the inventory.
- Provides user authentication and authorization for secure access.
- Supports pagination for better navigation through product lists.

## Setup

1. Clone the repository:

git clone https://github.com/ajmalrasouli/Inventory_app.git



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

## Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript
- Bootstrap

## Screenshots
<img width="821" alt="product-list" src="https://github.com/ajmalrasouli/Inventory_app/assets/88502375/e99e105a-4f7c-4bfd-975c-9ba765cfca2e">

<img width="251" alt="profile" src="https://github.com/ajmalrasouli/Inventory_app/assets/88502375/cb1ac8a4-11ba-4897-b9cb-440a171179d9">


## Contributing
If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (**git checkout -b feature-branch**).
3. Make your changes.
4. Commit your changes (**git commit -m 'Add some feature'**).
5. Push to the branch (**git push origin feature-branch**).
6. Create a new Pull Request.



# Inventory App

This repository contains a Dockerized Django application for managing inventory. Follow the instructions below to set up and run the application locally using Docker.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

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

### Dockerize the Django Application

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


### Step 2: Create a Docker Compose File
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

### Step 3: Build and Run the Docker Container
Build and run the Docker container using the following command:

```sh
docker-compose up --build
```

### Step 4: Apply Migrations and Create a Superuser
In a new terminal, run the following commands to apply migrations and create a superuser:

```sh
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```

### Step 5: Access the Application
Open your web browser and go to **http://localhost:8000** to access the Django application.

## Push Docker Image to Docker Hub
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


## Repository Overview
**Description**: A Dockerized Django Inventory Application
**Category**: Application
**Full Description**:

This repository contains a Dockerized Django application for managing inventory. The application includes features such as adding, editing, and deleting inventory items, and viewing inventory statistics.

## Features
- User authentication and authorization
- Inventory management (CRUD operations)
- Responsive web interface
- REST API for integration with other systems

## Getting Started
Follow the instructions in the `README.md` file to set up and run the application locally using Docker.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
