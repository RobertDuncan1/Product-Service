from flask import *

app = Flask(__name__)

product_list = [
    {"id": 0, "name": "apple", "price": 1.00, "amount": 100},
    {"id": 1, "name": "bread", "price": 2.99, "amount": 50},
    {"id": 2, "name": "banana", "price": 1.99, "amount": 75}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products": product_list})

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in product_list if product["id"] == product_id), None)
    if product:
        return jsonify({"product": product})
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route('/products', methods=['POST'])
def create_product():
    new_product = {
        "id": len(product_list),
        "name": request.json.get('name'),
        "price": request.json.get('price'),
        "amount": request.json.get('amount'),
    }
    product_list.append(new_product)
    return jsonify({"message": "Product created", "product": new_product}), 201

@app.route('/products/<int:product_id>', methods=['POST'])
def update_amount(product_id):
    product_list[product_id]["amount"] = request.json.get("amount")
    return jsonify({"message": "Product updated", "product": product_list[product_id]}), 201


if __name__ == '__main__':
    app.run(debug=True)