from django.shortcuts import render
from .models import Contact

def Index(request):
    if (request.method=='POST'):
        Name=request.POST.get('Name')
        Email=request.POST.get("Email")
        Number=request.POST.get("Number")
        Subject=request.POST.get("Subject")
        Message=request.POST.get("Message")

        FullInfo=Contact(None,Name,Email,Number,Subject,Message)
        FullInfo.save()
    else:
        print("error")

    return render(request,'index.html')
