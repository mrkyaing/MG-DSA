def add(x,y):return x+y
def sub(x,y):return x-y

operations={
    'add':add,
    'sub':sub
}

print(operations['add'](10,10))