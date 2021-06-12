import cgi
import config
frm=cgi.FieldStorage()
wheat=frm.getvalue('wheat')
rice=frm.getvalue('rice')
moong=frm.getvalue('moong')
arhar=frm.getvalue('arhar')
oats=frm.getvalue('oats')
print'''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>rates</title>
</head>

<body>'''
cursor=config.db.cursor()
cursor.execute("SELECT * from rate")
rs=cursor.fetchall()
for rec in rs:
#rec=rs[0]
  print'''
  <div>
  <ol>
	  <li><h1>Content for New Rate Tag Goes Here</h1></li>
    <form name ="frm" method ="post" action="rate_code.py"> 
	  <table width="850" border="1">
  <tbody>
    <tr>
      <td>&nbsp;Crop</td>
      <td>&nbsp;Wheat</td>
      <td>&nbsp;rice</td>
      <td>&nbsp;moong</td>
      <td>&nbsp;arhar</td>
      <td>&nbsp;oats</td>
    </tr>
    <tr>
      <td>&nbsp;Rates</td>
      <td>&nbsp;{}</td>
      <td>&nbsp;{}</td>
      <td>&nbsp;{}</td>
      <td>&nbsp;{}</td>
      <td>&nbsp;{}</td>
    </tr>'''.format(rec[0],rec[1],rec[2],rec[3],rec[4])
print'''
    <tr>
      <td>&nbsp;Update Section</td>
      <td>&nbsp;<a href="rate_update.py">Update</a></td>
      <td>&nbsp;<a href="url">Update</a></td>
      <td>&nbsp;<a href="url">Update</a></td>
      <td>&nbsp;<a href="url">Update</a></td>
      <td>&nbsp;<a href="url">Update</a></td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
  </tbody>
</table>
</form>

  </ol>
</div>
</body>
</html>'''
frm=cgi.FieldStorage()
