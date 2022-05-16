from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from django_tables2.tables import Table
import pandas as pd
# Create your views here.
def home(request):
    folder='my_folder/'
    if request.method == 'POST' and request.FILES['csvFile']:
        myfile = request.FILES['csvFile']
        fs = FileSystemStorage(location=folder) #defaults to   MEDIA_ROOT
        nam = myfile.name
        t = nam.find('.')
        if(nam[t+1:] == 'csv'):
            filename = fs.save(myfile.name, myfile)
            file_url = fs.url(filename)
            msg = 'uploaded'
            return render(request, 'index.html', {'file_url': file_url,'msg':msg})
        else:
            msg = 'Only csv file supported'
            return render(request, 'index.html', {'msg':msg})
    elif request.method == 'GET':
        path = "G:/SEMESTER_6/covidForcastingProject/covid19Prediction/my_folder"
        dir_list = os.listdir(path)
        return render(request, 'index.html',{'all_files':dir_list})
    else:
         return render(request, 'index.html')



def datatable(request, fileCSV):
    path = "G:/SEMESTER_6/covidForcastingProject/covid19Prediction/my_folder"
    data = pd.read_csv(path+'/'+fileCSV,encoding='latin-1', on_bad_lines='skip')#on_bad_lines='skip'    sep='delimiter'
    if(len(data) >= 100):
        first50 = data.head(50)
        last50 = data.tail(50)
        data1_html = first50.to_html()
        data2_html = last50.to_html()
        context = {'loaded_data1': data1_html,'loaded_data2':data2_html}
        return render(request, 'files.html', context)
    else:
        data1_html = data.to_html()
        context = {'loaded_data': data1_html}
        return render(request, 'files.html', context)
 

