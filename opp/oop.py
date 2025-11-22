# # class Word:
# #     def __init__(self,fayl_nomi):
# #         self.fayl=fayl_nomi
# #     def asosoi_bolim(self):
# #         return f"Siz asosiy bo'limdasiz"
# #     def joylashgan_kirish(self):
# #         return "siz joylash bo'limidasiz"
# #     def dizaynga_kirish(self):
# #         return "siz dizayn bo'limidasiz"
# #     def get_file(self):
# #         return f" Siz yaratgan word fayl nomi {self.fayl}"
    
# # fayl1=Word("Meros")
# # print(fayl1.dizaynga_kirish())

# # class Hayvon:
# #     def __init__(self, nomi):
# #         self.nomi = nomi

# #     def tovush_chiqar(self):
# #         print(f"{self.nomi} tovush chiqarmoqda")

# # class It(Hayvon):
# #     def tovush_chiqar(self):
# #         print(f"{self.nomi}: vov-vov!")
# import datetime as dt
# # class Mushuk(Hayvon):
# #     def tovush_chiqar(self):
# #         print(f"{self.nomi}: Miyov!")

# # it = It("itlar")
# # mushuk = Mushuk("Mushuklar")

# # it.tovush_chiqar()
# # mushuk.tovush_chiqar()

# # class Talabe:
# #     def __init__(self,ism,yil,yonalish,universitet):
# #         self.ismi=ism
# #         self.yili=yil
# #         self.yonalishi=yonalish
# #         self.unversisteti=universitet
        
# #     def get_name(self):
# #         return f"Talaba : {self.ismi}"
# #     def get_age(self):
# #         return f"Talaba yoshi {2025-self.yili}"
# #     def get_yonalish(self):
# #         return f"Talaba {self.unversisteti} ning {self.yonalishi} "
# #     def get_info(self):
# #         return f"TAlaba :{self.ismi}\n talaba yili : {2025-self.yili} \n Talaba universisteti :{self.unversisteti} ning {self.yonalishi}"
# # talaba1 = Talabe("Ulug'bek",2010,"Dasturlash","TATU")
# # print(talaba1.get_info())
# # from datetime import datetime
# # class Student:
# #     def __init__(self,ismi,yoshi,baho,hozir):
# #         self.ism=ismi
# #         self.yosh=yoshi
# #         self.bahosi=baho
# #         # self.hozir_date = dt.datetime.now()
# #         self.hozir = hozir
        
# #     def get_ism(self):
# #         return f"student :{self.ism}"
# #     def get_yosh(self):
# #         return f"student : {int(self.hozir)-self.yosh}"
# #     def get_bahosi(self):
# #         return f"student : {self.bahosi}"
# #     def get_info(self):
# #         return f"student :{self.ism} \n student : {self.yosh} \n student : {self.bahosi}"
# # hozir = datem = datetime.today().strftime("%Y")
# # student1=Student("Ulug'bek",2010,5,hozir)
# # print(student1.get_yosh())
# # 2
# # class Avto:
# #     def __init__(self,nomi,yili,rangi,yurgani):
# #         self.nom=nomi
# #         self.yil=yili
# #         self.rang=rangi
# #         self.yurgan=yurgani
# #     def get_nom(self):
# #         return f"mashina nomi {nom}"
# #     def get_yil(self):
# #         return f"mashina ishlab chiqarilgan sanasi {yil}"
# #     def get_rangi(self):
# #         return f"mashina rangi {rang}"
# #     def get_yurgan(self):
# #         return f"mashina yurgani {yurgan} km"
# #     def get_info(self):
# #         return f"mashina nomi {nom} \n mashina ishlab chiqarilgan sanasi {yil} \n mashina rangi {rang} \n mashina yurgani {yurgan} km"
# # avtobek=Avto("nexia",2000,'qora',10000)
# # print(avtobek.get_info())
# # 3
# # class Bank:
# #     def __init__(self,balans,pul_qosh,pul_ayir):
# #         self.balansi=balans
# #         self.pulqosh=pul_qosh
# #         self.pulayirish=pul_ayir
# #     def get_mablag(self):
# #         return f" bor mablag'ingiz {balans}"
# # 3 Bank kartasi
# # class Bank:
# #     def __init__(self, balans=0):
# #         self.balans = balans

