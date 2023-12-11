# Restaurant Reviews Management System

The Restaurant Reviews Management System is a Python application designed to manage restaurant information, customer details, and reviews using SQLAlchemy.

## Introduction

This project provides a comprehensive solution for managing restaurant reviews. Built with SQLAlchemy, it leverages a SQLite database to store information about restaurants, customers, and their reviews. The application offers a user-friendly command-line interface for efficient interaction with the database.

## Features

- **Restaurant Management:**
  - Create, retrieve, update, and delete restaurant information.
  - Find the fanciest restaurant based on the highest price.

- **Customer Management:**
  - Create, retrieve, update, and delete customer information.

- **Review Management:**
  - Create, retrieve, update, and delete reviews.
  - Retrieve all reviews for a specific restaurant.
  - Retrieve all reviews left by a specific customer.

- **Additional Features:**
  - Fetch all restaurants with associated reviews.
  - Fetch all customers with associated reviews.

## Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:ckorir/Restaurants-SQLAlchemy.git
   cd restaurant-reviews

2. **Install Dependancies:**
    ```pipenv install

3. **Run Tests**
    ```python3 lib/seed.py

## Models

- **Restaurant:**
    - Attributes: id, name, price.
    - Methods: restaurant_reviews(), restaurant_fanciest(), restaurant_all_reviews().

- **Customer:**
    - Attributes: id, first_name, last_name.
    - Methods: customer_reviews(), full_name(), customer_add_review(), customer_delete_reviews().

- **Review:**
    - Attributes: id, star_rating, restaurant_id, customer_id.
    - Methods: review_customer(), review_restaurant(), review_full_review().

## Licence

MIT License

Copyright (c) 2023 ckorir

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.