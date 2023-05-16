from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):

    title = "words!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):  # Filtering 된 객체들 return
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


class GoodFilter(admin.SimpleListFilter):

    title = "good or bad!"

    parameter_name = "grade"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]

    def queryset(self, request, reviews):
        grade = self.value()
        if grade == "good":
            return reviews.filter(rating__gte=3)
        elif grade == "bad":
            return reviews.filter(rating__lt=3)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (
        "rating",
        "user__is_host",
        "room__category",
        WordFilter,
        GoodFilter,
    )
