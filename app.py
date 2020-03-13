import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'receipt_book'
app.config["MONGO_URI"] = 'mongodb+srv://mongouser:bbmongo20@myfirstcluster-km3xj.mongodb.net/receipt_book?retryWrites=true&w=majority'
mongo = PyMongo(app)


@app.route('/')
@app.route('/get_receipts')
def get_receipts():
    return render_template("receipts.html", receipts=mongo.db.receipts.find())

@app.route('/add_receipt')
def add_receipt():
    return render_template('addreceipt.html',
                           categories=mongo.db.categories.find(),
                           allergens=mongo.db.allergens.find())
    
@app.route('/insert_receipt', methods=['POST'])
def insert_receipt():
    receipts = mongo.db.receipts
    receipts.insert_one(request.form.to_dict())
    return redirect(url_for('get_receipts'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            