from django.urls import path

from myshop.all_views.basket_view import ExportBasketInExcel, ProductInBasketView
from myshop.all_views.orders_view import OrdersView, ExportOrderInExcel
from myshop.views import ProductView, SocketsCategoryView, ColorsView, CollectionsView, BrendsView, CatalogView, \
    BasketView

urlpatterns = [
    path('catalog/create/', CatalogView.as_view()),
    path('catalog/get/<int:pk>/', CatalogView.as_view()),
    path('catalog/get/', CatalogView.as_view()),
    path('catalog/update/<int:pk>/', CatalogView.as_view()),
    path('catalog/delete/<int:pk>/', CatalogView.as_view())
]

urlpatterns += [
    path('brend/create/', BrendsView.as_view()),
    path('brend/get/<int:pk>/', BrendsView.as_view(), name="brand_get"),
    path('brend/get/', BrendsView.as_view()),
    path('brend/update/<int:pk>/', BrendsView.as_view()),
    path('brend/delete/<int:pk>/', BrendsView.as_view())
]
urlpatterns += [
    path('collection/create/', CollectionsView.as_view()),
    path('collection/get/<int:pk>/', CollectionsView.as_view()),
    path('collection/get/', CollectionsView.as_view()),
    path('collection/update/<int:pk>/', CollectionsView.as_view()),
    path('collection/delete/<int:pk>/', CollectionsView.as_view())
]
urlpatterns += [
    path('color/create/', ColorsView.as_view()),
    path('color/get/<int:pk>/', ColorsView.as_view()),
    path('color/get/', ColorsView.as_view()),
    path('color/update/<int:pk>/', ColorsView.as_view()),
    path('color/delete/<int:pk>/', ColorsView.as_view())
]
urlpatterns += [
    path('socket_category/create/', SocketsCategoryView.as_view()),
    path('socket_category/get/<int:pk>/', SocketsCategoryView.as_view()),
    path('socket_category/get/', SocketsCategoryView.as_view()),
    path('socket_category/update/<int:pk>/', SocketsCategoryView.as_view()),
    path('socket_category/delete/<int:pk>/', SocketsCategoryView.as_view())
]
urlpatterns += [
    path('product/create/', ProductView.as_view()),
    path('product/get/<int:pk>/', ProductView.as_view()),
    path('product/get/', ProductView.as_view(), name='products-list'),
    path('product/update/<int:pk>/', ProductView.as_view()),
    path('product/delete/<int:pk>/', ProductView.as_view())
]

#
# urlpatterns+=[
#     path('users/', ListUsersView.as_view())
# ]

urlpatterns += [
    path('basket/post/', BasketView.as_view()),
    path('basket/get/', BasketView.as_view()),
    path('basket/put/<int:pk>/', BasketView.as_view()),
    path('basket/delete/<int:pk>/', BasketView.as_view())
]

urlpatterns += [
    path('product_in_basket/post/', ProductInBasketView.as_view()),
    path('product_in_basket/get/', ProductInBasketView.as_view()),
    path('product_in_basket/put/<int:pk>/', ProductInBasketView.as_view()),
    path('product_in_basket/delete/<int:pk>/', ProductInBasketView.as_view())
]

urlpatterns += [
    path('basket_excel/get/', ExportBasketInExcel.as_view()),
    path('order_excel/get/<int:pk>/', ExportOrderInExcel.as_view()),
]

urlpatterns += [
    path('create_order/post/', OrdersView.as_view()),
]
