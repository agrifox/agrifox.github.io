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
<title>Farmer Status</title>
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
'''.format(fname,fname, fname))
import marq1
print ('<center>')
cursor=config.db.cursor()
cursor.execute('''SELECT f.*, w.* FROM fcnf f INNER JOIN wreg w ON f.wname=w.name WHERE fname="{}" '''.format(fname))
rs=cursor.fetchall()
rec=rs[0]

if rs:
    print ('''
         <br><h2>TRANSACTION REQUEST STATUS</h2>
                <br>
                <center>
                <table border=5 cellspacing=6 cellpadding=10>
                    <thead>
                        <tr>
                            <td><b>Sl.No.</b></td>
                            <td><b>Farmer Name</b></td>
                            <td><b>Wholesaler Name</b></td>
                            <td><b>Crop</b></td>
                            <td><b>Rate</b></td>
                            <td><b>Quantity</b></td>
                            <td><b>Cost</b></td>
                            <td><b>Status</b></td>
                            <td><b>Contact</b></td>
                            <td><b>Transportation</b></td>
                            <td><b>Cancel Request</b></td>
                        </tr>
                    </thead>
                    <tbody>
                ''')
    i=0
    for rec in rs:
        i=i+1
        print ('''
                <tr>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>Rs. {}/kg</td>
                    <td>{} kg</td>
                    <td>Rs. {}</td>
                    '''.format(i,rec[1],rec[2],rec[3],rec[4],rec[5],rec[6]))

        #print(status)
        if rec[7]==0:
            print ('''<td>Pending</td>
                      <td>NA</td>
                      <td>NA</td>
                      <td>
                        <form name="frm" method="post" action="fcancelreq_code1.py?fid={}">
                        <input type="hidden" name="fname" value="{}">
                        <input type="hidden" name="id" value={}>
                        <input type="submit" value="Cancel Request">
                        </form>
                    </td></tr>'''.format(rec[0], rec[1],rec[0]))
        elif rec[7]==2:
            print('''<td>Rejected</td>
                     <td>NA</td>
                     <td>NA</td>
                     <td>NA</td>''')
        elif rec[7]==3:
            print('''<td>Cancelled</td>
                     <td>NA</td>
                     <td>NA</td>
                     <td>NA</td>''')
        elif rec[7]==1:
            print ('''<td>Confirm</td>
                      <td>{}</td>
                      <td><a href="ftrans1.py?id={}">Avail Transportation</a></td>
                      <td>
                        <form name="frm" method="post" action="fcancelreq_code1.py?fid={}">
                        <input type="hidden" name="fname" value="{}">
                        <input type="hidden" name="id" value={}>
                        <input type="submit" value="Cancel Request">
                        </form>
                    </td></tr>'''.format(rec[10], rec[0], rec[0], rec[1],rec[0]))

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
