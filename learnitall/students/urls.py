from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path(
        "register/",
        views.StudentRegistrationView.as_view(),
        name="student_registration",
    ),
    path(
        "enroll-course/",
        views.StudentEnrollCourseView.as_view(),
        name="student_enroll_course",
    ),
    path(
        "courses/",
        cache_page(60 * 10)(views.StudentCourseListView.as_view()),
        name="student_course_list",
    ),
    path(
        "courses/<pk>/",
        cache_page(60 * 10)(views.StudentCourseDetailView.as_view()),
        name="student_course_detail",
    ),
    path(
        "courses/<pk>/<module_id>/",
        cache_page(60 * 10)(views.StudentCourseDetailView.as_view()),
        name="student_course_detail_module",
    ),
]
