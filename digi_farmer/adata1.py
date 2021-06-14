import config
import cgi
frm=cgi.FieldStorage()
id=frm.getvalue('id')
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
	<p><a href="home1.html"><img src="images/logo.jpg" width="287" height="137" alt="" align="left"></a></p>
	<p>''')
print('''<h3 align="right">Hello Admin </h3>''')
print ('''
<br><br><br><br>
<nav id="nav" style=" color: green; background-color: darkseagreen; width: 99%" align="right"><a href="adata1.py">ADMIN </a><a href="log_out.py"">  LOG OUT</a></nav>
''')
import marq
print('''
<br>
<br>
<br><center>
<table width=90% border=0 cellspacing=5 cellpadding=5 background="images/golden.jpg">
    <tr><td width=25% style="vertical-align:top;">
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
            <tr><td align="center"><h1>Welcome to the Admin Panel of the Project <br><b>DIGI FARMER</b></h1></td></tr>
        </table>
    </center>
    </td></tr>
</table>
</center>
<br><br><br><br><br><br><br>
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
