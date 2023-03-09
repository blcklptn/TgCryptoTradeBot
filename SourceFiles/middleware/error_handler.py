
def er_(func):
    try:
        res = func()
        return res
    except Exception as ex:
        print(ex)
    

