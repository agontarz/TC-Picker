from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import pandas as pd

df = pd.read_excel('C:/Users/Aleks/Google Drive/LongMill/Design/ToolChain-Picker/Code/mysite/myapp/SoftwareList.xlsx')
softReturn = df['Name'].loc[df['Difficulty'] == 1]
print(softReturn)

def index(request):
    return HttpResponse(softReturn+", ")
