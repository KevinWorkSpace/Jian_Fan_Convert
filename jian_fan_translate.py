import jieba
import MySQLdb
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="Zhchming1",
                  db="fanjian",
                  charset="utf8")
x = conn.cursor()
f = open('jian_fan.txt','w')
f2 = open("jian.txt", encoding='UTF-8')
line = f2.readline()
while line:
    seg_list = jieba.cut(line, cut_all=False, HMM=True)
    text = " ".join(seg_list)
    text_split = text.split(' ')
    for i in range(len(text_split)):
        word = text_split[i]
        x.execute('select fan from jian_fan where jian ="' + word + '"')
        row = x.fetchone()
        if (row is None):
            for j in range(len(word)):
                c = word[j]
                x.execute('select fan from fan_jian where jian ="' + c + '"')
                row2 = x.fetchone()
                if (row2 is None):
                    f.write(c)
                    # print(c, end='')
                else:
                    f.write(row2[0])
                    # print(row2[0], end='')
        else:
            f.write(row[0])
            # print(row[0], end='')
    line = f2.readline()
f2.close()

