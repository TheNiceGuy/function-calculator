from cx_Freeze import setup, Executable
import sys

includes = ["Pmw", "mtTkinter", "math", "os"]
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 
            'pywin.debugger', 'pywin.debugger.dbgcon', 'pywin.dialogs']
packages = ["package"]
path = []

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    version = "0.3",
    description = "Calculate stuff",
    author = "Gabriel-Andrew Pollo Guilbert",
    name = "Function Calculator 0.3",
    options = {"build_exe": {"includes": includes,
                             "excludes": excludes,
                             "packages": packages,
                             "path": path}},
    executables = [Executable("FunctionCalculator.pyw",
                                  base = base)])