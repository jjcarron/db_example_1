from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic, List, Optional, Dict, Any
from models.models import Base

T = TypeVar('T', bound=Base)

class CRUDRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    def create(self, db: Session, obj_in: T) -> T:
        db.add(obj_in)
        db.commit()
        db.refresh(obj_in)
        return obj_in

    def get(self, db: Session, id: int) -> Optional[T]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session) -> List[T]:
        return db.query(self.model).all()

    def update(self, db: Session, id: int, obj_in: Dict[str, Any]) -> Optional[T]:
        db_obj = db.query(self.model).filter(self.model.id == id).first()
        if not db_obj:
            return None
        for key, value in obj_in.items():
            if key != "id" and value is not None:
                setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, id: int) -> Optional[T]:
        db_obj = db.query(self.model).filter(self.model.id == id).first()
        if not db_obj:
            return None
        db.delete(db_obj)
        db.commit()
        return db_obj
