from django.shortcuts import render
from contactUs.models import Contact
from contactUs.contact_validation import ContactForm
from contactUs.models import Contact



# Create your views here.
def ContactView(request):
    return render(request, 'contact.html')


def submit_contact_formView(request):
    if request.method == 'POST':
        form_result = ContactForm(request.POST)

        if form_result.is_valid():
            # fetch data from form since it is valid
            user_name = form_result.cleaned_data['fullname']
            user_email = form_result.cleaned_data['email']
            user_phone = form_result.cleaned_data['phone']
            message_subject = form_result.cleaned_data['subject']
            user_message = form_result.cleaned_data['message']

            new_message = Contact(name = user_name, email=user_email,phoneNumber=user_phone,subject=message_subject, message=user_message)

            # submit data
            new_message.save()
            return render(request, 'home.html')

        else:
            print("data is invalid")
            return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')

# views.py
def view_contact_report(request):
    # Fetch contact data from the database
    contacts = Contact.objects.all()

    # Pass contact data to the template context
    context = {
        'contacts': contacts
    }

    # Render the contact report template
    return render(request, 'contactReport.html', context)