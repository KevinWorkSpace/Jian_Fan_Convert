import jieba
import MySQLdb
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="Zhchming1",
                  db="fanjian",
                  charset="utf8")
x = conn.cursor()
dict = {}
f2 = open('hong_jian.txt', encoding='UTF-8')
line = f2.readline()
while line:
    seg_list = jieba.cut(line, cut_all=False, HMM=True)
    text = " ".join(seg_list)
    text_split = text.split(' ')
    for i in range(len(text_split)):
        word = text_split[i]
        if(len(word) >= 2):
            for k in range(len(word)):
                c = word[k]
                x.execute('select jian from sp_jian where jian ="'+c+'"')
                row = x.fetchone()
                if (row is None):
                    pass
                else:
                    if(dict.get(word) is None):
                        dict[word] = 1
                    else:
                        dict[word] = dict[word] + 1
                break
    line = f2.readline()
f2.close()
print(dict)
f22 = open('hong_fan.txt', encoding='UTF-8')
f11 = open('hong_jian.txt', encoding='UTF-8')
line = f11.readline()
line2 = f22.readline()
while line:
    seg_list = jieba.cut(line, cut_all=False, HMM=True)
    text = " ".join(seg_list)
    text_split = text.split(' ')
    for i in range(len(text_split)):
        word = text_split[i]
        if((len(word) >= 2) & (dict.get(word) is not None)):
            if(dict.get(word) >= 20):
                pos = line.find(word)
                fan = line2[pos:pos+len(word)]
                print(word, fan)
                sql = "INSERT IGNORE INTO jian_fan(jian, fan) VALUES ('%s','%s')" % (word, fan)
                x.execute(sql)
                conn.commit()
    line = f11.readline()
    line2 = f22.readline()