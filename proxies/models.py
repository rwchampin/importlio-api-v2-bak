from django.db import models
from django.db import connection

class Proxy(models.Model):
    PROTOCOLS = (
        ('HTTP', 'HTTP'),
        ('HTTPS', 'HTTPS'),
    )

    ip_address = models.GenericIPAddressField()
    asn = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    port = models.PositiveIntegerField()
    protocol = models.CharField(max_length=10, choices=PROTOCOLS)
    isp = models.CharField(max_length=100)
    google = models.BooleanField(default=False)
    last_checked = models.DateTimeField()
    org = models.CharField(max_length=100)
    latency = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    times_used = models.PositiveIntegerField(default=0)
    # Additional fields that you may find useful
    connection_time = models.PositiveIntegerField(default=0)
    speed = models.PositiveIntegerField(default=0)
    response_time = models.PositiveIntegerField(default=0)
    anonymity_level = models.CharField(max_length=100, blank=True)
    usage_count = models.PositiveIntegerField(default=0)
    failure_count = models.PositiveIntegerField(default=0)
    last_used_at = models.DateTimeField(null=True, blank=True)
    up_time = models.PositiveIntegerField(default=0)
    up_time_success_count = models.PositiveIntegerField(default=0)
    up_time_try_count = models.PositiveIntegerField(default=0)
    working_percent = models.PositiveIntegerField(default=0)
    # Additional methods or functionality can be added here
            
    def __str__(self):
        return f'{self.ip_address}:{self.port}'
