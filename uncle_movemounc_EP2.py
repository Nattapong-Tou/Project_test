# สร้าง 	script ให้ Move เม้าแบบออโต้
import pyautogui
import time


time.sleep(1) # wait 1 minuts
print(pyautogui.position()) # หาตำแหน่งที่เม้าส์วางอยู่
# Point(x=661, y=152)
start_point = (864, 65)

pyautogui.moveTo(start_point) # สั่ง Move เม้าไปยังตำแหน่งที่ต้องการ
pyautogui.click(start_point) # สั่ง click เม้าไปยังตำแหน่งที่ต้องการ

# Move ไปให้สุดบรรทัด
time.sleep(1) # wait 1 minuts
end_point = (1000, 65)
pyautogui.dragTo(end_point, duration=2, button='left')

# กด commancd + c เพื่อ copy
pyautogui.hotkey('command', 'c')

# left text edit
let_note = (218, 93)
pyautogui.click(let_note)
pyautogui.click(let_note)




# วาง
pyautogui.hotkey('command', 'v')
pyautogui.press('enter')
