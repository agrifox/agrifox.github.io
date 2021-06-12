import config, cgi
frm=cgi.FieldStorage()
id=frm.getvalue('id')

try:
    upd="SELECT id FROM wreg"
    cur=config.db.cursor()
    cur.execute(upd)
    config.db.commit()
    config.db.close()
    print '''<script>
    window.location="Form_Output.py?msg=Student data updated successfully"
    </script>'''
except Exception as e:
    print e