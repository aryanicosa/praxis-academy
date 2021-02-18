from django.contrib import admin
from blog.models import Post, Category

# membuat class posting oleh admin
class PostAdmin(admin.ModelAdmin):
    pass

# membuat class category oleh admin
class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)