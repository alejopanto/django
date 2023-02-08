#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime

posts = [
    {
        'name': 'Moct Blac',
        'user': 'Jessica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'name': 'Via Lactea',
        'user': 'C, vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903'
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Fulanito de tal',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076'
    }
]

def list_posts(request):
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><strong>{user}</strong></p>
            <figure><img src="{picture}"></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))