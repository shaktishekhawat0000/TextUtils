from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def analyze(request):
    
    djtext = request.POST.get('text', 'default')
    
    
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newLineRemover = request.POST.get('newLineRemover', 'off')
    extraSpeaceRemover = request.POST.get('extraSpeaceRemover', 'off')
    charCounter = request.POST.get('charCounter', 'off')

    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char

        params = {'purpose' : 'Removed Punctuations' , 'analyzed_text' : analyzed}
            
        djtext = analyzed
    
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()

        params = {'purpose' : 'Changed to Upper case' , 'analyzed_text' : analyzed}

        djtext = analyzed
            
        
    
    if(newLineRemover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!= "\r":
                analyzed += char

        params = {'purpose' : 'New Line Removed' , 'analyzed_text' : analyzed}
            
        djtext = analyzed    


    if(extraSpeaceRemover == "on"):
        analyzed = ""
        for i,char in enumerate(djtext):
            if not (djtext[i] == " " and (djtext[i+1]) == " "):
                analyzed += char

        params = {'purpose' : 'Extra Space Removed' , 'analyzed_text' : analyzed}
            
        djtext = analyzed
    
    if(charCounter == "on"):
        analyze = 0
        for char in djtext:
            if char != " ":
                analyze = analyze + 1

        params = {'purpose' : 'Number of Characters' , 'analyzed_text' : analyze}
            
        djtext = analyzed
    
    if(removepunc != "on" and fullcaps != "on" and newLineRemover != "on" and extraSpeaceRemover != "on" and charCounter != "on" ):
        return HttpResponse("Please select an Operation and Try Again!!!")
    
    return render(request, 'analyze.html', params)


