from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import about,Project,Skills,Say

# Create your views here.
def home(request):

    # abt = about.objects.all()
    

    if request.method == 'POST':
        s = Say()
        s.name = request.POST.get("name")
        s.phone = request.POST.get("phone")
        s.email = request.POST.get("email")
        s.message = request.POST.get("message")
        s.save()

        return HttpResponse("<script>alert('Message Sent');window.location=' ';</script>")
    else:
        abt = about()

        pls = Project.objects.all()
        sk = Skills.objects.all()
        return render(request,'index.html',{'a':abt,'pls': pls,'s': sk})
        

    # dest1 = Dest()
    # dest1.name = 'Mumbai'
    
    # template = loader.get_template("index.html")
    # return HttpResponse(template.render(c, request))
  
