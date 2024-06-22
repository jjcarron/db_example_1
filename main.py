from sqlalchemy.orm import Session
from db import get_db, engine
from models import Base, TableXXX
from repositories.table_xxx_repository import TableXXXRepository

# Create the database tables
Base.metadata.create_all(bind=engine)

def main():
    # Getting a session
    db: Session = next(get_db())

    # Créer des instances des dépôts
    table_xxx_repo = TableXXXRepository()

    # Creating a new record in TableXXX
    new_xxx = TableXXX(name="New Record")
    created_xxx = table_xxx_repo.create(db, new_xxx)
    print(f"Added: ID: {created_xxx.id}, Name: {created_xxx.name}")

    # Finding a record by name in TableXXX
    found_xxx = table_xxx_repo.find_by_name(db, "New Record")
    if found_xxx:
        print(f"Found by name: ID: {found_xxx.id}, Name: {found_xxx.name}")

    # Getting a record from TableXXX
    record_xxx = table_xxx_repo.get(db, created_xxx.id)
    if record_xxx:
        print(f"Fetched: ID: {record_xxx.id}, Name: {record_xxx.name}")

    # Updating a record in TableXXX
    updated_data = {"name": "Updated Record"}
    updated_record_xxx = table_xxx_repo.update(db, created_xxx.id, updated_data)
    if updated_record_xxx:
        print(f"Updated: ID: {updated_record_xxx.id}, Name: {updated_record_xxx.name}")

    # Deleting a record from TableXXX
    deleted_record_xxx = table_xxx_repo.delete(db, created_xxx.id)
    if deleted_record_xxx:
        print(f"Deleted: ID: {deleted_record_xxx.id}, Name: {deleted_record_xxx.name}")

if __name__ == "__main__":
    main()
