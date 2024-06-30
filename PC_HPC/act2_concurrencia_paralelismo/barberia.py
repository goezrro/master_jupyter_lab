import threading
import time
import random
import queue

class Barberia:
    clientesenSala = queue.Queue()
    clientes_atendidos = []
    def __init__(self):       
        self.mutualex = threading.Semaphore(1) 
        self.sillon = threading.Semaphore(1)
        self.semaforosala = threading.Semaphore(3)
        self.barberodormido = True    

def actividadBarbero(Barberia):
    print("El barbero está durmiendo...\n")
    while len(Barberia.clientes_atendidos) < 6:
        time.sleep(3) # 3 segundos de delay en la actividad del barbero
        Barberia.mutualex.acquire()
        if Barberia.clientesenSala.qsize() == 0:
            print("El barbero sigue durmiendo\n")
            Barberia.mutualex.release()                
        else:
            if Barberia.barberodormido:
                print("El barbero se despierta \n") 
                Barberia.barberodormido = False                
            print("El barbero da paso a un cliente\n")            
            cliente = Barberia.clientesenSala.get()
            Barberia.semaforosala.release()
            Barberia.sillon.acquire() # podría ser útil si quisieramos aumentar el número de barberos y sillones en los que se puede cortar pelo, ahora es redundante
            print("El barbero le está cortando el pelo al cliente {}\n".format(cliente))
            time.sleep(random.randint(1,5))
            print("Ha terminado de cortar el pelo al cliente {}\n".format(cliente))
            Barberia.sillon.release()
            Barberia.clientes_atendidos.append(cliente)
            if Barberia.clientesenSala.qsize() == 0:
                print("El barbero se echa a dormir de nuevo\n")
                Barberia.barberodormido = True
            Barberia.mutualex.release()
            
            
            
def actividadCliente(cliente, Barberia):
    time.sleep(random.randint(3,10)) # con esto pretendo que los clientes lleguen un poco más espaciados a la barbería
    print("El cliente {} ha llegado a la barbería\n".format(cliente))
    Barberia.mutualex.acquire()
    if Barberia.clientesenSala.qsize() < 3:
        Barberia.clientesenSala.put(cliente)
        Barberia.semaforosala.acquire()
        print("El cliente {} se sienta en la sala de espera\n".format(cliente))
        Barberia.mutualex.release()
    else:
        print("El cliente {} tiene que esperar fuera a que se libere algún hueco en la sala".format(cliente))
        Barberia.mutualex.release()
        Barberia.semaforosala.acquire() # ponemos a este cliente a esperar hasta que se libere alguna silla en la sala de espera
        print("El cliente {} entra en la sala de espera.".format(cliente))
        Barberia.clientesenSala.put(cliente)


class client():
    def __init__(self, name):
        super().__init__(self)
        self.name=name          
        


if __name__=="__main__":
        barberia= Barberia()
        
        barbero = threading.Thread(target=actividadBarbero, args=(barberia,))
        clientes = []
        nombres=['A','B','C','D','E','F']
        for i in range(len(nombres)):            
           clientes.append(threading.Thread(target=actividadCliente, args=(nombres[i], barberia,)))
        
        barbero.start()
        for cliente in clientes:
            cliente.start()
        
        barbero.join()
        for cliente in clientes:
            cliente.join()
        


