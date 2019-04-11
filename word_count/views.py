from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, "start.html")

def next(request):
    ftxt=request.GET['fulltext']

    '''Count the no of characters'''

    ar =list()
    ar=ftxt.split()

    '''Counting the frequency of each entered word.'''

    wordlist={}
    for each in ar:
        if wordlist.__contains__(each):
            wordlist[each]+=1
        else:
            wordlist[each]=1

    arr=sorted(wordlist.items(),key=lambda x:x[1],reverse=True)

    return render(request,"home.html",{'text':ftxt,'no':len(ar),'lst':arr})

def about (request):
    return render(request,'about.html')
