
# install

```
pip install pyobjc pynput
ipython
from ScriptingBridge import SBApplication
app = SBApplication.applicationWithBundleIdentifier_("com.apple.Terminal")
windows = app.windows()
for window in app.windows():
print ("%s: %d"%(window.name(), window.index()))

active_window = app.windows()[0]
active_window.keystroke("ls\n")
dir(active_window)
# Get the Terminal application's frontmost window
frontmost_window = app.frontmost()

# Print the title of the frontmost window
print(frontmost_window.name())


```


```
from pynput.keyboard import Controller
active_window.activate()
# Send the "ls" command to the active window
keyboard = Controller()
dir(active_window)
keyboard.type("ls\n")

```
