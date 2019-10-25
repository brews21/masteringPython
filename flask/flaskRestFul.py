from flask import Flask, jsonify, make_response, abort, request
import json, logging, boto3, os, sys, requests, psycopg2
from flask_restful import abort, Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class MikeyB(Resource):
    def get(self):
        return {'name': 'mikeyb'}

class post_to_postgres(Resource):
    def get(self):
        args = request.get_json()
        return {args}

    def post(self):
        args = request.get_json()
        print(f'ARGS Are :::: {args}')
        first_name = args['first_name']
        last_name = args['last_name']
        age = args['age']

        hostname = 'localhost'
        conn = psycopg2.connect(dbname='test', user='postgres', password='password', host=hostname)
        # Open a cursor to perform database operations
        cur = conn.cursor()
        # Execute a command: this creates a new table
        # cur.execute("DROP TABLE IF EXISTS common.mikeyb cascade; CREATE TABLE common.mikeyb (id serial PRIMARY KEY, num integer, data varchar);")
        cur.execute("INSERT INTO common.mikeyb (first_name, last_name, age) VALUES (%s, %s, %s)",(first_name, last_name, age))
        # cur.execute("SELECT * FROM common.mikeyb;")
        # Make the changes to the database persistent
        conn.commit()
        # Close communication with the database
        cur.close()
        conn.close()
        return {'task': args}, 201

api.add_resource(HelloWorld, '/')
api.add_resource(MikeyB, '/mikeyb')
api.add_resource(post_to_postgres, '/post_to_postgres')

if __name__ == '__main__':
    app.run(debug=True, port='8000')#, host='0.0.0.0')
