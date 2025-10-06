from rest_framework.routers import DefaultRouter

from blog.viewsets import CategoryViewSet, PostViewSet, CommentViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'profile', ProfileViewSet)

urlpatterns = router.urls