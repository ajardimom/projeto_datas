from datetime import date
from typing import Optional


def calcular_idade(data_nascimento: date, data_referencia: Optional[date] = None) -> int:
    """
    Calcula a idade exata em anos de uma pessoa dada a sua data de nascimento.
    """
    hoje = data_referencia if data_referencia is not None else date.today()

    if data_nascimento > hoje:
        raise ValueError("A data de nascimento não pode estar no futuro.")

    fez_aniversario = (hoje.month, hoje.day) >= (data_nascimento.month, data_nascimento.day)
    return hoje.year - data_nascimento.year - (0 if fez_aniversario else 1)


def dias_para_data_futura(data_futura: date, data_referencia: Optional[date] = None) -> int:
    """
    Calcula a quantidade de dias restantes até uma data no futuro.
    """
    hoje = data_referencia if data_referencia is not None else date.today()

    if data_futura < hoje:
        raise ValueError("A data informada já passou. Informe uma data futura.")

    return (data_futura - hoje).days
