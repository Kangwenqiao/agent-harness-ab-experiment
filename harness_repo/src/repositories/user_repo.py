from dataclasses import dataclass, field


@dataclass
class InMemoryUserRepo:
    usernames: set[str] = field(default_factory=set)

    def exists(self, username: str) -> bool:
        return username in self.usernames

    def add(self, username: str) -> str:
        self.usernames.add(username)
        return username

    def list_usernames(self) -> list[str]:
        return sorted(self.usernames)
