from django.shortcuts import render

# Create your views here.

import re
from .forms import ImageUploadForm
from keras.applications.resnet import ResNet50
from keras.preprocessing import image
from keras.applications.resnet import preprocess_input, decode_predictions
import numpy as np

# Create your views here.

def handle_uploaded_file(f):
    with open('static/img.jpg','wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def home(request):
    return render(request, 'home.html')

def imageprocess(request):
    form = ImageUploadForm(request.POST, request.FILES)
    print('Validating')
    if form.is_valid():
        handle_uploaded_file(request.FILES['image'])
        model = ResNet50(weights='imagenet')
        img_path = 'static/img.jpg'
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)

        html = decode_predictions(preds, top=5)[0]
        res = []
        for i in html:
            res.append((i[1],np.round(i[2]*100,2)))

        return render(request, 'result.html',{'res':res})
    else:
        print('Invalid file')
    return render(request,'home.html')