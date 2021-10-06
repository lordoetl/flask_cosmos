from flask import Flask, jsonify
import run as db_code
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime

import config

HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']
CONTAINER_ID='Items'

app = Flask(__name__)
# Setup Cosmos connection
client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart", user_agent_overwrite=True)

# Create database if doesn't exist
try:
    db = client.create_database(id=DATABASE_ID)
    print('Database with id \'{0}\' created'.format(DATABASE_ID))

except exceptions.CosmosResourceExistsError:
    db = client.get_database_client(DATABASE_ID)
    print('Database with id \'{0}\' was found'.format(DATABASE_ID))

# setup container for this sample
try:
    container = db.create_container(id=CONTAINER_ID, partition_key=PartitionKey(path='/partitionKey'))
    print('Container with id \'{0}\' created'.format(CONTAINER_ID))

except exceptions.CosmosResourceExistsError:
    container = db.get_container_client(CONTAINER_ID)
    print('Container with id \'{0}\' was found'.format(CONTAINER_ID))

# Begin routes
@app.route('/')
def index():
    html=f"""This is the main page.
        <br> These links are for demo only.  If you use this as an api, route directly to the link that returns your data
        <br>  In this case the "get all of the data" link
        <br>
            <br> <a href=do_items/>Only do this once</a> 
            <br> <a href=get-all>get all of the data</a>"""
    return html
    
# @app.route('/get-items/')
# def get_items():
#     return jsonify(db_code.read_items(container))

@app.route('/get-all/')
def get_all():
    data=jsonify(db_code.read_items(container))
    print(data)
    return data


@app.route('/do_items/')
def do_items():
    response=db_code.create_items(container);
    return response

if __name__ == '__main__':
    app.run()
