from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from funcionarios.models import Funcionario


@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid='criar_funcionario')
def criar_funcionario(sender, instance, **kwargs):

    if not hasattr(instance, 'funcionario'):
        Funcionario.objects.create(user=instance)
