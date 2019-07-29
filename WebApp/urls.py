from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'question', api.QuestionViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Question
    path('', views.QuestionListView.as_view(), name='WebApp_question_list'),
    path('WebApp/question/create/', views.QuestionCreateView.as_view(), name='WebApp_question_create'),
    path('WebApp/question/detail/<slug:slug>/', views.QuestionDetailView.as_view(), name='WebApp_question_detail'),
    path('WebApp/question/update/<slug:slug>/', views.QuestionUpdateView.as_view(), name='WebApp_question_update'),
)
