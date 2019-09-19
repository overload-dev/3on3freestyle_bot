import controller.commonController as common
import constants as con

def getUser_info(user_id):
    #request user info on basic user param
    params = {
        'type' : con.TYPE_USER_INFO,
        'searchValue': user_id
    }
    #api call
    user_info = common.getBasic_apiData(con.URL_RANK, params)

    return user_info

def getUser_score(user_sn):
    #request detail user info on basic user param
    params = {
        'type' : con.TYPE_USER_SCORE,
        'userSN' : user_sn
        }

    #api call
    res_data = common.api_call(con.URL_DETAIL, params)
    user_score = res_data['data'][0] #filter param in 'data'

    return user_score

def getUser_matchLog(user_sn):
    params = {
        'type' : con.TYPE_USER_MATCH_LOG,
        'userSN' : user_sn
    }
    res_data = common.api_call(con.URL_DETAIL, params)
    user_matchLog = res_data['data'] #filter param in 'data'

    return user_matchLog
