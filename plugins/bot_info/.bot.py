from iamai import Plugin
from iamai.adapter.cqhttp.message import CQHTTPMessage, CQHTTPMessageSegment


class Hello(Plugin):
    async def handle(self) -> None:
        msg = CQHTTPMessage()
        msg += CQHTTPMessageSegment.text("Hello")
        msg += CQHTTPMessageSegment.image("file:///img/test.png")
        await self.event.reply(msg)

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return str(self.event.message) == "hello"

