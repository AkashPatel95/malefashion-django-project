from django.db import models

# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=50)
	lname=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	mobile=models.PositiveIntegerField()
	adress=models.TextField()
	password=models.CharField(max_length=50)
	profile_pic=models.ImageField(upload_to='profile_pic/',default="")
	usertype=models.CharField(max_length=100,default="buyer")

	def __str__(self):
		return self.fname+" "+self.lname

categories=(

	('Shirt','Shirt'),
	('Pant','Pant'),
	('Shoes','Shoes')

	)

class Product(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product_categories=models.CharField(max_length=60,choices=categories)
	product_name=models.CharField(max_length=100)
	product_brand=models.CharField(max_length=60)
	product_size=models.CharField(max_length=60)
	product_price=models.PositiveIntegerField()
	product_pic=models.ImageField(upload_to='product_pic/')
	product_information=models.TextField()
	product_description=models.TextField()

	def __str__(self):
		return self.user.fname+"-"+self.product_categories+"-"+self.product_brand

class Wishlist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)

	def __str__(self):
		return self.user.fname+"-"+self.product.product_name

class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	product_price=models.PositiveIntegerField()
	product_quantity=models.PositiveIntegerField(default=1)
	total_price=models.PositiveIntegerField()
	payment_status=models.BooleanField(default=False)

	def __str__(self):
		return self.user.fname+"-"+self.product.product_name