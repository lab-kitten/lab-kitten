
import time
import numpy as np
from LabKitten import LabKitten

def sin(f,t): return np.sin(2 * np.pi * f * t) 
def around(x): return np.around(x, 4).tolist()    
def makePlot(y1, y2):
    return {
        'data': [
            {'x': 'commonX', 'y': around(y1), 'type': 'scatter' },
            {'x': 'commonX', 'y': around(y2), 'type': 'scatter' },
        ],
        'layout': {'height': 300, 'title': 'lab kitten meow !'}
    }

N = 66; timeWindow = 0.5; startTime = time.time()
kitten = LabKitten(
    email='e0134117@u.nus.edu', password='123456', experimentName='sine wave',
    exePath=r'D:\GitHub\1-lab-kitten\LabKitten-win\LabKitten-win.exe',
)

while True:
    time.sleep(0.1)
    t1 = time.time() - startTime
    t = np.linspace( t1 - timeWindow, t1, N)
    kitten.observe({
        'plots': [
            makePlot( sin(1,t), sin(2,t) ), 
            makePlot( sin(3,t), sin(4,t) ), 
        ],
        'commonX': around(t),
    })