import os 
import random
a = [
    "import os", 
    "import numpy", 
    "import streamlit as st",
    "import pandas as pd",
    "import matplotlib.pyplot as plt",
    "import seaborn as sns",
    "import tensorflow as tf",
    "import torch",
    "import cv2",
    "import time",
    "import json",
    "import re",
    "import requests",
    "import sqlite3",
    "import plotly.express as px",
    "import scikit-learn as skl",
    "import keras",
    "import PIL.Image as Image",
    "import sys",
    "import random"
]

x = random.randrange(0, 20)
with open("main.py", "a+") as f1:  
    f1.write("\n"+a[x])
c1= "git add ." 
c2= 'git commit -m "commit"' 
c3= "git branch -M main" 
c4= "git remote add origin https://github.com/GarbhitSh/script.git" 
c5= "git push -u origin main" 
os.system(c1)    
os.system(c2)    
os.system(c3)    
os.system(c4)
os.system(c5)    

