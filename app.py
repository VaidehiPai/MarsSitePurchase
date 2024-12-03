from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client=MongoClient('mongodb+srv://test:password@cluster0.ia0nj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db=client.dbsparta
app = Flask(__name__)


@app.route('/')
def home():
   return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive=request.form['name_give']
    address_recieve=request.form['address_give']
    size_recieve=request.form['size_give']
    doc={
        'name':name_receive,
        'address':address_recieve,
        'size':size_recieve
    }
    db.orders.insert_one(doc)
    return jsonify({'msg': 'complete'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    orders_list=list(db.orders.find({},{'_id':False}))
    return jsonify({'orders':orders_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
