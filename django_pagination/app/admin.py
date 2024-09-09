from django.contrib import admin
from .models import Book




# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'price')
    
class BbAdmin (admin.ModelAdmin) :
    list_display = ('title', 'author', 'price')
    actions = ('discount', 'title_change')
    def discount(self, request, queryset):
        for rec in queryset:
            rec.price = rec.price / 2
            rec.save ()
        self.message_user(request, 'Действие выполнено') 
    def title_change(self, request, queryset):
        for rec in queryset:
            rec.title = rec.title + ' Change'
            rec.save ()
        self.message_user(request, 'Действие выполнено') 

    

admin.site.register(Book,BbAdmin)