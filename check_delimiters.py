


def check_delimiters(input, measure = None):
    #credit: joseph alexander naidoo
    m = (measure, 42)[measure == None]
    try:
        m = type(m)(m)
        input = type(input)(input)

        try:
            if str(input).isprintable() is True:
                if False not in [False for i in range(0,len(str(input)),1) if str(str(input)[i]) not in list([str(str(chars)[k]) for k in range(0,len(str(chars)),1)])]:
                    if type(type(input)(input)) is list and type(list(type(input)(input))[0]) is str:
                        input = str(list(type(input)(input))[0])
                    input = str(input)
        except:
            pass
    #except Exception as e:
        #return e
    except:
        pass
    
    results_dict = {'password': str(input), 'password_length': int(len(str(input)))}
    delimiter_check = {'delimiter': False, 'character': '', 'count': 0, 'spacing': 0}
    
    try:
        if len(str(input)) < int(m):
            for i in [2,3,4,5,6,7,8,9]:
                if str(str(input)[i]) is str(str(input)[int(i*2)+1]):
                    comparisons = list([str(str(input)[k]) for k in range(i,len(str(input)),i+1)])
                    if False not in [
                        False for k in range(0,len(list(comparisons)),1) if str(str(input)[i]) is not str(list(comparisons)[k])
                    ] and len(str(input)) is int(int(len(list(comparisons)))+int(int(int(len(list(comparisons)))+1)*int(i))):
                        delimiter_check.update(
                            {'delimiter': True,
                             'character': str(str(input)[i]),
                             'count': int(len(list(comparisons))),
                             'spacing': int(i)})
    except:
        pass
    
    results_dict.update({'delimiter_check': dict(delimiter_check), 'inputs': []})
    
    try:
        if bool(dict(delimiter_check)['delimiter']) is True:
            inputs = list(str(input).split(str(dict(delimiter_check)['character']), int(dict(delimiter_check)['count'])))
        else:
            inputs = [str(input)]
    #except Exception as e:
        #return e
    except:
        pass
    
    results_dict['inputs'] = list(inputs)
    
    return results_dict




