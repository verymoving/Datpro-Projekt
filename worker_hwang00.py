import puck
import box
import numpy as np
n = 0
name =""
def worker_hwang(id, secret, q_request, q_reply):
    #q_request ist eine Queue, in den Workers Kommandos einstecken und zu Tcas schicken...
    #q_reply ist die Antwort von Tcas
    #die Kommandos werden in Tupelform durchgeführt.
    q_request.put(('GET_BOX', id))
    GET_BOX, box = q_reply.get()
    
    #die Information von der Anzahl von Pucks
    q_request.put(('GET_SIZE', id))
    GET_SIZE, n_workers = q_reply.get()

    #fragt entsprechend der Anzahl von n_workers
    for n in range(n_workers):    
       q_request.put(('GET_PUCK', n, id ))
       if n is None :
          puck is None
       else : 
          continue
      
       GET_PUCK, puck = q_reply.get()
    
    q_request.put(('SET_NAME', name, secret, id))
    SET_NAME, id = q_reply.get()
    
    #Beschleunigung einstellen
    a= np.array([5,-2])
    q_request.put(('SET_ACCELERATION', a, secret, id))
    SET_ACCELERATION, a = q_reply.get()
    
    
    
    
    
    
    
        
    
    
    