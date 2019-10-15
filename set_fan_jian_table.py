import MySQLdb
import xlrd

data = xlrd.open_workbook("Simplified_Traditional_onlydif.xlsx")
table = data.sheets()[0]

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="Zhchming1",
                  db="fanjian",
                  charset="utf8")
x = conn.cursor()
# 使用 execute()  方法执行 SQL 查询
x.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = x.fetchone()
print("Database version : %s " % data)
# try:
nrows = table.nrows
# a = table.cell(1, 2).value
for i in range(nrows-1):
   jian = table.cell(i+1, 2).value
   fan = table.cell(i+1, 3).value
   print(fan, jian)
   sql = "INSERT IGNORE INTO fan_jian(fan, jian) VALUES ('%s','%s')" % (fan, jian)
   x.execute(sql)
   conn.commit()
# except:
#    conn.rollback()
conn.close()