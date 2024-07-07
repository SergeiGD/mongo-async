class UnknownCategoryException(Exception):
    detail = "unkown category"

    def __str__(self) -> str:
        return self.detail
    
class SaveException(Exception):
    detail = "got error on save"

    def __str__(self) -> str:
        return self.detail
    
class NotFoundException(Exception):
    detail = "record was not found"

    def __str__(self) -> str:
        return self.detail
    
class SchemaException(Exception):
    detail = "schema error"

    def __str__(self) -> str:
        return self.detail
    