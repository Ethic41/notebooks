#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-24 00:40:54
# @Author  : Dahir Muhammad Dahir
# @Description : something cool

from utils.custom_validators import UpStr
from enum import Enum
from typing import Any


from mixins.schemas import BaseSchemaMixin
from pydantic import BaseModel, ConfigDict, EmailStr, field_validator
from datetime import date


class Gender(str, Enum):
    male = "m"
    female = "f"
    na = "na"


class UserOut(BaseSchemaMixin):
    model_config = ConfigDict(from_attributes=True)

    email: EmailStr
    firstname: UpStr
    lastname: UpStr
    middlename: UpStr | None = ""
    is_active: bool
    is_system_user: bool


class DateRange(BaseModel):
    column_name: str = "date"
    from_date: date
    to_date: date


class FilterBase(BaseModel):
    skip: int
    limit: int


class UserMin(BaseSchemaMixin):
    email: str
    firstname: UpStr
    lastname: UpStr
    middlename: UpStr | None = ""
    phone: str | None


class UserPublic(BaseModel):
    uuid: str
    email: str
    firstname: UpStr
    lastname: UpStr
    middlename: UpStr | None = ""
    phone: str | None

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: Any):
        # obfuscate parts of the email with asterisks
        email_parts = value.split("@")
        email_parts[0] = email_parts[0][:5] + "*" * (len(email_parts[0]) - 5)
        email_parts[1] = email_parts[1][:5] + "*" * (len(email_parts[1]) - 5)
        return "@".join(email_parts)

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value: Any):
        # obfuscate the middle part of the phone with asterisks
        return value[:5] + "*" * (len(value) - 5) + value[-2:]


class Token(BaseModel):
    access_token: str
    token_type: str
    user_group: str | None = ""
    permissions: list[str] | None = None
