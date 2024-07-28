# Savings App Django

## Project Description

This is a Django-based savings application that allows users to manage their savings goals. Users can create, update, and delete savings goals, make contributions to these goals, and track the progress of their savings.

## Features

- User authentication (login, logout, register)
- Create, update, and delete savings goals
- Make contributions to savings goals
- Track progress of savings goals

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.8 or higher
- You have installed Git
- You have installed virtualenv

## Getting Started

### 1. Clone the Repository

First, clone the repository to your local machine:


git clone https://github.com/Faisal-Abdo/Savings_App_Django.git <br>
cd Savings_App_Django

### 2. Create a Virtual Environment
Create a virtual environment to manage project dependencies: <br>
python -m venv venv 

### 3. Activate the Virtual Environment
Activate the virtual environment:

On Windows: <br>
.\venv\Scripts\activate

On macOS and Linux: <br>
source venv/bin/activate

### 4. Install Dependencies
Install the project dependencies from requirements.txt: <br>
pip install -r requirements.txt

### 5. Set Up the Database
Run the following commands to set up the database:<br>
python manage.py makemigrations <br>
python manage.py migrate

### 6. Run the Development Server
Start the Django development server: <br>
python manage.py runserver

Open your web browser and go to http://127.0.0.1:8000 to see the application running.

Contact
If you have any questions or issues, please feel free to contact me at [faisalalbusaidy2015@gmail.com].
