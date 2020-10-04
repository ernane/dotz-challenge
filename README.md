# Dotz Challenge

## Arquitetura implementada

![arquitetura](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/arquitetura.png?raw=true)

## 1 - Upload de arquivos e Crawler

Colocando arquivos no `Bucket` e executando `crawler`

|      Etapa do processo   |      Demonstração      |
|:------------------------:|:-------------------------:|
| ![1-cvs-crawler](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/1-cvs-crawler.png?raw=true) | ![1-cvs-crawler](https://github.com/ernane/dotz-challenge/blob/develop/assets/gifs/1-cvs-crawler.gif?raw=true) |

## 2 - Data Catalog e Jobs

Analisando o `data catalog` e executando os `Jobs`

|      Etapa do processo   |      Demonstração      |
|:------------------------:|:-------------------------:|
| ![2-catalago-job](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/2-catalago-job.png?raw=true) | ![2-catalago-job](https://github.com/ernane/dotz-challenge/blob/develop/assets/gifs/2-catalago-job.gif?raw=true) |

## 3 - Data Catalog e Jobs Detalhe

São executados 3 `Jobs: job_comp_boss, job_price_quote, job_bill_of_materials`, e todos possuem os mesmos passos de execução. Os códigos fonte podem ser acessados em [jobs](https://github.com/ernane/dotz-challenge/tree/develop/jobs)

|                                                 Etapa do processo                                                  |                                                   Etapas dos Jobs                                                |
|:------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| ![2-catalago-job](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/2-catalago-job.png?raw=true) | ![diagrama-exec-job.png](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/diagrama-exec-job.png?raw=true) |

## 4 - Finalização do Job e Quicksight

Analisando a finalização dos `Glue Jobs` e importando dados no `Quicksight`

|      Etapa do processo   |      Demonstração      |
|:------------------------:|:-------------------------:|
| ![3-job-dashboard](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/3-job-dashboard.png?raw=true) | ![3-job-dashboard](https://github.com/ernane/dotz-challenge/blob/develop/assets/gifs/3-job-dashboard.gif?raw=true) |

## 5 - Dashboard com o Quicksight

Apartir do `Quicksight`, é possível criar `dashboards` com os dados que foram carregados para o banco de dados.

![dasboard-quicksight](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/dasboard-quicksight.png?raw=true)

## Provisionamento de Infraestrutura(Terraform)

Foi escolhido o [terraform](https://www.terraform.io/) para realizar entregas de infraestrutura como código. Todos códigos necessários para criação dos componentes entregues na `AWS`, estão nesse repositório com a extensão `.tf`

Também foi adotado o [Terraform Cloud](https://app.terraform.io/) que é um aplicativo SaaS de uso gratuito que fornece fluxo de trabalho para escrever e construir infraestrutura como código com o Terraform.

![terraform-init](https://github.com/ernane/dotz-challenge/blob/develop/assets/images/terraform-init.png?raw=true)

## Demonstração - Subindo Infraestrutura com Terraform

|      Provisionando com Terraform   |      Validando Componentes      |
|:------------------------:|:-------------------------:|
| ![terraform](https://github.com/ernane/dotz-challenge/blob/develop/assets/gifs/terraform.gif?raw=true) | ![aws-console-recursos](https://github.com/ernane/dotz-challenge/blob/develop/assets/gifs/aws-console-recursos.gif?raw=true) |
