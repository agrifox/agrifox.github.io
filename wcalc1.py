#import form

import config
import cgi
#import js2py
frm = cgi.FieldStorage()
id = frm.getvalue('id')
wid = frm.getvalue('wid')
print ('''
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
	<p><a href="home1.py"><img src="images/logo.jpg" width="287" height="137" alt="" align="left"></a></p>''')

import wpicture1

cursor5=config.db.cursor()
cursor5.execute("SELECT * FROM wreg WHERE id={}".format(id))
rs5=cursor5.fetchall()
rec5=rs5[0]
if rs5:
    print ('''
<br><br><br><br><br><br>
<nav id="nav" style=" color: green; background-color: darkseagreen; width: 100%" align="right">
<a href="home1.py"> HOME </a> | | 
<a href="wstatus1.py?wname={}">MY REQUEST</a> | |
<a href="wconfirm1.py?wname={}"> FARMER REQUEST </a> | | 
<a href="log_out.py""> LOG OUT </a></nav>
'''.format(rec5[1],rec5[1]))
import marq1
print ('''
<br>
<center>
	<h2><b>WHOLESALER RATE CALCULATION</b></h2>
<div class="container">
 <form name="wholesaler_rate" method="post" action="wcalcreg_code1.py">
	 <br>''')
cursor=config.db.cursor()
cursor.execute("SELECT * FROM wreg WHERE id='{}'".format(id))
rs=cursor.fetchall()
rec=rs[0]
if rs:
    print ('''
    <table cellspacing=5 cellpadding=5><tr><td>
     <div class="form-group">
        <label>Wholesaler Name</label></td>
        <td><input type="text" class="form-control" value="{}" name="wname" readonly>
         </div><br></td></tr>'''.format(rec[1]))
cursor1=config.db.cursor()
cursor1.execute("SELECT * FROM freg WHERE id='{}'".format(wid))
rs1=cursor1.fetchall()
rec1=rs1[0]
if rs1:
    print ('''
  <tr><td><div class="form-group">
    <label>Farmer Name</label></td>
    <td><input type="text" class="form-control" value="{}" name="fname" readonly>
  </div><br></td></tr>'''.format(rec1[1]))
    print ('''<tr><td><div class="form-group">
        <label>Crop*</label></td>
        <td><select name='crop' onChange="getPrice(this.value)">
        <option name="  " value="   ">Select Crops</option>''')
    print ('''
        <option name="crop1" value="{}">{}</option>
        <option name="crop2" value="{}">{}</option>
        <option name="crop3" value="{}">{}</option>
        <option name="crop4" value="{}">{}</option>
        <option name="crop5" value="{}">{}</option>'''.format(rec1[3], rec1[3], rec1[4], rec1[4], rec1[5], rec1[5], rec1[6],rec1[6],rec1[7],rec1[7]))

print ('''
    </select>
    
    </div><br></td></tr>
    <tr><td><div class="form-group">
    <label>Rate: </label></td>''')
cursor3=config.db.cursor()
cursor3.execute("SELECT * FROM rate")
rs3=cursor3.fetchall()
rec3=rs3[0]
if rs3:
    print ('''<td><label id="disp_rate"></label>''')

print ('''
  </div><br></td></tr>
  <tr><td><div class="form-group">
    <label>Quantity* (Kg)</label></td>
    <td><input type="text" class="form-control" placeholder="Quantity to sell" name="quant" required onblur="priceCal(this.value)">''')
print ('''
  </div><br></td></tr>
  <tr><td><div class="form-group">
    <label >Cost</label></td>
    <td><input type="text" class="form-control" id="cost" name="cost" readonly>''')
print ('''
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
  <script>
  function getPrice(str){
  if (str == "") {
    document.getElementById("disp_rate").innerHTML = "Please select a crop";
    return;
      } else {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
            document.getElementById("disp_rate").innerHTML = this.responseText;
          }
        };
        xmlhttp.open("GET","wgetcrop_rate1.py?crop="+str,true);
        xmlhttp.send();
      }
  }
  var tot=0;
  function priceCal(qty){
    var rate=document.getElementById("rate").value;
    tot=qty*rate;
    document.getElementById("cost").value = tot;
  }
  </script>
</body>
</html>''')
frm=cgi.FieldStorage()

