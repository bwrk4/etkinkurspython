72



print("ehliyet e sıav geçmek için 70 puan ve üzeri.")
puan = int(input ("e sıav puanın kaç"))
c = input ("Cinsiyetin nedir? ")
if puan < 0 or puan  : print("Yanlış giriş")
else :
    if puan > 100 : print ("mükemmel")
    elif puan > 70 : print ("orta")
    elif puan > 50 : print ("kaldın")
    elif puan > 30 : print ("bidaha sınava girme")
    else : print ("Kalmışsın tekrar deneyin.")


    if puan>85 and  (c.lower() in ["e","erkek"]):
        print("ehliyet e sınav")
    else : print("kalmışsın")


