import config
import cgi
frm=cgi.FieldStorage()
id=frm.getvalue('id')
fid=frm.getvalue('id')
print ('''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Wholesaler Data</title>
</head>

<body style="text-align: right; top: 120px; border-radius: 20px; background-color: #FFFFFF; width: 100%; height: 300px;">
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<p><a href="home1.py"><img src="images/logo.jpg" width="287" height="137" alt="" align="left"></a></p>
	<p>''')

import fpicture1
cursor5=config.db.cursor()
cursor5.execute("SELECT * FROM freg WHERE id={}".format(id))
rs5=cursor5.fetchall()
rec5=rs5[0]
if rs5:
    print ('''
<br><br><br><br><br><br>
<nav id="nav" style=" color: green; background-color: darkseagreen; width: 100%" align="right">
<a href="home1.py"> HOME </a> | | 
<a href="fstatus1.py?fname={}">MY REQUEST</a> | |
<a href="fconfirm1.py?fname={}"> WHOLESALER REQUEST </a> | | 
<a href="ftransstatus1.py?fname={}">TRANSPORTATION STATUS</a> | | 
<a href="log_out1.py""> LOG OUT </a></nav>
'''.format(rec5[1],rec5[1],rec5[1]))
import marq1
import fsearch1

print ('''
<br>
<br>''')
cursor1=config.db.cursor()
cursor1.execute("SELECT r.*, p.* FROM wreg r LEFT JOIN wpic p ON r.id=p.fid ORDER BY r.id")
rs1=cursor1.fetchall()
rec1=rs1[0]
if rs1:
    print ('''
    <div class="table-responsive">
    <center>
    <b><h2>WHOLESALERS AVAILABLE</h2></b>
    <table cellpadding="5" cellspacing="0" width=70% class="table" border=4>
    <tbody>
     ''')
    for rec1 in rs1:
        print('''
        <tr border=0>
            <td rowspan=4 align="center"><img src="{}" height=200 width=200></td>
            <td align="center">Name: {}</td>
            <td align="center" rowspan=4 width=15%><a href="fcalc1.py?fid={}&id={}">Sell Here</a></td>
            
        </tr>
        <tr>
            <td align="center">Crops he can Purchase: {} {} {} {} {}</td>
            
        </tr>
        <tr>
            <td align="center">Address: {}</td>
            
        </tr>
        <tr>
            <td align="center">Location:<a href="{}"><img src="images/map.jpg" height=20 width=40 alt="Click Here"></a></td>
            
        </tr>
        
        <tr>
            <td colspan=3></td>
        </tr> 
        '''.format(rec1[14],rec1[1],rec1[0],fid,rec1[3],rec1[4], rec1[5],rec1[6], rec1[7], rec1[11], rec1[10]))

    print('''</tbody>
    </table>
    </center>
    </div>''')
else:
    print ('No Wholesaler Data Found')
print ('''
<center>
		<br><br>
		<p>&nbsp;</p>
		<p>&nbsp;</p>
		<br><br>
<br>
  <footer id="footer" style="background-color: darkgrey; height: 80px">
      <div class="row text-center">
        <div class="small-18 medium-8 medium-offset-8 columns">
         <br> <p center:id="copyright">Copyright &copy; 2020 | Agri Fox</p>
        </div>
      </div>
    </footer>
  </center>
</body>
</html>''')
frm=cgi.FieldStorage()
