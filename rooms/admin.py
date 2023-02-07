from django.contrib import admin
from .models import Room, Amenity


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "kind",
        "total_amenities",
        "price",
        "owner",
        "created_at",
    )

    list_filter = (
        "price",
        "country",
        "city",
        "pet_friendly",
        "owner",
        "created_at",
    )

    def total_amenities(self, room):
        print(room)
        return room.amenities.count()


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "description",
        "updated_at",
        "created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
