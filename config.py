import os
# PUt all of you settings here
# settings = {
#     'host': os.environ.get('ACCOUNT_HOST', 'https://demo-dataviz.documents.azure.com:443/'),
#     'master_key': os.environ.get('ACCOUNT_KEY', ''),
#     'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
#     'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
# }

settings = {
    'host': os.environ['ACCOUNT_HOST'],
    'master_key': os.environ['ACCOUNT_KEY'],
    'database_id': os.environ['COSMOS_DATABASE'],
    'container_id': os.environ['COSMOS_CONTAINER'],
}