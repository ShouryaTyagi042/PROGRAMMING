path = input("Enter your txt file path :")
fh = open(path,"r")
records = fh.read().splitlines()
# print(record)
for record in records :
    data = record.split("||")
    # print(data)
    query = "insert into student(FirstName,LastName,MainsRank,College,Branch) values(%s,%s,%s,%s,%s)"
    values = (data[0],data[1],data[2],data[3],data[4])
    mycursor.execute(query,values)
    mydb.commit()
