#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-06 14:32:47
# @Author  : Dahir Muhammad Dahir
# @Description : Based on bills fastapi template

from enum import Enum
from config.database import Base
from mixins.columns import BaseMixin
from utils.custom_validators import Money
from utils.enums import ActionStatus
from datetime import datetime
from typing import Any, TypeVar, Generic
from pydantic import BaseModel, EmailStr, ConfigDict, computed_field


T = TypeVar("T")


class _SQLModel(BaseMixin, Base): ...


SQLModel = TypeVar("SQLModel", bound=_SQLModel)

class BaseSchemaMixin(BaseModel):
    uuid: str
    created_at: datetime
    last_modified: datetime

    model_config = ConfigDict(from_attributes=True)


class BaseUACSchemaMixin(BaseSchemaMixin):
    name: str
    description: str | None = None


class UserMin(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    email: EmailStr
    firstname: str
    lastname: str
    middlename: str | None = ""


class Processor(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    email: EmailStr
    firstname: str
    lastname: str
    middlename: str | None = ""


class BaseModelOut(BaseSchemaMixin):
    pass
    # created_by: str

    # creator: UserMin


class BaseModelMin(BaseSchemaMixin):
    pass


class BaseModelIn(BaseModel):
    model_config = ConfigDict(str_max_length=6144)


class BaseModelPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class OrderType(str, Enum):
    asc = "asc"
    desc = "desc"


class BaseModelFilter(BaseModelIn):
    model_config = ConfigDict(str_to_upper=False)
    skip: int = 0
    limit: int = 10
    order: OrderType = OrderType.asc


class JoinSearch(BaseModel):
    model: Any
    column: str
    onkey: str


class BaseModelSearch(BaseModelIn):
    model_config = ConfigDict(str_to_upper=False)
    search_term: str
    skip: int = 0
    limit: int = 10
    order: OrderType = OrderType.asc

    @computed_field
    @property
    def search_fields(self) -> list[str]:
        return []

    @computed_field
    @property
    def join_search(self) -> list[JoinSearch]:
        return []


class BaseModelCreate(BaseModel):
    created_by: str


class Status(BaseModel):
    status: ActionStatus


class PagedResult(BaseModel, Generic[T]):
    count: int
    sum: Money | None = None
    data: list[T]


class ResultBase(BaseModel):
    count: int
    sum: Money | None = None


class OperationResult(BaseModel):
    status: ActionStatus
    message: str


class BulkOperationResult(OperationResult):
    success_count: int = 0
    failed_count: int = 0
    total_count: int = 0


class DeletionResult(OperationResult):
    pass


class CreationResult(OperationResult, Generic[T]):
    data: T


class UpdateResult(OperationResult, Generic[T]):
    data: T
