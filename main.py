import folium
from tkinter import Tk, Frame
from tkinterweb import HtmlFrame

class SeuApp:
    def __init__(self):
        self.App2 = Tk()
        self.App2.title('GeoSaga: Brazil Edition')
        self.App2.geometry('400x400')

        # Criar um frame para exibir o mapa
        self.map_frame = HtmlFrame(self.App2, width=400, height=400)
        self.map_frame.grid(row=0, column=0)

        # Criar um mapa folium
        self.map = folium.Map(location=[-22.9068, -43.1729], zoom_start=10)

        # Converter o mapa folium em HTML e exibi-lo no frame
        self.map_frame.set_content(self.map._repr_html_())

        self.App2.mainloop()

SeuApp()
