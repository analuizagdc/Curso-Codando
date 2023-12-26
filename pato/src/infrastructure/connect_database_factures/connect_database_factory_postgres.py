
class ConnectDataBaseFactoryPostgres(ConnectDataBaseFactory): #criou uma class e esta herdando o connectDataBaseFactory
    def call (self, database_settings: DatabaseSettings) -> DatabaseControllerFactory:
        pass
    
#como a class esta herdando o connectDataBaseFactory, a estrutura tem que ser a mesma, e é isso que ta sendo feito aqui 