# 核算维度初始数据录入-gl_assgrp_initbal

## 核算维度初始数据录入-主表 t_gl_initbalance

- **表名称：** 核算维度初始数据录入-主表
- **表名：** t_gl_initbalance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbegincreditfor | fbegincreditfor | numeric | 19 | 6 | √ | 0.000000 |  |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fyearprofitdebitfor | fyearprofitdebitfor | numeric | 19 | 6 | √ | 0.000000 |  |
| 5 | fyearprofitdebitlocal | fyearprofitdebitlocal | numeric | 19 | 6 | √ | 0.000000 |  |
| 6 | fbegindebitfor | fbegindebitfor | numeric | 19 | 6 | √ | 0.000000 |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fyearprofitcreditqty | fyearprofitcreditqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fcurlocalid | fcurlocalid | int8 | 64 |  | √ | 0 |  |
| 10 | fyearprofitcreditlocal | fyearprofitcreditlocal | numeric | 19 | 6 | √ | 0.000000 |  |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | fbeginlocal | fbeginlocal | numeric | 19 | 6 | √ | 0.000000 |  |
| 13 | fbeginqty | fbeginqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | fyeardebitqty | fyeardebitqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fyearcreditfor | fyearcreditfor | numeric | 19 | 6 | √ | 0.000000 |  |
| 16 | fyeardebitlocal | fyeardebitlocal | numeric | 19 | 6 | √ | 0.000000 |  |
| 17 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 18 | fbegindebitlocal | fbegindebitlocal | numeric | 19 | 6 | √ | 0.000000 |  |
| 19 | fassgrpid | fassgrpid | int8 | 64 |  | √ | 0 |  |
| 20 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 21 | fbegindebitqty | fbegindebitqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 22 | fyearcreditqty | fyearcreditqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 23 | fbegincreditlocal | fbegincreditlocal | numeric | 19 | 6 | √ | 0.000000 |  |
| 24 | faccounttableid | faccounttableid | int8 | 64 |  | √ | 0 |  |
| 25 | fisdeleted | fisdeleted | bpchar | 1 |  | √ | '0' |  |
| 26 | fbookid | fbookid | int8 | 64 |  | √ | 0 |  |
| 27 | fbeginfor | fbeginfor | numeric | 19 | 6 | √ | 0.000000 |  |
| 28 | fyearprofitcreditfor | fyearprofitcreditfor | numeric | 19 | 6 | √ | 0.000000 |  |
| 29 | fbooktypeid | fbooktypeid | int8 | 64 |  | √ | 0 |  |
| 30 | fyearprofitdebitqty | fyearprofitdebitqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 31 | fbegincreditqty | fbegincreditqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 32 | fyeardebitfor | fyeardebitfor | numeric | 19 | 6 | √ | 0.000000 |  |
| 33 | fyearcreditlocal | fyearcreditlocal | numeric | 19 | 6 | √ | 0.000000 |  |
| 34 | fmeasureunitid | fmeasureunitid | int8 | 64 |  | √ | 0 |  |
| 35 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 36 | faccountid | faccountid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_initbal_acctid |  | faccountid |
| 2 | idx_gl_initbal |  | forgid,fbooktypeid,faccounttableid,faccountid,fassgrpid,fcurrencyid,fmeasureunitid |
| 3 | t_gl_initbalance_pkey |  | fid |
