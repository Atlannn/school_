import PySimpleGUI as pg
import datetime 
from datetime import date
import itertools

class Pakalpojums:
    Pakalpojuma_kategorija = ""
    Pakalpojuma_nosaukums = ""
    Pakalpojuma_cena = 0
    Pakalpojuma_datums = 0



    id_iter = itertools.count() 
    
    def __init__(self):
        self.Produkta_id = next(self.id_iter)+1
        self.Pakalpojums_pieejams = True

    def __init__(self, prod_kategorija=None, prod_nosaukums=None, Datums_cena=10):
        self.Produkta_id = next(self.id_iter)+1
        self.Pakalpojuma_kategorija = prod_kategorija
        self.Pakalpojuma_nosaukums = prod_nosaukums
        self.Pakalpojuma_cena = Datums_cena
        self.Pakalpojums_pieejams = True

    def __repr__(self):   
        if self.Pakalpojuma_kategorija:  return self.prod_kategorija
        elif self.Pakalpojuma_nosaukums:  return self.prod_nosaukums
        elif self.Pakalpojuma_cena:  return self.Datums_cena
        return ''
     
    def Cena_kopa(self):
        kopeja_cena = self.Pakalpojuma_cena
        return kopeja_cena



    def Pakalpojums_info(self):
        return [self.Pakalpojuma_kategorija, self.Pakalpojuma_nosaukums,self.Pakalpojuma_cena]
    

    def Pakalpojums_info_print(self):
        print("Pakalpojuma kategorija: " + str(self.Pakalpojuma_kategorija))
        print("Pakalpojuma nosaukums: " + str(self.Pakalpojuma_nosaukums))
        print("Pakalpojuma cena : " + str(self.Pakalpojuma_cena))
        print("Pakalpojums pieejams: " + str(self.Pakalpojums_pieejams) + "\n")




class Klients:
    Klienta_vards = ""
    Klienta_uzvards = ""
    Klienta_PK = ""
    Klienta_tel_numurs = 0

    id_iter_nom = itertools.count()
    
    def __init__(self, _vards, _uzvards, _pk, _tel_numurs):
        self.Nomnieka_id = next(self.id_iter_nom)+1
        self.Klienta_vards = _vards
        self.Klienta_uzvards = _uzvards
        self.Klienta_PK = _pk
        self.Klienta_tel_numurs = _tel_numurs

    def Klients_info(self):
        return[self.Klienta_vards, self.Klienta_uzvards, self.Klienta_PK, self.Klienta_tel_numurs]    

    def Klients_info_print(self):
        print("Klienta vards: " + self.Klienta_vards)
        print("Klienta uzvards: " +  self.Klienta_uzvards)
        print("Klienta personas kods: " +  self.Klienta_PK )
        print("Klienta telefons : " + str(self.Klienta_tel_numurs) + "\n")  




class Datums:

  
    def __init__(self, sakDat,beigtD, _ilgums):
        self.Datums_sakuma_datums =  sakDat
        self.Datums_beiguma_datums = beigtD
        self.Datuma_ilgums = _ilgums
    def Pakalpojuma_ilgums(self):
        print("Sakuma laiks: " +(self.Datums_sakuma_datums) +"\nBeiguma laiks:" +( self.Datums_beiguma_datums) +"\nPakalpojuma ilgums: " +str(self.Datuma_ilgums) +" minutes")




pg.theme("Reddit")
  
sadala1 = [
    [pg.T("Pakalpojuma kategorija",size=(19,1)),pg.Input("",key="prod_kategorija")],
    [pg.T("Pakalpojuma nosaukums",size =(19,1)),pg.Input("",key="prod_nosaukums")],
    [pg.T("Pakalpojuma cena",size =(19,1)),pg.Input("",key="tehn_raksturojumi")],
    [pg.T("Sakuma laiks",size=(19,1)),pg.Input("",key="sakDat")],
    [pg.T("Beiguma laiks",size=(19,1)),pg.Input("",key="beigtD")],
    [pg.T("Pakalpojuma ilgums",size =(19,1)),pg.Input("",key="_ilgums")],
    [pg.B("Saglabat pakalpojuma datus")],
    
    [pg.T("Klienta vards",size=(19,1)),pg.Input("",key="_vards")],
    [pg.T("Klienta uzvards",size =(19,1)),pg.Input("",key="_uzvards")],
    [pg.T("Personas kods",size =(19,1)),pg.Input("",key="_pk")],
    [pg.T("Telefons",size =(19,1)),pg.Input("",key="_tel_numurs")],
    [pg.B("Saglabat Klienta datus")]
]

sadala2 = [
     [pg.B("Pakalpojuma info, izvada ekrana")],
     [pg.B("Klienta info, izvada ekrana")],
     [pg.B("Pakalpojums: Cena par pakalpojumu kopa")],
     [pg.B("Pakalpojuma ilgums")]
]

sadala3 = [
     [pg.B("Pakalpojums: veidot atskaiti teskta faila formata")],
     [pg.B("Klients: veidot atskaiti teskta faila formata")]
]

tabgrp = [[pg.TabGroup([[pg.Tab("Datu ievade", sadala1, title_color="Red", border_width=10, background_color="Pink", element_justification="center"),
    pg.Tab("Datu izvade", sadala2, title_color="Yellow", border_width=10, background_color="Pink", element_justification="center"),
    pg.Tab("Atskaites printesana", sadala3, title_color="Red", border_width=10, background_color="Pink", tooltip="Veido atskaites teksta failu",  element_justification="center")]],tab_location="centertop", title_color="Black", tab_background_color="Cyan", selected_title_color="White", selected_background_color="Gray", border_width=5),pg.B("Aizvert")]]


window = pg.Window('Skaistumkopšanas salons', tabgrp)

file=open("pakalpojuma_atskaite.txt","w")
file=open("klients_atskaite.txt","w")
  
while True:
    event, values = window.read()
    print(event,values)
    if event == pg.WIN_CLOSED or event =="Aizvert":
      break
    elif event =="Saglabat pakalpojuma datus":
        pk1 = Pakalpojums(values["prod_kategorija"],values["prod_nosaukums"], values[ "tehn_raksturojumi"])
        dl4 = Datums(values["sakDat"],values["beigtD"],values["_ilgums"])
    elif event =="Saglabat Klienta datus":
        kl1 = Klients(values["_vards"],values["_uzvards"], values[ "_pk"],values[ "_tel_numurs"])



    elif event == 'Pakalpojuma ilgums':
        dl4.Pakalpojuma_ilgums() 
    elif event =="Pakalpojuma info, izvada ekrana":
        pk1.Pakalpojums_info_print()
    elif event =="Klienta info, izvada ekrana":
        kl1.Klients_info_print()

    elif event =="Pakalpojums: Cena par pakalpojumu kopa":
        print("Cena kopa:" + str(pk1.Cena_kopa()) +"€") 
     
    elif event =="Pakalpojums: veidot atskaiti teskta faila formata":
        file=open("pakalpojuma_atskaite.txt","a")
        file.write(str(pk1.Pakalpojums_info()))
        file.write("\n")
        file.close() 
    elif event =="Klients: veidot atskaiti teskta faila formata":
        file=open("klients_atskaite.txt","a")
        file.write(str(kl1.Klients_info()))
        file.write("\n")
        file.close()  



            


     
window.close()