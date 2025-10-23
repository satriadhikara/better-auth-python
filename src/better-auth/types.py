from typing import Any, Callable, Optional, Dict, List, TypedDict
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


# Database models
@dataclass
class User:
    id: str
    email: str
    name: Optional[str]
    image: Optional[str]
    emailVerified: bool
    createdAt: datetime
    updatedAt: datetime


@dataclass
class Account:
    id: str
    userId: str
    providerId: str  # "credential" for email/password
    accountId: str
    password: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


@dataclass
class Session:
    id: str
    userId: str
    token: str
    expiresAt: datetime
    createdAt: datetime = None
    updatedAt: datetime = None


@dataclass
class Verification:
    id: str
    identifier: str
    value: str
    expiresAt: datetime
    createdAt: datetime


# Context
class PasswordConfig(TypedDict):
    minPasswordLength: int
    maxPasswordLength: int


class SessionConfig(TypedDict):
    updateAge: int
    expiresIn: int
    freshAge: int


class RateLimitConfig(TypedDict):
    enabled: bool
    window: int
    max: int
    storage: str


# Request/Response
class AuthRequest(TypedDict, total=False):
    method: str
    path: str
    body: Dict[str, Any]
    headers: Dict[str, str]


class AuthResponse(TypedDict):
    status: int
    body: Dict[str, Any]
    headers: Dict[str, str]
