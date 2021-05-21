from .constants import Constants


class Utils:

    @staticmethod
    def format_message(channel: str, message: str) -> str:
        return f"from: @{channel} \n {message}"

    @staticmethod
    def chat_title_matches(
            chat: str,
            matches: list = Constants.CHAT_FORWARD_LIST.value
    ) -> bool:
        return any(chat in match for match in matches)
