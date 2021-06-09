from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = "home"),
    
    path('products',views.products,name = "products"),
    
    path('postadd',views.postadd,name = "postadd"),
    
    path('showdetails/<int:id>',views.showdetails,name = "showdetails"),
    
    path('profile',views.profile,name="profile"),
    
    path('login',views.login,name="login"),
    
    path('register',views.register,name="register"),
    
    path('logout',views.logout,name="logout"),
    
    path('managead',views.managead,name="managead"),
    
    path('profilesetup',views.profilesetup,name="profilesetup"),
    
    path('deletead/<int:id>',views.deletead,name="deletead"),
    
    path('updatead/<int:id>',views.updatead,name="updatead"),
    
    path('products/cat/<int:id>',views.products_cat,name="products_cat"),
    
]
