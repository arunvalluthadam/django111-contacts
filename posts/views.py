from posts.forms import ContactForm
from django.shortcuts import render
from posts.models import Contacts
from django.http import HttpResponse,  HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def manage_contacts(request):
    
    if request.method == 'POST':
        formset = ContactForm(request.POST, request.FILES)
        if formset.is_valid():
          link = formset.save(commit=False)
          link.user = request.user
          link.save()
         
    else:
        formset = ContactForm()
        
    return render(request, 'contacts.html', {'formset': formset})


@login_required
def edit_contacts(request, person_pk):
 
        
    instance = get_object_or_404(Contacts, pk=person_pk)
    formset = ContactForm(request.POST or None, request.FILES or None, instance=instance)
    if formset.is_valid():
        instance = formset.save(commit=False)
        instance.save()
      
        return HttpResponseRedirect('/')

    return render(request, 'contacts.html', {'formset': formset})

@login_required
def delete(request, person_pk):
    query = Contacts.objects.get(pk=person_pk)
    query.delete()
    return  HttpResponseRedirect('/')
@login_required
def list_contacts(request):
     
 contact_list = Contacts.objects.all()
  

 return render(request, 'contacts.html', {'contact_list' : contact_list })    		

def search_view(request):

    if request.POST:
        search_text = request.POST['search_text']
    else:
        search_text = ''
    contacts = Contacts.objects.filter(first_name__contains=search_text)
    return render(request, 'ajax_search.html', {'contacts': contacts})

