import stripe
from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')



def product_ex(request):
    form_data = Product.objects.all()
    return render(request, 'product_ex.html', {'form_data': form_data})

def contact(request):
    return render(request, 'contact.html')

class LoginView(LoginView):
    template_name = 'login.html'

stripe.api_key = settings.STRIPE_SECRET_KEY

def payment(request):
    if request.method == 'POST':
        try:
            token = request.POST['stripeToken']
            amount = int(request.POST['amount'])
            charge = stripe.Charge.create(
                amount=amount,
                currency='USD',
                description='Example Charge',
                source=token,
            )
            messages.success(request, 'Payment successful.')
            return redirect('payment')
        except stripe.error.CardError as e:
            messages.error(request, f"Card error: {e.error.message}")
        except stripe.error.InvalidRequestError as e:
            messages.error(request, f"Invalid parameters: {e.error.message}")
        except stripe.error.AuthenticationError as e:
            messages.error(request, f"Authentication error: {e.error.message}")
        except stripe.error.APIConnectionError as e:
            messages.error(request, f"Network error: {e.error.message}")
        except stripe.error.StripeError as e:
            messages.error(request, f"Payment failed: {e.error.message}")
    context = {'stripe_key': settings.STRIPE_PUBLISHABLE_KEY}
    return render(request, 'payment.html', context)