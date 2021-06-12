import config
import cgi
frm = cgi.FieldStorage()
id = frm.getvalue('id')
print '''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Wholesaler Aprx Rate</title>
</head>

<body style="text-align: right; top: 120px; border-radius: 20px; background-color: #FFFFFF; width: 100%; height: 300px;">
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<p><a href="home1.html"><img src="images/logo.jpg" width="287" height="137" alt="" align="left"></a></p>'''
import wpicture1

print '''
	<br><br><br><br><br><br>
<nav id="nav" style=" color: green; background-color: darkseagreen; width: 100%" align="=right"><a href="home1.html">HOME</a> <a href="log_out.py">LOGOUT</a></nav>
	<br>'''
import marq
print '''
<center>
	<h2><b>Wholesaler Rate Calculation</b></h2>
<div class="container">
 <form name="wholesaler_rate" method="post" action="wcalc_code.py">
	 <br>'''
cursor=config.db.cursor()
cursor.execute("SELECT * FROM wreg")
rs=cursor.fetchall()
rec=rs[0]
if rs:
    print '''
    <table cellspacing=5 cellpadding=5><tr><td>
     <div class="form-group">
        <label>Wholesaler Name</label></td>
        <td><input type="text" class="form-control" value="{}" name="wname" readonly>
         </div><br></td></tr>'''.format(rec[1])
cursor1=config.db.cursor()
cursor1.execute("SELECT * FROM freg WHERE id='{}'".format(id))
rs1=cursor1.fetchall()
rec1=rs1[0]
if rs1:
    print'''
  <tr><td><div class="form-group">
    <label>Farmer Name</label></td>
    <td><input type="text" class="form-control" value="{}" name="fname" readonly>
  </div><br></td></tr>'''.format(rec1[1])
print '''<tr><td><div class="form-group">
        <label>Crop*</label></td>
        <td><select name=crop>
        <option name="  " value="   ">Select Crops</option>'''
cursor2=config.db.cursor()
cursor2.execute("SELECT * FROM freg WHERE id='{}'".format(id))
rs2 = cursor2.fetchall()
rec2 = rs2[0]
for rec2 in rs2:
    if rs2:
        print'''
        <option name="crop1" value="{}">{}</option>
        <option name="crop2" value="{}">{}</option>
        <option name="crop3" value="{}">{}</option>
        <option name="crop4" value="{}">{}</option>
        <option name="crop5" value="{}">{}</option>'''.format(rec2[3], rec2[3], rec2[4], rec2[4], rec2[5], rec2[5], rec2[6],rec2[6],rec2[7],rec2[7])

print '''
    </select>
    </div><br></td></tr>
    <tr><td><div class="form-group">
    <label>Rate: </label></td>'''
cursor3=config.db.cursor()
cursor3.execute("SELECT * FROM rate")
rs3=cursor3.fetchall()
rec3=rs3[0]
if rs3:
    print'<td>'
    if("{}"=="Wheat"):
        print '''<input type="text" class="form-control" value="Wheat: Rs. {}/kg" name="crop1" readonly>'''.format(rec2[3], rec3[0])
    elif("{}"=="Rice"):
        print '''<input type="text" class="form-control" value="Rice: Rs. {}/kg" name="crop2" readonly>'''.format(rec2[4], rec3[1])
    elif("{}"=="Moong Dal"):
        print '''<input type="text" class="form-control" value="Moong Dal: Rs. {}/kg" name="crop3" readonly>'''.format(rec2[5], rec3[2])
    elif("{}"=="Arhar Dal"):
        print '''<input type="text" class="form-control" value="Arhar Dal: Rs. {}/kg" name="crop4" readonly>'''.format(rec2[6], rec3[3])
    elif("{}"=="Oats"):
        print '''<input type="text" class="form-control" value="Oats: Rs. {}/kg" name="crop5" readonly>'''.format(rec2[7], rec3[4])

    print'''
        <input type="text" class="form-control" value="Wheat: Rs. {}/kg" name="crop1" readonly><br>
        <input type="text" class="form-control" value="Rice: Rs. {}/kg" name="crop2" readonly><br>
        <input type="text" class="form-control" value="Moong Dal: Rs. {}/kg" name="crop3" readonly><br>
        <input type="text" class="form-control" value="Arhar Dal: Rs. {}/kg" name="crop4" readonly><br>
        <input type="text" class="form-control" value="Oats: Rs. {}/kg" name="crop5" readonly>
            '''.format(rec3[0], rec3[1], rec3[2], rec3[3], rec3[4])

print '''
  </div><br></td></tr>
  <tr><td><div class="form-group">
    <label>Quantity*(in KG)</label></td>'''
print '''<td><input type="text" class="form-control" placeholder="Quantity to sell" name="quantity" required>
  </div><br></td></tr>
  <tr><td><div class="form-group">
    <label >Cost</label></td>
    <td><input type="text" class="form-control" placeholder="" name="cost">
  </div><br></td></tr>
  <tr><td></td></tr>
  <center><tr><td align="center" colspan=2><button type="submit" class="btn btn-primary">Request the Farmer</button></td></tr></center>
  </table>
</form>
	</center>
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
</html>'''
frm=cgi.FieldStorage()