# EXTRA MEMORY VIEWA

x = memoryview(b"Hello")

print(x)

#return the Unicode of the first character
print(x[0])

#return the Unicode of the second character
print(x[1])
# B transform to bytes and use decode for decoding bytes
bytes = b'altaruru'
print(bytes)
print(bytes.decode("utf-8"))

import keyboard
# It writes the content to output
#keyboard.write("GEEKS FOR GEEKS\n") # MSG for console
  
# It writes the keys r, k and endofline 
#keyboard.press_and_release('shift + r, shift + k, \n')
#keyboard.press_and_release('R, K')
  
# it blocks until ctrl is pressed
# keyboard.wait('Ctrl') # is like to while True loop

# press a to print rk
#keyboard.add_hotkey('a', lambda: keyboard.write('Geek')) # just add a hotkeys to functions 
#keyboard.add_hotkey('ctrl + shift + a', print, args =('you entered', 'hotkey'))

#rk = keyboard.record(until='esc') # it recored all keys in a array
# print(str(keyboard.play(rk, speed_factor = 1))) # play keys recored
# it blocks until esc is pressed

# print(keyboard.is_pressed('ctrl')) can also check whether a button is actually pressed, and return boolean data


# keyboard.wait('esc')