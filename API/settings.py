settings = {
    
    'user': "postgres",
    'password': "1111",
    'url': "localhost:5432",
    'dbName': "diary",
    
}

connectionString = 'postgresql://' + settings['user'] + ':' + settings['password'] + '@' + settings['url'] + '/' + settings['dbName']
