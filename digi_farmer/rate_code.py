import config, cgi
frm=cgi.FieldStorage()
wheat=frm.getvalue('wheat')
rice=frm.getvalue('rice')
moong=frm.getvalue('moong')
arhar=frm.getvalue('arhar')
oats=frm.getvalue('oats')
try:
    upd="UPDATE student SET wheat='{}',rice='{}',moong='{}',arhar='{}',oats='{}'".format(wheat,rice,moong,arhar,oats)
    cur=config.db.cursor()
    cur.execute(upd)
    config.db.commit()
    config.db.close()
    print '''<script>
    window.location="rate.py?msg=Rates data updated successfully"
    </script>'''
except Exception as e:
    print e