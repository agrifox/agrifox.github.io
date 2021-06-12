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
</head>

<body style="text-align: right; top: 120px; border-radius: 20px; background-color: #FFFFFF; width: 100%; height: 300px;">
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	<span style="text-align: left"></span>
	'''

cursor1 = config.db.cursor()
cursor1.execute("SELECT r.*, p.* FROM wreg r INNER JOIN wpic p ON r.id=p.fid ORDER BY p.fid")
rs1 = cursor1.fetchall()
rec1 = rs1[0]
if rs1:
    print'''
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
        </td>'''.format(rec1[1], rec1[14])
print '''

    </tr>
    <tr align="center">
        <td>
            <form name="user_reg" method="post" action="wpicture_code.py">
            <div class="form-group">
            <label >Upload your Picture</label>
            <input type="file" class="form-control" name="image">
        </td>
        <td>
            <button type="submit" class="btn btn-primary">Submit</button>
        </td>
    </tr>
  </table>
  </body>
  </html>
'''
frm=cgi.FieldStorage()