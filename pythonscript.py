#!/bin/python

import pandas as pd
import prettytable
import psycopg2
import csv
conn = psycopg2.connect(database="db_admin", user="db_admin", host="192.168.20.2")
cur = conn.cursor()
cur.execute("SELECT a.id, b.name, c.type, d.author FROM articles as a JOIN magazines as b ON b.id = a.magazines_id JOIN article_types as c ON c.id = a.article_type_id JOIN author as d ON d.id = a.author_id")

myData = cur.fetchall()

myFile = open('articles.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)

with open('articles.csv', newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('articles.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['id', 'magazines', 'article_type', 'author'])
    w.writerows(data)


from prettytable import from_csv
with open('articles.csv') as fp:
    t = from_csv(fp)
    fp.close()


code = t.get_html_string(attributes={"id":"my_table", "class":"green_table"})
html_file = open('/var/www/articles-final.com/html/index.html', 'w')
