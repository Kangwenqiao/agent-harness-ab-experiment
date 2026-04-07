from src.api.onboarding_api import OnboardingAPI
from src.repositories.user_repo import InMemoryUserRepo
from src.services.onboarding_service import OnboardingService


def build_api(existing_usernames: set[str] | None = None) -> tuple[OnboardingAPI, InMemoryUserRepo]:
    repo = InMemoryUserRepo(set() if existing_usernames is None else set(existing_usernames))
    service = OnboardingService(repo)
    return OnboardingAPI(service), repo


def test_registers_plain_username() -> None:
    api, repo = build_api()

    response = api.register({"username": "alice_01"})

    assert response == {"status": "ok", "username": "alice_01"}
    assert repo.list_usernames() == ["alice_01"]


def test_normalizes_username_before_storing() -> None:
    api, repo = build_api()

    response = api.register({"username": " Alice "})

    assert response == {"status": "ok", "username": "alice"}
    assert repo.list_usernames() == ["alice"]
