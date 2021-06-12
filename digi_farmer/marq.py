import cgi
import config
frm=cgi.FieldStorage()
wheat=frm.getvalue('wheat')
rice=frm.getvalue('rice')
moong=frm.getvalue('moong')
arhar=frm.getvalue('arhar')
oats=frm.getvalue('oats')
print ('''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>rates</title>
</head>

<body>''')
cursor=config.db.cursor()
cursor.execute("SELECT * from rate")
rs=cursor.fetchall()
#for rec in rs:
rec=rs[0]
print ('''
  <marquee bgcolor="brown" style="color: white; width=100%;" onmouseover="this.stop()" onmouseout="this.start()">
  Rate List: Wheat = Rs. {}/kg, Rice = Rs. {}/kg, Moong Dal = Rs. {}/kg, Aarhar Dal = Rs. {}/kg, Oats = Rs. {}/kg
  </marquee>
  '''.format(rec[0],rec[1],rec[2],rec[3],rec[4]))
print ('''
</body>
</html>''')
frm=cgi.FieldStorage()
