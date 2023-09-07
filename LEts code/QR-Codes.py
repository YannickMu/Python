import pyqrcode

url = pyqrcode.create("https://www.youtube.com/watch?v=qH8bwfeUMIk", error='H')
url.png('../../Desktop/tests/Bilder/Yannick.png', module_color=(200, 255, 0, 255), background=(255, 255, 255, 255), scale=100)
print(url.terminal('green', 'black'))