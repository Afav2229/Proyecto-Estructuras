from bigtree import Node, print_tree, find_name, find_names, tree_to_dict

class SistemaTuristicoSantander:
    def __init__(self):
       
        self.raiz = Node("Aeropuerto Palonegro")
        self.municipios_principales = [
            "Bucaramanga", "Girón", "Floridablanca", 
            "Piedecuesta", "Lebrija"
        ]
        
        
        self._inicializar_estructura()
        
    def _inicializar_estructura(self):
       
        for municipio in self.municipios_principales:
            Node(municipio, parent=self.raiz)