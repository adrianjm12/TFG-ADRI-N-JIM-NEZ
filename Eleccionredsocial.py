import tkinter as tk
from tkinter import messagebox

# Datos de las redes sociales
social_media = {
    "Instagram": {
        "Visualmente atractivos": True,
        "Fotos": True,
        "Stories": True,
        "Videos cortos (<1min)": True,
        "Aumentar la visibilidad visual y la interacción directa con la audiencia": True,
        "Jóvenes y adultos": True,
        "Cualquier sexo": True,
    },
    "Facebook": {
        "Funcionales y prácticos": True,
        "Videos largos >1min": True,
        "Eventos": True,
        "Conectar con una audiencia amplia, generar leads y ventas directas": True,
        "Todas las edades": True,
        "Cualquier sexo": True,
    },
    "TikTok": {
        "De tendencia y creativos": True,
        "Videos cortos (<1min)": True,
        "Videos largos >1min": True,
        "Generar viralidad y captar la atención con contenido creativo": True,
        "Principalmente jóvenes": True,
        "Cualquier sexo": True,
    },
    "Pinterest": {
        "Artesanales y de inspiración": True,
        "Fotos": True,
        "Inspirar a los usuarios y dirigir tráfico hacia páginas de productos": True,
        "Jóvenes y adultos": True,
        "Mujeres": True,
    }
}

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Encuesta de Redes Sociales")
        self.root.configure(bg="#d0e7ff")  # Azul sutil
        self.current_section = 0
        self.responses = []
        self.setup_section()

        # Ajusta el tamaño de la fuente cuando la ventana se redimensiona
        self.root.bind('<Configure>', self.adjust_text_size)

    def adjust_text_size(self, event=None):
        """Ajusta el tamaño de la fuente según el tamaño de la ventana."""
        base_font_size = max(self.root.winfo_width() // 40, 14)  # Calcula el tamaño base, mayor para pantallas grandes
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(font=("Arial", base_font_size), justify="center", wraplength=self.root.winfo_width() - 100)  # Margen más amplio
            elif isinstance(widget, tk.Button):
                widget.config(font=("Arial", base_font_size))

    def setup_section(self):
        # Limpia la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.root, bg="#d0e7ff")
        frame.pack(expand=True)

        if self.current_section == 0:
            self.show_promotional_tools_section(frame)
        elif self.current_section == 1:
            self.show_social_media_options(frame)
        elif self.current_section == 2:
            self.show_section_1(frame)
        elif self.current_section == 3:
            self.show_section_2(frame)
        elif self.current_section == 4:
            self.show_section_3(frame)
        elif self.current_section == 5:
            self.show_section_4(frame)
        elif self.current_section == 6:
            self.show_section_5(frame)
        elif self.current_section == 7:
            self.show_results(frame)
        elif self.current_section == 8:
            self.show_final_message(frame)  # Asegúrate de que esta llamada esté presente.

    def show_promotional_tools_section(self, parent):
        tk.Label(parent, text="Herramientas de Promoción y Publicidad", bg="#d0e7ff", fg="black").pack(pady=10)
        tk.Label(parent, text="Ya sea que ofrezcas un producto o un servicio, existen herramientas que facilitan la promoción y otras que mejoran la calidad del servicio brindado a través de páginas web y otras plataformas.", bg="#d0e7ff", fg="black").pack(pady=10)
        
        tk.Button(parent, text="Aplicaciones Móviles", command=self.show_mobile_apps_info).pack(pady=5)
        tk.Button(parent, text="Redes Sociales", command=self.show_social_media_section).pack(pady=5)

    def show_mobile_apps_info(self):
        tk.messagebox.showinfo("Aplicaciones Móviles", 
            "Las aplicaciones móviles son herramientas clave para promocionar productos y servicios, facilitando la conexión directa con los clientes y mejorando la visibilidad en el mercado. Además, existen aplicaciones complementarias que se pueden vincular a sitios web, ofreciendo funciones adicionales como marketing, análisis y comunicación en tiempo real. Por ejemplo, WhatsApp Business permite interactuar con clientes de manera directa, mientras plataformas como Wix ofrecen aplicaciones que integran estas funcionalidades en una página web.")

    def show_social_media_section(self):
        self.current_section = 1
        self.setup_section()

    def show_social_media_options(self, parent):
        tk.Label(parent, text="Selecciona una red social para más información:", bg="#d0e7ff", fg="black").pack(pady=10)
        
        tk.Button(parent, text="Instagram", command=self.show_instagram_info).pack(pady=5)
        tk.Button(parent, text="Facebook", command=self.show_facebook_info).pack(pady=5)
        tk.Button(parent, text="TikTok", command=self.show_tiktok_info).pack(pady=5)
        tk.Button(parent, text="Pinterest", command=self.show_pinterest_info).pack(pady=5)

        tk.Button(parent, text="Siguiente", command=self.next_section).pack(side=tk.RIGHT, padx=10, pady=10)
        tk.Button(parent, text="Volver", command=self.go_back).pack(side=tk.LEFT, padx=10, pady=10)

    def show_instagram_info(self):
        tk.messagebox.showinfo("Instagram", 
            "Plataforma social enfocada en compartir fotos y videos, ideal para el marketing visual y la interacción con audiencias a través de imágenes y contenido efímero.")

    def show_facebook_info(self):
        tk.messagebox.showinfo("Facebook", 
            "Red social versátil que permite compartir actualizaciones, fotos, videos y eventos, utilizada ampliamente para conectar con amigos y promocionar productos o servicios.")

    def show_tiktok_info(self):
        tk.messagebox.showinfo("TikTok", 
            "Aplicación de videos cortos que permite a los usuarios crear y compartir clips creativos, siendo popular para tendencias virales y marketing de contenido dinámico.")

    def show_pinterest_info(self):
        tk.messagebox.showinfo("Pinterest", 
            "Plataforma visual que permite descubrir y guardar ideas en forma de imágenes, utilizada para inspiración y promoción de productos en sectores como moda, decoración y cocina.")

    def show_section_1(self, parent):
        self.show_question(parent, "¿Qué tipo de producto o servicio ofreces?", [
            "Visualmente atractivos",
            "De tendencia y creativos",
            "Artesanales y de inspiración",
            "Funcionales y prácticos"
        ])

    def show_section_2(self, parent):
        self.show_question(parent, "¿Cuál es el tipo de contenido que te resultaría más cómodo crear?", [
            "Fotos",
            "Stories",
            "Videos cortos (<1min)",
            "Videos largos >1min",
            "Eventos"
        ])

    def show_section_3(self, parent):
        self.show_question(parent, "¿Cuál es tú objetivo en redes sociales?", [
            "Aumentar la visibilidad visual y la interacción directa con la audiencia",
            "Generar viralidad y captar la atención con contenido creativo",
            "Conectar con una audiencia amplia, generar leads y ventas directas",
            "Inspirar a los usuarios y dirigir tráfico hacia páginas de productos"
        ])

    def show_section_4(self, parent):
        self.show_question(parent, "¿A qué tipo de audiencia va enfocado tu producto o servicio?", [
            "Principalmente jóvenes",
            "Jóvenes y adultos",
            "Todas las edades"
        ])

    def show_section_5(self, parent):
        self.show_question(parent, "¿A qué sexo va enfocado tu producto o servicio?", [
            "Mujeres",
            "Hombres",
            "Cualquier sexo"
        ])

    def show_question(self, parent, question, options, is_social_media=False):
        tk.Label(parent, text=question, bg="#d0e7ff", fg="black").pack(pady=10)
        for option in options:
            tk.Button(parent, text=option, command=lambda opt=option: self.handle_option(opt, is_social_media)).pack(pady=5)

        if self.current_section > 0:
            tk.Button(parent, text="Anterior", command=self.go_back).pack(side=tk.LEFT, padx=10, pady=10)

        if is_social_media:
            tk.Button(parent, text="Siguiente", command=self.next_section).pack(side=tk.RIGHT, padx=10, pady=10)

    def handle_option(self, option, is_social_media):
        if is_social_media:
            # Solo cambia a la siguiente sección si se hace clic en una opción de red social
            self.show_social_media_options(self.root.winfo_children()[0])
        else:
            self.record_response(option)

    def record_response(self, response):
        self.responses.append(response)
        self.next_section()

    def go_back(self):
        self.current_section -= 1
        self.setup_section()

    def next_section(self):
        self.current_section += 1
        self.setup_section()

    def show_results(self, parent):
        best_match = self.find_best_match()
        tk.Label(parent, text=f"Está es la red social que más se ajusta a tus intereses: {best_match}", bg="#d0e7ff", fg="black").pack(pady=10)
        tk.Button(parent, text="Siguiente", command=self.next_section).pack(pady=10)

    def find_best_match(self):
        scores = {name: 0 for name in social_media}
        for name, features in social_media.items():
            scores[name] = sum(1 for response in self.responses if features.get(response, False))
        return max(scores, key=scores.get)

    def show_final_message(self, parent):
        message = (
            "¡Enhorabuena! Has llegado al final de la guía. Aunque se te ha recomendado una plataforma de venta online y una red social según tus necesidades, "
            "es fundamental que investigues y descubras cuáles son las que mejor se adaptan a tu producto o servicio. Recuerda que no tienes que limitarte a una sola opción; "
            "combinar varias redes sociales puede fortalecer tu imagen de marca y ampliar tu alcance, aunque requerirá más tiempo y esfuerzo. Lo mismo ocurre al utilizar diferentes plataformas de venta. "
            "Te recomendamos que revises los consejos de los entrevistados en el TFG y la información proporcionada a lo largo del mismo, donde se analizan en detalle las funcionalidades, costos, públicos y experiencias relacionadas con cada plataforma y herramienta. ¡Gracias por tu tiempo!"
        )
        tk.Label(parent, text=message, wraplength=self.root.winfo_width() - 100, bg="#d0e7ff", fg="black", font=("Arial", 14), justify="center").pack(pady=10)
        tk.Button(parent, text="Volver al principio", command=self.restart).pack(pady=10)

    def restart(self):
        self.current_section = 0
        self.responses = []
        self.setup_section()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

