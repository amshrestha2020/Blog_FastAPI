# Blog FastAPI
Simple Blog Used FastAPI

## Getting Started

### Prerequisites

- Python 3.6+
- PostgreSQL
- FastAPI
- Uvicorn
- Pytest
- Sqlalchemy
- Postgres

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/amshrestha2020/Blog_FastAPI.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Blog_FastAPI
    ```
3. Create a virtual environment:
    ```bash
    python -m venv env
    ```
4. Activate the virtual environment:

    - Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - Linux/Mac:
        ```bash
        source env/bin/activate
        ```

5. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the App

Start the server using Uvicorn:

```bash
uvicorn main:app --reload
```
alembic would be creating empty migrations files on executing :

```bash
alembic revision --autogenerate -m "first commit"
```

#executes the migration files to make actual changes in db
```bash
alembic upgrade head
```

The server will start at http://localhost:8000/ or http://127.0.0.1:8000/.

Features
1. Comprehensive FastAPI course
2. Hello World example
3. Database connection setup
4. Database migration using Alembic
5. Schemas for data validation
6. Dependency injection for managing dependencies
7. Password hashing for secure storage
8. Unit testing for ensuring app stability
9. User authentication (login, create user, generate token)
10. Authorization and permission management
