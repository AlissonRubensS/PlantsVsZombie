class Material:
    def __init__(self, difuso, especular, ambiente, brilho):
        self.coeficiente_difuso = difuso
        self.coeficiente_especular = especular
        self.coeficiente_ambiente = ambiente
        self.brilho = brilho