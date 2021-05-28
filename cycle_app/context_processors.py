from cycle_app.models import Versity_life_cycle
from django.contrib.auth.decorators import login_required


def add_variable_to_context(request):
    user = request.user
    if user.is_anonymous:
        return {
            'testme':''
        }
    else:
        testme=Versity_life_cycle.objects.filter(user=user)
        return {
            'testme': testme,
        }