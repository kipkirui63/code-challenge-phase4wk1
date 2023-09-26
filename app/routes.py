from app import app
from flask import request, jsonify, make_response
from app.models import Restaurant, Pizzas, Restaurant_pizza
from app import db



@app.route('/', methods=['GET'])
def index():
    data = jsonify({"message": "Pizza Restaurant domain."})
    return data

@app.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.get_json()

    name = data.get('name')
    address = data.get('address')

    new_restaurant = Restaurant(name=name, address=address)

    db.session.add(new_restaurant)

    db.session.commit()

    return jsonify({'message': 'Restaurant added successfully'}), 201

# Route to get a list of restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = []

    for restaurant in restaurants:
        restaurant_data = {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
        restaurant_list.append(restaurant_data)

    return jsonify(restaurant_list)

# Route to get a restaurant by ID
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)

    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404

    pizzas = Restaurant_pizza.query.filter_by(restaurant_id=id)
    pizza_list = []

    for pizza in pizzas:
        pizza_data = {
            "id": pizza.pizza.id,
            "name": pizza.pizza.name,
            "ingredients": pizza.pizza.ingredients
        }
        pizza_list.append(pizza_data)

    restaurant_data = {
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": pizza_list
    }

    return jsonify(restaurant_data)

# Route to delete a restaurant by ID
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)

    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404

    # Delete associated Restaurant_pizza entries
    Restaurant_pizza.query.filter_by(restaurant_id=id).delete()

    db.session.delete(restaurant)
    db.session.commit()

    return '', 204

# Route to get a list of pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizzas.query.all()
    pizza_list = []

    for pizza in pizzas:
        pizza_data = {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }
        pizza_list.append(pizza_data)

    return jsonify(pizza_list)

# Route to create a new RestaurantPizza
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    if not data:
        return jsonify({"errors": ["Invalid JSON"]}), 400

    price = data.get("price")
    pizza_id = data.get("pizza_id")
    restaurant_id = data.get("restaurant_id")

    if None in (price, pizza_id, restaurant_id):
        return jsonify({"errors": ["Missing required fields"]}), 400

    restaurant_pizza = Restaurant_pizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)

    db.session.add(restaurant_pizza)
    db.session.commit()

    pizza = Pizzas.query.get(pizza_id)

    if pizza is None:
        return jsonify({"error": "Pizza not found"}), 404

    pizza_data = {
        "id": pizza.id,
        "name": pizza.name,
        "ingredients": pizza.ingredients
    }

    return jsonify(pizza_data), 201




# if __name__ == '__main__':
#     app.run(debug=True)