from django.urls import path
from sapp import views

urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('addcat/',views.addcat,name="addcat"),
    path('savedata/',views.savedata,name="savedata"),
    path('displaydata/',views.displaydata,name="displaydata"),
    path('editdata/<int:sid>/',views.editdata,name="editdata"),
    path('updatedata/<int:sid>/',views.updatedata,name="updatedata"),
    path('deletedata/<int:sid>/',views.deletedata,name="deletedata"),
    path('productdata/',views.productdata,name="productdata"),
    path('savepro/',views.savepro,name="savepro"),
    path('displaypro/',views.displaypro,name="displaypro"),
    path('editpro/<int:eid>/',views.editpro,name="editpro"),
    path('updatecat/<int:eid>/',views.updatecat,name="updatecat"),
    path('deletepro/<int:eid>/',views.deletepro,name="deletepro"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('logout/',views.logout,name="logout"),
    path('contact_display/',views.contact_dispaly,name="contact_display"),
    path('delete_user/<int:uid>/',views.delete_user,name="delete_user"),
]