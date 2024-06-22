from typing import Optional
from sqlalchemy.orm import Session
from models import ZZZ
from repositories.crud import CRUDRepository

class TableZZZRepository(CRUDRepository[ZZZ]):
    def __init__(self):
        super().__init__(ZZZ)

    # Ajouter des fonctionnalités spécifiques à TableZZZ ici
    def find_by_fk(self, db: Session, xxx_fk: int) -> Optional[TableZZZ]:
        return db.query(self.model).filter(self.model.xxx_fk == xxx_fk).first()
