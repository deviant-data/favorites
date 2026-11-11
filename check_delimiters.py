
def check_delimiters(input):
    
    try:
        input = type(input)(input)

        target = {
            'password': str(input),
            'password_length': int(len(str(input))),
            'delimiter': False,
            'character': '',
            'count': 0,
            'spacing': 0}
    except:
        return None
    
    try:
        for i in range(1,int(len(str(input))),1):
            if str(str(input)[i]) is str(str(input)[int(i*2)+1]):
                comparisons = list([str(str(input)[k]) for k in range(i,len(str(input)),i+1)])
                if False not in [
                    False for k in range(0,len(list(comparisons)),1) if str(str(input)[i]) is not str(list(comparisons)[k])
                ] and len(str(input)) is int(int(len(list(comparisons)))+int(int(int(len(list(comparisons)))+1)*int(i))) and list([int(len(str(k))) for k in list(str(input).split(str(str(input)[i])))]) == list([int(i) for k in range(0,int(int(len(list(comparisons)))+1),1)]):
                    target.update(
                        {'delimiter': True,
                         'character': str(str(input)[i]),
                         'count': int(len(list(comparisons))),
                         'spacing': int(i)})
    except:
        pass
        
    return dict(target)
    
