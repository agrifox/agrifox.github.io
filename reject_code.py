import config, cgi
frm=cgi.FieldStorage()
id=frm.getvalue('id')
try:
    cur=config.db.cursor()
    cur.execute("UPDATE fcnf SET status=2 WHERE id={} ".format(id))
    config.db.commit()
    config.db.close()
    print ('''<script>
    window.location="afconfirmed1.py?msg=Student data updated successfully"
    </script>''')
except Exception as e:
    print (e)