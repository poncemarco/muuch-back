from xhtml2pdf import pisa
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

class TicketManager:

    def __init__(self, order, client_email, name, phone, outter_items) -> None:
        self.to_email = ['marco@muuch-maaya.com']
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
        
        
    def create_context(self) -> dict:
        return {
            'items': self.order.items.all(),
            'total': self.order.get_total(),
            'client_email': self.client_email,
            'name': self.name,
            'phone': self.phone,
            'outter_items': self.outter_items
        }

    def create_pdf(self):
        content = render_to_string(self.ticket_template, self.context)
        open(self.ticket_path, 'x')
        with open(self.ticket_path, 'w+b') as file:
            pisa_status = pisa.CreatePDF(content, dest=file, context_meta=self.context)
        return pisa_status.err
    
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
        msg.attach_file(self.ticket_path)
        msg.send()