class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, product, request):    
        id = str(product.id)    
        if request.method == 'GET':
            cantidad = request.GET.get('cantidad')
            if cantidad == None or cantidad == 0 or cantidad == "":
                cantidad = 1
            precioCantidad = int(product.price) * int(cantidad)
    
            if id not in self.carrito.keys():
                self.carrito[id]={
                "producto_id": int(product.id),
                "nombre": str(product.name),
                "precio": int(product.price),
                "total": precioCantidad,
                "cantidad": int(cantidad),
            }
            else:
                self.carrito[id]["total"] += precioCantidad
                self.carrito[id]["cantidad"] += int(cantidad)
            self.guardar_carrito()

        else: 
            cantidad = request.POST['cantidad']
            if cantidad == None or cantidad == 0 or cantidad == "":
                cantidad = 1
            precioCantidad = int(product.price) * int(cantidad)
    
            if id not in self.carrito.keys():
                self.carrito[id]={
                "producto_id": int(product.id),
                "nombre": str(product.name),
                "precio": int(product.price),
                "total": precioCantidad,
                "cantidad": int(cantidad),
            }
            else:
                self.carrito[id]["total"] += precioCantidad
                self.carrito[id]["cantidad"] += int(cantidad)
            self.guardar_carrito()

            
        

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, product):
        id = str(product.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, product):
        id = str(product.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["total"] -= int(product.price)
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(product)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True