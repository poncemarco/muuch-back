from xhtml2pdf import pisa
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
import pandas as pd
import io

class TicketManager:

    def __init__(self, order, client_email, name, phone, outter_items, code: str = None) -> None:
        self.to_email = ['marco@muuch-maaya.com', 'ventas@muuch-maaya.com']
        self.header = "Nuevo pedido"
        self.from_email = 'info@muuch-maaya.com'
        self.message = "Se ha realizado un nuevo pedido"
        self.ticket_template = 'ticket.html'
        self.order = order
        self.name = name
        self.phone = phone
        self.client_email = client_email
        self.outter_items = outter_items
        self.context = self.create_context()
        self.ticket_path = f'media/pdfs/ticket_{self.order.id}.pdf'
        self.code = code
        self.excel = io.BytesIO()
        
        
    def create_context(self) -> dict:
        return {
            'items': self.order.items.all(),
            'total': self.order.get_total(),
            'discount': self.order.get_discount(),
            'client_email': self.client_email,
            'name': self.name,
            'phone': self.phone,
            'outter_items': self.outter_items,
        }
        
        
    def create_excel(self):
        writer = pd.ExcelWriter('archivo_excel.xlsx', engine='xlsxwriter')
        products = {
            "Cantidad" : [item.quantity for item in self.order.items.all()],
            "Unidad" : [item.item.unit for item in self.order.items.all()],
            "Producto" : [item.item.name for item in self.order.items.all()],
            "Valor unitario" : [float(item.item.price) for item in self.order.items.all()],
            "Descuento" : [float(item.item.price) * self.order.discount.discount_factor if self.order.discount else  item.item.price for item in self.order.items.all()],
            "IVA" : [float(item.item.price) * 0.16 for item in self.order.items.all()],
            "Importe" : [item.get_total_item_price() for item in self.order.items.all()]
        }
        
        info_custumer = {
            "Nombre" : [self.name],
            "Correo" : [self.client_email],
            "Telefono" : [self.phone]
        }
        
        df_products = pd.DataFrame(products)
        df_custumer = pd.DataFrame(info_custumer)
        with pd.ExcelWriter(self.excel) as writer:
            df_products.to_excel(writer, sheet_name='Productos')
            df_custumer.to_excel(writer, sheet_name='Cliente')
        

    def create_pdf(self):
        content = render_to_string(self.ticket_template, self.context)
        open(self.ticket_path, 'x')
        with open(self.ticket_path, 'w+b') as file:
            pisa_status = pisa.CreatePDF(content, dest=file, context_meta=self.context)
        return pisa_status.err
    
    def create_excel(self):
        writer = pd.ExcelWriter('archivo_excel.xlsx', engine='xlsxwriter')
        products = {
            "Cantidad" : [item.quantity for item in self.order.items.all()],
            "Unidad" : [item.item.unit for item in self.order.items.all()],
            "Producto" : [item.item.name for item in self.order.items.all()],
            "Valor unitario" : [float(item.item.price) for item in self.order.items.all()],
            "Descuento" : [float(item.item.price) * self.order.discount.discount_factor if self.order.discount else  item.item.price for item in self.order.items.all()],
            "IVA" : [float(item.item.price) * 0.16 for item in self.order.items.all()],
            "Importe" : [item.get_total_item_price() for item in self.order.items.all()]
        }
        
        info_custumer = {
            "Nombre" : [self.name],
            "Correo" : [self.client_email],
            "Telefono" : [self.phone]
        }
        
        if self.outter_items:
            outter_items = {
                "Producto" : [item['name'] for item in self.outter_items],
                "Cantidad" : [item['quantityDescription'] for item in self.outter_items],
                "Descripcion" : [item['description'] for item in self.outter_items]
            }
            df_outter_items = pd.DataFrame(outter_items)
        
        df_products = pd.DataFrame(products)
        df_custumer = pd.DataFrame(info_custumer)
        with pd.ExcelWriter(self.excel) as writer:
            df_products.to_excel(writer, sheet_name='Productos')
            df_custumer.to_excel(writer, sheet_name='Cliente')
            if self.outter_items:
                df_outter_items.to_excel(writer, sheet_name='Productos Solicitados')
        self.excel.seek(0)
        return self.excel
    
    def send_ticket(self):
        html_content = render_to_string(
            self.ticket_template,
            self.context
        )
        text_content = strip_tags(html_content)
        
        msg = EmailMultiAlternatives(
            self.header,
            text_content,
            self.from_email,
            self.to_email
        )
        msg.attach_alternative(html_content, "text/html")
        msg.attach(f"ticket_{self.order.id}.xlsx", self.excel.getvalue(), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        msg.send()