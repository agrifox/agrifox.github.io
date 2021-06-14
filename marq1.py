import cgi
import config
frm=cgi.FieldStorage()
crop=frm.getvalue('crop')
cursor=config.db.cursor()
cursor.execute("SELECT * FROM rate")
rs=cursor.fetchall()
rec=rs[0]
print ('''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>rates</title>
</head>

<body>
<marquee bgcolor="brown" style="color: white; width=100%;" onmouseover="this.stop()" onmouseout="this.start()">
Rate List:''')

for rec in rs:
    print ('''
  
   {} = Rs. {}/kg,
  
  '''.format(rec[0],rec[1]))
print ('''
</marquee>
</body>
</html>''')
frm=cgi.FieldStorage()
