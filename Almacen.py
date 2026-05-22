from Galletitas import *
from Gaseosas import *
from Golosinas import *
from Perfumeria import *
from Electrodomesticos import *
from Carniceria import *
from Verduleria import *
from Fiambreria import *
from collections import Counter 


class Almacen: 

    def __init__(self):
        self.__productos = []
        self.cantidad_productos=Counter()
    
    def precio_final_pre_promos(self,carrito):
        precio_final=0
        for i in carrito:
            precio_final+=i.get_precio()
            return precio_final
        
    def precio_final_con_promos(self,carrito):

        for i in carrito:
            if i.get_sector()=="Galletitas":
                self.cantidad_productos.append[i.codigo]+=1

            if i.get_sector()=="Gaseosas":
                self.cantidad_productos.append[i.codigo]+=1
            
            if i.get_sector()=="Perfumeria":
                self.cantidad_productos.append[i.codigo]+=1
            
            

        pitus=self.cantidad_productos["001"]
        sonris=self.cantidad_productos["002"]
        porte=self.cantidad_productos["003"]

        if pitus%2==0:
            preciodescuento1=(pitus*330)/2
        else:
            preciodescuento1=(((pitus-1)*330)/2) 

        if sonris%2==0:
            preciodescuento2=(sonris*400)/2
        else:
            preciodescuento2=(((sonris-1)*400)/2) 

        if porte%2==0:
            preciodescuento3=(porte*1200)/2
        else:
            preciodescuento3=(((porte-1)*1200)/2) 

        coca=self.cantidad_productos["004"]
        sprite=self.cantidad_productos["005"]
        manaos=self.cantidad_productos["006"]

        if coca%2==0:
            preciosdescuento4=(coca/2)*3000*0.30
        else:
            preciodescuento4=((coca-1)/2)*3000*0.30
        
        if sprite%2==0:
            preciosdescuento5=(sprite/2)*3000*0.30
        else:
            preciodescuento5=((sprite-1)/2)*3000*0.30
        if manaos%2==0:
            preciosdescuento6=(manaos/2)*1000*0.30
        else:
            preciodescuento6=((manaos-1)/2)*1000*0.30

        lavan=self.cantidad_productos["007"]
        zorro=self.cantidad_productos["008"]
        jabon=self.cantidad_productos["009"]

        preciodescuento7=(lavan*900)/2
        preciodescuento8=(zorro*900)/2
        preciodescuento9=(jabon*200)/2

        preciofinal=self.precio_final_pre_promos(carrito)
        preciofinaldefinitivo=preciofinal-preciodescuento9-preciodescuento8-preciodescuento7-preciodescuento6-preciodescuento5-preciodescuento4-preciodescuento3-preciodescuento2-preciodescuento1



        
        

        

        

        

        
            


                



        

            
        
