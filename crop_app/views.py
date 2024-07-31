from django.shortcuts import render,redirect
from django.urls import reverse
from crop_app.models import DealerRegistration,OtpCode,PesticidesMeasurement,CropPesticides,UserRegistration, UserLogin,AddFeedback,AddPayment,CustomerOrder,AddProduct,AddCategory,OtpCode
import random
import smtplib
from django.core.files.storage import FileSystemStorage
import os
from django.db.models import Avg, Max, Min, Sum
from crop.settings import BASE_DIR
import datetime
from django.db.models import Avg,Max,Min,Sum,Count
from django.contrib import messages #import messages
#from django.shortcuts import render_to_response



def index(request):
    return render(request, 'index.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def dealer_home(request):
    return render(request, 'dealer_home.html')

def user_home(request):
    udict = AddCategory.objects.values('category_name').distinct()
    userdict = AddProduct.objects.all()
    return render(request, 'user_home.html',{'userdict':userdict, 'udict': udict})



def reg(request):
    if request.method == "POST":
        firstname = request.POST.get('t1')
        lastname = request.POST.get('t11')
        pincode = request.POST.get('t3')
      
        city = request.POST.get('t2')
        address = request.POST.get('t22')
        email = request.POST.get('t5')
        contact = request.POST.get('t6')
        password = request.POST.get('t7')

        '''content = "Your Username is"+email+" and password is-"+password
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('jumppaints@gmail.com', 'ictudtafrdudsjaw')
        mail.sendmail('jumppaints@gmail.com', email, content)
        mail.close()'''

        UserRegistration.objects.create(firstname=firstname,lastname=lastname,pincode=pincode,city=city,address=address, email=email, contact=contact)
        UserLogin.objects.create(username=email,password=password,utype='user')
        return redirect('login')
        #return render(request, 'reg.html', {'msg':'Registration has done successfully'})
    return render(request, 'reg.html')


def dealer_reg(request):
    if request.method == "POST":
        firstname = request.POST.get('t1')
        lastname = request.POST.get('t11')
        pincode = request.POST.get('t3')

        city = request.POST.get('t2')
        address = request.POST.get('t22')
        email = request.POST.get('t5')
        contact = request.POST.get('t6')
        password = request.POST.get('t7')

        '''content = "Your Username is"+email+" and password is-"+password
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('jumppaints@gmail.com', 'ictudtafrdudsjaw')
        mail.sendmail('jumppaints@gmail.com', email, content)
        mail.close()'''

        DealerRegistration.objects.create(firstname=firstname, lastname=lastname, pincode=pincode, city=city,
                                        address=address, email=email, contact=contact)
        UserLogin.objects.create(username=email, password=password, utype='dealer')
        return redirect('login')
        #return render(request, 'dealer_reg.html', {'msg': 'Registration has done successfully'})
    return render(request, 'dealer_reg.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('t1')
        password = request.POST.get('t2')
        request.session['username']=username
        ucheck=UserLogin.objects.filter(username=username).count()
        if ucheck>=1:
            udata=UserLogin.objects.get(username=username)
            upass=udata.password
            utype=udata.utype
            order_no=random.randint(1000,9999)
            request.session['order_no']=order_no
            if(upass==password):
                if(utype=="admin"):
                    return render(request,'admin_home.html')
                if (utype == "dealer"):
                    return render(request, 'dealer_home.html')
                if(utype=="user"):
                    userdict = AddProduct.objects.all()
                    udict = AddCategory.objects.values('category_name').distinct()
                    return render(request,'user_home.html',{'userdict':userdict, 'udict': udict})

            else:
                return render(request,'login.html',{'msg':'invalid password'})
        else:
            return render(request,'login.html',{'msg':'invalid username'})
    return render(request, 'login.html')

def catwise_products(request):
    userdict=AddProduct.objects.all()
    return render(request,'catwise_products.html',{'userdict':userdict})



def add_qty(request,pk):
    order_no=request.session['order_no']
    udict=AddCategory.objects.values('category_name').distinct()
    username=request.session['username']
    now=datetime.datetime.now()
    order_date=now.strftime("%Y-%m-%d")
    udata=AddProduct.objects.get(id=pk)
    drug_name=udata.pesticides_name
    uom=udata.uom
    stock=int(udata.stock)
    price=int(udata.price)


    if request.method=="POST":
        qty=int(request.POST.get('t1'))

        if qty>stock:
            #return redirect('catwise_products')
            messages.info(request, "Sorry Insufficient Stock")
            return redirect('catwise_products')

        else:
            total=int(price*qty)
            ono=random.randint(1111,9999)
            ordernum=str(ono)
            rstock=stock-qty
            AddProduct.objects.filter(id=pk).update(stock=rstock)
            CustomerOrder.objects.create(order_no=order_no,cust_id=username,drug_name=drug_name,qty=qty,uom=uom,price=price,total=total,order_date=order_date,order_status='pending',payment_status='pending')
            return render(request,'add_qty.html',{'msg':'Order has been placed successfully','udict':udict})

    return render(request,'add_qty.html',{'udict':udict})



def view_bill(request,oid):
    order_data=CustomerOrder.objects.get(ordernum=oid)
    pname=order_data.paintname
    price=order_data.unitprice
    qty=order_data.qty
    gst=order_data.totalgst
    cgst=order_data.cgst
    sgst=order_data.sgst
    total=order_data.grandtotal
    uid=order_data.custid
    bill_no=order_data.id

    udata=UserRegistration.objects.get(email=uid)
    name=udata.name
    address=udata.address
    now=datetime.datetime.now()
    bdate=now.strftime("%Y-%m-%d")
    return render(request,'view_bill.html',{'pname':pname,'qty':qty,'price':price,'total':total,'name':name,'address':address,'bdate':bdate,'bill_no':bill_no,'gst':gst,'cgst':cgst,'sgst':sgst})







def cname(request):
    if request.method == "POST":
        cname= request.POST.get('t1')
        AddCategory.objects.create(category_name=cname)
        return render(request, 'category.html',{'msg':'Inserted Successfully'})
    return render(request, 'category.html')


def druginfo(request) :
    userdict=AddCategory.objects.values('category_name').distinct()
    if request.method == "POST" and request.FILES['myfile']:
        catg = request.POST.get('t1')
        drug_name = request.POST.get('t2')
        uom = request.POST.get('t3')
        qty = request.POST.get('t4')
        price = request.POST.get('t5')
        expirydate = request.POST.get('t7')
        usage = request.POST.get('t77')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)

        AddProduct.objects.create(category_name=catg,pesticides_name=drug_name, uom=uom, qty=qty,price=price,expiry_date=expirydate,image=myfile,usage=usage)
        return render(request, 'druginfo.html',{'msg':'Inserted Successfully','userdict':userdict})
    return render(request, 'druginfo.html',{'userdict':userdict})




def druginfo_edit(request,pk) :
    userdict=AddProduct.objects.filter(id=pk).values()
    if request.method == "POST":
        company_name = request.POST.get('t1')
        drug_name = request.POST.get('t2')
        uom = request.POST.get('t3')
        qty = request.POST.get('t4')
        price = request.POST.get('t5')
        expiry_date = request.POST.get('t7')
        usage = request.POST.get('t77')
        stock = request.POST.get('t78')
        if (len(request.FILES) != 0):
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            pat = os.path.join(BASE_DIR, '/media/' + filename)
            AddProduct.objects.filter(id=pk).update(stock=stock,category_name=company_name,pesticides_name=drug_name, uom=uom, qty=qty,price=price,expiry_date=expiry_date,image=myfile)
            base_url=reverse('druginfo_view')
            return redirect(base_url)
        else:
            AddProduct.objects.filter(id=pk).update(stock=stock,category_name=company_name,pesticides_name=drug_name, uom=uom, qty=qty,price=price,expiry_date=expiry_date)
            base_url = reverse('druginfo_view')
            return redirect(base_url)
    return render(request, 'druginfo_edit.html',{'userdict':userdict})



def reg_view(request):
    userdict = UserRegistration.objects.all()
    return render(request, 'reg_view.html', {'userdict': userdict})


def reg_view_dealer(request):
    userdict = DealerRegistration.objects.all()
    return render(request, 'reg_view_dealer.html', {'userdict': userdict})

def view_orders(request,pk):
    username=request.session['username']

    total = CustomerOrder.objects.filter(cust_id=username).filter(order_no=pk).aggregate(total=Sum("total"))['total']
    userdict = CustomerOrder.objects.filter(cust_id=username).filter(order_no=pk).values()
    return render(request, 'my_order.html', {'userdict': userdict,'total':total,'u':username,'ono':pk})

def custorder_view(request):
    username=request.session['username']
    udata=CustomerOrder.objects.filter(cust_id=username).values('order_no').distinct()
    return render(request,'custorder_view.html',{'udata':udata})
    '''udict = AddCategory.objects.values('category_name').distinct()
    userdict = CustomerOrder.objects.filter(cust_id=username).values()
    return render(request, 'my_order.html', {'userdict': userdict,'udict':udict})'''

def pay_amount(request,pk,ono):
    print(pk)
    username=request.session['username']
    order_no=request.session['order_no']
    now=datetime.datetime.now()
    pay_date=now.strftime("%Y-%m-%d")
    if request.method=="POST":
        CustomerOrder.objects.filter(order_no=ono).update(payment_status='paid')
        AddPayment.objects.create(order_no=order_no,cust_id=username,payment_date=pay_date,amount=pk)
        return render(request,'payment_notice.html',{'msg':'Payment has been done successfully'})
    return render(request,'online_payment.html',{'amount':pk})


def paymentinfo_view(request):
    username=request.session['username']
    udict = AddCategory.objects.values('category_name').distinct()
    userdict = AddPayment.objects.filter(cust_id=username).values()
    return render(request, 'my_payment.html', {'userdict': userdict,'udict':udict})


def customer_orders(request):
    userdict=CustomerOrder.objects.filter(orderstatus='confirmed').values()
    return render(request,'customer_orders.html',{'userdict':userdict})

def payment_report(request):
    userdict=AddPayment.objects.all()
    total = list(AddPayment.objects.aggregate(Sum('totalamt')).values())[0]
    return render(request,'payment_report.html',{'userdict':userdict,'total':total})




def cname_view(request):
    userdict = AddCategory.objects.all()
    return render(request, 'category_view.html', {'userdict': userdict})

def druginfo_view(request):
    userdict = AddProduct.objects.all()
    return render(request, 'druginfo_view.html', {'userdict': userdict})

def forgotpass(request):
    if request.method=="POST":
        username=request.POST.get('t1')
        request.session['username']=username
        ucheck=UserLogin.objects.filter(username=username).count()
        if ucheck>=1:
            otp = random.randint(1111, 9999)
            OtpCode.objects.create(otp=otp, status='active')
            content = "Your OTP IS-" + str(otp)
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('poojassavadi@gmail.com','qyziqbhydbuxuobb')
            mail.sendmail('poojassavadi@gmail.com',username,content)
            base_url = reverse('otp')
            return redirect(base_url)
        else:
            return render(request,'forgotpass.html',{'msg':'Invalid Username'})
    return render(request,'forgotpass.html')

def otp(request):
    if request.method=="POST":
        otp=request.POST.get('t1')
        ucheck=OtpCode.objects.filter(otp=otp).count()
        if ucheck>=1:
            base_url = reverse('resetpass')
            return redirect(base_url)
        else:
            return render(request,'otp.html',{'msg':'Invalid OTP'})
    return render(request,'otp.html')


def resetpass(request):
    username=request.session['username']
    if request.method=="POST":
        newpass=request.POST.get('t1')
        confirmpass=request.POST.get('t2')
        if newpass==confirmpass:
            UserLogin.objects.filter(username=username).update(password=newpass)
            base_url=reverse('login')
            return redirect(base_url)
        else:
            return render(request,'resetpass.html',{'msg':'New password and confirm password must be same'})
    return render(request,'resetpass.html')

def reg_del(request, pk):
    udata = UserRegistration.objects.get(id=pk)
    udata.delete()
    base_url=reverse('reg_view')
    return redirect(base_url)

def cname_del(request, pk):
    udata = AddCategory.objects.get(id=pk)
    udata.delete()
    base_url=reverse('cname_view')
    return redirect(base_url)

def custorder_del(request, pk):

    udata = CustomerOrder.objects.get(id=pk)
    udata.delete()
    base_url=reverse('custorder_view')
    return redirect(base_url)

def confirm_order(request,pk):
    username=request.session['username']
    CustomerOrder.objects.filter(id=pk).update(order_status='confirmed')
    content = "Thank you for confirm your order"
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('poojassavadi@gmail.com','qyziqbhydbuxuobb')
    mail.sendmail('poojassavadi@gmail.com', username, content)
    mail.close()
    base_url=reverse('custorder_view')
    return redirect(base_url)

def druginfo_del(request, pk):
    udata = AddProduct.objects.get(id=pk)
    udata.delete()
    base_url=reverse('paintinfo_view')
    return redirect(base_url)


def measurement(request):
    if request.method=="POST":
        category = request.POST.get('cat')
        pesticide_name=request.POST.get('t2')
        chemical_composition=request.POST.get('t3')
        Mode_action = request.POST.get('t5')
        active_ingredient = request.POST.get('t6')
        recmdn = request.POST.get('t7')
        against = request.POST.get('t8')
        PesticidesMeasurement.objects.create(category=category,pesticide_name=pesticide_name,chemical_composition=chemical_composition,Mode_action=Mode_action,active_ingredient=active_ingredient,recmdn=recmdn,against=against)
        return render(request,'measurement.html',{'msg':'inserted successfully'})

    return render(request,'measurement.html')

def measurement_view(request):
    userdict=PesticidesMeasurement.objects.all()
    return render(request,'measurement_view.html',{'userdict':userdict})

def search_measurement(request):
    udata=PesticidesMeasurement.objects.all()
    if request.method=="POST":
        search=request.POST.get('cat')
        udata=PesticidesMeasurement.objects.filter(pesticide_name=search).values()
        return render(request, 'search_measurement_view.html',{'udata':udata})
    return render(request,'search_measurement.html',{'udata':udata})


def crop_pesticides(request):
    if request.method=="POST":
        crop_name=request.POST.get('t1')
        pesticide_name = request.POST.get('t2')
        qty = request.POST.get('t3')
        usage = request.POST.get('t4')
        CropPesticides.objects.create(crop_name=crop_name,pesticide_name=pesticide_name,qty=qty,usage=usage)
        return render(request,'crop_pesticides.html',{'msg':'inserted successfully'})
    return render(request,'crop_pesticides.html')

def search_crop_pesticides(request):
    udata=CropPesticides.objects.all()
    if request.method=="POST":
        crop_name = request.POST.get('t1')
        udata=CropPesticides.objects.filter(crop_name=crop_name).values()
        return render(request,'crop_pesticides_view.html',{'udata':udata})
    return render(request,'search_crop_pesticides.html',{'udata':udata})

def crop_pesticides_view_admin(request):
    udata=CropPesticides.objects.all()
    return render(request,'crop_pesticides_view_admin.html',{'udata':udata})

def payment_report(request):
    if request.method=="POST":
        first_date=request.POST.get('t1')
        last_date=request.POST.get('t2')
        total = AddPayment.objects.aggregate(amount=Sum("amount"))['amount']
        udata=AddPayment.objects.filter(payment_date__range=[first_date, last_date])
        return render(request,'payment_report2.html',{'udata':udata,'total':total})
    return render(request,'payment_report.html')
    #Sample.objects.filter(date__year='2011',date__month='01')


def custorder_view_dealer(request):
    udata=CustomerOrder.objects.filter(payment_status='paid').values()
    return render(request,'custorder_view_dealer.html',{'udata':udata})

def custorder_view_a(request):
    udata=CustomerOrder.objects.filter(payment_status='paid').values()
    return render(request,'custorder_view_a.html',{'udata':udata})

def generate_bill(request,pk,email):

    ndata=UserRegistration.objects.get(email=email)
    fname=ndata.firstname
    lname=ndata.lastname
    address=ndata.address
    total = AddPayment.objects.filter(order_no=pk).aggregate(amount=Sum("amount"))['amount']
    userdict=CustomerOrder.objects.filter(order_no=pk).values()
    return render(request,'generate_bill.html',{'total':total,'userdict':userdict,'fname':fname,'lname':lname,'address':address})

def products_view_dealer(request):
    udata=AddProduct.objects.all()
    return render(request,'products_view_dealer.html',{'udata':udata})