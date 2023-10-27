# Menu drawer django application
This app implements tree menu using a template tag

## Getting started
These instructions will help you set up and run the project on your local machine.

### Prerequisites

- python 3.x
- pip
- Git
- Virtual Environment (recommended)

### Installation

1. Clone this repository to your local machine using the following command:

    ```bash
   git clone https://github.com/hamidullaorifov/UpTrader_Task.git
   ```

2. Navigate to the project directory:

    ```bash
   cd UpTrader_Task
   ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

- On Windows
    ```bash
    venv\Scripts\activate
    ```
- On macOS and Linux
    ```bash
    source venv/bin/activate
    ```
5. Install the project dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Apply database migrations:
    ```bash
    python manage.py migrate
    ```
7. Start the development server:
    ```bash
    python manage.py runserver
    ```
8. Open a web browser and go to http://localhost:8000 to access your Django application.

## Usage
1. Create a superuser using this command

    ```bash
    python manage.py createsuperuser
    ```
2. Navigate to admin page - http://localhost:8000/admin

3. Create menu items and return back to home page

## Configuration
If you are going to test
- Open `settings.py` file and change DEBUG to True and set SECRET_KEY
or 
- Create .env file and set environment variables





