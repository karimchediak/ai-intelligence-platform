import os
from dataclasses import dataclass
@dataclass(frozen=True)
class Settings:
 api_key:str=os.getenv('AEGIS_API_KEY','')
 environment:str=os.getenv('AEGIS_ENV','development')
settings=Settings()
