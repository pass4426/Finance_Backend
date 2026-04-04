# Finance Data Processing and Access Control Backend

## Overview

This project is a backend system designed to manage financial records with role-based access control. It provides APIs for handling users, financial transactions, and dashboard analytics. The system is structured to demonstrate clear backend architecture, proper data handling, and access restriction based on user roles.

## Technology Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite

## Features

### User Management

* Create and manage users
* Assign roles such as Admin, Analyst, and Viewer
* Manage user-related data

### Financial Records Management

* Create financial records
* Retrieve all records
* Delete records
* Filter records based on:

  * Type (income or expense)
  * Category
  * Date range

### Dashboard Summary

* Total income calculation
* Total expense calculation
* Net balance calculation

### Role-Based Access Control

* Admin: Full access to all operations
* Analyst: Access to records and dashboard
* Viewer: Read-only access

## API Endpoints

### User Endpoints

* POST /users
* GET /users

### Record Endpoints

* POST /records
* GET /records
* DELETE /records/{record_id}

### Dashboard Endpoint

* GET /dashboard/summary

## Role Access Example

The system uses a role parameter to simulate access control.

Example:

* /dashboard/summary?role=admin allows access
* /dashboard/summary?role=viewer returns access denied

## Project Structure

app/
main.py
database.py
models/
schemas/
routes/
utils/

## Setup and Installation

1. Install dependencies:
   pip install -r requirements.txt

2. Run the server:
   python -m uvicorn app.main:app --reload

3. Access the API documentation:
   http://127.0.0.1:8000/docs

## Assumptions

* Authentication is simulated using a role query parameter
* SQLite database is used for simplicity
* User identity is not fully implemented

## Future Improvements

* Implement JWT-based authentication
* Add pagination for large datasets
* Enhance analytics with category-wise and time-based insights
* Deploy the application to a cloud platform

## Conclusion

This project demonstrates backend development skills including API design, database integration, business logic implementation, and access control. It is structured to be clear, maintainable, and aligned with real-world backend development practices.
