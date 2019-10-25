from flask import Flask, jsonify, make_response, abort, request
import json, logging, boto3, os, sys, requests, psycopg2

app = Flask(__name__)

@app.route('/api/v1.0/postgres', methods=['POST'])
def post_to_postgres():
    print(request.json)
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    age = request.json['age']

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
    return jsonify({'task': request.json}), 201

if __name__ == '__main__':
    app.run(debug=True)
