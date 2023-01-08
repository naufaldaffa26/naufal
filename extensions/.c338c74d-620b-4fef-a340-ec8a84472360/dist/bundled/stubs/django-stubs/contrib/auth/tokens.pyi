from datetime import date
from typing import Any, Optional

from django.contrib.auth.base_user import AbstractBaseUser

class PasswordResetTokenGenerator:
    key_salt: str = ...
    secret: Any = ...
    def make_token(self, user: AbstractBaseUser) -> str: ...
    def check_token(
        self, user: Optional[AbstractBaseUser], token: Optional[str]
    ) -> bool: ...
    def _make_token_with_timestamp(
        self, user: AbstractBaseUser, timestamp: int
    ) -> str: ...
    def _make_hash_value(self, user: AbstractBaseUser, timestamp: int) -> str: ...
    def _num_days(self, dt: date) -> float: ...
    def _today(self) -> date: ...

default_token_generator: Any