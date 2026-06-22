from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView


class Principal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.contador_limpiar = 0

        self.layout = MDBoxLayout(
            orientation="vertical",
            spacing=10,
            padding=20
        )

        titulo = MDLabel(
            text="CALCULADORA",
            halign="center"
        )

        self.num1 = MDTextField(
            hint_text="Ingrese el primer número"
        )

        self.num2 = MDTextField(
            hint_text="Ingrese el segundo número"
        )

        self.resultado = MDLabel(
            text="Resultado:",
            halign="center"
        )

        # ===== FILA OPERACIONES =====
        fila1 = MDBoxLayout(
            size_hint_y=None,
            height=50,
            spacing=10
        )

        btn_sumar = MDRaisedButton(
            text="Sumar",
            on_press=self.sumar
        )

        btn_restar = MDRaisedButton(
            text="Restar",
            on_press=self.restar
        )

        btn_multiplicar = MDRaisedButton(
            text="Multiplicar",
            on_press=self.multiplicar
        )

        btn_dividir = MDRaisedButton(
            text="Dividir",
            on_press=self.dividir
        )

        fila1.add_widget(btn_sumar)
        fila1.add_widget(btn_restar)
        fila1.add_widget(btn_multiplicar)
        fila1.add_widget(btn_dividir)

        # ===== FILA FUNCIONES =====
        fila2 = MDBoxLayout(
            size_hint_y=None,
            height=50,
            spacing=10
        )

        btn_raiz = MDRaisedButton(
            text="√",
            on_press=self.raiz
        )

        btn_potencia = MDRaisedButton(
            text="x²",
            on_press=self.potencia
        )

        btn_porcentaje = MDRaisedButton(
            text="%",
            on_press=self.porcentaje
        )

        btn_limpiar = MDRaisedButton(
            text="Limpiar",
            on_press=self.limpiar
        )

        fila2.add_widget(btn_raiz)
        fila2.add_widget(btn_potencia)
        fila2.add_widget(btn_porcentaje)
        fila2.add_widget(btn_limpiar)

        # ===== HISTORIAL =====
        historial_titulo = MDLabel(
            text="Historial",
            halign="center"
        )

        scroll = ScrollView()

        self.historial = MDLabel(
            text="",
            size_hint_y=None,
            valign="top"
        )

        self.historial.bind(
            texture_size=self.actualizar_altura
        )

        scroll.add_widget(self.historial)

        # ===== AGREGAR WIDGETS =====
        self.layout.add_widget(titulo)
        self.layout.add_widget(self.num1)
        self.layout.add_widget(self.num2)
        self.layout.add_widget(fila1)
        self.layout.add_widget(fila2)
        self.layout.add_widget(self.resultado)
        self.layout.add_widget(historial_titulo)
        self.layout.add_widget(scroll)

        self.add_widget(self.layout)

    def actualizar_altura(self, instance, value):
        instance.height = value[1]

    def formatear(self, numero):
        if numero == int(numero):
            return str(int(numero))
        return str(numero)

    def obtener_numeros(self):
        try:
            n1 = float(self.num1.text)
            n2 = float(self.num2.text)
            return n1, n2
        except:
            self.resultado.text = "Resultado: Error"
            return None, None

    def agregar_historial(self, texto):
        self.historial.text += texto + "\n"

    # ===== OPERACIONES =====

    def sumar(self, obj):
        self.contador_limpiar = 0

        n1, n2 = self.obtener_numeros()

        if n1 is not None:
            r = n1 + n2

            self.resultado.text = f"Resultado: {self.formatear(r)}"

            self.agregar_historial(
                f"{self.formatear(n1)} + {self.formatear(n2)} = {self.formatear(r)}"
            )

    def restar(self, obj):
        self.contador_limpiar = 0

        n1, n2 = self.obtener_numeros()

        if n1 is not None:
            r = n1 - n2

            self.resultado.text = f"Resultado: {self.formatear(r)}"

            self.agregar_historial(
                f"{self.formatear(n1)} - {self.formatear(n2)} = {self.formatear(r)}"
            )

    def multiplicar(self, obj):
        self.contador_limpiar = 0

        n1, n2 = self.obtener_numeros()

        if n1 is not None:
            r = n1 * n2

            self.resultado.text = f"Resultado: {self.formatear(r)}"

            self.agregar_historial(
                f"{self.formatear(n1)} × {self.formatear(n2)} = {self.formatear(r)}"
            )

    def dividir(self, obj):
        self.contador_limpiar = 0

        n1, n2 = self.obtener_numeros()

        if n1 is not None:

            if n2 == 0:
                self.resultado.text = "Resultado: No se puede dividir por 0"
                return

            r = n1 / n2

            self.resultado.text = f"Resultado: {self.formatear(r)}"

            self.agregar_historial(
                f"{self.formatear(n1)} ÷ {self.formatear(n2)} = {self.formatear(r)}"
            )

    # ===== FUNCIONES =====

    def raiz(self, obj):
        self.contador_limpiar = 0

        try:
            n = float(self.num1.text)

            if n < 0:
                self.resultado.text = "Resultado: Error"
                return

            r = n ** 0.5

            self.resultado.text = f"Resultado: {self.formatear(r)}"

            self.agregar_historial(
                f"√{self.formatear(n)} = {self.formatear(r)}"
            )

        except:
            self.resultado.text = "Resultado: Error"

    def potencia(self, obj):
        self.contador_limpiar = 0

        try:
            n = float(self.num1.text)

            r = n ** 2

            self.resultado.text = f"Resultado: {self.formatear(r)}"

            self.agregar_historial(
                f"{self.formatear(n)}² = {self.formatear(r)}"
            )

        except:
            self.resultado.text = "Resultado: Error"

    def porcentaje(self, obj):
        self.contador_limpiar = 0

        n1, n2 = self.obtener_numeros()

        if n1 is not None:

            r = (n1 * n2) / 100

            self.resultado.text = f"Resultado: {self.formatear(r)}"

            self.agregar_historial(
                f"{self.formatear(n2)}% de {self.formatear(n1)} = {self.formatear(r)}"
            )

    # ===== LIMPIAR =====

    def limpiar(self, obj):

        self.contador_limpiar += 1

        if self.contador_limpiar == 1:

            self.resultado.text = "Resultado:"

        else:

            self.historial.text = ""
            self.resultado.text = "Resultado:"
            self.contador_limpiar = 0


class MiApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"

        sm = ScreenManager()
        sm.add_widget(Principal(name="principal"))

        return sm


MiApp().run()