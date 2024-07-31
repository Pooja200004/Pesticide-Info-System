"""drugs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crop_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('reg', views.reg, name='reg'),
    path('dealer_reg', views.dealer_reg, name='dealer_reg'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('dealer_home', views.dealer_home, name='dealer_home'),
    path('user_home', views.user_home, name='user_home'),
    path('login', views.login, name='login'),
    path('cname', views.cname, name='cname'),
    path('druginfo', views.druginfo, name='druginfo'),
    path('reg_view', views.reg_view, name='reg_view'),
    path('reg_view_dealer', views.reg_view_dealer, name='reg_view_dealer'),

    path('payment_report', views.payment_report, name='payment_report'),

    path('products_view_dealer', views.products_view_dealer, name='products_view_dealer'),


    path('custorder_view', views.custorder_view, name='custorder_view'),
    path('paymentinfo_view', views.paymentinfo_view, name='paymentinfo_view'),

    path('cname_view', views.cname_view, name='cname_view'),
    path('druginfo_view', views.druginfo_view, name='druginfo_view'),
    path('forgotpass',views.forgotpass,name='forgotpass'),
    path('otp',views.otp,name='otp'),
    path('resetpass',views.resetpass,name='resetpass'),
    path('reg_del/<int:pk>', views.reg_del, name='reg_del'),

    #path('tender_edit/<int:pk>', views.tender_edit, name='tender_edit'),

    path('cname_del/<int:pk>', views.cname_del, name='cname_del'),
    path('custorder_del/<int:pk>', views.custorder_del, name='custorder_del'),
    path('druginfo_del/<int:pk>', views.druginfo_del, name='druginfo_del'),
    path('druginfo_edit/<int:pk>', views.druginfo_edit, name='druginfo_edit'),
    path('add_qty/<int:pk>', views.add_qty, name='add_qty'),
    path('pay_amount/<int:pk>/<int:ono>', views.pay_amount, name='pay_amount'),
    path('catwise_products', views.catwise_products, name='catwise_products'),
    path('confirm_order/<int:pk>', views.confirm_order, name='confirm_order'),
    path('view_orders/<int:pk>',views.view_orders,name='view_orders'),
    path('customer_orders', views.customer_orders, name='customer_orders'),
    path('measurement', views.measurement, name='measurement'),
    path('measurement_view', views.measurement_view, name='measurement_view'),
    path('payment_report', views.payment_report, name='payment_report'),
    path('view_bill/<int:oid>', views.view_bill, name='view_bill'),
    path('search_measurement', views.search_measurement, name='search_measurement'),
    path('crop_pesticides', views.crop_pesticides, name='crop_pesticides'),
    path('crop_pesticides_view_admin', views.crop_pesticides_view_admin, name='crop_pesticides_view_admin'),

    path('search_crop_pesticides', views.search_crop_pesticides, name='search_crop_pesticides'),
    path('generate_bill/<int:pk>/<str:email>', views.generate_bill, name='generate_bill'),
    path('custorder_view_dealer', views.custorder_view_dealer, name='custorder_view_dealer'),
    path('search_crop_pesticides', views.search_crop_pesticides, name='search_crop_pesticides'),
    path('custorder_view_a',views.custorder_view_a,name="custorder_view_a"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)