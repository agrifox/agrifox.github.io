import cgi,cgitb, config
print ('''
<html>
<head>
<title>Password Recovery</title>
</head>
<body style="text-align: right; top: 120px; border-radius: 20px; background-color: #FFFFFF; width: 100%; height: 300px;">
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<p><a href="home1.py"><img src="images/logo.jpg" width="287" height="137" alt="" align="left"></a></p>
	<br><br><br><br><br><br>
<nav id="nav" style=" color: green; background-color: darkseagreen; width: 100%" align="=right"><a href="home1.py">HOME</a> | | <a href="flogin1.py">FARMER</a> | | <a href="wlogin1.py">WHOLESALER</a> | | <a href="contact1.html"> CONTACT US</a></nav>
	<center>''')

frm=cgi.FieldStorage()
contact = frm.getvalue('contact')
name=frm.getvalue('name')
cursor = config.db.cursor()
cursor.execute("SELECT * FROM freg WHERE contact='{}' AND name='{}' ".format(contact, name))
result = cursor.fetchall()
if result:
    for rec in result:
        print ('''<br><br>
              <table>
                <tr><td>Password:</td>
                <td><input type="text" value="{}" name="pwd" readonly></td></tr> </table>'''.format(rec[8]))
        print ('''<br><br><a href="flogin1.py"><input type="button" value="Login Again"></a>''')
else:
    print (''' <br><br>Not Registered
    <br><br><a href="fregister1.py">
            <input type= "button" value="Register"><a href="flogin1.py"><input type="button" value="Login Again"></a>
        </a>''')
print('''</body>
        </html>''')
