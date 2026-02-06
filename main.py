from random import randint,uniform,choice


def intlist(list_length : int,min_value : int,max_value : int) -> list[int]:
    if not isinstance(min_value,int) or not isinstance(max_value,int) or not isinstance(list_length,int):
        raise TypeError('list lenght, maximun and minimun must be integer')
    if list_length < 0:
        raise ValueError("List lenght needs to be 0 or higher")
    if min_value > max_value:
        raise ValueError("Minimum value must to be <=  max value")
        
    return[randint(min_value,max_value) for _ in range(list_length)]
    
def floatlist(list_length : int, min_value: float, max_value: float, places: int= 2) -> list[float]:
    if not isinstance(list_length,int):
        raise TypeError('List legnth needs to be integer')
    if not isinstance(places,int):
        raise TypeError('Places must be an integer')
    if not isinstance(min_value,int) and not isinstance(min_value,float):
        raise TypeError('Minimun value must be integer or float')
    if not isinstance(max_value,int) and not isinstance(max_value,float):
        raise TypeError('Maximun value must be integer or float')
    if list_length < 0:
        raise ValueError("List lenght needs to be 0 or higher")
    if min_value > max_value:
        raise ValueError("Minimum value must to be <=  max value")
    if places < 0:
        raise ValueError("Places must be >= 0")
    
    return [round(uniform(min_value,max_value),places) for _ in range(list_length)]

def boolist(list_length :int,one =True, zero =False):#scmt
    if not isinstance(list_length,int):
        raise TypeError('List legnth needs to be integer')
    
    binary = [one,zero]
    
    return [choice(binary) for _ in range(list_length)]