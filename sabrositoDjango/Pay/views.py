import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

# Create your views here.



def home(request): 
     host = request.get_host()
     paypal_dict = {
          'business': settings.PAYPAL_RECEIVER_EMAIL,
          'amount': '254', #Obtener el costo de la DB cuando se cree
          'item_name': 'Products',
          'invoice': str(uuid.uuid4()),
          'currency_code': 'USD',
          'notify_url': f'http://{host}{reverse("paypal-ipn")}',
          'return_url': f'http://{host}{reverse("paypal-return")}',
          'cancel_return': f'http://{host}{reverse("paypal-cancel")}',

     }
     form = PayPalPaymentsForm(initial=paypal_dict)
     context = {'form': form}
     return render(request, 'MiTemplateDePago.html', context)

def paypal_return(request):
     messages.success(request, 'Realizaste el pago con éxito!')
     return redirect('MiTemplateDePago.html')

def paypal_cancel(request):
     messages.error(request, 'Tu orden fue cancelada')
     return redirect('MiTemplateDePago.html')