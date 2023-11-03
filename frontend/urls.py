from django.urls import path
from frontend import views

urlpatterns=[

    path('homepage/',views.homepage,name="homepage"),
    path('pro_page/',views.pro_page,name="pro_page"),
    path('filter_pro/<filtid>/',views.filter_pro,name="filter_pro"),
    path('single_pro/<int:prod_id>/',views.single_pro,name="single_pro"),
    path('single_pro/<int:prod_id>/',views.single_pro,name="single_pro"),
    path('about_page/',views.about_page,name="about_page"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('savecontact/',views.savecontact,name="savecontact"),
    path('register_user/',views.register_user,name="register_user"),
    path('saveregister/',views.saveregister,name="saveregister"),
    path('user_login/',views.user_login,name="user_login"),
    path('log_out/',views.log_out,name="log_out"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('cartsave/',views.cartsave,name="cartsave"),

]