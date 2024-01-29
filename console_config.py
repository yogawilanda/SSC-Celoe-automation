#clear the 
import os
from tqdm import tqdm
import time

def loading_progress_bar():
    for i in tqdm(range(100), desc="Mengolah data", unit="Data"):
        time.sleep(0.01)
        
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')