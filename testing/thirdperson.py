import pymem
import pymem.process
import keyboard
import time

m_iObserverMode = (0x3378)
dwLocalPlayer = (0xD8D2CC)

swicht = 0

pm = pymem.Pymem('csgo.exe')
client = pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
while True:
    localplayer = pm.read_int(client + dwLocalPlayer)
    if keyboard.is_pressed('z') and swicht == 0:
        pm.write_int(localplayer + m_iObserverMode, 1)
        swicht = 1
        time.sleep(0.5)
    elif keyboard.is_pressed('z') and swicht == 1:
        pm.write_int(localplayer + m_iObserverMode, 0)
        swicht = 0
        time.sleep(0.5)