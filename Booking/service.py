from estate.models import Estate


# aqui creo una clase


#metodo va invocar al servicio de pago, y al servicio de estate.
class BookingService:
    @staticmethod
    def verify_available(estate:Estate) -> bool:
        #otra logica
        return estate.is_available
