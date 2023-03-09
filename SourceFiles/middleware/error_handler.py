
def error_handler(func: object):
    async def wrapper(*args, **kwargs):
        func()
    return wrapper



def er_(func):
    try:
        res = func()
        return res
    except Exception as ex:
        print(ex)
    

