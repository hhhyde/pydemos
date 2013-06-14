import psycopg2
cxn = psycopg2.connect(user = 'kejiangtao', database = 'dj_demo')
cur = cxn.cursor()
cur.execute('select * from my_cache_table')
rows = cur.fetchall()
row = ''
for r in rows:
    row = row + str(r)
print(row)
