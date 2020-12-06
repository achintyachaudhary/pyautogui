import pyautogui

print('x and y cordinate of your mouse currently is - '.format(pyautogui.position()))

is_instagram = False
message = 'hello world'
if is_instagram:
    for i in range(3000):
        pyautogui.moveTo(1000, 666, duration=0.1)
        pyautogui.click()
        pyautogui.write(message)
        pyautogui.moveRel(80, 0, duration=0.1)
        pyautogui.click()
else:
    for i in range(3000):
        pyautogui.moveTo(1281, 698, duration=0.0000000001)
        pyautogui.click()
        pyautogui.write(message)
        pyautogui.moveRel(60, 0, duration=0.0000000001)
        pyautogui.click()
