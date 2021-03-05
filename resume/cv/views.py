from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import about,Project,Skills,Say,Resume

# Create your views here.
def home(request):

    # abt = about.objects.all()
    

    if request.method == 'POST':
        s = Say()
        s.name = request.POST.get("name")
        s.subject = request.POST.get("subject")
        s.email = request.POST.get("email")
        s.message = request.POST.get("message")
        s.save()

        return HttpResponse("<script>alert('Message Sent');window.location=' ';</script>")
    else:
        abt = about.objects.all()
        rsume = Resume.objects.all()

        pls = Project.objects.all()
        sk = Skills.objects.all()
        return render(request,'index.html',{'a':abt,'pls': pls,'s': sk,'r': rsume})
        

    # dest1 = Dest()
    # dest1.name = 'Mumbai'
    
    # template = loader.get_template("index.html")
    # return HttpResponse(template.render(c, request))
# def pdf_view(request, data):
#     # c = pdf.HTMLToPDFConverter()
#     # context = {} # something
#     # html = get_template(template).render(context)
#     # data = c.convert(html)
#     response = HttpResponse(data, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=something.pdf'
#     return response
