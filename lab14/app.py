from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
items = {}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or not data:
        return jsonify({'error': 'Invalid input'}), 400

    item_id = str(len(items) + 1)
    items[item_id] = data
    return jsonify({'id': item_id, 'item': data}), 201


@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


@app.route('/items/<item_id>/update', methods=['GET', 'POST'])
def update_item_page(item_id):
    item = items.get(item_id)
    if item is None:
        return render_template(
            'error.html',
            title='Item not found',
            message=f"Unable to update item {item_id} because it does not exist.",
            item_id=item_id,
        ), 404

    if request.method == 'POST':
        name = request.form.get('name', item.get('name', ''))
        price_value = request.form.get('price', item.get('price', 0))

        try:
            price = float(price_value)
        except (TypeError, ValueError):
            return render_template(
                'error.html',
                title='Invalid input',
                message='Price must be a valid number.',
                item_id=item_id,
            ), 400

        updated_item = {'name': name, 'price': price}
        items[item_id] = updated_item
        return render_template('update.html', item_id=item_id, item=updated_item, success=True), 200

    return render_template('update.html', item_id=item_id, item=item, success=False), 200


@app.route('/items/<item_id>/delete', methods=['GET', 'POST'])
def delete_item_page(item_id):
    item = items.get(item_id)
    if item is None:
        return render_template(
            'error.html',
            title='Item not found',
            message=f"Unable to delete item {item_id} because it does not exist.",
            item_id=item_id,
        ), 404

    if request.method == 'POST':
        deleted_item = items.pop(item_id)
        return render_template('delete.html', item_id=item_id, deleted_item=deleted_item, success=True), 200

    return render_template('delete.html', item_id=item_id, deleted_item=item, success=False), 200


@app.route('/items/<item_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_item(item_id):
    item = items.get(item_id)

    if request.method == 'GET':
        if item is None:
            return jsonify({'error': 'Item not found'}), 404
        return jsonify(item)

    if request.method == 'PUT':
        if item is None:
            return render_template(
                'error.html',
                title='Item not found',
                message=f"Unable to update item {item_id} because it does not exist.",
                item_id=item_id,
            ), 404

        data = request.get_json(silent=True)
        if not isinstance(data, dict) or not data:
            return render_template(
                'error.html',
                title='Invalid input',
                message='Please provide a valid JSON object with item details.',
                item_id=item_id,
            ), 400

        items[item_id] = data
        return render_template('update.html', item_id=item_id, item=data, success=True), 200

    if request.method == 'DELETE':
        if item is None:
            return render_template(
                'error.html',
                title='Item not found',
                message=f"Unable to delete item {item_id} because it does not exist.",
                item_id=item_id,
            ), 404

        deleted_item = items.pop(item_id)
        return render_template('delete.html', item_id=item_id, deleted_item=deleted_item, success=True), 200

    return jsonify({'error': 'Method not allowed'}), 405


if __name__ == '__main__':
    app.run(debug=True)