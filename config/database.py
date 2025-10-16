#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-05-06 01:08:46
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


import contextlib
from typing import AsyncIterator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    async_sessionmaker,
    AsyncSession,
    create_async_engine,
)

from sqlalchemy.orm import DeclarativeBase, sessionmaker
from config.config import settings


engine_url_async = settings.local_db_url_async
engine_url_sync = settings.local_db_url_sync

# include query cache
sync_engine = create_engine(
    engine_url_sync,
    pool_size=settings.database_pool_size,
    max_overflow=settings.database_max_overflow,
    query_cache_size=1200,
    echo=True,
    echo_pool=True,
)

test_engine = create_engine(
    settings.test_db_url,
    pool_size=settings.database_pool_size,
    max_overflow=settings.database_max_overflow,
    # echo=True,
    # echo_pool=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


class Base(DeclarativeBase):
    pass


class DBSessionManager:
    """Context manager for database sessions."""

    def __init__(self):
        self._engine: AsyncEngine | None = create_async_engine(
            engine_url_async,
            pool_size=settings.database_pool_size,
            max_overflow=settings.database_max_overflow,
            query_cache_size=1200,
            echo=True,
            echo_pool=True,
        )

        self._sessionmaker: async_sessionmaker | None = async_sessionmaker(
            bind=self._engine, autocommit=False, expire_on_commit=False
        )

    def init(self, engine_url: str) -> None:
        """Initialize the database session manager with the engine URL."""
        self._engine = create_async_engine(
            engine_url,
            pool_size=settings.database_pool_size,
            max_overflow=settings.database_max_overflow,
            query_cache_size=1200,
        )
        self._sessionmaker = async_sessionmaker(
            bind=self._engine, autocommit=False, expire_on_commit=False
        )

    async def close(self) -> None:
        """Close the database engine."""
        if self._engine is None:
            raise Exception("DBSessionManager is not initialized.")
        await self._engine.dispose()
        self._engine = None
        self._sessionmaker = None

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        """Context manager for acquiring a database connection."""
        if self._engine is None:
            raise Exception("DBSessionManager is not initialized.")
        async with self._engine.begin() as conn:
            try:
                yield conn
            except Exception as e:
                await conn.rollback()
                raise e

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        """Context manager for acquiring a database session."""
        if self._sessionmaker is None:
            raise Exception("DBSessionManager is not initialized.")

        session = self._sessionmaker()
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()


db_session_manager = DBSessionManager()
