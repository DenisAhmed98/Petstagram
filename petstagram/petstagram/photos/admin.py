from django.contrib import admin

from petstagram.photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description', 'get_tagged_pets')

    @staticmethod
    def get_tagged_pets(obj):
        return ', '.join([pet.name for pet in obj.tagged_pets.all()])
