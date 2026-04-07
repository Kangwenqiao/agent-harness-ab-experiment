import pytest

from src.api.onboarding_api import OnboardingAPI
from src.repositories.user_repo import InMemoryUserRepo
from src.services.onboarding_service import OnboardingService, UsernameTakenError


def build_api(existing_usernames: set[str] | None = None) -> tuple[OnboardingAPI, InMemoryUserRepo]:
    repo = InMemoryUserRepo(set() if existing_usernames is None else set(existing_usernames))
    service = OnboardingService(repo)
    return OnboardingAPI(service), repo


def test_reserved_usernames_rejected() -> None:
    api, _ = build_api()

    with pytest.raises(ValueError):
        api.register({"username": "admin"})


def test_duplicate_after_normalization() -> None:
    api, _ = build_api({"alice"})

    with pytest.raises(UsernameTakenError):
        api.register({"username": " Alice "})


def test_invalid_characters_rejected() -> None:
    api, _ = build_api()

    with pytest.raises(ValueError):
        api.register({"username": "bad-name"})


def test_length_checked_after_normalization() -> None:
    api, _ = build_api()

    with pytest.raises(ValueError):
        api.register({"username": "  AB "})


def test_uppercase_and_lowercase_treated_same() -> None:
    api, _ = build_api({"demo_user"})

    with pytest.raises(UsernameTakenError):
        api.register({"username": "DEMO_USER"})
