from django.shortcuts import render
import requests
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Proxy
from .serializers import ProxySerializer
from api.settings import PROXY_API_URL

class ProxyViewSet(viewsets.ModelViewSet):
    queryset = Proxy.objects.all()
    serializer_class = ProxySerializer
    
    PROTOCOLS = Proxy.PROTOCOLS

    @action(detail=False, methods=['get'])
    def get_random_proxy(self, request):
        proxy = Proxy.objects.filter(is_active=True).order_by('?').first()
        serializer = self.get_serializer(proxy)
        return Response(serializer.data)

    @staticmethod
    def validate_proxy(proxy):
        valid_protocol = None
        for protocol in ProxyViewSet.PROTOCOLS:
            try:
                response = requests.get(f"{protocol}://{proxy.ip}:{proxy.port}", timeout=5)
                if response.status_code == 200:
                    valid_protocol = protocol
                    break
            except requests.exceptions.RequestException:
                pass

        if valid_protocol:
            proxy.protocol = valid_protocol
            proxy.save()
            return True
        else:
            proxy.delete()  # Remove the proxy from the database
            return False


    @staticmethod
    def mark_proxy_used(proxy):
        proxy.is_active = False
        proxy.save()

    @action(detail=True, methods=['post'])
    def delete_proxy(self, request, pk=None):
        proxy = self.get_object()
        proxy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['post'])
    def populate_proxies(self, request):
        response = requests.get(PROXY_API_URL)
        if response.status_code == 200:
            data = response.json()
            proxies = [self.parse_proxy_data(item) for item in data]
            Proxy.objects.bulk_create(proxies)
            return Response({'message': 'Proxy table populated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Failed to populate proxy table'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def parse_proxy_data(data):
        return Proxy(
            ip_address=data.get('ip'),
            asn=data.get('asn'),
            city=data.get('city'),
            region=data.get('region'),
            port=data.get('port'),
            protocol=data.get('protocols')[0] if data.get('protocols') else '',
            isp=data.get('isp'),
            google=data.get('google', False),
            last_checked=data.get('lastChecked'),
            org=data.get('org'),
            latency=data.get('latency'),
            country=data.get('country'),
            is_active=True
        )
