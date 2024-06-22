from typing import Optional
from sqlalchemy.orm import Session
from models.derived_models import XXX
from repositories.crud import CRUDRepository

class TableXXXRepository(CRUDRepository[XXX]):
    def __init__(self):
        super().__init__(XXX)

    # Ajouter des fonctionnalités spécifiques à TableXXX ici
    def find_by_name(self, db: Session, name: str) -> Optional[XXX]:
        return db.query(self.model).filter(self.model.name == name).first()

