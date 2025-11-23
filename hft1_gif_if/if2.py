print("bugün hava kaç derece dışarı çıkcam.")
derece = int(input("kaç derece"))
c = input ("hava açıkmı")
if derece < 10 or derece > 40: print("çoksıcak")
else:
    if derece > 40 : print ("yanıyoz")
    elif derece > 30 : print ("iyi hava")
    elif derece > 22 : print ("esiyo")
    elif derece > 10 : print ("soguk")
    
    if derece > 45 and  (c.lower() in ["h","hava"]):
         print("dışarı çıkabilirsin")
    else : print("dışarı çıkamasın")

    