from django.shortcuts import render
from django.http import HttpResponse
from service.models import Service
from news.models import News
def homePage(request):
    serviceData=Service.objects.all()
    print(Service)
    data={
        'title': 'Home Page',
        'bdata' : 'Welcome to Wscubetech',
        'clist' :  ['PHP','Java','Django'],
        'numbers' : [10,20,30,40,50],
        'student_details':[
            {'name':'pradeep','phone':9269698122},
            {'name': 'pradeep','phone':9269698122},

        ]
    }   
    return render(request,"index.html",{"data":data})

def aboutUs(request):
    #try:
        print(request.method)
        if request.method=='POST':
            n1=request.POST['num1']
            n2=request.POST['num2']
            result= int(n1)+int(n2)

            return render(request,"about_us.html",{"result":result})
        else:
            result=''
            return render(request,"about_us.html",{"result":result})   
    
def shownews(request):
   news_titles = list(News.objects.values_list('news_title', flat=True))
   news_titles= news_titles[0] if news_titles else "No titles available"

    #NewsData = News.objects.all()
    #for news in NewsData:
    #    title= news.news_title
    #return HttpResponse(title)
    
    
   return render(request,"newsDeatils.html",{'title':news_titles})       
   

def course(request):
    return HttpResponse("Welcome to mycourse")
def courseDetails(request,courseid):
    return HttpResponse(courseid)

def about(request):
    return render(request,'about.html')
def calculator(request):
    print(request.method)
    result=''
    if request.method=='POST':
           
        n1 = int(request.POST.get('num1'))  
        n2 = int(request.POST.get('num2'))  
        opr = request.POST.get('opr')    


        if opr == '+':
            result = n1 + n2
        elif opr == '-':
            result = n1 - n2
        elif opr == '*':
            result = n1 * n2
        elif opr == '/':
            if n2 != 0:
                result = n1 / n2
            else:
                result = 'Division by zero is not allowed'
        else:
            result = 'Invalid operator'

    print(result)

           
    return render(request, "calculator.html", {'result': result})