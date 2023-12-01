roster = {
        'STATS_385': ['Jack', 'Anne', 'John', 'Peter'],
        'PROG_388': ['Tom', 'Mark', 'Jack', 'Jin'],
        'LARGESCALE_487': ['Anne', 'John', 'Jin', 'Jack']
}
# d['Jack'] = ['STATS_385']
# d['Anne'] = ['STATS_385']
# ...
# d['Tom'] = ['PROG_388']    
# d['Mark'] = ['PROG_388']        
# d['Jack'].append('PROG_388') -> d['Jack'] = ['STATS_385', 'PROG_388']
    
d = dict()
for key in roster:
    names = roster[key]
    for name in names:
        # For the first time, we have the name, need to create the key and put the vlue
        if name not in d:
            d[name] = [key]
        # After the first time, we need to append the value to the existing list
        else:
            d[name].append(key)


print(d)        