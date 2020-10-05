# Dotz Challenge

## Solução Proposta

![arquitetura](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/arquitetura.png?raw=true)

## Sumário

- [Componentes](#Componentes)
  - [Glue](#glue)
    - [Pontos Positivos](#pontos-positivos)
  - [Amazon Relational Database Service](#amazon-relational-database-service)
  - [Amazon QuickSight](#amazon-quicksight)
- [Execução do Fluxo](#execução-do-fluxo)
  1. [Upload de arquivos e Crawler](#upload-de-arquivos-e-crawler)
  2. [Data Catalog e Jobs](#data-catalog-e-jobs)
  3. [Data Catalog e Jobs Detalhe](#data-catalog-e-jobs-detalhe)
  4. [Finalização do Job e Quicksight](#finalização-do-job-e-quicksight)
  5. [Dashboard com o Quicksight](#dashboard-com-o-quicksight)
- [Provisionamento de Infraestrutura e Serviços](#provisionamento-de-infraestrutura-e-serviços)
- [Subindo Infraestrutura com Terraform](#subindo-infraestrutura-com-terraform)
- [Custo da Proposta](#custo-da-proposta)
- [Passos Futuros](#passos-futuros)

## Componentes

### Glue

O `AWS Glue` é um serviço de ETL - Extração, transformação e carga totalmente gerenciado que facilita a preparação e o carregamento de dados para análise.

### Pontos Positivos

- É integrado com uma grande variedade de serviços da `AWS`
- Oferece suporte nativo a dados armazenados no `Amazon Aurora` e em todos os outros mecanismos do `Amazon RDS`, no `Amazon Redshift` e no `Amazon S3`
- Não tem servidor. Não é necessário provisionar ou gerenciar a infraestrutura.
- Executa tarefas de ETL em um ambiente `Apache Spark` gerenciado com aumento de escala horizontal.
- Executa o `crawling` de suas fontes de dados, identifica os formatos de dados e sugere esquemas e transformações.

### Amazon Relational Database Service

O `Amazon Relational Database Service` (Amazon RDS) facilita a configuração, a operação e a escalabilidade de bancos de dados relacionais na nuvem. Para este cenário foi escolhido utilizar o banco de dados [PostgreSQL](https://www.postgresql.org/)

### Amazon QuickSight

O `Amazon QuickSight` é um serviço de inteligência de negócios rápido e baseado na nuvem que facilita a entrega de `insights` a todos em sua organização.

## Execução do Fluxo

### Upload de arquivos e Crawler

Colocando arquivos no `Bucket` e executando `crawler`

|      Etapa do processo   |      Demonstração      |
|:------------------------:|:-------------------------:|
| ![1-cvs-crawler](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/1-cvs-crawler.png?raw=true) | ![1-cvs-crawler](https://github.com/ernane/dotz-challenge/blob/develop/assets/gifs/1-cvs-crawler.gif?raw=true) |

### Data Catalog e Jobs

Analisando o `data catalog` e executando os `Jobs`

|      Etapa do processo   |      Demonstração      |
|:------------------------:|:-------------------------:|
| ![2-catalago-job](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/2-catalago-job.png?raw=true) | ![2-catalago-job](https://github.com/ernane/dotz-challenge/blob/develop/assets/gifs/2-catalago-job.gif?raw=true) |

### Data Catalog e Jobs Detalhe

São executados 3 `Jobs: job_comp_boss, job_price_quote, job_bill_of_materials`, e todos possuem os mesmos passos de execução. Os códigos fonte podem ser acessados em [jobs](https://github.com/ernane/dotz-challenge/tree/develop/jobs)

|                                                 Etapa do processo                                                  |                                                   Etapas dos Jobs                                                |
|:------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| ![2-catalago-job](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/2-catalago-job.png?raw=true) | ![diagrama-exec-job.png](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/diagrama-exec-job.png?raw=true) |

### Finalização do Job e Quicksight

Analisando a finalização dos `Glue Jobs` e importando dados no `Quicksight`

|      Etapa do processo   |      Demonstração      |
|:------------------------:|:-------------------------:|
| ![3-job-dashboard](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/3-job-dashboard.png?raw=true) | ![3-job-dashboard](https://github.com/ernane/dotz-challenge/blob/develop/assets/gifs/3-job-dashboard.gif?raw=true) |

### Dashboard com o Quicksight

Apartir do `Quicksight`, é possível criar `dashboards` com os dados que foram carregados para o banco de dados.

![dasboard-quicksight](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/dasboard-quicksight.png?raw=true)

## Provisionamento de Infraestrutura e Serviços

Foi escolhido o [terraform](https://www.terraform.io/) para realizar entregas de infraestrutura como código. Todos códigos necessários para criação dos componentes entregues na `AWS`, estão nesse repositório com a extensão `.tf`

Também foi adotado o [Terraform Cloud](https://app.terraform.io/) que é um aplicativo SaaS de uso gratuito que fornece fluxo de trabalho para escrever e construir infraestrutura como código com o Terraform.

![terraform-init](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/terraform-init.png?raw=true)

## Subindo Infraestrutura com Terraform

|      Provisionando com Terraform   |      Validando Componentes      |
|:------------------------:|:-------------------------:|
| ![terraform](https://github.com/ernane/dotz-challenge/blob/develop/assets/gifs/terraform.gif?raw=true) | ![aws-console-recursos](https://github.com/ernane/dotz-challenge/blob/develop/assets/gifs/aws-console-recursos.gif?raw=true) |

## Custo da Proposta

|                                      Resumo de gastos                                       |                                                    Gastos do mês até a data por serviço                                                    |
|:------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
| ![billing-1](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/billing-1.png?raw=true) | ![billing-2](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/billing-2.png?raw=true) |

## Passos Futuros

- Execução Automática do Fluxo, explorando outros serviços da `AWS`. Ex: `SNS`, `SQS` e `Lambdas`
- Modulariação dos `scripts` dos `Jobs`
- Visualização com ganho de negócio através do `Amazon QuickSight`
