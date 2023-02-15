from django.shortcuts import render, HttpResponseRedirect
from django.views import View
import stripe
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.conf import settings
from .models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.

class ProductsLandingPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        item = Item.objects.get_queryset()
        context = super(ProductsLandingPageView, self).get_context_data(**kwargs)
        context.update(
            {
                'item': item,
                'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
            }
        )
        return context
class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price_data':{
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                            'images': ['link']
                        },
                    },
                    'quantity': 1
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })

# def page_orders(request):
#     context={
#         'order': Orders.objects.all(),
#     }
#     return render(request, 'orders.html', context)
#
# def orders_add(request, item_id):
#     item = Item.objects.get(id=item_id)
#     orders = Orders.objects.filter(order=item)
#
#     if not orders.exists():
#         Orders.objects.create(order=item, quantity=1)
#     else:
#         order = orders.first()
#         order.quantity += 1
#         order.save()
#
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])
#
# def orders_remove(request, id):
#     orders = Orders.objects.get(id=id)
#     orders.delete()
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])