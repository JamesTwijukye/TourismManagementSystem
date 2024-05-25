
from django.contrib import admin
from django.urls import path, include
from home import home_urls
from pay import pay_urls
from trips import trips_urls
from aboutUs import why_urls,when_urls,before_urls
from contactUs import contactUs_urls
from loginA import login_urls,signup_urls
from booking import booking_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(home_urls)),
    
    path('pay/',include(pay_urls)),
    path('trips/',include(trips_urls)),
    path('aboutus/why',include(why_urls)),
    path('aboutus/when',include(when_urls)),
    path('aboutus/before',include(before_urls)),
    path('contactus/',include(contactUs_urls)),
    path('login/',include(login_urls)),
    path('signup/',include(signup_urls)),
    path('booking/',include(booking_urls)),
    


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)