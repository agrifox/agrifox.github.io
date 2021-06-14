import config
import cgi
frm=cgi.FieldStorage()
id=frm.getvalue('id')
fid=frm.getvalue('fid')
print ('''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
</head>

<body style="text-align: right; top: 120px; border-radius: 20px; background-color: #FFFFFF; width: 100%; height: 300px;">
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	''')

cursor = config.db.cursor()
cursor.execute("SELECT r.*, p.* FROM freg r INNER JOIN fpic p ON r.id=p.fid where r.id='{}'".format(id))
rs = cursor.fetchall()
rec = rs[0]
if rs:
    print ('''
    <table cellpadding="5" cellspacing="0" width=10%  border=1 align="right">
    <tr align="center">
        <td colspan=2>
            <div class="form-group">
            <label> Hello {}</label>
            </div>
        </td>
        <td  rowspan=2>
            <div class="form-group">
            <img src="{}" height=90 width=90>
            </div>
        </td>'''.format(rec[1], rec[14]))

    print ('''

    </tr>
    <form name="form" method="post" enctype = "multipart/form-data" action="fpicture_code.py">
    <tr align="center">
        <td>
            <div class="form-group">
            <label >Upload your Picture</label>
            <input type="file" class="form-control" name="image">
            </div>
        </td>
        <td>
            <button type="submit" name="ok" class="btn btn-primary">Submit</button>
        </td>
    </tr>
    </form>''')
print ('''
  </table>
  </body>
  </html>
''')
frm=cgi.FieldStorage()