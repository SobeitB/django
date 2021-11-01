from django.shortcuts import render, redirect
from .models import Dann
from .forms import DannForm

def news_home(request):
	news = Dann.objects.all()
	return render(request, 'news/news.html', {'news': news})

def create_news(request):
	error = ''
	if request.method == 'POST' and request.is_ajax():
		form = DannForm(request.POST)
		if form.is_valid():
			form.save()
			# return redirect('news_home')
		else:
			error = 'Форма была неверна заполнена'

	form = DannForm()
	data = {
		'form': form,
		'error': error,
		'massage': Dann.objects.all()
	}

	return render(request, 'news/create_news.html', data)