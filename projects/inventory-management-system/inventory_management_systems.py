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

# 2 Calculate total unit in stock
def calculate_total_stock(products):
    total_stock = 0 
    for product in products:
        stock = product["stock"]
        total_stock += stock
    return total_stock

#3 Calculate total inventory value
def calculate_total_inventory_value(products):
    total_value = 0 
    for product in products:
        price = product["price"]
        stock = product["stock"]
        
        total_value +=  price * stock
    return total_value

#4 Calculate most expensive product
def calculate_most_expensive_products(products):
    highest_price = 0 
    most_expensive_product = {}
    
    for product in products:
        price = product["price"]
        if price > highest_price:
            highest_price = price
            most_expensive_product = product["name"]
    return highest_price, most_expensive_product

#5 Find the least expensive product
def calcualte_least_expensive_product(products):
    lowest_price = 9999
    lowest_product_name = {}

    for product in products:
        price = product["price"]
        if price < lowest_price:
            lowest_price = price
            lowest_product_name = product["name"]
    return lowest_product_name, lowest_price

#6 Find low stock products
def find_least_low_stock_product(products):
  
    low_stock_products = []

    for product in products:
         
        if product["stock"] <=5:
            low_stock_products.append(product)
    return low_stock_products


        
            


    


        

# Create final inventory report   
def create_inventory_report(products):

    total_products = count_products(products)
    total_stock = calculate_total_stock(products)
    total_value = calculate_total_inventory_value(products)
    highest_price, most_expensive_product = calculate_most_expensive_products(products)
    lowest_product_name, lowest_price = calcualte_least_expensive_product(products)
    low_stock_product = find_least_low_stock_product(products)

    return {

        "total_products": total_products,
        "total_stock" : total_stock,
        "total_value": total_value,
        "highest_price": highest_price,
        "most_expensive_product": most_expensive_product,
        "lowest_product_name": lowest_product_name,
        "lowest_price": lowest_price,
        "low_stock_products": low_stock_product
        

    }
# Print final inventory report
def print_inventory_report(report):

    print()
    print("========== INVENTORY REPORT ==========")
    print()

    print("Number of products:", report["total_products"])
    print("Total units in stock:", report["total_stock"])
    print("Total value of inventory :", report["total_value"])
    print()
    print("Most Expensive Product :", report["most_expensive_product"])
    print("Price:", report["highest_price"])
    print()
    print("Least Expensive Product:", report["lowest_product_name"])
    print("Price:", report["lowest_price"])
    print()
    print()
    print("========== LOW STOCK PRODUCTS ==========")
    print()
    for product in report["low_stock_products"]:
        print(
            product["name"],
            ":",
            product["stock"],
            "units"
        )
    print("")



report = create_inventory_report(products)

print_inventory_report(report)