"""Testes para o módulo principal."""

import sys
from pathlib import Path

# Adiciona o diretório src ao path para importar módulos
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from main import hello


def test_hello(capsys):
    """Testa a função hello."""
    hello()
    captured = capsys.readouterr()
    assert "Olá!" in captured.out
