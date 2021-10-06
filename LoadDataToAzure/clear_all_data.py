import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime

import config 
import simplejson as json
import decimal

#this script is to help you load a fairly simple JSON file to DynamoDB
HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']

client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart", user_agent_overwrite=True)
try:
    db = client.create_database(id=DATABASE_ID)
    print('Database with id \'{0}\' created'.format(DATABASE_ID))

except exceptions.CosmosResourceExistsError:
    db = client.get_database_client(DATABASE_ID)
    print('Database with id \'{0}\' was found'.format(DATABASE_ID))
def delete_Container(db, id):
    print("\n6. Delete Container")

    try:
        db.delete_container(id)

        print('Container with id \'{0}\' was deleted'.format(id))

    except exceptions.CosmosResourceNotFoundError:
        print('A container with id \'{0}\' does not exist'.format(id))

    
try:
    delete_Container(db,CONTAINER_ID)
except:
    print("no such container.")