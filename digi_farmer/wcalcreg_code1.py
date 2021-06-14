import config
import cgi, cgitb
frm=cgi.FieldStorage()
id=frm.getvalue('id')
wname=frm.getvalue('wname')
fname=frm.getvalue('fname')
crop=frm.getvalue('crop')
rate=frm.getvalue('rate')
quant=frm.getvalue('quant')
cost=frm.getvalue('cost')
status=frm.getvalue('status')

try:
    cursor=config.db.cursor()
    sql="INSERT INTO wcnf (wname,fname,crop,rate,quant,cost)VALUES ('%s','%s','%s','%s','%s','%s')"%(wname,fname,crop,rate,quant,cost)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        print ('''<script>
        window.location="wstatus1.py?wname={}"
        </script>'''.format(wname))
except Exception as e:
    print (e)
