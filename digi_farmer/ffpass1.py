import config
import cgi
print('''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Password Retrieval</title>
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
<h2 align="center">Password Retrieval</h2>
<form name="frm" method="post" action="ffpass_code1.py">
    <table cellpadding=5 cellspacing=5>
         <tr>
            <td>Name:</td>
            <td><input type="text" name="name" placeholder="Enter the name" required ></td>
        </tr>
        <tr>
            <td>Contact No.:</td>
            <td><input type="number" name="contact" placeholder="Enter the contact no." required ></td>
        </tr>
        <tr><td></td></tr>
        <tr>
                <td colspan=2 align="center"><input type="submit" name="ok" value="View Password">
            </td>
        </tr>
    </table>
</form>
		<p>&nbsp;</p>
		
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




