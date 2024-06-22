from typing import Optional
from sqlalchemy.orm import Session
from models import TableZZZ
from repositories.base import CRUDRepository

class TableZZZRepository(CRUDRepository[TableZZZ]):
    def __init__(self):
        super().__init__(TableZZZ)

    # Ajouter des fonctionnalités spécifiques à TableZZZ ici
    def find_by_fk(self, db: Session, xxx_fk: int) -> Optional[TableZZZ]:
        return db.query(self.model).filter(self.model.xxx_fk == xxx_fk).first()
