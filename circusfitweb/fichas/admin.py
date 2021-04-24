from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Modalidade
from .models import Nivel
from .models import Bloco
from .models import Movimento

class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ['modalidade_nome', 'modalidade_pub_date']
    search_fields = ['modalidade_nome']


class NivelAdmin(admin.ModelAdmin):
    list_display = ['nivel_nome', 'modalidade','nivel_pub_date']
    search_fields = ['nivel_nome']

class BlocoAdmin(admin.ModelAdmin):
    list_display = ['bloco_nome', 'nivel']
    search_fields = ['bloco_nome']

class MovimentoAdmin(admin.ModelAdmin):
    list_display = ['movimento_nome', 'bloco','movimento_dificuldade']
    search_fields = ['movimento_nome']


admin.site.register(Modalidade, ModalidadeAdmin)
admin.site.register(Nivel,NivelAdmin)
admin.site.register(Bloco, BlocoAdmin)
admin.site.register(Movimento,MovimentoAdmin)