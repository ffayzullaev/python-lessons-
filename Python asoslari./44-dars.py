class Avto:
    __num_avto = 0 
    def __init__(self,make,model,rang,yil,narh):
        self.make = make
        self.model = model
        self.rang = rang 
        self.yil = yil
        self.narh = narh
        Avto.__num_avto +=1
        
    def __repr__(self):
        return f"Avto: {self.make} {self.model}"
    
    def __eq__(self, y):
        return self.narh==y.narh
    
    def __lt__(self,y):
        return self.narh<y.narh
    
    def __le__(self,y):
        return self.narh<y.narh

class AvtoSalon:
    def __init__(self,name):
        self.name = name
        self.avtolar = []
        
    def __repl__(self):
        return f"{self.name} avtolasoni"
    
    def __len__(self):
        return len(self.avtolar)
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,qiymat):
        self.avtolar[index]=qiymat
        
    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting")
        
salon1 = AvtoSalon("MaxAvto")
    
avto1 = Avto("GM", "Malibu", "Qora", 2000, 40000)
avto2 = Avto("GM", "Lacetti", "Oq", 2020, 21000)
avto3 = Avto("Toyota", "Carolla", "Silver", 2018, 45000)
salon1.add_avto(avto1, avto2, avto3)
