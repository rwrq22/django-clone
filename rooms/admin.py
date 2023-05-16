from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):

    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices,)

    list_display = (
        "name",
        "kind",
        "total_amenities",
        "rating",
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

    search_fields = ("owner__username",)


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
