"""Module summing and displaying shopping chart items and total values"""

def calculatetotal(cart):
    """Function to calculate total"""
    total = 0
    for element in cart:
        total += element['price']
    return total

def displaytotal(total):
    """Function to print total values"""
    print("Total price: " + str(total))

CART = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': 8.49}
]

for item in CART:
    print(f"Item: {item['name']} - Price: ${item['price']}")

shopping_cart_total = calculatetotal(CART)
displaytotal(shopping_cart_total)
