import unittest
from zookeeper import Ztree

class TestZookeeper(unittest.TestCase):


    #Prueba para verificar si manda excepción al crear nodos con el mismo nombre en el misma path
    def test_nodo_mismo_nombre(self): ##APRUEBA
        with self.assertRaises(Exception):
            tree_1 = Ztree()
            tree_2.create('/Amazon', 'contenido', False, True, 0, '/')

            tree_2 = Ztree()
            tree_2.create('/Amazon', 'contenido', False, True, 0, '/')

    #Prueba para verificar si el deadtime admite valores negativos
    def test_deadtime_negativo(self): ##FALLA (No arroja excepcion)
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/Uber', 'Contenido', True, True, -10, '/')
    
    #Prueba para verificar los valores de estado onservice
    def test_estado_activo(self): ##FALLA (No arroja excepcion)
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/Didi', 'Contenido', 'String', 'String', 15, '/')
            tree.delete('/Didi', 0)

    #Prueba para verificar un manejo correcto de simbolos en el path
    def test_prueba_nombres_simbolos(self): #APRUEBA
        tree_2 = Ztree()
        tree_2.create('"/%/%/"', 'Contenido2', False, True, 0, '/')
        self.assertEqual(tree_2.getData('"/%/%/"'), 'Contenido2')

    #Prueba para verificar si encuentra un nodo de forma correcta 
    def test_prueba_buscar_nodo(self): #APRUEBA
        tree_1 = Ztree()
        tree_1.create('/Google', 'Contenido', False, True, 0, '/')
        self.assertTrue(tree_1.exist('/Google'))
        tree_1.delete('/Google', 0)
        self.assertFalse(tree_1.exist('/Google'))

if __name__ == '__main__':
    unittest.main()

