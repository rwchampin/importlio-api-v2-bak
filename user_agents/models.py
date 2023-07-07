from django.db import models

# Create your models here.
class UserAgent(Base):
    name = models.CharField(max_length=555, unique=True)
    user_agent = models.CharField(max_length=555, unique=True)
    user_agent_hash = models.CharField(max_length=64, unique=True)
    browser = models.CharField(max_length=30) 
    browser_version = models.CharField(max_length=30)
    os = models.CharField(max_length=30)
    os_version = models.CharField(max_length=30)
    device = models.CharField(max_length=30)
    device_brand = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name