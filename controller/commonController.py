import requests
import json

#common fn for get basic data ============================
def getBasic_apiData(url, params):
    res_data = api_call(url, params)
    
    try:
        data = res_data['data'][0] #get crew_sn on data param
    except KeyError: # if no search user id, return none
        return None

    return data
#============================================================

def api_call(url, params):
    res = requests.post(url, data = params) #request Post
    res_data = json.loads(res.text) #transform json
    return res_data

#=====logging...=====
def on_message_log(message, keyword):
    print('==========[  on_message log  ]==========')
    print('request user     - ', message.author)
    print('request keyword  - ', keyword)
    print('==========[  on_message log  ]==========')
#=====logging...=====