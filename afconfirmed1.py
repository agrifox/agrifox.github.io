import config
import cgi

cursor=config.db.cursor()
cursor.execute("SELECT * FROM fcnf WHERE status=1")
rs=cursor.fetchall()
rec=rs[0]

print('''
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
	<p>
    <br>
	<br><br><br><br><br>
<nav id="nav" style=" color: green; background-color: darkseagreen; width: 100%" align="right"><a href="adata1.py">ADMIN </a><a href="log_out.py"> LOG OUT</a></nav>
''')

import marq

print('''

<br>
<br>''')

print('''
    <div class="table-responsive">
    <center>
    <br>
    <table width=95% border=0 cellspacing=5 cellpadding=5>
    <tr style="vertical-align:top;"><td width=25% background="images/golden.jpg">
    <center>
        <table width=100% border=0 cellspacing=5 cellpadding=5>
        <ul>
            <tr><td></td></tr>
            <tr><td><a href="afarmer1.py"><h3><li>Farmers Available</h3></a></td></tr>
            <tr><td><a href="awholesaler1.py"><h3><li>Wholesalers Available</h3></a></td></tr>
            <tr><td><a href=""><h3><li>Farmers Requested Wholesaler</h3></a>
            <ul><a href="afconfirmed1.py"><h4><li>Confirmed Requests</h4></a>
            <a href="afpending1.py"><h4><li>Pending Requests</h4></a>
            <a href="afrejected1.py"><h4><li>Rejected Requests</h4></a></ul></td></tr>
            <tr><td><a href=""><h3><li>Wholesaler Requested Farmer</h3></a>
            <ul><a href="awconfirmed1.py"><h4><li>Confirmed Requests</h4></a>
            <a href="awpending1.py"><h4><li>Pending Requests</h4></a>
            <a href="awrejected1.py"><h4><li>Rejected Requests</h4></a></ul></td></tr>
            <tr><td><a href="afarmer1.py"><h3><li>Transportation Request</h3></a>
            <ul><a href="atconfirmed1.py"><h4><li>Confirmed Requests</h4></a>
            <a href="atpending1.py"><h4><li>Pending Requests</h4></a>
            <a href="atrejected1.py"><h4><li>Rejected Requests</h4></a></ul></td></tr>

        </ul>
        </table>
    </center>
    </td>
    <td width=65%>
    <center>
        <br><h2>Confirmed Transaction: Farmer Requested Wholesaler</h2><br>
        <table width=90% border=2 cellspacing=5 cellpadding=5>'''.format(id))
if rs:
    print('''        
            <tr>
                <td><b>S.No.</b></td>
                <td><b>Farmer Name</b></td>
                <td><b>Wholesaler Name</b></td>
                <td><b>Crop</b></td>
                <td><b>Rate</b></td>
                <td><b>Quantity</b></td>
                <td><b>Cost</b></td>
                <td><b>Status</b></td>
                <td><b>Reject</b></td>
            </tr>''')
    i = 0
    for rec in rs:
        i = i + 1
        print('''
                <tr>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>Rs. {}/kg</td>
                    <td>{} kg</td>
                    <td>{}</td>
                    <td>Confirm</td>
                    <td>
                        <form name="frm" method="post" action="reject_code.py?fid={}">
                            <input type="hidden" name="id" value={}><input type="submit" value="Reject">
                        </form>
                    </td>
                </tr>
                    '''.format(i, rec[1], rec[2], rec[3], rec[4], rec[5], rec[6],rec[0],rec[0]))
else:
    print('No Confirmed Request Found')

print ('''</table>
    </form>
    </td></tr>
    </center>
    </table>
    </center>
    </div>''')

print('''
<center>''')
frm = cgi.FieldStorage()
print('''
<br><br><br><br><br><br>
</center>
<center>
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
