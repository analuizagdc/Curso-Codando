from domain.services.database_controller import DatabaseController

class DatabaseControllerFactory:
    def call(self) -> DatabaseController:   #criou uma def para retornar o DatabaseController
        raise NotImplementedError()    #criou uma raise NotImplementedError pra nao dar error pq o codigo vai ser implementado dps 
    