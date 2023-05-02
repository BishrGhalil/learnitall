from courses.views import CourseListView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LoginView.as_view(), name="logout"),
    path("admin/", admin.site.urls),
    path("", CourseListView.as_view(), name="course_list"),
    path("courses/", include("courses.urls")),
    path("students/", include("students.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)