# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:07:06 2019

@author: IMGADMIN
"""

from flask import Flask, jsonify,request,render_template


app=Flask(__name__)

#@app.route('/api/test')   
#def home():
#    return "Hell0 World"


#@app.route('/')
#def home():
#    return render_template('index.html')

stores = [{
    'name': 'My Store',
    'items': [{'name':'my item', 'price': 15.99 }]
}]



#Nothing can be send over network in the dictionary format.
#Therefore the dictionary content as to be converted into string format so that it can be send over the internet
#Python dictionary is not understandable in javascript.
#Normal text can be read in javascript and coverted into the required format 
        
#json format helps to send python dictionary as plain text without altering the format

#POST- used to recieve data
#GET - used to send data back only

#POST /store data: {name:}
#GET /store/<string:name>
#GET /store
#POST /store/<string:name>/item
#GET /store/<string:name>/item
#print (jsonify({'store':store}))


# POST /store data: {name:}
#@app.route('/store',methods=['POST'])
#def create_store():
#    request_data = request.get_json()
#    new_store ={
#            'name' : request_data['name'],#request_data helps to extract the name from the request made by the browser
#            'items':[]
#            }
#    stores.append(new_store)
#    return jsonify(new_store)
#
##GET /store/<string:name>
#@app.route('/store/<string:name>')
#def get_store(name):
#    for store in stores:
#        if store['name'] == name:
#            return jsonify(store)
#    return jsonify({'Message':'Store not found'})
#
## GET /store
#@app.route('/stores',methods=['GET'])
#def get_stores():
#    #Iterate over the stores
#    #If the store name matches, return it
#    #If none match, return an error message
#    return jsonify({'stores': stores})
#
#
##POST /store/<string:name>/item {name:,price:}
#@app.route('/store/<string:name>/item',methods=['POST'])
#def create_item_in_the_store(name):
#    request_data = request.get_json()
#    for store in stores:
#        if store['name']==name:
#            new_item={
#                    'name':request_data['name'],
#                    'price':request_data['price']
#                    }
#            store['items'].append(new_item)
#            return jsonify(new_item)
#    return jsonify({'message':'Store not found'}) 
#
#@app.route('/store/<string:name>/item')
#def get_items_in_store(name):
#    for store in stores:
#        if store['name'] == name:
#            return jsonify({'Items':store['items']})
#    return jsonify({'message':'store not found'})

app.run(port=5000)


