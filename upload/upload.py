import cgi
import cgitb; cgitb.enable()
import os, sys
try: import msvcrt
except ImportError: pass
else:
    for fd in (0,1): msvcrt.setmode(fd, os.O_BINARY)

UPLOAD_DIR = "D:/tmp"

HTML_TEMPLATE = \
"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>upload files</title>
</head>
<body>
    <form action="%(SCRIPT_NAME)s" method="POST" enctype="multipart/form-data">
        File name:<input name = "file_1" type="file"><br>
        <input name = "submit" type="submit">
    </form>
</body>
</html>"""
def print_html_form():
    print("content-type: text/html; charset = iso-8859-1\n")
    print(HTML_TEMPLATE % {'SCRIPT_NAME':os.environ["SCRIPT_NAME"]})

def save_uploaded_file(form_field, upload_dir):
    form = cgi.FieldStorage()
    if not form.has_key(form_field):return
    fileitem = form[form_field]
    if not fileitem.file: return
    fout = open(os.path.join(upload_dir, fileitem.filename), 'wb')
    while True:
        chunk = fileitem.file.read(1000000)
        if not chunk:break
        fout.write(chunk)
    fout.close()

save_uploaded_file("file_1", UPLOAD_DIR)
