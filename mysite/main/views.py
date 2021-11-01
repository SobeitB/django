from django.shortcuts import render

def index(request): 
	news = Dann.objects.all()
	return render(request, 'main/index.html', {'news': news})