
import time
import numpy as np
from LabKitten import LabKitten

def sin(f,t): return np.sin(2 * np.pi * f * t) 
def around(x): return np.around(x, 4).tolist()    
def makePlot(y1, y2):
    return {
        'data': [
            {'x': 'commonX', 'y': around(y1), 'z': around(y2), 'type': 'scatter3d' },
        ],
        'layout':{
            'scene':{
	            'aspectmode': "manual",
                'aspectratio': { 'x': 1, 'y': 1, 'z': 1 },
                'yaxis': { 'nticks': 10, 'range': [-1, 1] },
                'zaxis': { 'nticks': 10, 'range': [-1, 1] }
            }
        }
    }

N = 66; timeWindow = 0.5; startTime = time.time()
kitten = LabKitten(
    email='e0134117@u.nus.edu', password='123456', experimentName='sine wave',
    exePath=r'C:\Users\Rick\Desktop\LabKitten-win\LabKitten-win.exe',
)

while True:
    time.sleep(0.1)
    t1 = time.time() - startTime
    t = np.linspace( t1 - timeWindow, t1, N)
    kitten.observe({
        'plots': [
            makePlot( sin(1,t), sin(2,t) ), 
        ],
        'commonX': around(t),
    })