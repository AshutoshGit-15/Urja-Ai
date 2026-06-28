from django.shortcuts import render
from django.http import HttpResponse
import joblib

model=joblib.load("../models/model.pkl")
# Create your views here.

def home(request):
    prediction=None
    if request.method=="POST":
        pass
        # COLLECT DATA FROM WEBPAGE



        # SEND DATA TO MODEL USING DATAFRAME


        # Get Prediction from model

    return render(request,'index.html',{'prediction':prediction})