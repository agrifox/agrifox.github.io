import cgi,config
print ('''
<form name ="frm" method ="post"> 
<table align='right'>
    <tr>
        <td><input type='text' placeholder='Search the Name' name='name' </td>
        <td><input type = "submit" name = "ok" value = "Search"</td>
    </tr>
</table>
</form>''')
frm=cgi.FieldStorage()
if frm.getvalue('ok'):
    name=frm.getvalue('name')
    cursor=config.db.cursor()
    cursor.execute("SELECT r.*, p.* FROM freg r INNER JOIN fpic p ON r.id=p.fid WHERE r.name='{}'".format(name))
    rs=cursor.fetchall()
    if rs:
        print ('''<table cellpadding="5" cellspacing="0" width=70% class="table" border=4>
        <tbody>''')
        for rec in rs:
            print ('''
            <tr border=0>
            <td rowspan=4 align="center"><img src="{}" height=200 width=200></td>
            <td align="center">Name: {}</td>
            <td align="center" rowspan=4 width=15%><a href="wcalc1.py?id={}">Buy Here</a></td>
            
        </tr>
        <tr>
            <td align="center">Crops he can Sell: {} {} {} {} {}</td>
            
        </tr>
        <tr>
            <td align="center">Address: {}</td>
            
        </tr>
        <tr>
            <td align="center">Location:<a href="{}"><img src="images/map.jpg" height=20 width=40 alt="Click Here"></a></td>
            
        </tr>
        
        <tr>
            <td colspan=3></td>
        </tr> '''.format(rec[14],rec[1],rec[0],rec[3],rec[4], rec[5],rec[6], rec[7], rec[11], rec[10]))
        print ('''</tbody>
        </table>''')
    else:
        print ('''No student data found''')

