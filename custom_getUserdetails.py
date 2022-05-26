def custom_getUserdetails(sn_env, sn_user, sn_user_name, sn_email_user):
    import requests
    import json
    
    params = {
        'sysparm_query': 'user_name =' + sn_user,
        'sysparm_query': 'name =' + sn_user_name,
        'sysparm_query': 'email =' + sn_email_user,
        'sysparm_fields': 'sys_id',
        'sysparm_limit': '1',
        'sysparm_display_value': 'all'
    }
    headers = {
         'Content-Type':  'application/json',
         'Accept':        'application/json'
         
    }
    HEADERS = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    AUTH = (runtime['connector']['username'], runtime['connector']['password'])
    url = 'https://' + sn_env + '.service-now.com/api/now/v2/table/sys_user'
    response = requests.get(url, params=params, headers=headers, auth=AUTH, verify=False)
    
    if response.status_code != 200:
            print('Status:', response.status_code, 'Headers:',
                  response.headers, 'Error Response:', response.json())
            exit()
    
    data = response.json()
    
    
    
    rawData = data
    resultData = data
    returnData = 'Successful'
    keyfields = data
    contextData = ''
    error = ''
    return pb.returnOutputModel(resultData, returnData, keyfields, contextData, rawData, error)