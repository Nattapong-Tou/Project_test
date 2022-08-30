from tqdm import tqdm
from time import sleep
import psutil

with tqdm(total=100, desc='CPU%', position=1) as cpubar, tqdm(total=100, desc='RAM%', position=0) as rambar:
    while True:
        rambar.n=psutil.virtual_memory().percent
        cpubar.n=psutil.cpu_percent()
        rambar.refresh()
        cpubar.refresh()
        sleep(0.5)