import cgi
import config

print ('''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Admin Login</title>
</head>
<body style="text-align: right; top: 120px; border-radius: 20px; background-color: #FFFFFF; width: 100%; height: 300px;">
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<p><a href="home1.html"><img src="images/logo.jpg" width="287" height="137" alt="" align="left"></a></p>
	<br><br><br><br><br><br><br>
<nav id="nav" style=" color: green; background-color: darkseagreen; width: 99%" align="=right"><a href="home1.html">HOME</a><a href="contact1.html"> CONTACT US</a></nav>
	<center>
<br>
		<p>&nbsp;</p>
		<h2><b>Admin Sign In</b></h2>
		<br><br>
<div class="container">
<form name="frm" method="post" action="alogin_code.py" class="loginbox">
<table cellpadding="10">
    <tr>
    	<td>Email</td>
        <td><input type="text" name="email" required class="form-control"></td>
    </tr>
    <tr>
    	<td>Password</td>
        <td><input type="password" name="pwd" required class="form-control"></td>
    </tr>
    <tr>
    	<td>&nbsp;</td>
        <td><input type="submit" name="ok" value="Login"></td>
    </tr>
</table>
</form>


<table cellpadding="10"  align="center">
<tr>
</table>
	</center>
		<center>
			<br><br>
		<p>&nbsp;</p>
		<br><br>
		<br><br>
<br>	
  <footer id="footer" style="background-color: darkgrey; height: 80px">
      <div class="row text-center">
        <div class="small-18 medium-8 medium-offset-8 columns">
         <br> <p center:id="copyright">Copyright &copy; 2019 | Agri Fox</p>
        </div>
      </div>
    </footer>
  </center>
  <script src="js/jquery.js"></script>
  <script src="js/bootstrap.min.js"></script>
  ''')
frm=cgi.FieldStorage()
if frm.getvalue('msg'):
    print( frm.getvalue('msg'))
print('''
</body>
</html>''')
