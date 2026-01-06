from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    def __str__(self):
        return self.user.first_name

class Product(models.Model):
    CAT_CHOICES = (
        ('Fashion', 'Fashion'),
        ('Bags and Travel', 'Bags and Travel'),
        ('Medicine', 'Medicine'),
        ('Mobiles', 'Mobiles'),
        ('Books', 'Books'),
        ('Food', 'Food'),
        ('Watch','Watch'),
        ('Groceries','Groceries'),
        ('Furniture & Décor','Furniture & Décor'),
        ('Woman Dress','Woman Dress'),
        ('Kitchen Utensils','Kitchen Utensils'),
        ('Electronics','Electronics'),
        ('Tour','Tour'),
        
    )
    name = models.CharField(max_length=40)
    product_image = models.ImageField(upload_to='product_image/', null=True, blank=True)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=40)
    category = models.CharField(max_length=50, choices=CAT_CHOICES, default='Fashion')
    
    def __str__(self):
        return self.name
    
class Feedback(models.Model):
    name = models.CharField(max_length=40)
    # Added email to match contact form fields
    email = models.EmailField(max_length=50, null=True, blank=True) 
    feedback = models.CharField(max_length=500) # This stores the 'Message'
    date = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name

class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('On the Way','On the Way'), 
        ('Delivered','Delivered'),
    )
    
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)

class CabinBooking(models.Model):
    STATUS = (('Pending','Pending'), ('Confirmed','Confirmed'), ('Cancelled','Cancelled'))
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    source = models.CharField(max_length=100, null=True)
    destination = models.CharField(max_length=100, null=True)
    cabin_type = models.CharField(max_length=100)
    booking_date = models.DateField()
    cabin_no = models.CharField(max_length=20, null=True, blank=True)
    assigned_price = models.PositiveIntegerField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Pending', choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)