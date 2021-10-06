import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://demo-dataviz.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', '8P4ViC6iioxDQEiXiq78PLGfxafOalaD33fPVMecl3IIIlmmuViGSDeqex1WauYFIAkPDF4hrFTxg7FyIqIt3g=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}