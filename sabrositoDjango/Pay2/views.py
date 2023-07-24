import uuid
import smtplib
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
     messages.success(request, 'Tu pago fue realizado exitosamente!')

     #script para enviar correo de comprobante
     def enviar_email():
          # Datos del restaurante
          nombre_restaurante = 'Sabrosito'
          correo_restaurante = 'sabrositoRte@gmail.com'

          # Mensaje para el cliente
          mensaje = f'Hola,\n\nGracias por elegir {nombre_restaurante}!'
          mensaje += '\n\nQueremos informarte que tu pago ha sido realizado con exito.'
          mensaje += ' Estamos procesando tu pedido y pronto te lo enviaremos a la comodidad de tu hogar.'
          mensaje += '\n\nApreciamos sinceramente tu preferencia y confianza en nosotros.'
          mensaje += ' Nos esforzamos por brindarte la mejor experiencia culinaria mexicana.'
          mensaje += '\n\nEsperamos que disfrutes de nuestra deliciosa comida y que vuelvas pronto para probar mas sabores.'
          mensaje += f'\n\nAtentamente,\nEl equipo de {nombre_restaurante}'

          # Asunto del correo
          subject = 'Comprobante de pago - ' + nombre_restaurante

          # Construir el mensaje completo
          msgEmail = f'Subject: {subject}\n\n{mensaje}'

          # Configurar el servidor SMTP
          server = smtplib.SMTP('smtp.gmail.com', 587)
          server.starttls()
          server.login(correo_restaurante, 'ylzempbethtbnkyv')

          # Enviar el correo electrónico
          server.sendmail(correo_restaurante, 'davidcame124@gmail.com', msgEmail)

     enviar_email()


     return redirect('pago')


def paypal_cancel(request):
     messages.error(request, 'Tu orden fue cancelada')
     return redirect('pago')