import MySQLdb
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="Zhchming1",
                  db="fanjian",
                  charset="utf8")
x = conn.cursor()
f = open('fan_jian.txt','w')
f2 = open("fan.txt", encoding='UTF-8')
line = f2.readline()
while line:
    for i in range(len(line)):
        c = line[i]
        x.execute('select jian from fan_jian where fan ="' + c + '"')
        row = x.fetchone()
        # print(row)
        if (row is None):
            # print(c,end='')
            f.write(c)
        # else: print(row[0],end='')
        else:
            f.write(row[0])
        f.flush()
    line = f2.readline()
f2.close()

