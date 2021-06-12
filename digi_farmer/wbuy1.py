import config
import cgi
frm=cgi.FieldStorage()
id=frm.getvalue('id')
fid=frm.getvalue('fid')
print '''
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
	<p>'''

import wpicture1

print'''
<br><br><br><br><br><br>
<nav id="nav" style=" color: green; background-color: darkseagreen; width: 100%" align="right"><a href="home1.html">HOME      .                 .</a> <a href="log_out.py"">  LOG OUT</a></nav>
'''
import marq
import wsearch1
print
'''<br>
<br>'''
cursor = config.db.cursor()
cursor.execute("SELECT r.*, p.* FROM freg r INNER JOIN fpic p ON r.id=p.fid ORDER BY r.id")
rs = cursor.fetchall()
if rs:
    print'''
    <div class="table-responsive">
    <center>
    <h2>FARMERS AVAILABLE</h2>
    <table cellpadding="5" cellspacing="0" width=70% class="table" border=4>
    <tbody>
     '''
    for rec in rs:
        print'''
        <tr border=0>
            <td rowspan=4 align="center"><img src="{}" height=200 width=200></td>
            <td align="center">Name: {}</td>
            <td align="center" rowspan=4 width=15%><a href="wcalc1.py?id={}">Buy Here</a></td>

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
        '''.format(rec[14], rec[1], rec[0], rec[3], rec[4], rec[5], rec[6], rec[7], rec[11], rec[10])
    print'''</tbody>
    </table>
    </center>
    </div>'''
else:
    print 'No Farmer Data Found'
print'''
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
</html>'''
frm=cgi.FieldStorage()
