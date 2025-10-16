#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2025-10-15 20:06:49
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from sqlalchemy import ForeignKey, String, Boolean, Table, Column
from sqlalchemy.orm import relationship, Mapped, mapped_column
from config.database import Base
from mixins.columns import BaseModelMixin, BaseMixin, BaseUACMixin


# Many to Many associations
permission_role = Table(
    "permission_role",
    Base.metadata,
    Column("permission_id", String(length=50), ForeignKey("permissions.uuid")),
    Column("role_id", String(length=50), ForeignKey("roles.uuid")),
)
role_group = Table(
    "role_group",
    Base.metadata,
    Column("role_id", String(length=50), ForeignKey("roles.uuid")),
    Column("group_id", String(length=50), ForeignKey("groups.uuid")),
)

user_group = Table(
    "user_group",
    Base.metadata,
    Column("group_id", String(length=50), ForeignKey("groups.uuid")),
    Column("user_id", String(length=50), ForeignKey("users.uuid")),
)


class Permission(BaseUACMixin, Base):
    pass


class Role(BaseUACMixin, Base):
    permissions: Mapped[list["Permission"]] = relationship(
        "Permission", secondary=permission_role
    )


class Group(BaseUACMixin, Base):
    roles: Mapped[list["Role"]] = relationship("Role", secondary=role_group)


class User(BaseMixin, Base):
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    old_password_hash: Mapped[str | None] = mapped_column(String(255))
    temp_password_hash: Mapped[str] = mapped_column(
        String(255), nullable=True, default=None
    )
    firstname: Mapped[str] = mapped_column(String(255))
    lastname: Mapped[str] = mapped_column(String(255))
    middlename: Mapped[str | None] = mapped_column(String(255))
    fullname: Mapped[str] = mapped_column(
        String(255), nullable=True, default=None, server_default=None
    )
    phone: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    is_active: Mapped[bool | None] = mapped_column(Boolean, default=True)
    is_admin: Mapped[bool] = mapped_column(
        Boolean, default=False, server_default="0", nullable=False
    )
    can_login: Mapped[bool] = mapped_column(
        Boolean, default=True, server_default="1", nullable=False
    )
    is_temp_email: Mapped[bool] = mapped_column(
        Boolean, default=False, server_default="0", nullable=False
    )
    is_temp_phone: Mapped[bool] = mapped_column(
        Boolean, default=False, server_default="0", nullable=False
    )

    groups: Mapped[list["Group"]] = relationship(
        "Group", secondary=user_group, uselist=True, lazy="joined"
    )


class Faculty(BaseModelMixin, Base):
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    display_name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    departments: Mapped[list["Department"]] = relationship(
        "Department",
        back_populates="faculty",
        lazy="selectin",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class Department(BaseModelMixin, Base):
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    faculty_id: Mapped[str] = mapped_column(
        String(45), ForeignKey("faculties.uuid", ondelete="CASCADE"), nullable=False
    )
    display_name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    faculty: Mapped["Faculty"] = relationship(
        "Faculty",
        back_populates="departments",
        lazy="joined",
        foreign_keys=[faculty_id],
    )
