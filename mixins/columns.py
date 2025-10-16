#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-06 13:46:25
# @Author  : Dahir Muhammad Dahir
# @Description : taken from Bill's template codebase


from datetime import date
from typing import Any
from uuid_utils import uuid7

import inflect

from sqlalchemy import DateTime, String, Date
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql.functions import func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date as dt, datetime

get_plural = inflect.engine()


def get_uuid() -> str:
    return uuid7().hex


class BaseMixin:
    __allow_unmapped__ = True
    """
    Provides id, created_at and last_modified columns
    """

    @declared_attr  # type: ignore
    def __tablename__(cls: Any) -> str:
        try:
            cls.__tablename__
        except RecursionError:
            pass
        plural_name: str = get_plural.plural_noun(cls.__name__.lower())
        return plural_name

    uuid: Mapped[str] = mapped_column(
        String(length=50), primary_key=True, default=get_uuid
    )
    date: Mapped[dt | None] = mapped_column(
        Date,
        index=True,
        default=date.today,
        nullable=True,
        server_default=func.current_date(),
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, index=True, server_default=func.now(), nullable=False
    )
    last_modified: Mapped[datetime] = mapped_column(
        DateTime,
        index=True,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


class BaseImportMixin:
    __allow_unmapped__ = True
    """
    Provides id, created_at and last_modified columns
    """

    @declared_attr  # type: ignore
    def __tablename__(cls: Any) -> str:
        try:
            cls.__tablename__
        except RecursionError:
            pass
        plural_name: str = get_plural.plural_noun(cls.__name__.lower())
        return plural_name

    uuid: Mapped[str] = mapped_column(
        String(length=50), primary_key=True, default=get_uuid
    )
    date: Mapped[dt | None] = mapped_column(
        Date,
        index=True,
        default=date.today,
        nullable=True,
        server_default=func.current_date(),
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, index=True, server_default=func.now(), nullable=False
    )
    last_modified: Mapped[datetime] = mapped_column(
        DateTime,
        index=True,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


class BaseUACMixin(BaseMixin):
    """
    Defines common columns for user access control models
    """

    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(String(255))


class BaseModelMixin(BaseMixin):
    """
    Defines common columns for models
    """

    pass
