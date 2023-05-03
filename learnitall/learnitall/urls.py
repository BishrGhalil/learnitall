from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from courses.views import CourseListView

urlpatterns = [
    path("", CourseListView.as_view(), name="course_list"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LoginView.as_view(), name="logout"),
    path("admin/", admin.site.urls),
    path("courses/", include("courses.urls")),
    path("students/", include("students.urls")),
    path("api/", include("courses.api.urls"), name="api"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
