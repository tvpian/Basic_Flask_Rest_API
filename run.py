from app import app

from flask import Flask, jsonify,request,render_template


@app.route('/')
def home():
    return render_template('index.html') 


@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store ={
            'name' : request_data['name'],#request_data helps to extract the name from the request made by the browser
            'items':[]
            }
    app.stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in app.stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'Message':'Store not found'})

# GET /store
@app.route('/stores',methods=['GET'])
def get_stores():
    #Iterate over the stores
    #If the store name matches, return it
    #If none match, return an error message
    return jsonify({'stores': app.stores})


#POST /store/<string:name>/item {name:,price:}
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_the_store(name):
    request_data = request.get_json()
    for store in app.stores:
        if store['name']==name:
            new_item={
                    'name':request_data['name'],
                    'price':request_data['price']
                    }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'Store not found'}) 

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in app.stores:
        if store['name'] == name:
            return jsonify({'Items':store['items']})
    return jsonify({'message':'store not found'})