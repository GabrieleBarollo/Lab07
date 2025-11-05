import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def compila_dd_museo(self):
        l = self._model.get_musei()
        for museo in l:
            self._view.dd_museo.options.append(ft.dropdown.Option(museo))
        self._view.page.update()

    def compila_dd_epoca(self):
        l = self._model.get_epoche()
        for epoca in l:
            self._view.dd_epoca.options.append(ft.dropdown.Option(epoca))
        self._view.page.update()


    # CALLBACKS DROPDOWN
    # TODO
    #scrivendo ciò, il bottone non mi serve più.... che cosa si intende per "CALLBACKS DROPDOWN"?
    #IL PROGRAMMA FUNZIONA PERFETTAMENTE ANCHE SENZA QUESTA IMPLEMENTAZIONE
    #def dropdown_changed(self,e):
    #    if self._view.dd_museo.value is None or self._view.dd_epoca.value is None:
    #        messaggio = "Ricordati di compilare i filtri"
    #        self._view.show_alert(messaggio)
    #
    #    elif self._view.dd_museo.value == "Nessun filtro" and self._view.dd_epoca.value == "Nessun filtro":
    #        lista = self._model.get_artefatti_filtrati(self._view.dd_museo.value,self._view.dd_epoca.value)
    #        if len(lista) == 0:
    #            self._view.show_alert("Nessun elemento trovato")
    #        self._view.lst_artefatti.clean()
    #        for oggetto in lista:
    #            self._view.lst_artefatti.controls.append(ft.Text(f"{oggetto}"))\
    #        self._view.page.update()
    #
    #    elif self._view.dd_museo.value != "Nessun filtro" and self._view.dd_epoca.value == "Nessun filtro":
    #        lista = self._model.get_artefatti_filtrati(self._view.dd_museo.value,self._view.dd_epoca.value)
    #        if len(lista) == 0:
    #            self._view.show_alert("Nessun elemento trovato")
    #        self._view.lst_artefatti.clean()
    #        for oggetto in lista:
    #            self._view.lst_artefatti.controls.append(ft.Text(f"{oggetto}"))
    #        self._view.page.update()
    #
    #    elif self._view.dd_museo.value == "Nessun filtro" and self._view.dd_epoca.value != "Nessun filtro":
    #        lista = self._model.get_artefatti_filtrati(self._view.dd_museo.value,self._view.dd_epoca.value)
    #        if len(lista) == 0:
    #            self._view.show_alert("Nessun elemento trovato")
    #        self._view.lst_artefatti.clean()
    #        for oggetto in lista:
    #            self._view.lst_artefatti.controls.append(ft.Text(f"{oggetto}"))
    #        self._view.page.update()
    #
    #    elif self._view.dd_museo.value != "Nessun filtro" and self._view.dd_epoca.value != "Nessun filtro":
    #        lista = self._model.get_artefatti_filtrati(self._view.dd_museo.value,self._view.dd_epoca.value)
    #        if len(lista) == 0:
    #            self._view.show_alert("Nessun elemento trovato")
    #        self._view.lst_artefatti.clean()
    #        for oggetto in lista:
    #            self._view.lst_artefatti.controls.append(ft.Text(f"{oggetto}"))
    #        self._view.page.update()

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def gestione_handler(self, e):
        if self._view.dd_museo.value is None or self._view.dd_epoca.value is None:
            messaggio = "Ricordati di compilare i filtri"
            self._view.show_alert(messaggio)

        elif self._view.dd_museo.value == "Nessun filtro" and self._view.dd_epoca.value == "Nessun filtro":
            lista = self._model.get_artefatti_filtrati(self._view.dd_museo.value,self._view.dd_epoca.value)
            if len(lista) == 0:
                self._view.show_alert("Nessun elemento trovato")
            self._view.lst_artefatti.clean()
            for oggetto in lista:
                self._view.lst_artefatti.controls.append(ft.Text(f"{oggetto}"))
            self._view.page.update()

        elif self._view.dd_museo.value != "Nessun filtro" and self._view.dd_epoca.value == "Nessun filtro":
            lista = self._model.get_artefatti_filtrati(self._view.dd_museo.value,self._view.dd_epoca.value)
            if len(lista) == 0:
                self._view.show_alert("Nessun elemento trovato")
            self._view.lst_artefatti.clean()
            for oggetto in lista:
                self._view.lst_artefatti.controls.append(ft.Text(f"{oggetto}"))
            self._view.page.update()

        elif self._view.dd_museo.value == "Nessun filtro" and self._view.dd_epoca.value != "Nessun filtro":
            lista = self._model.get_artefatti_filtrati(self._view.dd_museo.value,self._view.dd_epoca.value)
            if len(lista) == 0:
                self._view.show_alert("Nessun elemento trovato")
            self._view.lst_artefatti.clean()
            for oggetto in lista:
                self._view.lst_artefatti.controls.append(ft.Text(f"{oggetto}"))
            self._view.page.update()

        elif self._view.dd_museo.value != "Nessun filtro" and self._view.dd_epoca.value != "Nessun filtro":
            lista = self._model.get_artefatti_filtrati(self._view.dd_museo.value,self._view.dd_epoca.value)
            if len(lista) == 0:
                self._view.show_alert("Nessun elemento trovato")
            self._view.lst_artefatti.clean()
            for oggetto in lista:
                self._view.lst_artefatti.controls.append(ft.Text(f"{oggetto}"))
            self._view.page.update()
