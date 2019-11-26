provider = 'mysql'
host = 'localhost'
port = 3306
user = 'root'
password = 'root'
databaseName = 'todoit'

def getDatabaseURI():
    return f'{provider}://{user}:{password}@{host}:{port}/{databaseName}'