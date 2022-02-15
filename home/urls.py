from django.db import router
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import *


router=DefaultRouter()
router.register('medviewset', MedicineViewset, basename='medicine')
router.register('comviewset', CompanyViewset, basename='company')
router.register('comviewset', CompanyViewset, basename='company')
router.register('custviewset', CustomerViewset, basename='customer')
router.register('emploviewset', EmployeeViewset, basename='employee')
router.register('emplosalviewset', EmployeeSalViewset, basename='employeesal')
router.register('billviewset', BillViewset, basename='billv')
router.register('homeview', Homeviewset, basename='homeview')






urlpatterns = [
    #path('', views.apiOverview, name="apiOverview"),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    

    
]+router.urls


