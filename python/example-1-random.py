
import time
import numpy as np
from LabKitten import LabKitten

def around(x): return np.around(x, 4).tolist()    
def makePlot(x, y):
    return {
        'data': [{'x': around(x), 'y': around(y), 'type': 'scatter' }],
    }

N = 66; timeWindow = 0.5; startTime = time.time()
kitten = LabKitten(
    email='e0134117@u.nus.edu', password='123456', experimentName='random',
    exePath=r'C:\Users\Rick\Desktop\LabKitten-win\LabKitten-win.exe',
)

while True:
    time.sleep(0.1)
    t1 = time.time() - startTime
    t = np.linspace( t1 - timeWindow, t1, N)
    kitten.observe({
        'plots': [ makePlot( t, np.random.rand(*t.shape) ) ],
    })