import tkinter as hss

arayüz = hss.Tk()
arayüz.title("hisse(kar)hesaplama")
arayüz.geometry("400x400")

#1 girilen deger(kişi)
kullanıcı=hss.Label(text="kullanıcı adı:")
kullanıcı.place(x=10,y=10)

y=hss.StringVar()
kullanıcı_girişi=hss.Entry(textvariable=y)
kullanıcı_girişi.place(x=85,y=12)

#2 girilen deger(toplam para)
kullanıcı1=hss.Label(text="toplam para:")
kullanıcı1.place(x=10,y=35)

x=hss.StringVar()
toplam_para=hss.Entry(textvariable=x)
toplam_para.place(x=85,y=36)

#3 girilen deger(kar)
kullanıcı2=hss.Label(text="kar:")
kullanıcı2.place(x=57,y=60)

z=hss.StringVar()
kar=hss.Entry(textvariable=z)
kar.place(x=85,y=60)

#ekrana cıktı verme için(kişi)
dogru_yanlis= hss.Label(font="Verdana 15 bold")
dogru_yanlis.place(x=20,y=100)

#ekrana cıktı verme için(toplam para)
dogru_yanlis= hss.Label(font="Verdana 15 bold")
dogru_yanlis.place(x=140,y=100)

#ekrana cıktı verme için(kar)
dogru_yanlis= hss.Label(font="Verdana 15 bold")
dogru_yanlis.place(x=140,y=100)

#buton atama işlemi
def giris_komut():
    kullan1 = y.get()
    kullan2 = float(x.get())
    kullan3 = float(z.get())
    print(kullan1,"\n",kullan2,"\n",kullan3)
    
    #ekrana çıkacak olan metin yazısının döngüsü
    if kullan1 == "mustafa" :
        if  kullan2<=1300:
            mus=kullan3*(((550*100)/1300)/100)
            dogru_yanlis.config(text=mus,fg="green")
        else:
            mus=kullan3*(((550*100)/kullan2)/100)
            dogru_yanlis.config(text=mus,fg="green")
            
    
    elif kullan1 == "furkan":
        if  kullan2<=1300:
            fur=kullan3*(((750*100)/1300)/100)
            dogru_yanlis.config(text=fur,fg="green")
        else:
            fur=kullan3*(((750*100)/kullan2)/100)
            dogru_yanlis.config(text=fur,fg="green")
            

    else:
        print("yanlış isim:")
        
#buton koyma 
giris =hss.Button(text="sorgula",command=giris_komut)
giris.place(x=260,y=70)


arayüz.mainloop()