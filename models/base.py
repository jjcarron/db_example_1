from sqlalchemy.ext.declarative import as_declarative

@as_declarative()
class Extended_Base:
    id = None
    __name__: str

    def display(self):
        print(f"{self.__class__.__name__}:")
        for attr, value in self.__dict__.items():
            if not attr.startswith('_sa_'):  # Exclude SQLAlchemy internal attributes
                print(f"  {attr}: {value}")
