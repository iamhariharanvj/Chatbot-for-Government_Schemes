import os
from time import sleep
os.system('cmd /c "pip install -r requirements.txt"')


directory = __file__[:-len('run.py')]
os.chdir(directory)
os.system('cmd /c "python train.py"')

os.system('cmd /c "python api.py"')
