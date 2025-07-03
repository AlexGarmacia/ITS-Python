from abc import ABC, abstractmethod
import math

class Volo(ABC):
    def __init__(self,codice_volo, captacita_massima):
        self.codice_volo = codice_volo
        self.capacita_massima = captacita_massima
        self.prenotazioni = 0
    
    @abstractmethod

    def prenota_posto(self, posti, classe_servizio=None):
        pass

    @abstractmethod
    def posti_disponibili(self):
        pass

class VoloCommerciale(Volo):
    def __init__(self, codice_volo:str, capacita_massima:int):
        super().__init__(codice_volo,capacita_massima)
        
        self.posti_economica = math.floor(self.capacita_massima * 0.70)
        self.posti_business = math.floor(capacita_massima * 0.20)
        self.posti_prima = capacita_massima - self.posti_economica - self.posti_business

        self.prenotazioni_economica = 0
        self.prenotazioni_business = 0
        self.prenotazioni_prima = 0

    def posti_disponibili(self):
        disp_economica = self.posti_economica - self.prenotazioni_economica
        disp_business = self.posti_business - self.prenotazioni_business
        disp_prima = self.posti_prima - self.prenotazioni_prima

        disp_economica = max(0, disp_economica)
        disp_business = max(0, disp_business)
        disp_prima = max(0, disp_prima)
        disp_totale = max(0, disp_totale)

        return {
            'posti disponibili': disp_totale,
            'classe economica': disp_economica,
            'classe business' : disp_business,
            'prima classe' : disp_prima
            }
    def prenota_posto(self, posti, classe_servizio=None):
        classe_servizio = classe_servizio if classe_servizio else None
        disp = self.posti_disponibili()

         if disp['posti disponibili'] == 0:
            print(f"Volo {self.codice_volo} al completo!")
            return

        if classe_servizio not in ['economica', 'business', 'prima']:
            print(f"Errore: classe '{classe_servizio}' non valida.")
            return

        posti_disponibili_classe = disp[f'classe {classe_servizio}']

        if posti > posti_disponibili_classe:
            print(f"Non è possibile riservare {posti} posti in classe {classe_servizio}. Numero posti disponibili: {posti_disponibili_classe}")
            return

        # Prenotazione
        if classe_servizio == 'economica':
            self.prenotazioni_economica += posti
        elif classe_servizio == 'business':
            self.prenotazioni_business += posti
        elif classe_servizio == 'prima':
            self.prenotazioni_prima += posti

        self.prenotazioni = self.prenotazioni_economica + self.prenotazioni_business + self.prenotazioni_prima

        print(f"{posti} posti prenotati su {self.codice_volo} in classe {classe_servizio}.")

       


        









        





