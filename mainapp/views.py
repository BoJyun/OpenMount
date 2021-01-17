from django.shortcuts import render
from mount.models import Mount
from datetime import datetime,timedelta
# Create your views here.

def get_index(request):
    title="OpenMount"
    mounts=Mount.objects.all()
    resopnse=render(request,'index.html',locals())
    resopnse.set_cookie(key='name',value='hahahaha',expires=datetime.now()+timedelta(days=30))# 存30天
    #return render(request,'index.html',locals())

    request.session['age']=25
    return resopnse

def signup(request):
    print(request.session['age'])
    return render(request,'signup.html')