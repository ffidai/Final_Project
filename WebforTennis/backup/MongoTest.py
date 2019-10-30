from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo


# Use PyMongo to establish Mongo connection
#mongo = PyMongo(app, uri="mongodb://localhost:27017/misson_to_mars_app")


# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_app


db.mars_data.insert_one(
{
    'name': 'Ahmed',
    'row': 3,
    'favorite_python_library': 'Matplotlib',
    'hobbies': ['Running', 'Stargazing', 'Reading']
}
)
    #mongo.db.mars_data.update({}, results, upsert=True)

