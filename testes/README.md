# Área de Testes — BuskMate

Esta pasta reúne toda a documentação de QA (Quality Assurance) do projeto **BuskMate**, com foco no frontend.

**Site:** https://silvanoandrade.github.io/buskmate/

## 📄 Documento principal

**[BuskMate_Plano_de_Requisitos.pdf](./BuskMate_Plano_de_Requisitos.pdf)** — o arquivo de referência desta área. Reúne os 54 requisitos funcionais (RF) e não-funcionais (RNF) do frontend, organizados por módulo, com a convenção de IDs (`RF-MÓDULO-NN` / `RNF-NN`) usada em todos os artefatos abaixo.

## 📁 Estrutura

| Pasta / arquivo | Conteúdo | Status |
|---|---|---|
| [`manual/casos-de-teste.md`](./manual/casos-de-teste.md) | 54 casos de teste manuais, um ou mais por requisito, prontos para execução | ✅ Disponível |
| `bugs/` | Relatório de bugs encontrados durante a execução dos testes | 🔜 Em breve |
| `automacao/` | Testes automatizados em Python + Selenium | 🔜 Em breve |

## Rastreabilidade

Todo artefato desta área referencia o ID de um requisito do PDF principal:

```
requisito (RF-CAD-02)  →  caso de teste manual (TC-016)  →  execução / bug / automação
```

Isso garante que qualquer pessoa (tutores incluídos) consiga partir de um requisito e encontrar rapidamente como ele é verificado.
