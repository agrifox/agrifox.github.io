import config, cgi
frm=cgi.FieldStorage()
id=frm.getvalue('id')
wname=frm.getvalue('wname')
try:
    cur=config.db.cursor()
    cur.execute("UPDATE wcnf SET status=3 WHERE id={} ".format(id))
    config.db.commit()
    config.db.close()
    print('''<script>
    window.location="wstatus1.py?wname={}"
    </script>'''.format(wname))
except Exception as e:
    print (e)