import os
import ex5

def function6(target, to_search, callback):
    try:
        return ex5.ex5(target,to_search)
    except Exception as e:
        callback(e)
        return []

print(function6("C:\\Users\\Alin\\Desktop\\Anul3\\Python\\Lab1", "alabala", print))