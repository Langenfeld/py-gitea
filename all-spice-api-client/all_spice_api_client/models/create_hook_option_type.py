from enum import Enum


class CreateHookOptionType(str, Enum):
    DINGTALK = "dingtalk"
    DISCORD = "discord"
    GITEA = "gitea"
    GOGS = "gogs"
    MSTEAMS = "msteams"
    SLACK = "slack"
    TELEGRAM = "telegram"
    FEISHU = "feishu"
    WECHATWORK = "wechatwork"
    PACKAGIST = "packagist"

    def __str__(self) -> str:
        return str(self.value)
