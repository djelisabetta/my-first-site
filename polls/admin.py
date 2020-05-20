from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    # in questo modo gli Choice oggetti vengono modificati nella Question pagina di amministrazione.
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    # es. 1 dati visualizzati singolarmente su ogni riga
    # fieldsets = [
    #     ('Informazioni generali', {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]
    # es. 2 dati visualizzati il lista
    # l'intestazione di colonna per was_published_recentlyè, per impostazione predefinita,
    # il nome del metodo (con i trattini bassi sostituiti con spazi) e che ogni riga contiene la rappresentazione in formato stringa dell'output.
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
