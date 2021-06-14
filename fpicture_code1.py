import cgi, config
import os, cgitb, random
cgitb.enable()
#print(random.random())

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

frm = cgi.FieldStorage()
# Generator to buffer file chunks
def fbuffer(f, chunk_size=10000):
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
        yield chunk
# A nested FieldStorage instance holds the file
fileitem = frm["image"]
#about=form.getvalue('about')
# Test if the file was uploaded
if fileitem.filename:
    # strip leading path from file name to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    mfn=str(random.random())+fn
    fpath = 'uploaded_files/' + mfn
    f = open('Final_Project/' + fpath, 'wb', 10000)
    # Read the file in chunks
    for chunk in fbuffer(fileitem.file):
        f.write(chunk)
    f.close()
    cursor=config.db.cursor()
    sql="INSERT INTO fpic (fname,fpath) VALUES ('{}','{}')".format(mfn,fpath)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        print('''<script>
        window.location="fsell1.py?msg=File Uploaded successfully"
        </script>''')
    else:
        print('''<script>
                window.location="fsell1.py?msg=File not Uploaded successfully"
        </script>''')
else:
    print('''File was not uploaded''')
    #msg = 'The file "' + os.path.basename(fileitem.filename) + '" was not uploaded successfully'

