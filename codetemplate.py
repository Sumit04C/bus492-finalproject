from appJar import gui


#Sample Team Project Extra Credit -- Shopping Application 110%
#Make sure to include the files for your team csv and .gif in your submission!
#include the app.Jar folder in the folder where your team files are stored

#Function to greet the user and ask for a category

import pandas
import chatbot
import tkinter
cart = ""
total = 0
bye = []
tdf=pandas.read_csv("KeyboardTeam15.csv")
switcheslist = list(tdf.Switches)
layoutlist = list(tdf.CaseLayout)
keycaplist = list(tdf.KeycapProfiles)
def greet_user(greeting,sentinel,categoryq,readyq):
    canswer = ' '
    ranswer = sentinel
    print(greeting)
    while ranswer == sentinel:
        canswer = input(categoryq)
        ranswer = input(readyq)
    if canswer == "Switches":
        switches("Welcome to our Switches section! Here are your choices:",switcheslist,"Which Switch would you like or enter None? ")
    elif canswer == "Case Layout":
        layouts("Welcome to our Case Layout section!  Here are your choices:",layoutlist,"Which Case Layout would you like or enter None? ")
    elif canswer == "Keycap Profiles":
        profiles("Welcome to our Keycap Profiles section! Here are your choices:",keycaplist,"Which Keycap would you like or enter None? ")
    else:
        print('Sorry, we do not carry that category.  See you next time!')

#Sumit Chhabra
#Function to ask user to pick a Switch
def switches(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    switchespick = input(pickq)
    if switchespick == "None":
        print("Goodbye")
    elif switchespick == "Linear":
        closing("Linear",21,"Have fun typing with your Linear switches!" )
    elif switchespick == "Tactile":
        closing("Tactile",20,"Have fun typing with your Tactile switches!" )
    elif switchespick == "Clicky":
        closing("Clicky",25,"Have fun typing with your Clicky switches!" )
    else:
        closing("Silent",30,"Have fun typing with your Silent switches!" )
    
#Tina Du
#Function to ask user to pick a Case Layout
def layouts(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    layoutpick = input(pickq)
    if layoutpick == "None":
        print("Goodbye")
    elif layoutpick == "TKL":
        closing("TKL",70,"Great choice! Hope the TKL layout meets your typing needs!" )
    elif layoutpick == "75%":
        closing("75%",60,"Great choice! Hope the 75% layout meets your typing needs!" )
    elif layoutpick == "65%":
        closing("65%",50,"Great choice! Hope the 65% layout meets your typing needs!" )
    else:
        closing("Full Size",80,"Great choice! Hope the Full Size layout meets your typing needs!" )

#David Le        
#Function to ask user to pick a Keycap Profile
def profiles(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    profilespick = input(pickq)
    if profilespick == "None":
        print("Goodbye")
    elif profilespick == "OEM":
        closing("OEM",20,"Experience the comfort and style of your chosen OEM profile keycaps!")
    elif profilespick == "Cherry":
        closing("Cherry",30,"Experience the comfort and style of your chosen Cherry profile keycaps!")
    elif profilespick == "XDA":
        closing("XDA",45,"Experience the comfort and style of your chosen XDA profile keycaps!")
    else:
        closing("SA",50,"Experience the comfort and style of your chosen SA profile keycaps!")

#Johnson Luong        
#Function to give user total price of purchase
def closing(pickeditem,price,goodbye):
    global cart
    global total
    global bye
    cart = cart + " " + pickeditem
    bye.append(goodbye)
    total = total + price
    ttotal = total*1.09
    print("Your items so far:",cart)
    print("Your cost for the",pickeditem,"is $%.2f."%price)
    print("Your total cost is $%.2f."%total)
    print("Your total cost plus tax is $%.2f."%ttotal)
    more = input("Would you like to pick another item (y/n)?")
    if more == "y":
        greet_user("Great!", "n", "What category would you like to browse (Switches, Case Layout, Keycap Profiles)? ", "Ready to browse (y/n)? ")
    else:
        print("Please pay $%.2f!"%ttotal)
        print("Your menu:")
        for l in cart:
            print(l,end="")
        print()
        for b in bye:
            print(b)
        print("Thanks for shopping at DSJT Keyboard Shop. We hope you enjoy your purchase and shop with us again!")


    
#make the code on line 119 a comment (use #) for 100% submission
        
#greet_user("Welcome to our store", "n", "What category would you like to browse (Switches, Case Layout, Keycap Profiles)? ", "Ready to browse (y/n)? ")





#Uncomment this section for 100% submission (remove the three quote marks from lines 123 and 183)
#This is the function that determines code executed when each button is pressed

#Each teammember should replace the Button name assigned to btn (see line 91 for an example) 
#in the if-elif statements below with
#a short title for his/her function.  Then place a call to the
#corresponding function on the next line



def press(btn):
    if btn == "Exit":
        app.stop()
    elif btn == "Hello":
        greet_user("Welcome to our store", "n", "What category would you like to browse (Switches, Case Layout, Keyboard Profiles)? ", "Ready to browse (y/n)? ")
    elif btn == "Switches":
        switches("Welcome to our Switches section! Here are your choices:",switcheslist,"Which Switch would you like or enter None? ")
    elif btn == "Case Layout":
         layouts("Welcome to our Case Layout section!  Here are your choices:",layoutlist,"Which Case Layout would you like or enter None? ")    
    elif btn == "Keycap Profiles":
         profiles("Welcome to our Keycap Profiles section! Here are your choices:",keycaplist,"Which Keycap would you like or enter None? ")   
    elif btn == "Close":
        app.infoBox("b1","Thanks for shopping at DSJT Keyboard Shop!")
    elif btn == "Chatbot":
        chatbot.chatter()
    else:
        print('Pick a valid option')


#The code below defines the gui, adding buttons, labels, images, color, etc.
#
#Make changes to the title (line 163), image (line 169), and button
#names (lines 175 to 180)

#Edit 500x500 in line 159 to make your window bigger or smaller

app=gui("Main Menu","500x500")

#Replace "Welcome to Our Store's Main Menu" with your team's greeting in line 117

app.addLabel("title", "Welcome to DSJT Keyboard Shop's Main Menu")
app.setLabelBg("title", "orange")

#Find your team gif image, save to your project code folder, and replace k.gif
#with the image file name in line 166

app.addImage("decor","bongocat.gif")
app.setFont(18)

#change the first parameter of the addButton method in lines 172 to 177 with names aligning with your team functions
#make sure they match the Button names in the press function above

app.addButton("Hello", press)
app.addButton("Switches", press)
app.addButton("Case Layout", press)
app.addButton("Keycap Profiles", press)
app.addButton("Chatbot",press)
app.addButton("Close", press)
app.addButton("Exit",press)
app.go() #displays the gui


