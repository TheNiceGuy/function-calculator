#-------------------------MODULE------------------------------
from package.object.framewindow import *
from package.function.volumefunction import *
#-------------------------CLASS-------------------------------
class writer(object):
    def write(self, data):
        app.notebook.selectpage("Console")
        app.consoleoutput["state"] = "normal"
        app.consoleoutput.insert(END, data)
        app.consoleoutput["state"] = "disabled"
#--------------------------MAIN-------------------------------
if __name__ == "__main__":      
    root = Tk()
    root.title("Function Calculator 0.3")
    root.resizable(width=FALSE, height=FALSE)
    
    app = Application(master=root)

    sys.stdout = writer()
    sys.stderr = writer()

    app.mainloop()
    #root.destroy()