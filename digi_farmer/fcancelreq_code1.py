import config, cgi
frm=cgi.FieldStorage()
id=frm.getvalue('id')
fname=frm.getvalue('fname')
try:
    cur=config.db.cursor()
    cur.execute("UPDATE fcnf SET status=3 WHERE id={} ".format(id))
    config.db.commit()
    config.db.close()
    print('''<script>
    window.location="fstatus1.py?fname={}"
    </script>'''.format(fname))
except Exception as e:
    print (e)