from api.settings import PROXY_API_URL
import requests
import logging
from .models import Proxy

logger = logging.getLogger(__name__)

def populate_proxies():
    logger.info('Populating proxies...')
    response = requests.get(PROXY_API_URL)
    proxies_data = response.json()

    for proxy_data in proxies_data:
        # Parse the proxy data and create Proxy objects
        proxy = Proxy.objects.create(
            ip_address=proxy_data['ip'],
            port=proxy_data['port'],
            # Set other fields based on the proxy data
        )
