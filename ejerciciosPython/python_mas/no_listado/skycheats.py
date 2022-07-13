from re import fullmatch
import eel
import scripts.bunny, scripts.glow, scripts.glowBunny
eel.init("views")
def main(): 
    @eel.expose
    def Bunny(bolean):
        if bolean == True:
            scripts.bunny.main()
    @eel.expose
    def Glow(bolean):
        if bolean == True:
            scripts.glow.main()
    @eel.expose
    def GlowAndBunny(bolean):
        if bolean == True:
            scripts.glowBunny.main()
while True:
    main() 
    eel.start("index.html", block=True ,size=(fullmatch))