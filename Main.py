

from Models.App import myApp
app = myApp(True, None, None, None)
try :
    # print("[- Try app -]")
    app.run()
    exit()
except Exception as err :
    # print("#- Main exception : -#")
    print(f"{err}")
    app.kill()

