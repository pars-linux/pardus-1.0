#/usr/bin/python

import os

def postInstall():
    for root, dirs, files in os.walk("/usr/lib/python2.3"):
        for file in files:
            # split filename and its extension
            filename = os.path.splitext(file)[0]
            extension = os.path.splitext(file)[1]

            # if extension is pyc or pyo and, if there is no corresponding py, remove it!
            if extension in (".pyc", ".pyo"):
                if not os.access(os.path.join(root, filename + ".py"), os.F_OK):
                    os.remove(os.path.join(root, file))
 

    os.system("/usr/bin/python /usr/lib/python2.4/compileall.py -q")
    os.system("/usr/bin/python -O /usr/lib/python2.4/compileall.py -q")

    os.system("/usr/bin/python /usr/lib/python2.4/compileall.py -q -x site-packages -x test /usr/lib/python2.4")
    os.system("/usr/bin/python -O /usr/lib/python2.4/compileall.py -q -x site-packages -x test /usr/lib/python2.4")
