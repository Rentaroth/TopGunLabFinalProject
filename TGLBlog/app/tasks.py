from celery import shared_task
from django.core.mail import send_mail

@shared_task
def confirm_mail(to, message):
  try:
    send_mail(
      'User creation',
      message,
      'antonio_tabares_enterprise@outlook.com',
      [to]
    )
  except Exception as err:
    print(err)
  return 'Done!'
