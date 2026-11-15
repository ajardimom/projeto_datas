from datetime import date
import pytest
from datas import calcular_idade, dias_para_data_futura, dias_desde_data_passada


def test_calcular_idade_ja_fez_aniversario_no_ano():
    assert calcular_idade(date(1995, 3, 10), date(2026, 11, 15)) == 31


def test_calcular_idade_ainda_nao_fez_aniversario_no_ano():
    assert calcular_idade(date(1995, 12, 25), date(2026, 11, 15)) == 30


def test_calcular_idade_exatamente_no_dia_do_aniversario():
    assert calcular_idade(date(2000, 11, 15), date(2026, 11, 15)) == 26


def test_calcular_idade_nascido_hoje():
    hoje = date(2026, 11, 15)
    assert calcular_idade(hoje, hoje) == 0


def test_calcular_idade_data_futura_lanca_erro():
    with pytest.raises(ValueError, match="A data de nascimento não pode estar no futuro"):
        calcular_idade(date(2030, 1, 1), date(2026, 11, 15))


def test_dias_para_data_futura_mesmo_mes():
    assert dias_para_data_futura(date(2026, 11, 25), date(2026, 11, 15)) == 10


def test_dias_para_data_futura_outro_ano():
    assert dias_para_data_futura(date(2027, 1, 1), date(2026, 11, 15)) == 47


def test_dias_para_data_futura_considerando_ano_bissexto():
    assert dias_para_data_futura(date(2028, 3, 1), date(2028, 2, 28)) == 2


def test_dias_para_data_futura_mesmo_dia_retorna_zero():
    hoje = date(2026, 11, 15)
    assert dias_para_data_futura(hoje, hoje) == 0


def test_dias_para_data_passada_lanca_erro():
    with pytest.raises(ValueError, match="A data informada já passou"):
        dias_para_data_futura(date(2026, 11, 10), date(2026, 11, 15))


def test_dias_desde_data_passada_mesmo_mes():
    assert dias_desde_data_passada(date(2026, 11, 5), date(2026, 11, 15)) == 10


def test_dias_desde_data_passada_outro_ano():
    assert dias_desde_data_passada(date(2025, 11, 15), date(2026, 11, 15)) == 365


def test_dias_desde_data_passada_mesmo_dia_retorna_zero():
    hoje = date(2026, 11, 15)
    assert dias_desde_data_passada(hoje, hoje) == 0


def test_dias_desde_data_futura_lanca_erro():
    with pytest.raises(ValueError, match="A data informada está no futuro"):
        dias_desde_data_passada(date(2026, 12, 1), date(2026, 11, 15))
