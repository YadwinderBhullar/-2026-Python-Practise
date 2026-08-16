products = [
    {
        "name": "Laptop",
        "category": "Electronics",
        "price": 1200,
        "stock": 5
    },
    {
        "name": "Phone",
        "category": "Electronics",
        "price": 800,
        "stock": 10
    },
    {
        "name": "Desk",
        "category": "Furniture",
        "price": 300,
        "stock": 3
    },
    {
        "name": "Chair",
        "category": "Furniture",
        "price": 150,
        "stock": 8
    },
    {
        "name": "Headphones",
        "category": "Electronics",
        "price": 100,
        "stock": 15
    }
]

# 1. Count products
def count_products(products):
    count = 0 
    for product in products :
        count += 1
    return count


# Create final inventory report   
def create_inventory_report(products):

    total_products = count_products(products)

    return {
        "total_products": total_products
    }
# Print final inventory report
def print_inventory_report(report):

    print()
    print("========== INVENTORY REPORT ==========")
    print()

    print("Number of products:", report["total_products"])


report = create_inventory_report(products)

print_inventory_report(report)