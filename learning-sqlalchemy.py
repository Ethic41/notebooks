# %%
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2024-10-15 17:07:17
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0
# Generated with: jupytext --to py:percent learning-sqlalchemy.ipynb

from typing import Any
from mixins.schemas import DeletionResult, PagedResult
from config.database import db_session_manager as db
from utils.crud_util import CrudUtil
import models
import schemas
from faker import Faker

fake = Faker()

# %%


async def create_faculty(name: str) -> models.Faculty:
    async with db.session() as session:
        cu: CrudUtil = CrudUtil(session)

        faculty = schemas.FacultyIn(name=name)
        db_faculty: models.Faculty = await cu.create_model(models.Faculty, faculty)
        return db_faculty


async def create_department(name: str, faculty_id: str) -> models.Department:
    async with db.session() as session:
        cu: CrudUtil = CrudUtil(session)

        department = schemas.DepartmentIn(name=name, faculty_id=faculty_id)
        db_department: models.Department = await cu.create_model(
            models.Department, department
        )
        return db_department


async def create_user(user: schemas.UserCreate) -> models.User:
    async with db.session() as session:
        cu: CrudUtil = CrudUtil(session)

        db_user: models.User = await cu.create_model(models.User, user)
        return db_user


async def get_faculty_by_id(faculty_id: str) -> models.Faculty | None:
    async with db.session() as session:
        cu: CrudUtil = CrudUtil(session)
        db_faculty = await cu.get_model_or_none(
            models.Faculty, {"faculty_id": faculty_id}
        )

        return db_faculty


async def get_department_by_id(department_id: str) -> models.Department | None:
    async with db.session() as session:
        cu: CrudUtil = CrudUtil(session)
        db_department = await cu.get_model_or_none(
            models.Department, {"department_id": department_id}
        )

        return db_department


async def get_user_by_id(user_id: str) -> models.User | None:
    async with db.session() as session:
        cu: CrudUtil = CrudUtil(session)
        db_user = await cu.get_model_or_none(models.User, {"user_id": user_id})

        return db_user


async def get_all_faculties() -> list[models.Faculty]:
    async with db.session() as session:
        cu: CrudUtil = CrudUtil(session)
        db_faculties: PagedResult[models.Faculty] = await cu.list_model(models.Faculty)
        return db_faculties.data


async def get_all_departments() -> list[models.Department]:
    async with db.session() as session:
        cu: CrudUtil = CrudUtil(session)
        db_departments: PagedResult[models.Department] = await cu.list_model(
            models.Department
        )
        return db_departments.data


async def get_all_users() -> list[models.User]:
    async with db.session() as session:
        cu: CrudUtil = CrudUtil(session)
        db_users: PagedResult[models.User] = await cu.list_model(models.User)
        return db_users.data


async def delete_faculty(faculty_id: str, autocommit: bool = True) -> DeletionResult:
    async with db.session() as session:
        cu: CrudUtil = CrudUtil(session)
        return await cu.delete_model(
            models.Faculty, {"uuid": faculty_id}, autocommit=autocommit
        )


async def delete_all_faculties() -> DeletionResult:
    async with db.session() as session:
        cu: CrudUtil = CrudUtil(session)
        return await cu.delete_model(models.Faculty, {})


async def delete_department(department_id: str) -> DeletionResult:
    async with db.session() as session:
        cu: CrudUtil = CrudUtil(session)
        return await cu.delete_model(models.Department, {"uuid": department_id})


async def delete_all_departments() -> DeletionResult:
    async with db.session() as session:
        cu: CrudUtil = CrudUtil(session)
        return await cu.delete_model(models.Department, {})


async def delete_user(user_id: str) -> DeletionResult:
    async with db.session() as session:
        cu: CrudUtil = CrudUtil(session)
        return await cu.delete_model(models.User, {"uuid": user_id})


async def delete_all_users() -> DeletionResult:
    async with db.session() as session:
        cu: CrudUtil = CrudUtil(session)
        return await cu.delete_model(models.User, {})


# %%
# We will create fake data here


async def generate_faculties(count: int = 4) -> list[dict[str, Any]]:
    faculties: list[dict[str, Any]] = []

    for _ in range(count):
        faculty_name = f"Faculty of {fake.word().title()}"
        faculties.append({"name": faculty_name, "departments": []})

    return faculties


async def generate_departments(
    faculties: list[dict[str, Any]], departments_per_faculty: int = 3
) -> list[dict[str, Any]]:
    for faculty in faculties:
        for _ in range(departments_per_faculty):
            department_name = f"Department of {fake.word().title()}"
            faculty["departments"].append({"name": department_name})

    return faculties


async def gen_phone():
    return "0" + fake.basic_phone_number().replace("-", "").replace("(", "").replace(
        ")", ""
    )


async def generate_users(count: int = 10) -> list[schemas.UserCreate]:
    users: list[schemas.UserCreate] = []

    for _ in range(count):
        user = schemas.UserCreate(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            middlename=fake.first_name(),
            email=fake.email(),
            phone=await gen_phone(),
        )

        users.append(user)

    return users


# %%
# Seed the data


async def seed_users():
    users = await generate_users(10)
    for user in users:
        db_user = await create_user(user)
        print(f"Created User: {db_user}")


async def seed_faculties_and_departments():
    faculties = await generate_faculties(4)
    faculties_with_departments = await generate_departments(faculties, 3)
    for faculty_data in faculties_with_departments:
        db_faculty = await create_faculty(faculty_data["name"])
        print(f"Created Faculty: {db_faculty}")

        for department_data in faculty_data["departments"]:
            db_department = await create_department(
                department_data["name"], db_faculty.uuid
            )
            print(f"  Created Department: {db_department}")


async def seed_all():
    await seed_faculties_and_departments()
    await seed_users()


# %%
await seed_all()  # noqa # type: ignore

# %%
faculties = await get_all_faculties()  # noqa # type: ignore

# %%
faculty_schemas = [schemas.FacultyOut.model_validate(faculty) for faculty in faculties]


for faculty in faculties:
    for department in faculty.departments:
        print(f"Faculty: {faculty.name}, Department: {department.name}")
    print("-----")

# %%
departments = await get_all_departments()  # noqa # type: ignore

# %%
departments_schemas = [
    schemas.DepartmentOut.model_validate(dept) for dept in departments
]
# for ds in departments_schemas:
#     print(ds)

for dept in departments:
    print(
        f"Department: {dept.name}, Faculty ID: {dept.faculty_id}, Faculty Name: {dept.faculty.name}"
    )

# %%
users = await get_all_users()  # noqa # type: ignore
for user in users:
    print(f"User: {user.firstname} {user.lastname} {user.email} {user.fullname}")

# %%
# Delete a faculty
# result = await delete_faculty("0199ecacf2f6788095e61212076ea57e", autocommit=False)

# Delete all faculties
# result = await delete_all_faculties()


# %%
