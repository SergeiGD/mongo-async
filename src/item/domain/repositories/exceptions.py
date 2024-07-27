class UnknownCategoryException(Exception):
    detail = "unkown category"

    def __str__(self) -> str:
        return self.detail
    