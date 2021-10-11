# Teste para desenvolvedor back-end 

## Desafio

Criar um serviço para calcular o valor de um CDB pós fixado indexado ao CDI em uma data específica e uma página web em que esses dados calculados serão expostos.

## Aplicação

A API foi desenvolvida em python com o uso do Django Rest Framework(DRF), e o deploy foi realizado através do herokuapp.

## Acesso ao deploy

A aplicação está disponível na seguinte URL:

https://teste-gorila-cdb.herokuapp.com/cdb/


- Para obter o resultado, faça uma requisição POST para a url acima
- No corpo da requisição é necessário informar as datas de início e fim do investimento (investmentDate e currentDate, respectivamente) e a % do CDI do investimento (cdbRate)

ex.: POST https://teste-gorila-cdb.herokuapp.com/cdb/

`Request Body:`
```JSON
{
    "investmentDate":"2016-11-14",
    "cdbRate": 103.5,
    "currentDate":"2016-12-26"
}
```

Com essa requisição você deverá receber a evolução do investimento da data data inicial("investmentDate") até a data final("currentDate") a partir taxa do cdb indicada("cdbRate")
```JSON
[
  {
        "date": "2016-12-23",
        "unitPrice": 1015.44545
    },
    {
        "date": "2016-12-22",
        "unitPrice": 1014.91269
    },
    {
        "date": "2016-12-21",
        "unitPrice": 1014.38021
    },
    {
        "date": "2016-12-20",
        "unitPrice": 1013.84801
    },
    {
        "date": "2016-12-19",
        "unitPrice": 1013.31609
    },
    {
        "date": "2016-12-16",
        "unitPrice": 1012.78445
    },
    {
        "date": "2016-12-15",
        "unitPrice": 1012.25308
    },
    {
        "date": "2016-12-14",
        "unitPrice": 1011.722
    },
    {
        "date": "2016-12-13",
        "unitPrice": 1011.19119
    },
    {
        "date": "2016-12-12",
        "unitPrice": 1010.66066
    },
    {
        "date": "2016-12-09",
        "unitPrice": 1010.13042
    },
    {
        "date": "2016-12-08",
        "unitPrice": 1009.60044
    },
    {
        "date": "2016-12-07",
        "unitPrice": 1009.07075
    },
    {
        "date": "2016-12-06",
        "unitPrice": 1008.54134
    },
    {
        "date": "2016-12-05",
        "unitPrice": 1008.0122
    },
    {
        "date": "2016-12-02",
        "unitPrice": 1007.48334
    },
    {
        "date": "2016-12-01",
        "unitPrice": 1006.95476
    },
    {
        "date": "2016-11-30",
        "unitPrice": 1006.42645
    },
    {
        "date": "2016-11-29",
        "unitPrice": 1005.88934
    },
    {
        "date": "2016-11-28",
        "unitPrice": 1005.35252
    },
    {
        "date": "2016-11-25",
        "unitPrice": 1004.81598
    },
    {
        "date": "2016-11-24",
        "unitPrice": 1004.27973
    },
    {
        "date": "2016-11-23",
        "unitPrice": 1003.74376
    },
    {
        "date": "2016-11-22",
        "unitPrice": 1003.20808
    },
    {
        "date": "2016-11-21",
        "unitPrice": 1002.67269
    },
    {
        "date": "2016-11-18",
        "unitPrice": 1002.13758
    },
    {
        "date": "2016-11-17",
        "unitPrice": 1001.60276
    },
    {
        "date": "2016-11-16",
        "unitPrice": 1001.06822
    },
    {
        "date": "2016-11-14",
        "unitPrice": 1000.53397
    }
]
```

## Django Rest Framwork View

O DRF possui uma view nativa para realizar as requisições, basta acessar a url https://teste-gorila-cdb.herokuapp.com/cdb/ e você podreá realizar as requisições POST por lá, como na figura abaixo

![image](https://github.com/jvsm10/images/blob/main/im1.PNG)
![image](https://github.com/jvsm10/images/blob/main/im2.PNG)
![image](https://github.com/jvsm10/images/blob/main/im3.PNG)
****
