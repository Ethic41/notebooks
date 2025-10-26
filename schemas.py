#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2025-10-15 22:26:15
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    computed_field,
)
from mixins.schemas import (
    BaseModelIn,
    BaseModelCreate,
    BaseModelFilter,
    BaseModelSearch,
    BaseModelOut,
    PagedResult,
)
from utils.custom_validators import CapStr, UpStr
from faker import Faker


# ========[ Fake ]========

fake = Faker()


# ====================[ Faculty ]====================


class FacultyIn(BaseModelIn):
    name: UpStr

    @computed_field
    @property
    def display_name(self) -> str:
        return f"{self.name}"


class FacultyCreate(BaseModel):
    name: UpStr
    display_name: UpStr


class FacultyUpdate(BaseModelIn):
    name: UpStr | None = None

    @computed_field
    @property
    def display_name(self) -> str | None:
        return f"{self.name}" if self.name else None


class FacultyFilter(BaseModelFilter):
    name: UpStr | None = None


class FacultySearch(BaseModelSearch):
    @computed_field
    @property
    def search_fields(self) -> list[str]:
        return ["name"]


class FacultyOut(BaseModelOut):
    name: UpStr
    display_name: UpStr

    departments: list["DepartmentOut"]


class FacultyMin(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    uuid: str
    name: UpStr
    display_name: UpStr


class FacultyPublic(BaseModel):
    uuid: str
    name: UpStr
    display_name: UpStr


class FacultyList(PagedResult):
    data: list[FacultyMin]


# ====================[ Department ]====================


class DepartmentIn(BaseModelIn):
    name: UpStr
    faculty_id: str

    @computed_field
    @property
    def display_name(self) -> str:
        return f"{self.name}"


class DepartmentCreate(BaseModelCreate):
    name: UpStr
    faculty_id: str
    display_name: UpStr


class DepartmentUpdate(BaseModelIn):
    name: UpStr | None = None
    faculty_id: str | None = None

    @computed_field
    @property
    def display_name(self) -> str | None:
        return f"{self.name}" if self.name else None


class DepartmentFilter(BaseModelFilter):
    name: UpStr | None = None
    faculty_id: str | None = None


class DepartmentSearch(BaseModelSearch):
    @computed_field
    @property
    def search_fields(self) -> list[str]:
        return ["name"]


class DepartmentOut(BaseModelOut):
    name: UpStr
    faculty_id: str
    display_name: UpStr

    faculty: FacultyMin


class DepartmentMin(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    uuid: str
    name: UpStr
    display_name: UpStr
    faculty_id: str

    faculty: FacultyMin


class DepartmentPublic(BaseModel):
    uuid: str
    name: UpStr
    display_name: UpStr


class DepartmentList(PagedResult):
    data: list[DepartmentMin]


class DepartmentPublicList(PagedResult):
    data: list[DepartmentPublic]


class UserCreate(BaseModel):
    email: EmailStr
    firstname: CapStr
    lastname: CapStr
    middlename: CapStr | None = None
    phone: str

    @computed_field
    @property
    def password_hash(self) -> str:
        return fake.sha256()
