TOKEN ="Your Token"

URL_RANK ='http://3on3rank.fsgames.com/rank'
URL_DETAIL = 'http://3on3rank.fsgames.com/rank/detail'

TYPE_USER_INFO = int(1)

TYPE_USER_SCORE = int(2)
TYPE_USER_MATCH_LOG = int(3)
TYPE_CREW_INFO = int(4)
TYPE_CREW_SCORE = int(5)
TYPE_CREW_MATCH_LOG = int(7)
TYPE_CREW_MEMBER = int(8)

USER_SCORE_COMMAND = { # number is api's period value (period)
    1 : {'COMMAND' : '!score_t ', 'SCRIPT' : 'TOTAL'}, #SCORE_TOTAL
    2 : {'COMMAND' : '!score_n ', 'SCRIPT' : 'Now Session'}, #SCORE_NOW
    3 : {'COMMAND' : '!score_p ', 'SCRIPT' : 'Past Session'} #SCORE_PAST
}

CREW_SCORE_COMMAND = { # number is api's period value (period)
    1 : {'COMMAND' : '!crew_score_t ', 'SCRIPT' : 'TOTAL'}, #SCORE_TOTAL
    2 : {'COMMAND' : '!crew_score_n ', 'SCRIPT' : 'Now Session'}, #SCORE_NOW
    3 : {'COMMAND' : '!crew_score_p ', 'SCRIPT' : 'Past Session'} #SCORE_PAST
}

MATCH = {
    0 : 'LOSE',
    1 : 'WIN'
}

MODE ={
    0 : 'Co-op MATCH'
}
CHARACTER = {
    0 : {'CHARACTER' : '','POSITION' : ''},    
    1 : {'CHARACTER' : 'Luther','POSITION' : '[C]'},
    2 : {'CHARACTER' : 'Bigdog','POSITION' : '[C]'},
    3 : {'CHARACTER' : 'Lee','POSITION' : '[C]'},
    4 : {'CHARACTER' : 'Clarke','POSITION' : '[PF]'},
    5 : {'CHARACTER' : 'Murdock','POSITION' : '[PF]'},
    6 : {'CHARACTER' : 'Lulu','POSITION' : '[PF]'},
    7 : {'CHARACTER' : 'Amanda','POSITION' : '[SF]'},
    8 : {'CHARACTER' : 'Joey','POSITION' : '[SF]'},
    9 : {'CHARACTER' : 'William','POSITION' : '[SF]'},
    10 : {'CHARACTER' : 'Kim','POSITION' : '[SG]'},
    11 : {'CHARACTER' : 'Pedro','POSITION' : '[PG]'},
    12 : {'CHARACTER' : 'Cindy','POSITION' : '[PG]'},
    13 : {'CHARACTER' : 'Helena','POSITION' : '[PG]'},
    14 : {'CHARACTER' : 'Carolina','POSITION' : '[SG]'},
    15 : {'CHARACTER' : 'Fred','POSITION' : '[SG]'},
    16 : {'CHARACTER' : 'Christa','POSITION' : '[C]'},
    17 : {'CHARACTER' : 'PROFESSOR','POSITION' : '[PG]'},
    18 : {'CHARACTER' : 'Rin','POSITION' : '[SG]'},
    19 : {'CHARACTER' : 'Carter','POSITION' : '[SF]'},
    20 : {'CHARACTER' : 'Jason','POSITION' : '[SG]'},
    21 : {'CHARACTER' : 'Max','POSITION' : '[PF]'},
    22 : {'CHARACTER' : 'Rebecca','POSITION' : '[SF]'},
    23 : {'CHARACTER' : 'Little Fox','POSITION' : '[PG]'},
    24 : {'CHARACTER' : 'Jimmy','POSITION' : '[C]'},
}
