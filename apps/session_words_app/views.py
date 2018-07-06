# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
#imports datetime module to be used. 
from datetime import datetime


def index(request):
	#checks to see if there is anything in var list, which is a class variable in the html template.
	if request.session.get('list') == None:
		#if nothing sets it equal to an empty list to be filled, for words to be looped through. 
		request.session['list'] = []
	return render(request, 'session_words_app/index.html')

def word_process(request):
	#sets POST variables to variables 
	word = request.POST['word']
	color = request.POST['color']

	#checks to see if font was checked in template using the name variable in HTML template. 
	#which can then be used in css to style. 
	#this is an if statement because it is optional on the form. 
	if 'font' in request.POST:
		font = "big_font"
	else:
		font = "reg_font"

	#sets a variable time to present time in this format. 
	time = datetime.strftime(datetime.now(), "%H:%M:%S %p, %B %d, %Y")
	#appends this dictionary to the var list, which represents a <div> in our index.html template.
	#because <request.session> is a dictionary, so you can attach key/value pairs
	request.session['list'].append({'word': word, 'color': color, 'font': font, 'time': time})
	return redirect("/")

def clear(request):
	#deletes session list and returns back to homepage. 
	request.session.clear()
	return redirect("/")
