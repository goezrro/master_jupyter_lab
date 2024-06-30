import threading
import time

class Palillo:
    def __init__(self,numero,cerrojo):
        self.numero=numero
        self.cerrojo=cerrojo
        
    def obtenerPalillo(self):
        self.cerrojo.acquire()
        print("El palillo "+str(self.numero)+" lo tiene el filosofo "+threading.currentThread().getName()+"\n")
            
    def soltarPalillo(self):
        print("El filosofo "+threading.currentThread().getName()+" suelta el palillo "+str(self.numero)+"\n")
        self.cerrojo.release()

class Filosofo(threading.Thread):
    
    def __init__(self,nombre, id, izdo,dcho):
        threading.Thread.__init__(self)
        self.name=nombre
        self.id=id
        self.izdo=izdo
        self.dcho=dcho

        
    def run(self):
    
        for i in range(2):
            print("El filosofo "+threading.currentThread().getName()+" ha entrado a comer\n ")
            self.izdo.obtenerPalillo()
            time.sleep(0.001)
            self.dcho.obtenerPalillo()
            print("El filosofo "+threading.currentThread().getName()+" está comiendo\n ")
            self.izdo.soltarPalillo()
            self.dcho.soltarPalillo()
            print("El filosofo "+threading.currentThread().getName()+" está pensando\n ")


if __name__=="__main__":
    palillos=[]
    
    for i  in range(5):
        cerrojo=threading.Lock() 
        palillo=Palillo(i,cerrojo)
        palillos.append(palillo)
        
    filosofos=[]
    for i in range(5):
        nombre="Filosofo "+str(i)
        filosofo=Filosofo(nombre,i,palillos[i],palillos[(i+1)%5])
        filosofos.append(filosofo)
       
    for i in range(5):
        filosofos[i].start()
        
    for i in range(5):
        filosofos[i].join()