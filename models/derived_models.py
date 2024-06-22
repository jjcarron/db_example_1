from models.models import TableXXX as Base_XXX, TableZZZ as Base_ZZZ
from base import Base as Root_Base

class XXX(Base_XXX):
    def __init__(self, extra):
        super().__init__()
        self.name = self.__tablename__
        self.extra = extra


class ZZZ(Base_ZZZ):
    def __init__(self,  extra):
        super().__init__()
        self.extra = extra

    def display(self):
        # Add code to display all attributes
        for attr, value in self.__dict__.items():
            if not attr.startswith('_sa_'):  # Exclude SQLAlchemy internal attributes
                print(f"{attr}: {value}")