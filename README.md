# automacao-e-gestao-energetica# Sistema de Gestão Inteligente - Colônia Aurora 🚀

Este repositório contém o protótipo do sistema integrado de gerenciamento energético e tomada de decisão para a base espacial Aurora Siger.

## 📌 Sobre o Projeto
O sistema foi desenvolvido em Python e tem como objetivo organizar os dados da colônia, prever a geração de energia eólica e tomar decisões autônomas para evitar o colapso energético da base. O projeto foi construído utilizando estruturas de dados nativas (Dicionários/Hash), lógica booleana e um modelo matemático de Regressão Linear Simples.

## ⚙️ Como funciona
1. **Organização de Dados:** Os dados de clima, módulos e energia são armazenados de forma hierárquica usando dicionários (tabelas chave-valor).
2. **Previsão:** Uma função aplica o Método dos Mínimos Quadrados em um histórico de dados de vento para prever quanta energia será gerada no momento atual.
3. **Decisão Lógica:** O sistema confronta o consumo, a geração e o nível da bateria. Em caso de déficit crítico, ele automaticamente desliga módulos não essenciais (ex: Pesquisa) para manter o Suporte à Vida funcionando.

## 🖥️ Exemplo de Entrada e Saída
**Entrada (Variáveis Iniciais):**
- Vento detectado: 11 km/h
- Geração Solar: 40 MW
- Bateria: 45%
- Consumo Total: 70 MW

**Saída (Terminal):**
- Previsão Matemática: 27.5 MW de energia eólica gerada.
- ALERTA CRÍTICO: Consumo (70 MW) maior que geração (67.5 MW) e bateria baixa.
- Ação: Desligando Módulo de Pesquisa Científica.
- Ação: Novo Consumo Total ajustado para: 40 MW.
- Ação: Módulo de Suporte à Vida mantido LIGADO.
