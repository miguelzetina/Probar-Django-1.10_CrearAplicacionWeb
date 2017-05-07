from django.contrib import admin

# Register your models here.
from .models import Registrado
from .forms import RegModelForm


class AdminRegistrado(admin.ModelAdmin):
    form = RegModelForm
    list_display = ["email", "nombre", "timestamp"]
    list_display_links = ["email"]
    list_filter = ["timestamp"]
    list_editable = ["nombre"]
    search_fields = ["nombre", "email"]

    # class Meta:
    #     model = Registrado


admin.site.register(Registrado, AdminRegistrado)
