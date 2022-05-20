def requestGroup(sn_credential, sn_env):
    import requests
    import json

    params = {
        'sysparm_query': 'group.nameSOC Blue',
        'sysparm_limit': '500',
        'sysparm_display_value': 'all',
        'sysparm_fields': 'user,group'
    }
    headers = {
         'Authorization': 'Basic ' + sn_credential,
         'Content-Type':  'application/json',
         'Accept':        'application/json'
    }
    url = 'https://' + sn_env + '.service-now.com/api/now/v2/table/sys_user_grmember'
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code != 200:
            print('Status:', response.status_code, 'Headers:',
                  response.headers, 'Error Response:', response.json())
            exit()
    
    data = response.json()       
    rawData = data
    resultData = ''
    returnData = 'Successful'
    keyfields = data
    contextData = ''
    error = ''
    return pb.returnOutputModel(resultData, returnData, keyfields, contextData, rawData, error)
