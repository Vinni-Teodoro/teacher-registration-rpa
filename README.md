# 🎓 Teacher Registration RPA

> Automação desenvolvida em **Python** para otimizar o cadastro e vínculo de docentes em um ERP acadêmico, reduzindo drasticamente o tempo operacional e eliminando tarefas repetitivas.

---

# 📖 Visão Geral

Este projeto foi desenvolvido para automatizar o processo de cadastro e vínculo de docentes em um sistema ERP acadêmico.

Antes da automação, cada docente precisava ser cadastrado manualmente, exigindo o preenchimento de diversos campos, validação de duplicidade e posterior vínculo ao ambiente correto.

A solução automatiza todo esse fluxo, proporcionando maior velocidade, padronização e redução de erros.

---

# 🚨 O Problema

O processo era totalmente manual e envolvia:

- Pesquisa para verificar se o docente já existia;
- Cadastro manual de informações pessoais;
- Preenchimento de documentos;
- Vínculo do docente ao ambiente correto;
- Atualização da planilha de controle.

Esse processo demandava aproximadamente **30 minutos por docente**, além de estar sujeito a erros de digitação e inconsistências.

---

# 💡 A Solução

Foi desenvolvido um **RPA em Python** que:

- 📄 Lê automaticamente uma planilha Excel;
- 🔍 Verifica se o docente já está cadastrado;
- 👤 Realiza o cadastro apenas quando necessário;
- 🔗 Efetua automaticamente o vínculo ao ambiente correto;
- 📊 Gera um relatório contendo o status de cada processamento.

---

# 🏗 Arquitetura da Solução

<p align="center">
  <img src="./images/architecture.png" width="90%">
</p>

Fluxo da automação:

```text
Excel
   │
   ▼
Python
   │
   ▼
Pandas
   │
   ▼
Selenium
   │
   ▼
ERP Acadêmico
   │
   ▼
Relatório Final
```

---

# ⚙️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| Python | Desenvolvimento da automação |
| Selenium | Automação Web |
| Pandas | Leitura e tratamento dos dados |
| Excel | Entrada e saída de informações |

---

# 📈 Resultados

## Antes

- ⏱️ Aproximadamente **30 minutos por docente**
- ❌ Processo totalmente manual
- ❌ Alto risco de erros de digitação
- ❌ Verificações repetitivas

## Depois

- ⚡ Aproximadamente **30 segundos por docente**
- ✅ Processo automatizado
- ✅ Validação automática
- ✅ Padronização das operações
- ✅ Geração automática de relatório

---

# 📂 Estrutura do Projeto

```text
teacher-registration-rpa/

├── docs/
├── images/
├── src/
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🚀 Próximas Melhorias

- Interface gráfica para execução da automação;
- Logs estruturados;
- Integração com banco de dados;
- Execução agendada;
- Containerização utilizando Docker.

---

# 📚 Aprendizados

Durante o desenvolvimento deste projeto aprofundei conhecimentos em:

- Automação Web com Selenium;
- Manipulação de dados utilizando Pandas;
- Tratamento de exceções;
- Estruturação de RPAs para ambientes corporativos;
- Boas práticas para automação de processos.

---

# ⚠️ Aviso

Este repositório apresenta um estudo de caso baseado em um projeto desenvolvido em ambiente corporativo.

Por questões de confidencialidade, **códigos-fonte, dados, URLs e informações proprietárias não são disponibilizados**.

O objetivo deste material é apresentar a arquitetura da solução, as tecnologias utilizadas e os resultados alcançados.

---

# 👨‍💻 Autor

**Vinícius Teodoro**

- 💼 LinkedIn: https://www.linkedin.com/in/vinicius-ateodoro
- 💻 GitHub: https://github.com/Vinni-Teodoro
