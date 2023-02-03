from iamai import Plugin

ver = 1.0

class bot(Plugin):
    async def handle(self) -> None:
        await self.event.reply(f"蕗蕨(v{ver}) for IAMAI(5.0.0)")

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return (
            str(self.event.message).lower() == ".bot"
        )

