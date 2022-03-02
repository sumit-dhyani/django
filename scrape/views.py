from django.http import HttpResponse
from django.shortcuts import render
from scrape_bot.main_page import scrapping

# Create your views here.
def home(request):
    return render(request,'index.html',{'name':'yes'})
def scrape(request):
    url=request.POST['url']
    m=scrapping(url)
    m.sign_in()
    m.emp_overview()
    

    
    return HttpResponse('Scraping is completed')