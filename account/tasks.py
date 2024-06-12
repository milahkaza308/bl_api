from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from celery import shared_task

@shared_task
def send_activation_code(email, actication_code):
    context = {
        'text_detail': 'Спасибо за регистрацию!',
        'email':email,
        'domin':'http://localhost:8000',
        'activation_code':actication_code
    }
    msg_html = render_to_string('email.html', context)
    message = strip_tags(msg_html)
    send_mail(
        'Account Activation',
        message,
        'admin@admin.com',
        [email],
        html_message=msg_html,
        fail_silently=False
    )
