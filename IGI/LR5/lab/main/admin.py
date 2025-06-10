from django.contrib import admin
from .models import News, Reviews, Animal, Staf, Sales, Vacationss, QaA


@admin.register(Staf)
class StafAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'birth_date', 'animal')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')


admin.site.register(News)
admin.site.register(Reviews)
admin.site.register(Animal)
admin.site.register(Sales)
admin.site.register(Vacationss)
admin.site.register(QaA)