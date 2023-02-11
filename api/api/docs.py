from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Inventory Management API",
      default_version='v1',
      description="This API is for product inventory management",
      terms_of_service="https://www.scvconsultants.com",
      contact=openapi.Contact(email="ygpark2@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
