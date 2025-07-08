#pip install tqdm
from tqdm import tqdm
import time
list=['M','O','H','A','M','M','E','D',' ','T','A','H','A',' ','T','A','V','A','N','A']
w=''
for i in tqdm(list,desc='Progressbar with python ',colour='MAGENTA'):
    w=w+i
    time.sleep(.25)
print(w)