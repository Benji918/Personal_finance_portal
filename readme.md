#  Personal Finance

This is a personal finance application built using the Django web framework. It allows users to track their expenses, create budgets, and see their spending habits over time.

## Proposed Features

- Add and categorize expenses
- Create and track budgets
- View spending trends and statistics
- Set financial goals and track progress towards them
- Secure login and data encryption

## Project ER Diagram
![model diagram](https://github.com/Benji918/Personal_finance_portal/blob/main/Django%20app.png)

## Prerequisites

Before you can run this project, you need to have the following software installed on your machine:

- Python (3.8 or later)
- Django (2.2 or later)

To check if you have Python installed, run the following command in your terminal:

`python --version`


To check if you have Django installed, run the following command in your terminal:

`python -m django --version`


If you don't have either of these programs installed, you can install them by following the instructions at the following links:

- [Install Python](https://www.python.org/downloads/)
- [Install Django](https://docs.djangoproject.com/en/3.1/topics/install/)

## Running the project

1. Clone this repository to your local machine:

git clone https://github.com/Benji918/Personal_finace_portal.git


2. Navigate to the root directory of the project:

`cd django-project`

3. Install the required dependencies using the command:

`pip install -r requirements.txt`

4. Create a PostgreSQL database for the application and add the database credentials to the settings.py file.

5. Run the migrations to create the database tables using the command:

`python manage.py migrate`

6. Create a superuser for the application using the command:

`python manage.py createsuperuser`

7. Create a file named `.env` in the root directory of the application. This file should contain the following environment variables:

`EMAIL_HOST_USER=<your_email_address_here>`
`EMAIL_HOST_PASSWORD=<your_email_host_here>`
`SECRET_KEY=<your_secret_key_here>`
`POSTGRES_HOST=<your_database_host_here>`
`POSTGRES_PASSWORD=<your_database_password_here>`
`POSTGRES_PORT=<your_database_port_here>`
`POSTGRES_USER=<your_database_user_here>`
`POSTGRES_NAME=<your_database_name_here>`
`RECAPTCHA_PUBLIC_KEY=<your_recaptcha_public_key_here>`
`RECAPTCHA_PRIVATE_KEY=<your_recaptcha_private_key_here>`
`CLOUD_NAME=<your_cloudinary_name_here>`
`API_KEY=<your_cloudinary_api_key_here>`
`API_SECRET=<your_cloudinary_api_secret_here>`

8. Run the development server:

`python manage.py runserver`


This will start the development server at http://127.0.0.1:8000/.

If you want to specify a different port, you can do so by using the `--port` flag, like this:

`python manage.py runserver --port 8080`


This will start the development server at http://127.0.0.1:8080/.

Keep in mind that the development server is for development purposes only, and is not intended for use in production. For more information on how to deploy a Django project, see the Django documentation.

## Using the application

Once the development server is running, you can access the application at http://127.0.0.1:8000/. Use the links and form inputs on the page to interact with the application.

## Shutting down the development server

To shut down the development server, open the terminal window in which it is running, and press `CTRL+C`. This will stop the server, and you will be returned to the command prompt.

## Features
The Personal Finance Portal application provides the following features:
- Users can create and manage multiple savings accounts, deposits, withdrawals, and savings goals.
- Users can view their savings account balance and progress towards their savings goals.
- Users can view a summary of their monthly expenses and savings.
- Users can generate a pie chart to visualize their expenses.
- Users can generate a line chart to visualize their savings progress.

## Technologies Used
The Personal Finance Portal application uses the following technologies:
- Django: a Python web framework for building web applications
- PostgresSQL: an open-source relational database management system
- JavaScript: for visualizations and interactivity on the dashboard
- Chart.js: a JavaScript library for visualizing data in charts
- Bootstrap: a popular CSS framework for building responsive websites

## Contributors
The Personal Finance Portal application is maintained by Benji918. If you'd like to contribute to the project, please feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the LICENSE file for details.