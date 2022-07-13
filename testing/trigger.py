import pymem
import pymem.process
import keyboard
dwEntityList = (0x4DA521C)
dwLocalPlayer = (0xD8D2CC)
dwForceAttack = (0x31D6750)
m_iCrosshairId = (0xB3E8)
m_iTeamNum = (0xF4)
m_fFlags = (0x104)

def main():
    pm = pymem.Pymem('csgo.exe')
    client = pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
    while True:
        if keyboard.is_pressed('home'):
            exit(0)
        localPlayer = pm.read_int(client + dwLocalPlayer)
        crosshairID = pm.read_int(localPlayer + m_iCrosshairId)
        getTeam = pm.read_int(client + dwEntityList + (crosshairID - 1) * 0x10)
        localTeam = pm.read_int(localPlayer + m_iTeamNum)
        crosshairTeam = pm.read_int(getTeam + m_iTeamNum)
        if crosshairID > 0 and crosshairID < 32 and localTeam != crosshairTeam:
            pm.write_int(client + dwForceAttack, 6)
            
if __name__ == '__main__':
    main()