from iamai import Plugin


class hellobot(Plugin):
    async def handle(self) -> None:
        await self.event.reply(f"Hello, I am {self.config.selfName}!")

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return (
            self.event.user_id == self.bot.config.superuser
            and str(self.event.message).lower() == "hello"
        )

