import cgi, config
frm=cgi.FieldStorage()
crop=frm.getvalue('crop')
cursor=config.db.cursor()
cursor.execute("SELECT * FROM rate WHERE crop='{}'".format(crop))
rs=cursor.fetchone()
if rs:
    print('''<input type="text" class="form-control" value="{}" name="rate" id="rate" readonly>'''.format(rs[1]))
else:
    print("")