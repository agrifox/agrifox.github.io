import config
import cgi, cgitb
frm=cgi.FieldStorage()
id=frm.getvalue('id')
fname=frm.getvalue('fname')
wname=frm.getvalue('wname')
crop=frm.getvalue('crop')
quant=frm.getvalue('quant')
fadd=frm.getvalue('fadd')
wadd=frm.getvalue('wadd')
dist=frm.getvalue('dist')
tcost=frm.getvalue('tcost')
status=frm.getvalue('status')

try:
    cursor=config.db.cursor()
    sql="INSERT INTO tcnf (fname,wname,crop,quant,fadd,wadd,dist,tcost)VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')"%(fname,wname,crop,quant,fadd,wadd,dist,tcost)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        print ('''<script>
        window.location="ftransstatus1.py?fname={}"
        </script>'''.format(fname))
except Exception as e:
    print (e)
