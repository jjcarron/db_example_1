from typing import Optional
from sqlalchemy.orm import Session
from models import TableXXX
from repositories.base import CRUDRepository

class TableXXXRepository(CRUDRepository[TableXXX]):
    def __init__(self):
        super().__init__(TableXXX)

    # Ajouter des fonctionnalités spécifiques à TableXXX ici
    def find_by_name(self, db: Session, name: str) -> Optional[TableXXX]:
        return db.query(self.model).filter(self.model.name == name).first()

