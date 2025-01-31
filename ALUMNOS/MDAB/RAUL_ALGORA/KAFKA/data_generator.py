import json
import random
import time

def generate_order():
    products = ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse']
    order = {
        "order_id": random.randint(1000, 9999),
        "product": random.choice(products),
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(50, 500), 2),
        "timestamp": time.time()
    }
    return json.dumps(order)

if __name__ == "__main__":
    while True:
        print(generate_order())
        time.sleep(1)  # Genera un pedido cada segundo
