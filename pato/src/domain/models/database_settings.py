from dataclasses import dataclass

@dataclass      # Aqui uma data class está sendo adicionada pra class que estiver embaixo so ter a funcao de armazenar os dados
class DatabaseSettings:  #criou uma class chamada DatabaseSettings pra tipar os dados
    host: str
    port: int
    user: str
    password: str
    database_name: str
    
    