import controller.commonController as common
import math
import constants as con

def getCrew_info(crew_id):
    #request crew info on basic crew param
    params = {
        'type' : con.TYPE_CREW_INFO,
        'searchValue': crew_id
    }
    #api call
    crew_info = common.getBasic_apiData(con.URL_RANK, params)
    return crew_info

def getCrew_score(crew_sn, scoreType):
    params = {
        'type' : con.TYPE_CREW_SCORE,
        'crewSN' : crew_sn,
        'period' : scoreType
        }
    #api call
    res_data = common.api_call(con.URL_DETAIL, params)
    user_score = res_data['data'] #filter param in 'data'
    return user_score

def getCrew_matchLog(crew_sn):
    params = {
        'type' : con.TYPE_CREW_MATCH_LOG,
        'crewSN' : crew_sn
        }
    res_data = common.api_call(con.URL_DETAIL, params)
    crew_matchLog = res_data['data']
    return crew_matchLog

def getCrew_members(crew_sn):
    params = {
        'type' : 8,
        'crewSN' : crew_sn,
        'curPage' : 1
        }
    res_data = common.api_call(con.URL_DETAIL, params)
    totalCount = res_data['totalCount']
    endPage = math.ceil(res_data['totalCount'] / 10)
    member_list =  res_data['data']

    for i in range(2, endPage + 1):
        params = {
            'type' : 8,
            'crewSN' : crew_sn,
            'curPage' : i
        }
        #api call
        res_data = common.api_call(con.URL_DETAIL, params)
        for j in res_data['data']:
            member_list.append(j)
    return member_list, totalCount