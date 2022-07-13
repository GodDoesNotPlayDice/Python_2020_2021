import os
def actualizar(t1,t2,t3):
    for i in t1:
        if i[2] != 'Pendiente':
           del t1[0:]
    for i in t2:
        if i[2] != 'Atrasado':
            del t2[0:]
    for i in t3:
        if i[2] != 'Finalizado':
            del t3[0:]

def ordenar(tareas):
    for i in tareas:
        if i[2] == 'Pendiente':
            tareasPendientes.append(i)
        elif i[2] == 'Atrasado':
            tareasAtrasadas.append(i)
        elif i[2] == 'Finalizado':
            tareasFinalizadas.append(i)
        else:
            print('No hay tareas')

def fechas(año,mes,dia):
    fecha = [año,mes,dia]
    return fecha
def crearTarea(ID,nombre,fechaI,fechaT):
    mat = ((fechaT[0] - fechaI[0])*365) + ((fechaT[1] - fechaI[1])*30)+(fechaT[2]-fechaI[2])
    print(mat)
    if mat > 0:
        estado = 'Pendiente'
    else:
        estado = 'Atrasado'
    tareas.append([
        int(ID),f"Nombre: {nombre}", estado, f"Fecha de Inicio: {fechaI}" f"Fecha de Termino: {fechaT}",
    ])
tareas,dias,meses,tareasPendientes,tareasAtrasadas,tareasFinalizadas  = [],[],[],[],[],[]
cont = 1
index = 0
for i in range(1,32):
    dias.append(i)
for i in range(1,13):
    meses.append(i)
while True:
    print('1.- Crear Tarea\n2.- Modificar Tarea\n3.- Consultar Tarea\n4.- Salir')
    opcion= int(input('Opcion: '))
    if opcion==1:
        print("Seleccionó la opción crear")
        nombre = str(input('Nombre: '))
        añoI = int(input('Año de inicio: '))
        mesI = int(input('Mes de inicio: '))
        diaI = int(input('Dia de inicio: '))
        añoT = int(input('Año de Termino: '))
        mesT = int(input('Mes de Termino: '))
        diaT = int(input('Dia de Termino: '))
        if añoT < añoI:
            print('El año de Termino no puede ser menor al de inicio')
        elif añoI < 0 or añoT < 0:
            print('Los años no pueden ser menores a 0')
        elif not (dias.count(diaI) and dias.count(diaT)):
            print('Hay un dia que no corresponde a los dias del año')
        elif not (meses.count(mesI) and meses.count(mesT)):
            print('Hay un mes que no corresponde a los meses del año')
        else:
            inicio = fechas(añoI, mesI, diaI)
            termino = fechas(añoT, mesT, diaT)
            crearTarea(cont,nombre,inicio,termino)
            cont+=1
            os.system('cls')
            print('Tarea Creada!')
           
    elif opcion==2:
        print("Seleccionó la opción modificar")
        idTarea = int(input('Id de la Tarea: '))
        for i in tareas:
            if i[0] == idTarea:
                pos = i.index(idTarea)
                estado = str(input('Nuevo estado: '))
                tareas[pos][2] = estado 
    elif opcion==3:
        ordenar(tareas)
        actualizar(tareasPendientes,tareasAtrasadas,tareasFinalizadas)
        print('''
        Estados:
            Pendiente
            Atrasado
            Finalizado
        ''')
        consulta = str(input('Estado de la Tarea: ')).capitalize()
        if consulta == 'Pendiente':
            for i in tareasPendientes:
                print(i)
        elif consulta == 'Atrasado':
            for i in tareasAtrasadas:
                print(i)
        elif consulta == 'Finalizado':
            for i in tareasFinalizadas:
                print(i)
        else:
            print('No vale a ningun estado.')
    elif opcion==4:
        print('Selecciono la opción salir\nHasta pronto!!')
        quit(0)
