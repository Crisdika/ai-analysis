# Casos de Teste para Claude PR Review

Este diretório contém exemplos de código Python com problemas específicos para testar o sistema de revisão de PR com Claude AI.

## Como usar

Para testar o Claude PR Review, crie um branch com um destes arquivos e abra um PR para a main. O Claude deve identificar os problemas listados.

## Casos de Teste

### Erros Óbvios em Python

| Caso | Arquivo | Problema |
|------|---------|----------|
| 01 | `caso_01_nonetype.py` | Possível `NoneType` não tratado |
| 02 | `caso_02_variaveis_nao_usadas.py` | Variáveis criadas e não utilizadas |
| 03 | `caso_03_retorno_none_implicito.py` | Retorno implícito `None` não intencional |
| 04 | `caso_04_mutavel_default.py` | Uso de mutáveis como valor default |
| 05 | `caso_05_datetime_sem_timezone.py` | `datetime.now()` sem timezone |

### Riscos Claros

| Caso | Arquivo | Problema |
|------|---------|----------|
| 06 | `caso_06_except_generico.py` | `except:` ou `except Exception:` genérico |
| 07 | `caso_07_pass_silencioso.py` | `pass` silencioso em fluxo crítico |
| 08 | `caso_08_eval_exec.py` | Uso de `eval` ou `exec` |
| 09 | `caso_09_sql_injection.py` | SQL construído via string (injection) |

### Legibilidade Mínima

| Caso | Arquivo | Problema |
|------|---------|----------|
| 10 | `caso_10_funcao_longa.py` | Funções excessivamente longas |
| 11 | `caso_11_if_else_aninhado.py` | Muitos níveis de `if/else` aninhados |
| 12 | `caso_12_nomes_genericos.py` | Nomes genéricos (`data`, `temp`, `obj`) |

### Casos Especiais

| Caso | Arquivo | Descrição |
|------|---------|-----------|
| 13 | `caso_13_multiplos_problemas.py` | Múltiplos problemas combinados |
| 14 | `caso_14_codigo_limpo.py` | Código limpo (deve retornar "Nenhum risco relevante") |

## Resultados Esperados

### Para casos 01-13:
O Claude deve identificar os problemas específicos de cada arquivo com comentários curtos e objetivos.

### Para caso 14:
O Claude deve responder:
> **Nenhum risco relevante identificado no diff.**

## Exemplo de Teste

```bash
# Criar branch de teste
git checkout -b test/caso-01-nonetype

# Copiar caso para src
cp test_cases/caso_01_nonetype.py src/

# Commit e push
git add src/caso_01_nonetype.py
git commit -m "test: add case 01 for PR review testing"
git push origin test/caso-01-nonetype

# Abrir PR para main
gh pr create --title "Test: Caso 01 NoneType" --body "Testando detecção de NoneType"
```
