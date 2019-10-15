import MySQLdb
import xlrd
data = xlrd.open_workbook("special.xlsx")
table = data.sheets()[0]
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="Zhchming1",
                  db="fanjian",
                  charset="utf8")
x = conn.cursor()
nrows = table.nrows
for i in range(nrows-1):
   jian = table.cell(i+1, 2).value
   print(jian)
   sql = "INSERT IGNORE INTO sp_jian(jian) VALUES ('%s')" % (jian)
   # sql = "INSERT INTO fan_jian(fan, jian) VALUES ('哈','哈胡')"
   x.execute(sql)
   conn.commit()
# except:
#    conn.rollback()
conn.close()