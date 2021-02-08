import sys
sys.path.append('.')
import pytest
from model.logistics import Logistic
from dao.logistic_dao import LogisticDao
from sqlalchemy.orm.exc import UnmappedInstanceError
import pytest 


class TestLogisticDao:
    @pytest.fixture
    def create_instance(self):
        obj = Logistic("TEsts dao name", "Teste dao descricao")
        return obj
    
    def test_instance(self):
        logistic = LogisticDao()
        assert isinstance(logistic, LogisticDao)

    def test_save(self, create_instance):
        obj_save = LogisticDao().save(create_instance)
        assert obj_save.id_ is not None
        LogisticDao().delete(obj_save)

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            obj_error = LogisticDao().save('testes')

    def test_read_by_id(self, create_instance):
        obj_save = LogisticDao().save(create_instance)
        obj_read = LogisticDao().read_by_id(obj_save.id_)
        assert isinstance(obj_read, Logistic)
        LogisticDao().delete(obj_read)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            obj_error = LogisticDao().read_by_id('teste by id')

    def test_read_all(self):
        obj_all = LogisticDao().read_all()
        assert isinstance(obj_all, list)

    def test_delete(self, create_instance):
        obj_save = LogisticDao().save(create_instance)
        obj_read = LogisticDao().read_by_id(obj_save.id_)
        LogisticDao().delete(obj_read)
        obj_read = LogisticDao().read_by_id(obj_save.id_)
        assert obj_read is None

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            LogisticDao().delete('test delete dao')
