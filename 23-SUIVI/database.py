

class dbase:
    """


    """
    def __init__(self, p_base_name):
               
        self.base_name = p_base_name

        print("Création d'une instance dbase {}".format(self.base_name))        

    def base_open( self):
        pass


    def base_close(self):
        pass


    def student_add(self, classe_name, student_name):
        pass

    def student_delete(self, student_name):
        pass

    def student_get( self,  sql):
        pass

    def student_update( self, sql ):
        pass

    
    
    def sequence_add(self, sequence_name):
        pass

    def sequence_delete( self, sequence_name):
        pass


    def sequence_get( self,  sql):
        pass

    def sequence_update( self, sql ):
        pass


    def seance_add(self, seance_name):
        pass

    def seance_delete(self, seance_add):
        pass


    def seance_get( self,  sql):
        pass

    def seance_update( self, sql ):
        pass
    

print("Hello world !")
B= dbase("PROGRESSION-202223.DB")
