from django.shortcuts import render


def index(request):
    return render(request, 'personal\home.html')



def contact(request):
    return render(request, 'personal/basic.html',{'content':['if u would like to contact me ', 'tohidulalam216@gmail.com' ]})
