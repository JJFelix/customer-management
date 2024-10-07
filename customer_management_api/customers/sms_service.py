import africastalking
from django.conf import settings

class SMSService:
    def __init__(self):
        africastalking.initialize(settings.AFRICAS_TALKING_USERNAME, settings.AFRICAS_TALKING_API_KEY)
        self.sms = africastalking.SMS

    def send_sms(self, recipients, message, sender):
        try:
            response = self.sms.send(message, recipients, sender)
            return response
        except Exception as e:
            return {'error': str(e)}
