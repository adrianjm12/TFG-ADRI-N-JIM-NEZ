import tkinter as tk
from tkinter import messagebox

# Definir las plataformas y sus características con nombres actualizados
PLATFORMS = {
    "Crear tu propia página web desde cero": {
        "Presupuesto": ["Medio (500-1.000€)"],
        "Conocimiento": ["Medio (estoy aprendiendo)"],
        "Tiempo": ["Alto"],
        "Personalización": ["Elevado, quiero hacerlo todo a mi gusto"],
        "Duración de ventas": ["Largo plazo, lo voy a vender siempre que sea posible"],
        "Alcance": ["Limitado (necesito invertir en publicidad para darme a conocer)"],
        "Tipo de producto": ["No vendo un producto físico"]
    },
    "Utilizar una plantilla web de un servicio que ofrece plantillas en línea": {
        "Presupuesto": ["Bajo (<500€)"],
        "Conocimiento": ["Ninguno"],
        "Tiempo": ["Una semana o menos"],
        "Personalización": ["Reducido, me vale con seguir una plantilla"],
        "Duración de ventas": ["Corto plazo, es algo que está de moda", "Medio plazo, quiero venderlo durante un tiempo pero en unos años dejaré de hacerlo"],
        "Alcance": ["Limitado (necesito invertir en publicidad para darme a conocer)"],
        "Tipo de producto": ["No vendo un producto físico"]
    },
    "Contratar a alguien para que te haga una página web": {
        "Presupuesto": ["Alto (>1.000€)"],
        "Conocimiento": ["Ninguno"],
        "Tiempo": ["Poco"],
        "Personalización": ["Elevado, quiero hacerlo todo a mi gusto"],
        "Duración de ventas": ["Largo plazo, lo voy a vender siempre que sea posible"],
        "Alcance": ["Limitado (necesito invertir en publicidad para darme a conocer)"],
        "Tipo de producto": ["No vendo un producto físico"]
    },
    "Utilizar un Marketplace": {
        "Presupuesto": ["Bajo (<500€)", "Medio (500-1.000€)"],
        "Conocimiento": ["Poco"],
        "Tiempo": ["Una semana o menos"],
        "Personalización": ["Reducido, me vale con seguir una plantilla"],
        "Duración de ventas": ["Corto plazo, es algo que está de moda", "Medio plazo, quiero venderlo durante un tiempo pero en unos años dejaré de hacerlo"],
        "Alcance": ["Significativo (voy a tener un alcance amplio y no me va a costar mucho dar a conocer mi producto)"]
    },
    "Crear una tienda online a través de una plataforma existente": {
        "Presupuesto": ["Bajo (<500€)", "Medio (500-1.000€)"],
        "Conocimiento": ["Ninguno", "Poco"],
        "Tiempo": ["Una semana o menos", "Entre una y dos semanas"],
        "Personalización": ["Reducido, me vale con seguir una plantilla", "Moderado, quiero personalizar alguna cosa", "Elevado, quiero hacerlo todo a mi gusto"],
        "Duración de ventas": ["Corto plazo, es algo que está de moda", "Medio plazo, quiero venderlo durante un tiempo pero en unos años dejaré de hacerlo", "Largo plazo, lo voy a vender siempre que sea posible"],
        "Alcance": ["Moderado (parto de una plataforma conocida que dispone de herramientas de marketing)"]
    }
}

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Guía para Emprendedores")
        self.root.geometry("800x600")
        self.responses = {}
        
        self.create_main_screen()
        
    def create_main_screen(self):
        self.clear_screen()
        self.root.configure(bg='lightblue')

        tk.Label(self.root, text="Gracias por acceder a la guía para emprendedores cuya misión es enseñar a los usuarios a utilizar las herramientas digitales disponibles en el comercio electrónico que más se adapten a sus necesidades", bg='lightblue', wraplength=750, font=('Arial', 16)).pack(pady=20)
        tk.Button(self.root, text="Comenzar", command=self.create_ecommerce_question).pack(pady=20)
    
    def create_ecommerce_question(self):
        self.clear_screen()
        
        tk.Label(self.root, text="¿Sabes qué es el e-commerce?", font=('Arial', 18)).pack(pady=20)
        tk.Button(self.root, text="Sí", command=self.create_budget_section).pack(pady=10)
        tk.Button(self.root, text="No", command=self.show_ecommerce_explanation).pack(pady=10)
        tk.Button(self.root, text="Anterior", command=self.create_main_screen).pack(pady=10)
    
    def show_ecommerce_explanation(self):
        messagebox.showinfo("Explicación", "El e-commerce es el uso de las tecnologías de la informática y las telecomunicaciones, que soportan las transacciones de productos o servicios entre las empresas, entre estas y particulares o con el Estado")
        self.create_ecommerce_question()

    def create_budget_section(self):
        self.clear_screen()
        
        tk.Label(self.root, text="¿De qué presupuesto dispones para abrir tu tienda online?", font=('Arial', 18)).pack(pady=20)
        tk.Button(self.root, text="Bajo (<500€)", command=lambda: self.save_response("Presupuesto", "Bajo (<500€)")).pack(pady=10)
        tk.Button(self.root, text="Medio (500-1.000€)", command=lambda: self.save_response("Presupuesto", "Medio (500-1.000€)")).pack(pady=10)
        tk.Button(self.root, text="Alto (>1.000€)", command=lambda: self.save_response("Presupuesto", "Alto (>1.000€)")).pack(pady=10)
        tk.Button(self.root, text="Anterior", command=self.create_ecommerce_question).pack(pady=10)
    
    def save_response(self, category, response):
        self.responses[category] = response
        if category == "Presupuesto":
            self.create_knowledge_section()
        elif category == "Conocimiento":
            self.create_time_section()
        elif category == "Tiempo":
            self.create_customization_section()
        elif category == "Personalización":
            self.create_sales_duration_section()
        elif category == "Duración de ventas":
            self.create_reach_section()
        elif category == "Alcance":
            self.show_recommendation()

    def create_knowledge_section(self):
        self.clear_screen()
        
        tk.Label(self.root, text="¿Qué nivel de conocimiento tienes sobre creación de tiendas online?", font=('Arial', 18)).pack(pady=20)
        tk.Button(self.root, text="Ninguno", command=lambda: self.save_response("Conocimiento", "Ninguno")).pack(pady=10)
        tk.Button(self.root, text="Poco", command=lambda: self.save_response("Conocimiento", "Poco")).pack(pady=10)
        tk.Button(self.root, text="Medio (estoy aprendiendo)", command=lambda: self.save_response("Conocimiento", "Medio (estoy aprendiendo)")).pack(pady=10)
        tk.Button(self.root, text="Alto", command=lambda: self.save_response("Conocimiento", "Alto")).pack(pady=10)
        tk.Button(self.root, text="Anterior", command=self.create_budget_section).pack(pady=10)

    def create_time_section(self):
        self.clear_screen()
        
        tk.Label(self.root, text="¿Cuánto tiempo quieres invertir en la creación del sitio web?", font=('Arial', 18)).pack(pady=20)
        tk.Button(self.root, text="Una semana o menos", command=lambda: self.save_response("Tiempo", "Una semana o menos")).pack(pady=10)
        tk.Button(self.root, text="Entre una y dos semanas", command=lambda: self.save_response("Tiempo", "Entre una y dos semanas")).pack(pady=10)
        tk.Button(self.root, text="Más de dos semanas", command=lambda: self.save_response("Tiempo", "Más de dos semanas")).pack(pady=10)
        tk.Button(self.root, text="Anterior", command=self.create_knowledge_section).pack(pady=10)
    
    def create_customization_section(self):
        self.clear_screen()
        
        tk.Label(self.root, text="¿Qué nivel de personalización y diseño quieres que tenga tu tienda en línea?", font=('Arial', 18)).pack(pady=20)
        tk.Button(self.root, text="Reducido, me vale con seguir una plantilla", command=lambda: self.save_response("Personalización", "Reducido, me vale con seguir una plantilla")).pack(pady=10)
        tk.Button(self.root, text="Moderado, quiero personalizar alguna cosa", command=lambda: self.save_response("Personalización", "Moderado, quiero personalizar alguna cosa")).pack(pady=10)
        tk.Button(self.root, text="Elevado, quiero hacerlo todo a mi gusto", command=lambda: self.save_response("Personalización", "Elevado, quiero hacerlo todo a mi gusto")).pack(pady=10)
        tk.Button(self.root, text="Anterior", command=self.create_time_section).pack(pady=10)

    def create_sales_duration_section(self):
        self.clear_screen()
        
        tk.Label(self.root, text="¿Cuál es tu objetivo con la tienda online?", font=('Arial', 18)).pack(pady=20)
        tk.Button(self.root, text="Corto plazo, es algo que está de moda", command=lambda: self.save_response("Duración de ventas", "Corto plazo, es algo que está de moda")).pack(pady=10)
        tk.Button(self.root, text="Medio plazo, quiero venderlo durante un tiempo pero en unos años dejaré de hacerlo", command=lambda: self.save_response("Duración de ventas", "Medio plazo, quiero venderlo durante un tiempo pero en unos años dejaré de hacerlo")).pack(pady=10)
        tk.Button(self.root, text="Largo plazo, lo voy a vender siempre que sea posible", command=lambda: self.save_response("Duración de ventas", "Largo plazo, lo voy a vender siempre que sea posible")).pack(pady=10)
        tk.Button(self.root, text="No vendo un producto físico", command=self.find_platform_for_non_physical_product).pack(pady=10)
        tk.Button(self.root, text="Anterior", command=self.create_customization_section).pack(pady=10)
    
    def create_reach_section(self):
        self.clear_screen()
        
        tk.Label(self.root, text="¿Qué alcance esperas tener desde un principio?", font=('Arial', 18)).pack(pady=20)
        tk.Button(self.root, text="Limitado (necesito invertir en publicidad para darme a conocer)", command=lambda: self.save_response("Alcance", "Limitado (necesito invertir en publicidad para darme a conocer)")).pack(pady=10)
        tk.Button(self.root, text="Moderado (parto de una plataforma conocida que dispone de herramientas de marketing)", command=lambda: self.save_response("Alcance", "Moderado (parto de una plataforma conocida que dispone de herramientas de marketing)")).pack(pady=10)
        tk.Button(self.root, text="Significativo (voy a tener un alcance amplio y no me va a costar mucho dar a conocer mi producto)", command=lambda: self.save_response("Alcance", "Significativo (voy a tener un alcance amplio y no me va a costar mucho dar a conocer mi producto)")).pack(pady=10)
        tk.Button(self.root, text="Anterior", command=self.create_sales_duration_section).pack(pady=10)

    def show_promotion_tools(self):
        messagebox.showinfo("Herramientas de Promoción y Publicidad", "Aquí iría la información sobre herramientas de promoción y publicidad.")
    
    def find_best_platform(self):
        best_platform = None
        max_matches = -1
        
        for platform, attributes in PLATFORMS.items():
            matches = 0
            for key, values in attributes.items():
                if self.responses.get(key) in values:
                    matches += 1
            
            if matches > max_matches:
                max_matches = matches
                best_platform = platform
        
        return best_platform
    
    def find_platform_for_non_physical_product(self):
        # Evaluar las opciones disponibles
        options = {
            "Crear tu propia página web desde cero": ["Medio (500-1.000€)", "Medio (estoy aprendiendo)", "Alto", "Más de dos semanas", "Elevado (quiero hacerlo todo a mi gusto)", "Largo plazo, lo voy a vender siempre que sea posible", "No vendo un producto físico", "Limitado (necesito invertir en publicidad para darme a conocer)"],
            "Utilizar una plantilla web de un servicio que ofrece plantillas en línea": ["Bajo (<500€)", "Ninguno", "Poco", "Una semana o menos", "Entre una y dos semanas", "Reducido, me vale con seguir una plantilla", "Moderado, quiero personalizar alguna cosa", "Corto plazo, es algo que está de moda", "Medio plazo, quiero venderlo durante un tiempo pero en unos años dejaré de hacerlo", "No vendo un producto físico", "Limitado (necesito invertir en publicidad para darme a conocer)"],
            "Contratar a alguien para que te haga una página web": ["Alto (>1.000€)", "Ninguno", "Poco", "Entre una y dos semanas", "Más de dos semanas", "Moderado, quiero personalizar alguna cosa", "Elevado, quiero hacerlo todo a mi gusto", "Largo plazo, lo voy a vender siempre que sea posible", "No vendo un producto físico", "Limitado (necesito invertir en publicidad para darme a conocer)"]
        }

        # Encontrar la mejor opción
        best_platform = None
        max_matches = -1
        
        for platform, attributes in options.items():
            matches = 0
            for attr in attributes:
                if attr in self.responses.values():
                    matches += 1
            
            if matches > max_matches:
                max_matches = matches
                best_platform = platform

        if best_platform:
            self.show_recommendation_for_non_physical_product(best_platform)
        else:
            messagebox.showinfo("Recomendación", "No se pudo encontrar una recomendación adecuada.")

    def show_recommendation_for_non_physical_product(self, platform):
        self.clear_screen()
        
        tk.Label(self.root, text="Basado en tus respuestas, te recomendamos la siguiente opción:", font=('Arial', 18)).pack(pady=20)
        tk.Label(self.root, text=f"Te recomendamos: {platform}", font=('Arial', 16)).pack(pady=20)
        
        tk.Button(self.root, text="Información adicional", command=self.show_additional_info).pack(pady=10)
        tk.Button(self.root, text="Información de las plataformas", command=self.show_platform_info).pack(pady=10)
        tk.Button(self.root, text="Siguiente", command=self.create_promotion_tools_section).pack(pady=10)
        tk.Button(self.root, text="Anterior", command=self.create_sales_duration_section).pack(pady=10)
    
    def show_recommendation(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Basado en tus respuestas, te recomendamos la siguiente opción:", font=('Arial', 18)).pack(pady=20)
        
        best_platform = self.find_best_platform()
        if best_platform:
            tk.Label(self.root, text=f"Te recomendamos: {best_platform}", font=('Arial', 16)).pack(pady=20)
        else:
            tk.Label(self.root, text="No se pudo encontrar una recomendación adecuada.", font=('Arial', 16)).pack(pady=20)
        
        tk.Button(self.root, text="Información adicional", command=self.show_additional_info).pack(pady=10)
        tk.Button(self.root, text="Información de las plataformas", command=self.show_platform_info).pack(pady=10)
        tk.Button(self.root, text="Siguiente", command=self.create_promotion_tools_section).pack(pady=10)
        tk.Button(self.root, text="Anterior", command=self.create_reach_section).pack(pady=10)

    def show_additional_info(self):
        messagebox.showinfo("Información Adicional", "Pese a que se te ha recomendado un tipo de plataforma en base a tus preferencias, se recomienda que hagas clic en el botón de “Información de las plataformas” y leas en qué consiste cada una, ya que, tu idea de negocio también puede ser compatible con las demás. Más información disponible en el TFG: Guía para emprendedores: Decálogo del uso de herramientas digitales en el comercio electrónico.")
    
    def show_platform_info(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Información sobre las plataformas:", font=('Arial', 18)).pack(pady=20)
        
        tk.Button(self.root, text="Sistemas de Gestión de Contenidos (CMS)", command=lambda: self.show_platform_detail("CMS")).pack(pady=10)
        tk.Button(self.root, text="Plataformas de Comercio Electrónico", command=lambda: self.show_platform_detail("Plataformas de Comercio Electrónico")).pack(pady=10)
        tk.Button(self.root, text="Constructores de Sitios Web", command=lambda: self.show_platform_detail("Constructores de Sitios Web")).pack(pady=10)
        tk.Button(self.root, text="Marketplaces", command=lambda: self.show_platform_detail("Marketplaces")).pack(pady=10)
        
        tk.Button(self.root, text="Anterior", command=self.show_recommendation).pack(pady=10)

    def show_platform_detail(self, category):
        if category == "CMS":
            detail = "Sistemas de Gestión de Contenidos (CMS): Software que permite crear, gestionar y modificar contenido en un sitio web. Facilita la administración de contenido web y, a veces, el comercio electrónico. Ejemplos: WordPress y Joomla."
        elif category == "Plataformas de Comercio Electrónico":
            detail = "Plataformas de Comercio Electrónico: Servicios que permiten crear y gestionar tiendas en línea sin necesidad de conocimientos técnicos avanzados. Facilita la venta de productos o servicios en internet. Ejemplos: Shopify y PrestaShop."
        elif category == "Constructores de Sitios Web":
            detail = "Constructores de Sitios Web: Herramientas que permiten crear sitios web mediante la selección de plantillas y arrastrar y soltar elementos. Facilita la creación rápida de sitios web sin necesidad de programación. Ejemplos: Wix y Zyro."
        elif category == "Marketplaces":
            detail = "Marketplaces: Plataformas en línea donde los vendedores pueden listar y vender productos junto a otros vendedores. Permite a los vendedores acceder a una base de clientes amplia y preexistente. Ejemplos: Amazon y eBay."
        else:
            detail = "Información no disponible."
        
        messagebox.showinfo(category, detail)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

