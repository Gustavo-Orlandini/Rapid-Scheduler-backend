# Project Documentation

## Overview
This project is a Python-based application that serves as a backend for a booking system. It utilizes FastAPI for building RESTful APIs, with data managed using a JSON file for simplicity. A virtual environment is used for dependency management.

## Requirements
- Python 3.11.9
- FastAPI
- Uvicorn
- Libraries listed in `requirements.txt`

## Setup
1. Clone the repository to your local machine:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```sh
    cd <project-directory>
    ```
3. Create a virtual environment using the following command:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Ensure the virtual environment is activated.
2. Run the FastAPI application:
    ```sh
    python -m uvicorn app.main:app --reload
    ```
3. Access the application:
    - Swagger UI for API testing: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - ReDoc for API documentation: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Configuration
### Environment Variables
The application uses environment variables stored in a `.env` file for configuration. Below are the supported variables:
- `APP_ENV`: Defines the environment mode (`development`, `production`). Default is `production`.
- `DEBUG`: Enables or disables debug mode (`true` or `false`).

### JSON Data File
All available slots and bookings are stored in `app/slots.json`. Ensure the file exists and follows the structure below:

```json
[
    {
        "id": 1,
        "start_time": "2025-02-04T09:00:00",
        "end_time": "2025-02-04T10:00:00",
        "reserved": false
    }
]

### Project Structure

project/
│
├── app/
│   ├── main.py           # Entry point for the FastAPI application
│   ├── models.py         # Pydantic models for data validation
│   ├── routes/           # API route definitions
│   │   ├── bookings.py   # Booking-related endpoints
│   │   ├── slots.py      # Slot-related endpoints
│   ├── slots.json        # JSON file for storing slot data
│   ├── utils.py          # Utility functions for JSON handling
│
├── venv/                 # Virtual environment directory
├── requirements.txt      # List of Python dependencies
├── .env                  # Environment variables
└── README.md             # Project documentation
