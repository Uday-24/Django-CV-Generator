from django.shortcuts import render, redirect
from .froms import ProfileForm
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.
def accept(request):

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accept')

    return render(request, 'pdf/accept.html')

def resume(request, id):
    profile = Profile.objects.get(id = id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'profile' : profile})
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf') 
    response['Content-Disposition'] = 'attachment'

    return response

def list(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/list.html', {'profiles':profiles})