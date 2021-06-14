import config
import cgi, cgitb
frm=cgi.FieldStorage()

name=frm.getvalue('name')
contact=frm.getvalue('contact')
crop1=frm.getvalue('crop1')
crop2=frm.getvalue('crop2')
crop3=frm.getvalue('crop3')
crop4=frm.getvalue('crop4')
crop5=frm.getvalue('crop5')
location=frm.getvalue('location')
address=frm.getvalue('address')
pwd=frm.getvalue('pwd')

cur=config.db.cursor()
cur.execute("SELECT contact FROM wreg WHERE contact='{}'".format(contact))
rs=cur.fetchall()

if rs:
    print ('''<script>
    window.location='wlogin1.py?msg=User Already Registerd'
    </script>''')
else:
    try:
        cursor=config.db.cursor()
        sql="INSERT INTO wreg (name,contact,crop1,crop2,crop3,crop4,crop5,location,address,pwd)VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name,contact,crop1,crop2,crop3,crop4,crop5,location,address,pwd)
        if cursor.execute(sql):
            config.db.commit()
            config.db.close()
            print (''''<script>
            window.location='wlogin1.py?msg=User Saved Successfully'
            </script>''')
    except Exception as e:
        print (e)
