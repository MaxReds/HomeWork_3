def getQueryString(params): 
    keys = sorted(params) 
    query_string = [] 

    for key in keys: 
        query_string.append('{}={}'.format(key, params[key])) 
        return '&'.join(query_string)
params = { 
    'user': 'John', 
    'age': '30', 
    'country': 'US' 
} 
query_string = getQueryString(params) 
print(query_string)