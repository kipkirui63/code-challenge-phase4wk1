# code-challenge-phase4wk1

# Flask Code Challenge - Pizza Restaurants

This is a Flask API for managing pizza restaurants and their menus. It includes features such as creating, retrieving, and deleting restaurants, pizzas, and restaurant-pizza associations. Below are details on how to set up and use this API.

## Getting Started

To get started with the Pizza Restaurant API, follow these steps:

### Prerequisites

Before running the application, ensure you have the following installed:

- Python (3.6 or higher)
- Flask
- SQLAlchemy
- Postman or any API testing tool

###
dbdiagram.io link:'https://dbdiagram.io/d/650ff9a1ffbf5169f061a4b9'

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/pizza-restaurant-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd pizza-restaurant-api
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows (Command Prompt):

     ```bash
     venv\Scripts\activate
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Configure the Database:

   - Create a database (e.g., SQLite, PostgreSQL).
   - Update the `config.py` file with your database URI.

7. Initialize the database:

   ```bash
   flask db init
   ```

8. Migrate and upgrade the database:

   ```bash
   flask db migrate
   flask db upgrade
   ```

9. Start the application:

   ```bash
   flask run
   ```

The API should now be running locally at `http://127.0.0.1:5000/`.

## API Endpoints

The following endpoints are available for interacting with the API:

### GET /restaurants

- Description: Retrieve a list of all restaurants.
- Response Format:

  ```json
  [
    {
      "id": 1,
      "name": "Dominion Pizza",
      "address": "Good Italian, Ngong Road, 5th Avenue"
    },
    {
      "id": 2,
      "name": "Pizza Hut",
      "address": "Westgate Mall, Mwanzi Road, Nrb 100"
    }
  ]
  ```

### GET /restaurants/:id

- Description: Retrieve details of a specific restaurant by ID.
- Response Format (If restaurant exists):

  ```json
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "Good Italian, Ngong Road, 5th Avenue",
    "pizzas": [
      {
        "id": 1,
        "name": "Cheese",
        "ingredients": "Dough, Tomato Sauce, Cheese"
      },
      {
        "id": 2,
        "name": "Pepperoni",
        "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
      }
    ]
  }
  ```

- Response Format (If restaurant does not exist):

  ```json
  {
    "error": "Restaurant not found"
  }
  ```

### DELETE /restaurants/:id

- Description: Delete a restaurant by ID. Deletes associated RestaurantPizzas as well.
- Response (If restaurant exists): Empty response body with HTTP status 204 (No Content).
- Response (If restaurant does not exist):

  ```json
  {
    "error": "Restaurant not found"
  }
  ```

### GET /pizzas

- Description: Retrieve a list of all pizzas.
- Response Format:

  ```json
  [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
  ```

### POST /restaurant_pizzas

- Description: Create a new RestaurantPizza associated with an existing Pizza and Restaurant.
- Request Body Format:

  ```json
  {
    "price": 5,
    "pizza_id": 1,
    "restaurant_id": 3
  }
  ```

- Response (If RestaurantPizza is created successfully):

  ```json
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  }
  ```

- Response (If RestaurantPizza is not created successfully):

  ```json
  {
    "errors": ["validation errors"]
  }
  ```

## Validations

- RestaurantPizza model must have a price between 1 and 30.
- Restaurant model must have a name less than 50 characters in length and must have a unique name.

## Testing

You can test the API by running a local Flask server and using Postman or any API testing tool to make requests to the specified endpoints.

## Contributing

If you'd like to contribute to this project, please follow the contribution guidelines in the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy coding!

