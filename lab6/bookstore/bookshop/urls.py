from django.urls import path
from bookshop.views import bshop
from bookshop.views import booksinfo
from bookshop.views import contactus
from bookshop.views import aboutus , showbook , deletebook


urlpatterns = [
    path('bshop', bshop, name="bookshopMainPage"),
    path('booksinfo', booksinfo, name="booksinfo"),
    path('contactus', contactus, name="contactus"),
    path('aboutus', aboutus, name="aboutus"),
    path('booksinfo/show/<int:id>', showbook , name="book.show"),
    path('booksinfo/delete/<id>', deletebook , name="book.delete")
]