# #     def pul_qoshish(self, miqdor):
# #         if miqdor > 0:
# #             self.balans += miqdor
# #             print(f"{miqdor} doll qo'shildi. Yangi balans: {self.balans} doll")
# #         else:
# #             print("Musbat bo'lishi kerak!")
# #     def pul_yechish(self, miqdor):
# #         if miqdor <= 0:
# #             print("musbat bo'lishi kerak!")
# #         elif miqdor > self.balans:
# #             print("hiobda pul yoq!")
# #         else:
# #             self.balans -= miqdor
# #             print(f"{miqdor} doll yechildi. Yangi balans: {self.balans} doll")
# # hisob = Bank(10000)
# # hisob.pul_qoshish(15001)
# # hisob.pul_yechish(1)
# # 4
# # class Dokon:
# #     def _init__(self, dokon_nomi):
# #         self.dokon = dokon_nomi
# #         self.mahsulot = []
# #         self.mahsulot_soni = 0
# #     def add_product(self, mahsulot_nomi):
# #         self.mahsulot.append(mahsulot_nomi) 
# #         self.mahsulot_soni +=1
# #     def delete_product(self,product_name): 
# #         self.mahsulot.remove(product_name)
# #         self.mahsulot_soni -=1
# #     def get_info(self): 
# #         matn = "\n".join([name for name in self.mahsulot]) 
# #         return f"{self.dokon} da {self.mahsulot_soni}"
        
# # xalimaxon  = Dokon ("Xalimahon")
# # xalimaxon.add_product("Non")
# # xalimaxon.add_product("Shakar")
# # xalimaxon.add_product("Tuz")
# # xalimaxon.add_product("Qatiq")
# # magnit = Dokon("Magnit")
# # magnit.add_product("Olma")
# # magnit.add_product("Uzum")
# # magnit.add_product("Anor")
# # xalimaxon.delete_product("Non")
# # magnit.delete_product("Uzum")
# # print(xalimaxon.get_info(), magnit.get_info())
# # 6
# # class Mashina:
# #     def __init__(self,model,telik,hududi):
# #         self.model=model
# #         self.tezlik=telik
# #         self.hududi=hududi
        
# #     def yol_tezlikini_kamaytiruvchi(self,hudud,yol,yol1,yol2):
        
# #         hudud=["trasa","shahar","Aholi yoq joy"]
# #         # yol=[150,80,100]
# #         yol1=150
# #         yol2=80
# #         yol=100
# #         if hudud[0]==self.hududi:
            
# #             if self.tezlik>yol1:
# #                 return f"{ self.model} haydovchi tezligi {self.tezlik - yol1} km/h pasay tiring"
            
# #         if hudud[1]==self.hududi:
            
# #             if self.tezlik>yol2:
# #                 return f'{ self.model} haydovchi tezligi  {self.tezlik - yol2 } km/h pasay tiring '
            
# #         if hudud[2]==self.hududi:
            
# #             if self.tezlik>yol:
# #                 return f"{ self.model} haydovchi tezligi {self.tezlik  - yol}  km/h pasay tiring"
            

            
# # mashinaa=Mashina('KIA',100,'trasa')
# # print(mashinaa.yol_tezlikini_kamaytiruvchi(90 , 'trasa',90 ,90))







# class Mashina :
    
#     def __init__(self , model , tezlik , hudut):
#         self.model = model 
#         self.tezlik = tezlik
#         self.hudut = hudut


#     def decrease_speed(self , car_speed , hududlar):
#         hududlar = ['Shahar' , 'aholi_yoq' , 'trassa']
#         car_speed = [60 , 90 , 150]
#         if self.hudut == hududlar[0] :

#             if self.tezlik > car_speed[0] :
#                 return f"{self.model} Haydovchisi tealigingizni {self.tezlik - car_speed[0]} km/h ga kamaytiring"
            
#             return 'siz tog\'ri harakat qilayapsiz'
        
#         elif self.hudut == hududlar[1] :

#             if self.tezlik > car_speed[1] :
#                 return f"{self.model} Haydovchisi tealigingizni {self.tezlik - car_speed[1]} km/h ga kamaytiring"
            
#             return 'siz tog\'ri harakat qilayapsiz'
        
#         elif self.hudut == hududlar[2] :

#             if self.tezlik > car_speed[2] :
#                 return f"{self.model} Haydovchisi tealigingizni {self.tezlik - car_speed[0]} km/h ga kamaytiring"
            
#             return 'siz tog\'ri harakat qilayapsiz'
    
#     def increase_speed(self , car_speed , drive_road):
#         drive_road = ['Shahar' , 'aholi_yoq' , 'trassa']
#         car_speed = [60 , 90 , 150]
#         if self.hudut == drive_road[0] :

#             if self.tezlik > car_speed[0] :
#                 return f"{self.model} mashinasi haydovchisi siz tezligingizni {self.tezlik - car_speed[0]} km/h gacha oshirishingiz mumkin"
            
#         if self.hudut == drive_road[1] :

#             if self.tezlik > car_speed[1] :
#                 return f"{self.model} mashinasi haydovchisi siz tezligingizni {self.tezlik - car_speed[1]} km/h gacha oshirishingiz mumkin"
            
#         if self.hudut == drive_road[2] :

#             if self.tezlik > car_speed[2] :
#                 return f"{self.model} mashinasi haydovchisi siz tezligingizni {self.tezlik - car_speed[2]} km/h gacha oshirishingiz mumkin"
    
# mashina1 = Mashina('cobalt' , 120 , 'aholi_yoq')
# print(mashina1.increase_speed(90 , 'trassa'))