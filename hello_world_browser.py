import webbrowser
import tempfile
import os

html_content = """
<html>
<head><title>Hello</title></head>
<body><h1>Hello World</h1></body>
</html>
"""

with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as f:
    f.write(html_content.encode('utf-8'))
    tmp_path = f.name

webbrowser.open('file://' + os.path.realpath(tmp_path))
