from src.services.onboarding_service import OnboardingService


class OnboardingAPI:
    def __init__(self, service: OnboardingService) -> None:
        self.service = service

    def register(self, payload: dict[str, str]) -> dict[str, str]:
        username = payload["username"]
        created_username = self.service.register(username)
        return {"status": "ok", "username": created_username}
