import requests
import random
from datetime import datetime

# Base URL for Fake Store API
BASE_URL = "https://fakestoreapi.com"


def create_products_additional_info(products_with_details):
        products_no_sql = []
        print("Generating product_no_sql content")
        for product in products_with_details:
            products_no_sql.append({
                "productId": int(product['id']),
                "description": product['description'],
                "image": product['image'],
                "rating": product['rating']
            })
        return products_no_sql


def create_order(user, products_with_details, num_order_generated):
    """Create an order for a given user with random products."""
    selected_products = random.sample(products_with_details, random.randint(1, 3))  # Randomly select 1 to 3 products
    products_payload = []
    total_price = 0.0

    for product in selected_products:
        quantity = random.randint(1, 5)  # Random quantity between 1 and 5
        products_payload.append({
            "productId": product['id'],
            "name": product['title'],
            "quantity": quantity,
            "price": product['price']
        })
        total_price += product['price'] * quantity

    payload = {
        "numOrderGenerated": num_order_generated,  # Assign a unique order ID
        "user": {
            "id": user['id'],  # Use the user's unique ID
            "name": user['name'],
            "email": user['email']
        },
        "timestamp": datetime.now().isoformat(),  # ISO 8601 timestamp
        "products": products_payload,
        "totalPrice": round(total_price, 2)  # Total price rounded to 2 decimal places
    }
    # Simulate saving order locally or in memory, since Fake Store API doesn't support unique order IDs
    print(f"Order created for {user['name']} ({user['email']}): {payload}")
    return payload


def get_limited_products(limit=40):
    """Retrieve a limited number of products (up to `limit`) from the API."""
    response = requests.get(f"{BASE_URL}/products")
    if response.status_code == 200:
        products = response.json()
        return [{"id": product['id'], "title": product['title'], "price": product['price'],
                 "image": product['image'], "description": product['description'], "rating": product["rating"]} 
                 for product in products[:limit]]
    else:
        print("Failed to fetch products:", response.status_code)
        return []


def get_limited_users(limit=10):
    """Retrieve a limited number of users (up to `limit`) from the API."""
    response = requests.get(f"{BASE_URL}/users")
    if response.status_code == 200:
        users = response.json()
        return [{"id": user['id'], "name": f"{user['name']['firstname']} {user['name']['lastname']}", "email": user['email']} for user in users[:limit]]
    else:
        print("Failed to fetch users:", response.status_code)
        return []


def simulate_order_creation(num_order_generated):
    """Simulate creating 10 orders per minute."""
    print("Fetching products and users...")
    products_with_details = get_limited_products(limit=20)
    users = get_limited_users(limit=10)
    if not products_with_details or not users:
        print("No products or users available. Exiting.")
        return
    user = random.choice(users)  # Randomly pick a user from the list
    order = create_order(user, products_with_details, num_order_generated)
    return order


if __name__ == "__main__":
    payload = simulate_order_creation(5)
    print(payload)
