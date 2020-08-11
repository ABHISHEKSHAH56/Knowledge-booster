from django.contrib import admin
from booster.models import suscriberr,comment, Post,Blogdes,contact

@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
 list_display = ('name', 'email')

 search_fields = ('name', 'email')


@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
 list_display = ('name', 'email')
 search_fields = ('name', 'email')


class ModuleInline(admin.StackedInline):
        model = Blogdes



 



@admin.register(suscriberr)
class suscriberrAdmin(admin.ModelAdmin):
 list_display = ('name', 'email')

 search_fields = ('name', 'email')


@admin.register(Post)


class PostAdmin(admin.ModelAdmin):

        list_display = ('title', 'slug', 'author', 'publish', 'status')
        list_filter = ('status', 'created', 'publish', 'author')
        search_fields = ('title', 'body')
        prepopulated_fields = {'slug': ('title',)}
        raw_id_fields = ('author',)
        date_hierarchy = 'publish'
        ordering = ('status', 'publish')
        inlines = [ModuleInline]        