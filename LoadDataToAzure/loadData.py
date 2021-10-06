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

# setup container for this sample
def delete_Container(db, id):
    print("\n6. Delete Container")

    try:
        db.delete_container(id)

        print('Container with id \'{0}\' was deleted'.format(id))

    except exceptions.CosmosResourceNotFoundError:
        print('A container with id \'{0}\' does not exist'.format(id))

    
try:
    delete_Container(db,CONTAINER_ID)
    container = db.create_container(id=CONTAINER_ID, partition_key=PartitionKey(path='/partitionKey'))
    print('Container with id \'{0}\' created'.format(CONTAINER_ID))

except exceptions.CosmosResourceExistsError:
    container = db.get_container_client(CONTAINER_ID)
    print('Container with id \'{0}\' was found'.format(CONTAINER_ID))

file="moviedata.json" #full path to your json data

#this will loop through your file and put_item each row into your table
#note taht you have to make sure you are "putting" your key and
#you have to add the columnnames for each item
with open(file) as json_file:  
    movies = json.load(json_file)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']
        event = str(year)+title
        id=title.replace("/","").replace(" ","")

        print("Adding movie:", year, title)
        try:
            container.create_item(
            body={
                'id':id,
                'event':event,
                'year': year,
                'title': title,
                'info': info,
                }
            )
        except:
            print('oops')
