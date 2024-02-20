import mysql.connector as mysql
print()
print('Welcome to the mysql application\nDesigned by Pulkit')
print()
def input_query(a=0):
    global query
    if a==0:
        query = input('mysql> ')
    else:
        query = input('    -> ')
    
    if len(query) == 0:
        Error('P01')
        return 'Error'

    if query[-1] == ';':
        return query
    else:
        return query +' '+ input_query(a=1)
        
def Error(code):
    print()
    print('Error ( '+code+' ) ',end='')
    if code == 'P01':
        print('Query Empty')
    elif code == 'P02':
        print('Invalid Statement')
    print()
        
My_DB = mysql.connect(host='localhost',user='root',password='root')
My_cursor = My_DB.cursor()
while True:
    print()
    q = input_query()
    print(q)
    if q != 'Error':
        try:
            My_cursor.execute(q)
            print('Command Executed')
            print()
        except:
            Error('P02')
    keywords = ['select','show']
    fetch = None
    for i in keywords:
        a = q.lower()
        if a.count(i)!=0 :
            fetch = True
    if fetch == True:
        results = My_cursor.fetchall()
        for i in results:
            if len(i) ==1:
                print(i[0])
            else:
                print(i)
