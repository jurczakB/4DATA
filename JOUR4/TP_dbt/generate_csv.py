import numpy as np
import pandas as pd

# Paramètres
num_orders = 10000
num_customers = 1000
num_products = 500

# Génération des clients (customers.csv)
customers_data = {
    "customer_id": np.arange(1, num_customers + 1),
    "customer_name": [f"Customer {i}" for i in range(1, num_customers + 1)],
    "email": [f"customer{i}@example.com" for i in range(1, num_customers + 1)],
    "signup_date": pd.date_range(start="2022-01-01", periods=num_customers, freq="D").strftime("%Y-%m-%d")
}
customers_df = pd.DataFrame(customers_data)

# Génération des produits (products.csv)
products_data = {
    "product_id": np.arange(1, num_products + 1),
    "product_name": [f"Product {i}" for i in range(1, num_products + 1)],
    "category": np.random.choice(["Electronics", "Home", "Clothing", "Toys", "Books"], num_products),
    "price": np.round(np.random.uniform(5, 500, num_products), 2)
}
products_df = pd.DataFrame(products_data)

# Génération des commandes (orders.csv)
orders_data = {
    "order_id": np.arange(1, num_orders + 1),
    "customer_id": np.random.randint(1, num_customers + 1, num_orders),
    "product_id": np.random.randint(1, num_products + 1, num_orders),
    "quantity": np.random.randint(1, 10, num_orders),
    "total_amount": np.round(np.random.uniform(10, 2000, num_orders), 2),
    "order_date": pd.date_range(start="2023-01-01", periods=num_orders, freq="H").strftime("%Y-%m-%d %H:%M:%S")
}
orders_df = pd.DataFrame(orders_data)

# Sauvegarde en fichiers CSV
orders_file = "./data/orders.csv"
customers_file = "./data/customers.csv"
products_file = "./data/products.csv"

orders_df.to_csv(orders_file, index=False)
customers_df.to_csv(customers_file, index=False)
products_df.to_csv(products_file, index=False)

# Retourner les fichiers générés
orders_file, customers_file, products_file
