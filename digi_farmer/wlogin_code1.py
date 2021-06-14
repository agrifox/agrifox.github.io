import cgi
import config
frm=cgi.FieldStorage()
id=frm.getvalue('id')
contact=int(frm.getvalue('contact'))
pwd=frm.getvalue('pwd')
cursor=config.db.cursor()
cursor.execute("SELECT * FROM wreg")
row=cursor.fetchall()
x=0

for i in row:
    if i[2]==contact:
        x=1
        y=i[8]
        z=i[0]
        break


if x==1:
    if y==pwd:
        print('''<html>
        <head></head>
        <body><script>
              window.location="wbuy1.py?id={}" '''.format(z))
        print ('''</script></body>
        </html>''')
    else:
        print('''<html>
        <head></head>
        <body><script>
          window.location='wlogin1.py?msg=Incorrect Password'
        </script></body>
        </html>''')
else:
    print('''<html>
            <head></head>
            <body><script>
              window.location='wlogin1.py?msg=Incorrect Phone Number'
            </script></body>
            </html>''')


