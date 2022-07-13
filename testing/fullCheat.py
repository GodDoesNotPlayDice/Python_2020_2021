import pymem
import pymem.process
import keyboard
import math
import time


dwEntityList = (0x4DA521C)
dwLocalPlayer = (0xD8D2CC)
dwForceAttack = (0x31D6750)
m_iTeamNum = (0xF4)
dwGlowObjectManager = (0x52ED6A8)
m_iGlowIndex = (0xA438)
m_iCrosshairId = (0xB3E8)
m_fFlags = (0x104)
dwForceJump = (0x524EFFC)
m_iHealth = (0x100)
m_bDormant = (0xED)
m_vecViewOffset = (0x108)
m_vecOrigin = (0x138)
m_dwBoneMatrix = (0x26A8)
dwClientState = (0x589FE4)
dwClientState_ViewAngles = (0x4D90)
m_iObserverMode = (0x3378)



def normalizeAngles(viewAngleX, viewAngleY):
    if viewAngleX > 89:
        viewAngleX -= 360
    if viewAngleX < -89:
        viewAngleX += 360
    if viewAngleY > 180:
        viewAngleY -= 360
    if viewAngleY < 180:
        viewAngleY += 360
    return viewAngleX, viewAngleY

def checkangles(x, y):
    if x > 89:
        return False
    elif x < -89:
        return False
    elif y > 360:
        return False
    elif y < -360:
        return False
    else:
        return True

def nanchecker(first, second):
    if math.isnan(first) or math.isnan(second):
        return False
    else:
        return True

def calc_distance(current_x, current_y, new_x, new_y):
    distancex = new_x - current_x
    if distancex < -89:
        distancex += 360
    elif distancex > 89:
        distancex -= 360
    if distancex < 0.0:
        distancex = -distancex

    distancey = new_y - current_y
    if distancey < -180:
        distancey += 360
    elif distancey > 180:
        distancey -= 360
    if distancey < 0.0:
        distancey = -distancey
    return distancex, distancey 

def calcangle(localpos1, localpos2, localpos3, enemypos1, enemypos2, enemypos3):
    try:
        delta_x = localpos1 - enemypos1
        delta_y = localpos2 - enemypos2
        delta_z = localpos3 - enemypos3
        hyp = math.sqrt(delta_x * delta_x + delta_y * delta_y + delta_z * delta_z)
        x = math.atan(delta_z / hyp) * 180 / math.pi
        y = math.atan(delta_y / delta_x) * 180 / math.pi
        if delta_x >= 0.0:
            y += 180.0
        return x, y
    except:
        pass

def main():
    pm = pymem.Pymem('csgo.exe')
    aimfov = 120
    swicht = 0
    engine = pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll
    client = pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
    player = pm.read_int(client + dwLocalPlayer)
    engine_pointer = pm.read_int(engine + dwClientState)
    localTeam = pm.read_int(player + m_iTeamNum)
    while True:
        if keyboard.is_pressed('home'):
            exit(0)
        glow_manager = pm.read_int(client + dwGlowObjectManager)
        for i in range(1,32):
            entity = pm.read_int(client + dwEntityList + i * 0x10)
            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)
                if entity_team_id == 2:
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(1)) # R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0)) # G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0)) # B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1)) # A
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1) # Enabling

                elif entity_team_id == 3:
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0)) # R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0)) # G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1)) # B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1)) # A
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1) # Enabling
            if keyboard.is_pressed("space"):
                force_jump = client + dwForceJump
                player = pm.read_int(client + dwLocalPlayer)
                on_ground = pm.read_int(player + m_fFlags)
                if player and on_ground and on_ground == 257:
                    pm.write_int(force_jump, 5)
                    time.sleep(0.08)
                    pm.write_int(force_jump, 4)
        target = None
        olddistx = 111111111111
        olddisty = 111111111111
        for i in range(1,32):
            entity = pm.read_int(client + dwEntityList + i * 0x10)
            if entity:
                try:
                    entity_team_id = pm.read_int(entity + m_iTeamNum)
                    entity_hp = pm.read_int(entity + m_iHealth)
                    entity_dormat = pm.read_int(entity + m_bDormant)
                except:
                    print('finds player info once')
                if localTeam != entity_team_id and entity_hp > 0:
                    entity_bones = pm.read_int(entity + m_dwBoneMatrix)
                    localpos_x_angles = pm.read_float(engine_pointer + dwClientState_ViewAngles)
                    localpos_y_angles = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)
                    localpos_z_angles = pm.read_float(player + m_vecViewOffset + 0x8)
                    localpos1 = pm.read_float(player + m_vecOrigin)
                    localpos2 = pm.read_float(player + m_vecOrigin + 4)
                    localpos3 = pm.read_float(player + m_vecOrigin + 8) + localpos_z_angles
                    
                    try:
                        entitypos_x = pm.read_float(entity_bones + 0x30 * 8 + 0xC)
                        entitypos_y = pm.read_float(entity_bones + 0x30 * 8 + 0x1C)
                        entitypos_z = pm.read_float(entity_bones + 0x30 * 8 + 0x2C)
                    except:
                        continue
                    X, Y = calcangle(localpos1, localpos2, localpos3, entitypos_x, entitypos_y, entitypos_z)
                    newdist_x, newdist_y = calc_distance(localpos_x_angles, localpos_y_angles, X, Y)

                    if newdist_x < olddistx and newdist_y < olddisty and newdist_x <= aimfov and newdist_y <= aimfov:
                        olddistx, olddisty = newdist_x, newdist_y
                        target, target_hp, target_dormart = entity, entity_hp, entity_dormat
                        target_x, target_y, target_z = entitypos_x, entitypos_y, entitypos_z
                if keyboard.is_pressed('alt') and player:
                    if target and target_hp > 0 and not target_dormart:
                        x,y = calcangle(localpos1, localpos2, localpos3, target_x, target_y, target_z)
                        normalize_x, normalize_y = normalizeAngles(x,y)
                        pm.write_float(engine_pointer + dwClientState_ViewAngles, normalize_x)
                        pm.write_float(engine_pointer + dwClientState_ViewAngles + 0x4, normalize_y)
        localPlayer = pm.read_int(client + dwLocalPlayer)
        crosshairID = pm.read_int(localPlayer + m_iCrosshairId)
        getTeam = pm.read_int(client + dwEntityList + (crosshairID - 1) * 0x10)
        localTeam = pm.read_int(localPlayer + m_iTeamNum)
        crosshairTeam = pm.read_int(getTeam + m_iTeamNum)
        if crosshairID > 0 and crosshairID < 32 and localTeam != crosshairTeam:
            pm.write_int(client + dwForceAttack, 6)
        if keyboard.is_pressed('z') and swicht == 0:
            pm.write_int(localPlayer + m_iObserverMode, 1)
            swicht = 1
            time.sleep(0.5)
        elif keyboard.is_pressed('z') and swicht == 1:
            pm.write_int(localPlayer + m_iObserverMode, 0)
            swicht = 0
            time.sleep(0.5)
if __name__ == '__main__':
    main()