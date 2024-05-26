from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm
import os

# Create your views here.
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_manager/contact_list.html', {'contacts': contacts})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contact_manager/contact_form.html', {'form': form})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            if 'profile_image' in request.FILES or 'profile_image-clear' in request.POST:
                # Handle the old image deletion
                if contact.profile_image:
                    if os.path.isfile(contact.profile_image.path):
                        os.remove(contact.profile_image.path)
            contact.profile_image = request.FILES.get('profile_image', contact.profile_image)
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_manager/contact_form.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contact_manager/contact_confirm_delete.html', {'contact': contact})
