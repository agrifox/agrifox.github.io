import config
import cgi, cgitb
frm=cgi.FieldStorage()
id=frm.getvalue('id')
fname=frm.getvalue('fname')
wname=frm.getvalue('wname')
crop=frm.getvalue('crop')
rate=frm.getvalue('rate')
quant=frm.getvalue('quant')
cost=frm.getvalue('cost')
status=frm.getvalue('status')

try:
    cursor=config.db.cursor()
    sql="INSERT INTO fcnf (fname,wname,crop,rate,quant,cost)VALUES ('%s','%s','%s','%s','%s','%s')"%(fname,wname,crop,rate,quant,cost)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        print ('''<script>
        window.location="fstatus1.py?fname={}"
        </script>'''.format(fname))
except Exception as e:
    print (e)
