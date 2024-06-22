from sqlalchemy.orm import Session
from db.db import get_db, engine
from models.models import BaseModel, AnotherBaseModel, Base
from db.crud import CRUDRepository


# Create the database tables
Base.metadata.create_all(bind=engine)

def main():
    # Getting a session
    db: Session = next(get_db())

    # Create repository instances for each model
    base_model_repo = CRUDRepository(BaseModel)
    another_base_model_repo = CRUDRepository(AnotherBaseModel)

    # Create instances of the models
    base_model = BaseModel("Base Name")
    another_base_model = AnotherBaseModel("Attribute Value")

    # Add and commit the models to the database using the CRUD repository
    base_model_repo.create(db, base_model)
    another_base_model_repo.create(db, another_base_model)

    # Display the information of the models
    base_model.display()
    another_base_model.display()

if __name__ == "__main__":
    main()
