from .models import FooterSettings

def footer_settings(request):
    settings = FooterSettings.objects.first()
    return {'footer_settings': settings}

