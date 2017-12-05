my_dict = {'name': 'ahmed', 'age':'25', 'country':'Ukraine', 'city':'Kharkiv', 'work':'QA'}
def dict_1(slovar, keys):
    if keys in slovar:
        return slovar[keys]
    else:
        return None

print dict_1(my_dict, 'work')
QA
