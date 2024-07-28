from django.utils.deprecation import MiddlewareMixin
from django.template.loader import render_to_string
from datetime import datetime

class FooterMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if 'text/html' in response.get('Content-Type', ''):
            footer_html = render_to_string('footer.html', {'year': datetime.now().year})
            content = response.content.decode('utf-8')
            response.content = content.replace('</body>', f'{footer_html}</body>')
            response['Content-Length'] = len(response.content)
        return response
