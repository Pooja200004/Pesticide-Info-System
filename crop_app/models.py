from django.db import models

class UserLogin(models.Model):
    username=models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=50)

class UserRegistration(models.Model):
    firstname=models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=50)


class DealerRegistration(models.Model):
    firstname=models.CharField(max_length=50,null=True,blank=True)
    lastname = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    pincode = models.CharField(max_length=6,null=True,blank=True)
    contact = models.CharField(max_length=10,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)

class AddCategory(models.Model):
    category_name=models.CharField(max_length=50)


class AddProduct(models.Model):
    category_name=models.CharField(max_length=50,null=True,blank=True)
    pesticides_name = models.CharField(max_length=50,null=True,blank=True)
    qty = models.IntegerField(null=True,blank=True)
    uom = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    usage = models.CharField(max_length=1000,null=True,blank=True)
    image = models.CharField(max_length=500,null=True,blank=True)
    expiry_date = models.DateField(null=True,blank=True)
    stock = models.IntegerField(null=True,blank=True)


class CustomerOrder(models.Model):
    order_no = models.IntegerField(null=True,blank=True)
    cust_id=models.CharField(max_length=50,null=True,blank=True)
    drug_name = models.CharField(max_length=50,null=True,blank=True)
    qty = models.IntegerField(null=True,blank=True)
    uom = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    total = models.IntegerField(null=True,blank=True)
    order_date = models.DateField(null=True,blank=True)
    order_status = models.CharField(max_length=50,null=True,blank=True)
    payment_status = models.CharField(max_length=50,null=True,blank=True)

class AddPayment(models.Model):
    order_no=models.CharField(max_length=50)
    cust_id = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    payment_date = models.DateField()

class AddFeedback(models.Model):
    cust_id=models.CharField(max_length=50)
    about_product = models.CharField(max_length=50)
    comments = models.CharField(max_length=50)

class OtpCode(models.Model):
    otp=models.IntegerField()
    status=models.CharField(max_length=20)

class CropPesticides(models.Model):
    crop_name=models.CharField(max_length=200, null=True, blank=True)
    pesticide_name=models.CharField(max_length=200, null=True, blank=True)
    qty = models.CharField(max_length=20, null=True, blank=True)
    usage = models.CharField(max_length=2000, null=True, blank=True)

class PesticidesMeasurement(models.Model):
    category = models.CharField(max_length=200, null=True, blank=True)
    pesticide_name=models.CharField(max_length=200,null=True,blank=True)
    chemical_composition=models.CharField(max_length=200,null=True,blank=True)
    Mode_action = models.CharField(max_length=20,null=True,blank=True)
    active_ingredient = models.CharField(max_length=200,null=True,blank=True)
    recmdn = models.CharField(max_length=2000,null=True,blank=True)
    against = models.CharField(max_length=2000,null=True,blank=True)



class OtpCode(models.Model):
    otp=models.CharField(max_length=50,null=True,blank=True)
    status = models.CharField(max_length=50,null=True,blank=True)




    