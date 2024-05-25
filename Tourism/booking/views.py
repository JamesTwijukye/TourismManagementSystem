from django.shortcuts import render
from trips.models import Trip, LinkedImage
from trips.models import Trip

from django.contrib import messages
from booking.booknow_validation import BookNowForm

# Create your views here.
trip_id_clicked = ""


def BookingView(request):
    global trip_id_clicked

    image_id_Clicked = request.GET["id"]

    trip_id_clicked = image_id_Clicked

    image_photo = Trip.objects.get(trip_id=image_id_Clicked)

    linked_images = LinkedImage.objects.filter(image_id=image_id_Clicked)

    return render(
        request,"booking.html", {"trip_photo": image_photo, "linked_images": linked_images},
    )


def BookNowView(request):
    global trip_id_clicked

    if request.method == "GET":

        form_result = BookNowForm(request.GET)
        if form_result.is_valid():

            hotel_price = form_result.cleaned_data["hotel_price"]
            number_of_rooms = form_result.cleaned_data["number_of_rooms"]
            number_of_adults = form_result.cleaned_data["number_of_adults"]
            number_of_children = form_result.cleaned_data["number_of_children"]

            personal_name = form_result.cleaned_data["personal_name"]
            personal_mobile = form_result.cleaned_data["personal_mobile"]
            personal_nin = form_result.cleaned_data["personal_nin"]

            total = number_of_rooms * hotel_price

            context = {
                "total": total,
                "number_of_rooms": number_of_rooms,
                "hotel_id": trip_id_clicked,

                "number_of_adults": number_of_adults,
                "number_of_children": number_of_children,
                "personal_name": personal_name,
                "personal_mobile": personal_mobile,
                "personal_nin": personal_nin,
            }

            return render(request, "pay.html",context)

        else:

            messages.error(request, "Invalid data, please check again !")

            image_photo = Trip.objects.get(trip_id=trip_id_clicked)

            linked_images = LinkedImage.objects.filter(image_id=trip_id_clicked)
            return render(
                request,
                "booking.html",
                {"trip_photo": image_photo, "linked_images": linked_images},
            )

    else:
        messages.error(request, "Something went wrong !, please try again")
        trip_items = Trip.objects.all()
        return render(request, "trips.html", {"trips": trip_items})
