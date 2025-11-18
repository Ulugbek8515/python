# class Word:
#     def __init__(self,fayl_nomi):
#         self.fayl=fayl_nomi
#     def asosoi_bolim(self):
#         return f"Siz asosiy bo'limdasiz"
#     def joylashgan_kirish(self):
#         return "siz joylash bo'limidasiz"
#     def dizaynga_kirish(self):
#         return "siz dizayn bo'limidasiz"
#     def get_file(self):
#         return f" Siz yaratgan word fayl nomi {self.fayl}"
    
# fayl1=Word("Meros")
# print(fayl1.dizaynga_kirish())

# class Hayvon:
#     def __init__(self, nomi):
#         self.nomi = nomi

#     def tovush_chiqar(self):
#         print(f"{self.nomi} tovush chiqarmoqda")

# class It(Hayvon):
#     def tovush_chiqar(self):
#         print(f"{self.nomi}: vov-vov!")
import datetime as dt
# class Mushuk(Hayvon):
#     def tovush_chiqar(self):
#         print(f"{self.nomi}: Miyov!")

# it = It("itlar")
# mushuk = Mushuk("Mushuklar")

# it.tovush_chiqar()
# mushuk.tovush_chiqar()

# class Talabe:
#     def __init__(self,ism,yil,yonalish,universitet):
#         self.ismi=ism
#         self.yili=yil
#         self.yonalishi=yonalish
#         self.unversisteti=universitet
        
#     def get_name(self):
#         return f"Talaba : {self.ismi}"
#     def get_age(self):
#         return f"Talaba yoshi {2025-self.yili}"
#     def get_yonalish(self):
#         return f"Talaba {self.unversisteti} ning {self.yonalishi} "
#     def get_info(self):
#         return f"TAlaba :{self.ismi}\n talaba yili : {2025-self.yili} \n Talaba universisteti :{self.unversisteti} ning {self.yonalishi}"
# talaba1 = Talabe("Ulug'bek",2010,"Dasturlash","TATU")
# print(talaba1.get_info())
# from datetime import datetime
# class Student:
#     def __init__(self,ismi,yoshi,baho,hozir):
#         self.ism=ismi
#         self.yosh=yoshi
#         self.bahosi=baho
#         # self.hozir_date = dt.datetime.now()
#         self.hozir = hozir
        
#     def get_ism(self):
#         return f"student :{self.ism}"
#     def get_yosh(self):
#         return f"student : {int(self.hozir)-self.yosh}"
#     def get_bahosi(self):
#         return f"student : {self.bahosi}"
#     def get_info(self):
#         return f"student :{self.ism} \n student : {self.yosh} \n student : {self.bahosi}"
# hozir = datem = datetime.today().strftime("%Y")
# student1=Student("Ulug'bek",2010,5,hozir)
# print(student1.get_yosh())

class Avto:
    def __init__(self,nomi,yili,rangi,yurgani):
        self.nomi=nomi
        self.yil=yili
        self.rang=rangi
        self.yurgan=yurgani
    def get_nom():
        return f"Avto mobil nomi: {nomi}"
    def get_yil():
        return f"Avto mobil yili:{yili}"
    def get_rang():
        return f"Avto mobil rangi:{rangi}"
    def get_yurgani():
        return f"Avto mobil yurgani:{yurgani} km"
    def get_info():
        return f"Avto mobil nomi: {nomi}\n Avto mobil yili:{yili} \n Avto mobil rangi:{rangi} \n Avto mobil yurgani:{yurgani} km"
Avtobek=Avto("nexia",2000,'oq',1700,'km')
print(Avtobek.get_info())