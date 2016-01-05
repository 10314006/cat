from django.shortcuts import render
import datetime
# Create your views here.
def main(request):
        now = datetime.datetime.now()
        context = {'like':'是不是覺得貓咪很可愛呢？','now':now}
        return render(request, 'main/main.html', context)

def about(request):
    return render(request, 'main/about.html')   