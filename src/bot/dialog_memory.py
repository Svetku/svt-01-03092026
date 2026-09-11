class DialogMemory:
    def __init__(self, limit: int = 20) -> None:
        self._limit = limit
        self._chats: dict[int, list[dict[str, str]]] = {}

    def get(self, chat_id: int) -> list[dict[str, str]]:
        return list(self._chats.get(chat_id, []))

    def add(self, chat_id: int, role: str, content: str) -> None:
        history = self._chats.setdefault(chat_id, [])
        history.append({"role": role, "content": content})
        del history[:-self._limit]

    def reset(self, chat_id: int) -> None:
        self._chats.pop(chat_id, None)
