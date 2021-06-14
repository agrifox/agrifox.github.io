import cgi
import config
frm=cgi.FieldStorage()
email=frm.getvalue('email')
pwd=frm.getvalue('pwd')
cursor=config.db.cursor()
cursor.execute("SELECT * FROM admin WHERE email='{}' AND pwd='{}'".format(email,pwd))
row=cursor.fetchall()
if row:

    print ("""
    <html>
        <body>
        <script>
        window.location='adata1.py?msg=Login sucessfully'
        </script>
        </body>
    </html>""")
else:
    print ("""
    <html>
        <body>
        <script>
        window.location='alogin1.py?msg=Invalid Email or Password'
        </script>
        </body>
    </html>""")

