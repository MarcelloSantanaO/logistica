from dao.base_dao import BaseDao
from model.logistics import Logistic


class LogisticDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(Logistic)