import eel
import scripts.GlowBunny, scripts.Glow
eel.init("views")
@eel.expose
def GlowBunnySelect(on,off):
    if on == True:
        try:
            scripts.GlowBunny.main()
        except:
            print('Closed')
    if off == True:
        print('Finish...')
        quit()
@eel.expose
def Glow(on,off):
    if on == True:
        try:
            scripts.Glow.main()
        except:
            print('pls open CSGO')
    if off == True:
        print('Finish...')
        quit()

eel.start("index.html", block=True ,size=(1000,600))
