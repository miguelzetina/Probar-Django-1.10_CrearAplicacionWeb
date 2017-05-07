from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegForm, RegModelForm, ContactForm
from .models import Registrado


def inicio(request):
    titulo = "HOLA"
    if request.user.is_authenticated():
        titulo = "Bienvenido %s" % (request.user)
    el_form = RegModelForm(request.POST or None)
    # print(dir(form))

    context = {
        "el_titulo": titulo,
        "el_form": el_form,
    }

    if el_form.is_valid():
        instance = el_form.save(commit=False)
        nombre = el_form.cleaned_data.get("nombre")
        email = el_form.cleaned_data.get("email")
        if not instance.nombre:
            instance.nombre = "USUARIO"
        instance.save()

        context = {
            "titulo": "Gracias %s!" % (nombre)
        }

        if not nombre:
            context = {
                "titulo": "Gracias %s!" % (email)
            }

        print(instance)
        print(instance.timestamp)
        # form_data = form.cleaned_data
        # abc = form_data.get("email")
        # abc2 = form_data.get("nombre")
        # obj = Registrado.objects.create(email=abc, nombre=abc2)
    return render(request, "inicio.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
    #    for key, value in form.cleaned_data.iteritems():
    #        print key, value
        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = "Form de contacto"
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "otrormail@gmail.com"]
        email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
        send_mail(asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=False
            )

    context = {
        "form": form
    }
    return render(request, "forms.html", context)
