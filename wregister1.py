import config
import cgi
print ('''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Wholesaler Sign Up</title>
</head>

<body style="text-align: right; top: 120px; border-radius: 20px; background-color: #FFFFFF; width: 100%; height: 300px;">
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<p><a href="home1.py"><img src="images/logo.jpg" width="287" height="137" alt="" align="left"></a></p>
	<br><br><br><br><br><br>
<nav id="nav" style=" color: green; background-color: darkseagreen; width: 99%" align="=right"><a href="home1.py">HOME</a> | | <a href="wlogin1.py">LOGIN</a></nav>
	<br>
<center>
	<h2><b>Wholesaler Sign Up</b></h2>
<div class="container">
 <form name="user_reg" method="post" action="wregister_code1.py">
	 <br>
	 <table cellspacing=5 cellpadding=5>
 <div class="form-group">
    <tr><td><label>Wholesaler Name*</label></td>
    <td><input type="text" class="form-control" placeholder="Wholesaler Name" name="name" required></td></tr>
	 </div>
  <div class="form-group">
    <tr><td><label>Phone Number*</label></td>
    <td><input type="text" class="form-control" placeholder="Phone Number" name="contact" min=10 max=10 required></td></tr>
  </div>
  <div class="form-group">
    <tr><td><label>Crops he can Sell*</label></td>
    <td><input type="checkbox" name="crop1" value="Wheat">Wheat
    <input type="checkbox" name="crop2" value="Rice">Rice
    <input type="checkbox" name="crop3" value="Moong Dal">Moong Dal
    <input type="checkbox" name="crop4" value="Arhar Dal">Aarhar Dal
    <input type="checkbox" name="crop5" value="Oats">Oats</td></tr>
  </div>
  <div class="form-group">
    <tr><td><label>Location Link*</label></td>
    <td><input type="text" class="form-control" placeholder="Location Link of your Farm" name="location" required></td></tr>
  </div>
  <div class="form-group">
    <tr><td><label>Address*</label></td>
    <td><input type="text" class="form-control" placeholder="Address of your Farm" name="address" required></td>
  </div>
  <div class="form-group">
    <tr><td><label >Password*</label></td>
    <td><input type="password" class="form-control" placeholder="Password" name="pwd" required></td></tr>
  </div>
  <tr><td colspan=2 align="center"><button type="submit" class="btn btn-primary">Submit</button></td></tr>
  </table>
</form>
	</center>
	<br><br><br>
	<br><br><br>
	<center>''')
import footer
print('''
</center></body>
</html>''')
