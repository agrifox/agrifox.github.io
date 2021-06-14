import config
import cgi
frm = cgi.FieldStorage()
#status=frm.getvalue('status')
fname = frm.getvalue('fname')
id = frm.getvalue('id')
print ('''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Transportation Status</title>
</head>

<body style="text-align: right; top: 120px; border-radius: 20px; background-color: #FFFFFF; width: 100%; height: 300px;">
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<p><a href="home1.py"><img src="images/logo.jpg" width="287" height="137" alt="" align="left"></a></p>''')

#import fpicture1
print ('''
<br><br><br><br><br><br>
<nav id="nav" style=" color: green; background-color: darkseagreen; width: 100%" align="right">
<a href="home1.py"> HOME </a> | | 
<a href="fstatus1.py?fname={}">MY REQUEST</a> | |
<a href="fconfirm1.py?fname={}"> WHOLESALER REQUEST </a> | | 
<a href="ftransstatus1.py?fname={}">TRANSPORTATION STATUS</a> | | 
<a href="log_out1.py""> LOG OUT </a></nav>
'''.format(fname,fname,fname))
import marq1
print ('<center>')
cursor=config.db.cursor()
cursor.execute('''SELECT * FROM tcnf WHERE fname="{}" '''.format(fname))
rs=cursor.fetchall()
rec=rs[0]

if rs:
    print ('''
         <br><h2>TRANSPORTATION REQUEST STATUS</h2>
                <br>
                <center>
                <table border=2 cellspacing=1 cellpadding=4>''')
    i=0
    for rec in rs:
        i=i+1
        print ('''
                <tr><td><b>Sl.No.</b></td>
                    <td>{}</td></tr>
                <tr><td><b>Farmer Name</b></td>
                    <td>{}</td></tr>
                <tr><td><b>Wholesaler Name</b></td>
                    <td>{}</td></tr>
                <tr><td><b>Crop</b></td>
                    <td>{}</td></tr>
                <tr><td><b>Quantity</b></td>
                    <td>{} Kg</td></tr>
                <tr><td><b>Farmer's Address</b></td>
                    <td>{}</td></tr>
                <tr><td><b>Wholesaler's Address</b></td>
                    <td>{}</td></tr>
                <tr><td><b>Distance</b></td>
                    <td>{} Kms</td></tr>
                <tr><td><b>Rate</b></td>
                    <td>Rs. 24/km</td></tr>
                <tr><td><b>Cost</b></td>
                    <td>Rs. {}</td></tr>
                    '''.format(i,rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],rec[7],rec[8]))

        #print(status)
        if rec[9]==0:
            print ('''<tr><td><b>Status</b></td>
                            <td>Pending</td></tr>
                      <tr><td colspan=2></td></tr>''')
        elif rec[9]==2:
            print('''<tr><td><b>Status</b></td>
                            <td>Rejected</td></tr>
                      <tr><td colspan=2></td></tr>''')
        elif rec[9]==1:
            print ('''<tr><td><b>Status</b></td>
                            <td>Confirm</td>
                      <tr><td><b>Admin Contact</b></td>
                          <td>8709569656</td></tr>
                      <tr><td colspan=2></td></tr>''')

else:
    print ("No Data Found")
print ('''

	</tbody>
	</table>
	</center>
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
</html>''')
frm=cgi.FieldStorage()
