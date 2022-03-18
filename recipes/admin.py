from django.contrib import admin

from .models import Category, Recipe

# Register your models here.




class CategoryAdmin(admin.ModelAdmin):
    ...

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at', 'is_published','preparation_steps',)
    list_editable = ('is_published', 'preparation_steps',)
    list_display_links =  ('title',)
    search_fields = ('id','title','created_at', 'is_published', 'description',
                      'slug', 'preparation_steps',)
    list_filter = ('category', 'author', 'is_published', 'preparation_steps_is_html',)
    list_per_page = 10
    ordering = ('-id',)
    


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
