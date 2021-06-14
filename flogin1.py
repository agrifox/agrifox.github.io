import cgi
import config
print('''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Farmer Login</title>
</head>
<body style="text-align: right; top: 120px; border-radius: 20px; background-color: #FFFFFF; width: 100%; height: 300px;">
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<p><a href="home1.py"><img src="images/logo.jpg" width="287" height="137" alt="" align="left"></a></p>
	<br><br><br><br><br><br>
<nav id="nav" style=" color: green; background-color: darkseagreen; width: 100%" align="=right"><a href="home1.py">HOME</a> | | <a href="flogin1.py">FARMER</a> | | <a href="wlogin1.py">WHOLESALER</a> | | <a href="contact1.html"> CONTACT US</a></nav>
	<center>
<br>
		<p>&nbsp;</p>
		<h2><b>Farmer Sign In/Register</b></h2>
		<br><br>
<div class="container">
<form name="frm" method="post" action="flogin_code1.py" class="loginbox">
<table cellpadding="10">
    <tr>
    	<td>Phone Number</td>
        <td><input type="text" name="contact" required class="form-control"></td>
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

<td>Forgot Password?</td>
<td align="center"><a class="btn btn-success" href="ffpass1.py" role="button">Retrieve your Password</a></td></tr>
<tr>
<td>Haven't registered yet?</td>
<td colspan="2" align="center"><a class="btn btn-success" href="fregister1.py" role="button">Register</a></td></tr>
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
  <script src="js/bootstrap.min.js"></script>''')
frm=cgi.FieldStorage()
if frm.getvalue('msg'):
    print (frm.getvalue('msg'))
print('''
</body>
</html>''')
