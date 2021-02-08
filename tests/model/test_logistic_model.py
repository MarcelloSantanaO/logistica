import sys
sys.path.append('.')
from model.logistics import Logistic
import pytest

class TestLogisticModel:

    @pytest.fixture
    def create_instance(self):
        name = 'Correio'
        description = "descricao"
        obj = Logistic(name, description)
        return obj

    def test_logistic_instance(self, create_instance):
        assert(create_instance, Logistic)

    def test_logistic_name_empty(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.name = ''

    def test_logistic_name_len(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.name = 'Teste nome'*200

    def test_logistic_name_no_str(self, create_instance):
        with pytest.raises(TypeError):
            create_instance.name = 100

    def test_logistic_description_len(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.description = 'descricao' * 500

    def test_logistic_description_no_string(self, create_instance):
        with pytest.raises(TypeError):
            create_instance.description = 10
