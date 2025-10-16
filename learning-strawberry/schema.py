#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2025-09-25 13:16:32
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0

import strawberry
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Book:
    title: str
    author: str


@strawberry.type
class Library:
    name: str
    address: str
    books: list[Book]


@strawberry.type
class School:
    name: str
    location: str
    libraries: list[Library]


@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> list[Book]:
        return [
            Book(title="1984", author="George Orwell"),
            Book(title="To Kill a Mockingbird", author="Harper Lee"),
        ]

    @strawberry.field
    def libraries(self) -> list[Library]:
        return [
            Library(
                name="Central Library",
                address="123 Main St",
                books=[
                    Book(title="1984", author="George Orwell"),
                    Book(title="To Kill a Mockingbird", author="Harper Lee"),
                ],
            ),
            Library(
                name="Community Library",
                address="456 Elm St",
                books=[
                    Book(title="The Great Gatsby", author="F. Scott Fitzgerald"),
                    Book(title="Moby Dick", author="Herman Melville"),
                ],
            ),
        ]

    @strawberry.field
    def schools(self) -> list[School]:
        return [
            School(
                name="Springfield High",
                location="Springfield",
                libraries=[
                    Library(
                        name="Springfield Library",
                        address="789 Oak St",
                        books=[
                            Book(title="1984", author="George Orwell"),
                            Book(
                                title="The Great Gatsby", author="F. Scott Fitzgerald"
                            ),
                        ],
                    )
                ],
            ),
            School(
                name="Shelbyville High",
                location="Shelbyville",
                libraries=[
                    Library(
                        name="Shelbyville Library",
                        address="101 Pine St",
                        books=[
                            Book(title="To Kill a Mockingbird", author="Harper Lee"),
                            Book(title="Moby Dick", author="Herman Melville"),
                        ],
                    )
                ],
            ),
        ]


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        # In a real application, you'd save the book to a database here
        return Book(title=title, author=author)


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)
