from domain.services.connect_database_factory import ConnectDatabaseFactory
from domain.services.database_controller import DatabaseController
from domain.models.database_settings import DatabaseSettings

class GetDatabaseController:
    def __init__(self, connect_database_factory: ConnectDatabaseFactory):  #Criou a classe e criiu parametros 
        self.connect_database_factory = connect_database_factory # o self ta fazendo com que nao seja necessario usar uma  variavel local, e tambem o valor esta sendo atribuido ao connect_database_factory
    
    def call(self, database_settings: DatabaseSettings) -> DatabaseController:  #criou uma def com o nome de call e recebe um parametro (database_settings) do tipo DatabaseSettings e retorna uma DatabaseController  
       database_controller_factory =  self.connect_database_factory.call(database_settings) #
       database_controller = database_controller_factory.call()
       return database_controller
   
#as duas ultimas linhas, o database_controller esta criando uma instancia de databasecontrollerfactory que ta chamando o metodo call dele mesmo o objeto que ta sendo retornado vai ser armaezado na variavel database_controller.