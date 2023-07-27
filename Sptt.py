for x in range(1,101):
    i = "" 
    if x % 3 == 0:
        i = 'fizz'
    if x % 3 == 0:
        i += 'buzz'
        #continue 
    print(x if not i else i)   
