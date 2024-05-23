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




## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
