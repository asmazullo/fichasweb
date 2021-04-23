from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Modalidade
from .models import Nivel
from .models import Bloco
from .models import Movimento

admin.site.register(Modalidade)
admin.site.register(Nivel)
admin.site.register(Bloco)
admin.site.register(Movimento)