from django.urls import path
from .views import groups_page, join_group

urlpatterns = [
    path("", groups_page, name="groups"),
    path("join/<int:group_id>/", join_group, name="join_group"),
]
