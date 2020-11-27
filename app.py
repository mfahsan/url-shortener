
import json
import string
import random
import os
from flask import Flask, redirect, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
mongo = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


@app.route('/submit', methods=['POST'])
def submit():
	message = json.loads(request.get_data().decode('utf8'))
	body = message['body'] # full URL
	rand = get_random_string(6) #random string for short URL 
	doc = mongo.db.dictionary.insert({ "short": rand, "long": body })
	ret = "Short URL: " + "http://localhost:5000/" + rand + "\n"
	return ret 

 
@app.route('/<short>', methods = ['GET'])
def redirect_to_long(short):
	redir = mongo.db.dictionary.find({"short": short})
	for r in redir:
			return redirect(r["long"])
	return "not a valid URL"

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug =True)


