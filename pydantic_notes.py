# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: notebooks
#     language: python
#     name: python3
# ---

# %%
from pydantic import BaseModel, ConfigDict, constr, RootModel
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import declarative_base


# %%

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime = None
    friends: list[int] = []


# %%
user_1 = User(id=1, signup_ts='2017-06-01 12:22', friends=[2, '3', b'4'])

# %%
user_1.model_dump()

# %%
user_1.model_fields_set

# %%
Base = declarative_base()


# %%
class CompanyOrm(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)
    domains = Column(ARRAY(String(255)))


# %%



class CompanyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    public_key: constr(max_length=20)
    name: constr(max_length=63)
    domains: list[constr(max_length=255)]



# %%
co_orm = CompanyOrm(
    id=123,
    public_key='foobar',
    name='Testing',
    domains=['example.com', 'foobar.com'],
)


# %%
co_orm

# %%
co_model = CompanyModel.model_validate(co_orm)
co_model


# %%
class Pets(RootModel):
    root: list[str]

    def __iter__(self):
        return iter(self.root)
    
    def __getitem__(self, item):
        return self.root[item]


pets = Pets.model_validate(['dog', 'cat', 'goldfish'])
pets

# %%
pets[0]

# %%
for pet in pets:
    print(pet)

# %%
