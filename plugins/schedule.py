from time import strftime, localtime

from iamai import Plugin
from iamai.adapter.apscheduler import scheduler_decorator


@scheduler_decorator(
    trigger="interval", trigger_args={"seconds": 10}, override_rule=True
)
class Schedule(Plugin):
    async def handle(self) -> None:
        await self.bot.get_adapter("cqhttp").send(
            f"Time: {strftime('%Y-%m-%d %H:%M:%S', localtime())}",
            message_type="group",
            id_=597049442,  # 群号
        )

    async def rule(self) -> bool:
        return False

