from iamai import Plugin

ver = 1.03

class bot(Plugin):
    async def handle(self) -> None:
        await self.event.reply(f"蕗蕨(v{ver}) on IAMAI(5.0.0) for {self.event.adapter.name}")

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return (
            str(self.event.message).lower() == ".bot"
        )

