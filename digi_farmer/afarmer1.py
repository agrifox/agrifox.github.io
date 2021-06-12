import config
import cgi

cursor = config.db.cursor()
cursor.execute("SELECT r.*, p.* FROM freg r LEFT JOIN fpic p ON r.id=p.fid ORDER BY r.id")
rs = cursor.fetchall()
print ('''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Farmers Data</title>
</head>

<body style="text-align: right; top: 120px; border-radius: 20px; background-color: #FFFFFF; width: 100%; height: 300px;">
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<p><a href="home1.html"><img src="images/logo.jpg" width="287" height="137" alt="" align="left"></a></p>
	<p>
    <br>
	<br><br><br><br><br>
<nav id="nav" style=" color: green; background-color: darkseagreen; width: 100%" align="right"><a href="adata1.py">ADMIN </a><a href="log_out.py"> LOG OUT</a></nav>
''')

import marq

print ('''

<br>
<br>''')
if rs:
    print('''
    <div class="table-responsive">
    <center>
    <br>
    <table width=90% border=0 cellspacing=5 cellpadding=5>
    <tr><td width=25% style="vertical-align:top;" background="images/golden.jpg">
    <center>
        <table width=100% border=0 cellspacing=5 cellpadding=5>
        <ul>
            <tr><td></td></tr>
            <tr><td><a href="afarmer1.py"><h3><li>Farmers Available</h3></a></td></tr>
            <tr><td><a href="awholesaler1.py"><h3><li>Wholesalers Available</h3></a></td></tr>
            <tr><td><a href=""><h3><li>Farmers Requested Wholesaler</h3></a>
            <ul><a href="afconfirmed1.py"><h4><li>Confirmed Requests</h4></a>
            <a href="afpending1.py"><h4><li>Pending Requests</h4></a>
            <a href="afrejected1.py"><h4><li>Rejected Requests</h4></a></ul></td></tr>
            <tr><td><a href=""><h3><li>Wholesaler Requested Farmer</h3></a>
            <ul><a href="awconfirmed1.py"><h4><li>Confirmed Requests</h4></a>
            <a href="awpending1.py"><h4><li>Pending Requests</h4></a>
            <a href="awrejected1.py"><h4><li>Rejected Requests</h4></a></ul></td></tr>
            <tr><td><a href="afarmer1.py"><h3><li>Transportation Request</h3></a>
            <ul><a href="atconfirmed1.py"><h4><li>Confirmed Requests</h4></a>
            <a href="atpending1.py"><h4><li>Pending Requests</h4></a>
            <a href="atrejected1.py"><h4><li>Rejected Requests</h4></a></ul></td></tr>

        </ul>
        </table>
    </center>
    </td>
    <td width=65%>
    <center>
        <table width=90% border=2 cellspacing=5 cellpadding=5>
        <h2>FARMERS AVAILABLE</h2>
        <table cellpadding="5" cellspacing="0" width=90% class="table" border=4>
        <tbody>
     ''')
    for rec in rs:
        print('''
        <tr border=0>
            <td rowspan=4 align="center"><img src="{}" height=200 width=200></td>
            <td align="center">Name: {}</td>
        </tr>
        <tr>
            <td align="center">Crops he can Sell: {} {} {} {} {}</td>

        </tr>
        <tr>
            <td align="center">Address: {}</td>

        </tr>
        <tr>
            <td align="center">Location:<a href="{}"><img src="images/map.jpg" height=20 width=40></a></td>

        </tr>
        
        <tr>
            <td colspan=3></td>
        </tr> 
    </tbody>
        '''.format(rec[14], rec[1], rec[3], rec[4], rec[5], rec[6], rec[7], rec[11], rec[10]))
    print('''</tbody>
    </table>
    </td></tr>
    </center>
    </table>
    </div>''')
else:
    print ('No Farmer Data Found')
print('''
<center>''')
frm = cgi.FieldStorage()
print ('''
<br><br><br><br><br><br>
</center>
<center>
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
