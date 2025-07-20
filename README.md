# KPA ERP - Backend API Implementation

This project is a submission for the Backend Developer assignment from Sarva Suvidhan Pvt. Ltd. It features a fully functional API built with Python and FastAPI that adheres to the provided Postman collection specifications.

## Implemented APIs

As per the assignment instructions, I chose to implement two endpoints for the **Wheel Specifications** form:

1.  **`POST /api/forms/wheel-specifications`**
    *   **Description:** Creates a new wheel specification record in the PostgreSQL database. It validates the incoming JSON body and ensures the `formNumber` is unique.
    *   **Success Response:** `201 Created`

2.  **`GET /api/forms/wheel-specifications`**
    *   **Description:** Retrieves a list of wheel specification records. This endpoint supports filtering by `formNumber`, `submittedBy`, and `submittedDate` via query parameters.
    *   **Success Response:** `200 OK`

## Tech Stack & Features

*   **Language:** Python
*   **Framework:** FastAPI
*   **Database:** PostgreSQL
*   **Key Libraries:** Uvicorn, SQLAlchemy, psycopg2-binary
*   **Environment Variables:** Secure database configuration via a `.env` file.
*   **Live Interactive Docs:** Auto-generated Swagger UI is available at `/docs` for live API testing.

## Setup and Installation

1.  **Clone the repository.**
2.  **Navigate to the `kpa_backend` directory.**
3.  **Create a virtual environment:** `python -m venv venv`
4.  **Activate it:** `venv\Scripts\activate`
5.  **Install dependencies:** `pip install -r requirements.txt`
6.  **Create a `.env` file** and add your database URL: `DATABASE_URL="postgresql://user:password@host/db_name"`
7.  **Run the server:** `uvicorn app.main:app --reload`

## Frontend Integration Analysis

I successfully set up the Flutter environment, resolved multiple build and null-safety errors present in the provided `KPA-ERP-FE` codebase, and launched the application.

My analysis concluded that the frontend is hardcoded to work with the `bogie-checksheet` API, not the `wheel-specifications` API I implemented. Furthermore, the application has internal bugs related to its Firebase implementation that prevent it from getting past the login screen, as shown in the screenshot below.

![Frontend Execution Error](docs/frontend_error.png)

As this is a backend-focused assignment, I have prioritized delivering a robust and thoroughly tested backend. My API has been verified with both Postman and the Swagger UI and is ready for integration.