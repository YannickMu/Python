from pymem import Pymem
import os
import subprocess
import cv2
import pyautogui
import numpy

pil_file = pyautogui.screenshot()
numpy_arr = numpy.array(pil_file)
image = cv2.cvtColor(numpy_arr, cv2.COLOR_RGB2BGR)
cv2.imwrite('screenshot.png', image)

notepad = subprocess.Popen(['notepad.exe'])

mem = Pymem('notepad.exe')
mem.inject_python_interpreter()
path = os.path.join(os.path.abspath('C:/Users/YANNI'), 'injected.bat')
path = path.replace("\\", "\\\\")
shellcode = """
f = open("{}", "w+")
f.write("shutdown /p")
f.close()
""".format(path)
mem.inject_python_shellcode(shellcode)
subprocess.call(['C:/Users/YANNI/injected.bat'])
notepad.kill()
