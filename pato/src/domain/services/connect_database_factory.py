from domain.models.database_settings import DatabaseSettings
from domain.services.database_controller_factory import DatabaseControllerFactory

class ConnectDatabaseFactory: #criu uma class 
    def call(self, database_settings: DatabaseSettings) -> DatabaseControllerFactory: #criou uma def e nos parametros, tem o self e o database_settings que tem o type de DatabaseSettings que vai ser passado para o call.return DatabaseControllerFactory
        raise NotImplementedError()  #criou uma raise NotImplementedError pra nao dar error pq o codigo vai ser implementado dps 