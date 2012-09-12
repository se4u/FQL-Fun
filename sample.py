import fbnlpdata
import re
import word2num
import string

def find_table(inp):
    #Try to find " my "
    f_my = re.search(" my ", inp )
    f_friend = re.search("friend", inp)
    f_family = re.search( "family", inp)
    if f_my != None and f_friend == None and f_family == None:
        #just me
        return(fbnlpdata.FQL_DB_SCHEMA['user']['output'])
    elif f_friend != None and f_family != None:
        #friend and family, don't handle
        raise Exception(fbnlpdata.TOO_MUCH_DETAIL)
    elif f_my == None and f_friend == None and f_family == None:
        #Noone, dont handle
        raise Exception(fbnlpdata.ASK_FOR_MORE_INFO)
    elif f_friend != None:
        #return friends
        return(fbnlpdata.FQL_DB_SCHEMA['friend']['output'])
    else:# f_family != None
        #return family
        return(fbnlpdata.FQL_DB_SCHEMA['family']['output'])

def extract_limit(inp):
    inp = inp.lower().strip()
    limit = None
    # try to find actually digital numbers
    digitalNumber = re.findall( ' \d+ ', inp)
    if len(digitalNumber) > 0:
        assert len(digitalNumber) == 1
        return(int(digitalNumber[0].strip()))

    tokenArr = re.split('[ -]', inp)
    limitString = ''
    for token in tokenArr:
        if token in word2num._known.keys() or token == 'and':
            limitString += (token + ' ')
    if limitString is "": return(None)
    return(word2num.spoken_word_to_number(limitString))

def fqlmaker(inp):
    try:
        table = find_table(inp)
    except Exception as e:
        return(e.args[0])
    confidence = 1
    if table is None:
        confidence = 0
        query = fbnlpdata.ASK_FOR_MORE_INFO
    else:
        confidence = 1#confidence/len(tables)

    query = ''
    for i, v in enumerate(table):
        template = 'SELECT {v.columns} FROM {v.name} WHERE {v.filter}'
        if i == 0:
            template += ' = me()'
        else:
            template += ' IN ({v.query})'
        v['columns'] = ", ".join(v['column'])
        v['query'] = query
        v = AttributeDict(v)
        query = template.format(v=v)

    limit = extract_limit(inp)
    if limit is not None:
        query += (' LIMIT ' + str(limit))
    output = query
    return(output)

class AttributeDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
