

from Models.App import myApp
app = myApp(True, None, None, None)
try :
    app.run()
    exit()
except Exception as err :
    print(f"{err}")
    app.kill()

