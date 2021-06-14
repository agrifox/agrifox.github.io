import config
import cgi

frm = cgi.FieldStorage()
# status=frm.getvalue('status')
fname = frm.getvalue('fname')
id = frm.getvalue('id')
print('''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Wholesaler Request</title>
</head>

<body style="text-align: right; top: 120px; border-radius: 20px; background-color: #FFFFFF; width: 100%; height: 300px;">
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<p><a href="home1.py"><img src="images/logo.jpg" width="287" height="137" alt="" align="left"></a></p>''')

# import fpicture1

print('''
<br><br><br><br><br><br>
<nav id="nav" style=" color: green; background-color: darkseagreen; width: 100%" align="right">
<a href="home1.py"> HOME </a> | | 
<a href="fstatus1.py?fname={}">MY REQUEST</a> | |
<a href="fconfirm1.py?fname={}"> FARMER REQUEST </a> | | 
<a href="ftransstatus1.py?fname={}">TRANSPORTATION STATUS</a> | | 
<a href="log_out.py""> LOG OUT </a></nav>
'''.format(fname, fname, fname))

import marq1

print('<center>')
cursor = config.db.cursor()
cursor.execute("SELECT * FROM wcnf WHERE fname='{}' ".format(fname))
#cursor.execute('''SELECT f.*, w.* FROM wcnf f INNER JOIN wreg w ON f.wname=w.name WHERE f.fname="{}" '''.format(fname))
rs = cursor.fetchall()
rec = rs[0]
print('''
        <br><center><h2>WHOLESALER PENDING REQUEST</h2>
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
                                    <td><b>Approve Request</b></td>
                                    <td><b>Cancel Request</b></td>
                                </tr>
                            </thead>
                            <tbody>
                        ''')
if rs:
    i = 0
    for rec in rs:
        if rec[7] == 0:
            i = i + 1
            print('''
                <tr>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>Rs. {}/kg</td>
                    <td>{} kg</td>
                    <td>Rs. {}</td>
                    <td>Pending</td>
                    <td>
                        <form name="frm" method="post" action="wconfirmreq_code1.py?wid={}">
                        <input type="hidden" name="wname" value="{}">
                        <input type="hidden" name="id" value={}>
                        <input type="submit" value="Approve Request">
                        </form>
                    </td>
                    <td>
                        <form name="frm" method="post" action="wcancelreq_code1.py?wid={}">
                        <input type="hidden" name="wname" value="{}">
                        <input type="hidden" name="id" value={}>
                        <input type="submit" value="Cancel Request">
                        </form>
                    </td>
                    </tr>
                    '''.format(i, rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[0], rec[2], rec[0], rec[0],
                               rec[2], rec[0]))

        else:
            print('''<tr><td colspan=10>No Rejected Request Found</td></tr>''')
        print('''</tbody>
                                    </table>
                                    </center>
                                    </center>''')

print('''
        <br><center><br><br><h2>WHOLESALER CONFIRMED REQUEST</h2>
                        <br>

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
                                    <td><b>Cancel Request</b></td>
                                </tr>
                            </thead>
                            <tbody>
                        ''')
if rs:
    i = 0
    for rec in rs:
        if rec[7] == 1:
            i = i + 1
            print('''
                <tr>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>Rs. {}/kg</td>
                    <td>{} kg</td>
                    <td>Rs. {}</td>
                    <td>Confirm</td>
                    <td>{}</td>
                    <td>
                        <form name="frm" method="post" action="wcancelreq_code1.py?wid={}">
                        <input type="hidden" name="wname" value="{}">
                        <input type="hidden" name="id" value={}>
                        <input type="submit" value="Cancel Request">
                        </form>
                    </td>
                    </tr>
                    '''.format(i, rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[10], rec[0], rec[2], rec[0]))

        else:
            print('''<tr><td colspan=10>No Rejected Request Found</td></tr>''')
        print('''</tbody>
                                    </table>
                                    </center>
                                    </center>''')

print('''
        <br><center><br><br><h2>WHOLESALER REJECTED REQUEST</h2>
                        <br>

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
                                    <td><b>Approve Request</b></td>
                                </tr>
                            </thead>
                            <tbody>
                        ''')
if rs:
    i = 0
    for rec in rs:
        if rec[7] == 1:
            i = i + 1
            print('''
                <tr>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>Rs. {}/kg</td>
                    <td>{} kg</td>
                    <td>Rs. {}</td>
                    <td>Rejected</td>
                    <td>
                        <form name="frm" method="post" action="wconfirmreq_code1.py?wid={}">
                        <input type="hidden" name="wname" value="{}">
                        <input type="hidden" name="id" value={}>
                        <input type="submit" value="Approve Request">
                        </form>
                    </td>
                    </tr>
                    '''.format(i, rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[0], rec[2], rec[0]))

        else:
            print('''<tr><td colspan=9>No Rejected Request Found</td></tr>''')
        print('''</tbody>
                                    </table>
                                    </center>
                                    </center>''')

print('''
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
