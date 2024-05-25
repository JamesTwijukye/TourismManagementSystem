from django.shortcuts import render

from pay.models import Payment
from pay.submit_pay_validation import PayForm

from booking.models import Booking
from trips.models import Trip, LinkedImage

from django.contrib import messages

trip_id_clicked = "not set yet"

# Create your views here.
def PayView(request):
    return render(request, 'pay.html')


# here the payview created
def submit_pay_formView(request):
    global trip_id_clicked
    # if the method in the payform is post then the method acts on the payform and stores result in payformresult
    if request.method == 'POST':
        payformresult = PayForm(request.POST)

        # if the payform result is valid,store the form details in userservices,usertotal and user cardholder

        if payformresult.is_valid():

            userservices = payformresult.cleaned_data['services']
            usertotal = payformresult.cleaned_data['price']
            usercardholder = payformresult.cleaned_data['cardholder']

            # these are new payment details all stored in newdetails and then save them and of not then take us o the home page

            newDetails = Payment(services = userservices,price = usertotal,cardholder = usercardholder)

            newDetails.save()

            # Create a new Booking object
            hotel_id = trip_id_clicked
            # Use request.GET to access URL parameters
            personal_name = payformresult.cleaned_data["personal_name"]
            # Use request.GET to access URL parameters
            personal_mobile = payformresult.cleaned_data["personal_mobile"]
            # Use request.GET to access URL parameters
            usertotal = payformresult.cleaned_data["price"]
            # Use request.GET to access URL parameters
            personal_nin = payformresult.cleaned_data["personal_nin"]
            # Use request.GET to access URL parameters
            number_of_adults = payformresult.cleaned_data["number_of_adults"]
            # Use request.GET to access URL parameters
            number_of_children = payformresult.cleaned_data["number_of_children"]
            # Use request.GET to access URL parameters
            number_of_rooms = payformresult.cleaned_data["services"]

            print(personal_mobile)

            new_booking = Booking(
                hotel_id=hotel_id,
                personal_name=personal_name,
                personal_mobile=personal_mobile,
                total=usertotal,
                personal_nin=personal_nin,
                number_of_adults=number_of_adults,
                number_of_children=number_of_children,
                number_of_rooms=number_of_rooms,
            )
            new_booking.save()
            messages.success(request, "THank you for booking with us, waiting to receive you soon")

            return render(request, "home.html")

        # if not take us to the paypage

        else:


            print(payformresult.errors)
            messages.error(
                request, "Data Invalid"
            )
            return render(request, "pay.html")

    else:

        return render(request, 'pay.html')


def view_html_report(request):
    # Fetch payment data from the database
    payments = Payment.objects.all()

    # Pass payment data to the template context
    context = {
        'payments': payments
    }

    # Render the HTML report template
    return render(request, 'payReport.html', context)
