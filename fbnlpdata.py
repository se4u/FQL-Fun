ASK_FOR_MORE_INFO = 'please provide more details'
TOO_MUCH_DETAIL = 'please ask for less information, try to break query in two parts'

FQL_DB_SCHEMA = {
    'user': {
        'name': 'user',
        'synonyms': ['user', 'name'],
        'columns': {
            'uid':['id'],
            'name':['name'],
            'pic_square':['picture', 'pic']
            },
         'output':[{
             'name': 'user',
             'filter': 'uid',
             'column': ['name', 'pic_square']}]
        },
    'friend': {
        'name': 'friend',
        'synonyms': ['friend'],
        'columns': {
            },
        'output': [{
             'name': 'friend',
             'filter': 'uid1',
             'column': ['uid2']},
             {
             'name': 'user',
             'filter': 'uid',
             'column': ['name', 'pic_square']}],
        },
    'family': {
        'name': 'family',
        'synonyms': ['family'],
        'columns': {
            'uid': ['id'],
            'name': ['name'],
            'birthday': ['birthday', 'bday'],
            'relationship': ['relation'],
            },
         'output':[{
             'name': 'family',
             'filter': 'profile_id',
             'column': ['uid']},
             {
             'name': 'user',
             'filter': 'uid',
             'column': ['name', 'pic_square']}],

        },
    'checkin': {
        'name': 'checkin',
        'synonyms': ['checkin'],
        'columns': {
            'coords':['location'],
            'timestamp':['time'],
            'tagged_uids':['others', 'everyone'],
            'message':['status', 'message']
            }
        },
    'status': {
        'name': 'status',
        'synonyms': ['status'],
        'columns': {
            'uid':['id', 'owner'],
            'time':['time'],
            'source':['application', 'source'],
            'status_id':['status id'],
            'message':['status']
            }
        },
    }

samples = [
        {'input': '', 'output': {
            'query':'please provide more details',
            'confidence':1,
            'table': None,
            'limit': None
             }},
        {'input': 'Show Top 20 friends',
         'output': {
             'query':'SELECT name, pic_square FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me()) LIMIT 20',
             'confidence':1,
             'table': [{
                 'name': 'friend',
                 'filter': 'uid1',
                 'column': ['uid2']},
                 {
                 'name': 'user',
                 'filter': 'uid',
                 'column': ['name', 'pic_square']}],
             'limit': 20
             }},
        # {'input': 'show my name',
        #  'output': {
        #      'query':'SELECT name FROM user WHERE uid = me()',
        #      'confidence':1,
        #      'table': [{
        #          'name': 'user',
        #          'filter': 'uid',
        #          'column': ['name']}],
        #          'limit': None
        #      }},
        {'input': 'show name',
         'output': {
             'query':'please provide more details',
             'confidence':0,
             'table': None,
             'limit':None
             }},
        {'input': 'show all my family members',
         'output': {
             'query':'SELECT name, pic_square FROM user WHERE uid IN (SELECT uid FROM family WHERE profile_id = me())',
             'confidence':1,
             'table': [{
                 'name': 'family',
                 'filter': 'profile_id',
                 'column': ['uid']},
                 {
                 'name': 'user',
                 'filter': 'uid',
                 'column': ['name', 'pic_square']}],
             'limit':None
             }},
        {'input': 'show ten of my friends',
         'output': {
             'query':'SELECT name, pic_square FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me()) LIMIT 10',
             'confidence':1,
             'table': [{
                 'name': 'friend',
                 'filter': 'uid1',
                 'column': ['uid2']},
                 {
                 'name': 'user',
                 'filter': 'uid',
                 'column': ['name', 'pic_square']}],
             'limit':10
             }},
        {'input': 'show all of my friends',
         'output': {
             'query':'SELECT name, pic_square FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())',
             'confidence':1,
             'table': [{
                 'name': 'friend',
                 'filter': 'uid1',
                 'column': ['uid2']},
                 {
                 'name': 'user',
                 'filter': 'uid',
                 'column': ['name', 'pic_square']}],
             'limit':None
             }},
        {'input': 'Show my friends',
         'output': {
             'query':'SELECT name, pic_square FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())',
             'confidence':1,
             'table': [{
                 'name': 'friend',
                 'filter': 'uid1',
                 'column': ['uid2']},
                 {
                 'name': 'user',
                 'filter': 'uid',
                 'column': ['name', 'pic_square']}],
             'limit':None
             }},
        {'input': 'show 10 of my friends',
         'output': {
             'query':'SELECT name, pic_square FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me()) LIMIT 10',
             'confidence':1,
             'table': [{
                 'name': 'friend',
                 'filter': 'uid1',
                 'column': ['uid2']},
                 {
                 'name': 'user',
                 'filter': 'uid',
                 'column': ['name', 'pic_square']}],
             'limit':10
             }},
        {'input': 'show top 10 of my friends',
         'output': {
             'query':'SELECT name, pic_square FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me()) LIMIT 10',
             'confidence':1,
             'table': [{
                 'name': 'friend',
                 'filter': 'uid1',
                 'column': ['uid2']},
                 {
                 'name': 'user',
                 'filter': 'uid',
                 'column': ['name', 'pic_square']}],
             'limit': 10
             }},
        {'input': 'show my 10 friends',
         'output': {
             'query':'SELECT name, pic_square FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me()) LIMIT 10',
             'confidence':1,
             'table': [{
                 'name': 'friend',
                 'filter': 'uid1',
                 'column': ['uid2']},
                 {
                 'name': 'user',
                 'filter': 'uid',
                 'column': ['name', 'pic_square']}],
             'limit': 10
             }},
        {'input': 'display all of my friends',
         'output': {
             'query':'SELECT name, pic_square FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())',
             'confidence':1,
             'table': [{
                 'name': 'friend',
                 'filter': 'uid1',
                 'column': ['uid2']},
                 {
                 'name': 'user',
                 'filter': 'uid',
                 'column': ['name', 'pic_square']}],
             'limit':None
             }},
    ]
