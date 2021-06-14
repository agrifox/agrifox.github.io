# import form

import config
import cgi

# import js2py
frm = cgi.FieldStorage()
id = frm.getvalue('id')
fid = frm.getvalue('fid')
fname=frm.getvalue('fname')
cursor = config.db.cursor()
cursor.execute("SELECT s.*, f.*, w.* FROM fcnf s INNER JOIN freg f ON s.fname=f.name INNER JOIN wreg w ON s.wname=w.name WHERE s.id='{}'".format(id))
rs = cursor.fetchall()
rec = rs[0]
print('''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Transportation Cost</title>
</head>

<body style="text-align: right; top: 120px; border-radius: 20px; background-color: #FFFFFF; width: 100%; height: 300px;">
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<p><a href="home1.py"><img src="images/logo.jpg" width="287" height="137" alt="" align="left"></a></p>''')


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

print('''
<br>
<center>
	<h2><b>TRANSPORTATION COST CALCULATION</b></h2>
<div class="container">
 <form name="farmer_rate" method="post" action="ftrans_code1.py">
	 <br>''')

if rs:
    print('''
    <table cellspacing=5 cellpadding=5><tr>
    <td><div class="form-group">
        <label>Farmer Name</label></td>
        <td><input type="text" class="form-control" value="{}" name="fname" readonly>
         </div><br></td></tr>
         <tr><td><div class="form-group">
    <label>Wholesaler Name</label></td>
    <td><input type="text" class="form-control" value="{}" name="wname" readonly>
  </div><br></td></tr>
  <tr><td><div class="form-group">
    <label>Crop</label></td>
    <td><input type="text" class="form-control" value="{}" name="crop" readonly>
  </div><br></td></tr>
  <tr><td><div class="form-group">
    <label>Quantity (Kg)</label></td>
    <td><input type="text" class="form-control" value="{}" name="quant" readonly>
  </div><br></td></tr>
  <tr><td><div class="form-group">
    <label>Farmer's Address</label></td>
    <td><input type="text" class="form-control" value="{}" name="fadd" readonly>
  </div><br></td></tr>
  <tr><td><div class="form-group">
    <label>Wholesaler's Address</label></td>
    <td><input type="text" class="form-control" value="{}" name="wadd" readonly>
  </div><br></td></tr>'''.format(rec[1],rec[2],rec[3],rec[5], rec[19], rec[31]))

from geopy.geocoders import Nominatim
from geopy import distance

geolocator = Nominatim(user_agent="geoapiExercises")

place1 = geolocator.geocode(rec[19])
place2 = geolocator.geocode(rec[31])

Loc1_lat, Loc1_lon = (place1.latitude), (place1.longitude)
Loc2_lat, Loc2_lon = (place2.latitude), (place2.longitude)

location1 = (Loc1_lat, Loc1_lon)
location2 = (Loc2_lat, Loc2_lon)

dist=(distance.distance(location1, location2).km)



print('''<tr><td><div class="form-group">
    <label>Distance (Kms)</label></td>
    <td><input type="text" class="form-control" value="{:.2f}" name="dist" readonly>
  </div><br></td></tr>
  <tr><td><div class="form-group">
    <label>Rate of Transportation</label></td>
    <td><input type="text" class="form-control" value="Rs. 24/km" name="rate" readonly>
  </div><br></td></tr>
  <tr><td><div class="form-group">
    <label>Cost of Transportation (Rs.)</label></td>
    <td><input type="text" class="form-control" value="{:.2f}" name="tcost" readonly>
  </div><br></td></tr>
  <tr><td></td></tr>
  <center><tr><td align="center" colspan=2><button type="submit" class="btn btn-primary">Request for Transportation</button></td></tr></center>
  </table>
</form>'''.format(dist, 24*dist))

print('''</center>
	<center>
		<br><br>
		<p>&nbsp;</p>
		<br><br>
		<br><br>
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
frm = cgi.FieldStorage()

