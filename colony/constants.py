UNCOMMITTED_BRANCH_NAME = "tmp-colony-"
TIMEOUT = 30
FINAL_SB_STATUSES = ["Active", "ActiveWithError", "Ended", "EndedWithError", "Ending"]

DONE_STATUS = "Done"


class ConstantBase:
    def __new__(cls, *args, **kwargs):
        raise TypeError("Constants class cannot be instantiated")


class ColonyConfigKeys(ConstantBase):
    TOKEN = "token"
    SPACE = "space"
    ACCOUNT = "account"
