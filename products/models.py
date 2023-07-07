from django.db import models
from urllib.parse import urlparse, parse_qs

class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reviews = models.IntegerField()
    ratings = models.IntegerField() 
    availability = models.BooleanField(default=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey('Store', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.product.name + '-image'
    
class ProductUrl(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='urls')
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.product.name + '-url'
    
    def save(self, *args, **kwargs):
        # Parse the URL
        url_components = urlparse(self.url)
        query_params = parse_qs(url_components.query)

        # Check for 'tag' in the query parameters
        if 'tag' in query_params:
            # Remove the 'tag' parameter and its value from the query parameters
            del query_params['tag']

            # Reconstruct the URL without the 'tag' parameter
            query_string = '&'.join(f"{param}={value}" for param, values in query_params.items() for value in values)
            url_components = url_components._replace(query=query_string)

            # Update the URL field with the modified URL
            self.url = url_components.geturl()

        super().save(*args, **kwargs)
        
        
class Store(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name