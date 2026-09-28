# 往来账基础资料-gl_reciprocal_record_base

## 往来账基础资料-主表 t_gl_acccurrent

- **表名称：** 往来账基础资料-主表
- **表名：** t_gl_acccurrent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facctableid | facctableid | int8 | 64 |  | √ | 0 |  |
| 3 | famountbalfor | famountbalfor | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | famount | famount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | fbiznum | fbiznum | varchar | 30 |  | √ | ' ' |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | flocalcurrencyid | flocalcurrencyid | int8 | 64 |  | √ | 0 |  |
| 9 | fstatus | 核销状态 | bpchar | 1 |  | √ | '0' | 核销状态,枚举: 0 :未核销 1 :部分核销 2 :全部核销 |
| 10 | fentrydc | fentrydc | varchar | 2 |  | √ | '1' |  |
| 11 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | fbookeddate | fbookeddate | timestamp | 0 |  |  | null |  |
| 14 | fsourcetype | fsourcetype | bpchar | 1 |  | √ | '0' |  |
| 15 | fexpiredate | fexpiredate | timestamp | 0 |  |  | null |  |
| 16 | feffectivedate | feffectivedate | timestamp | 0 |  |  | null |  |
| 17 | famountfor | famountfor | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 18 | famountbal | famountbal | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fvoucherid | fvoucherid | int8 | 64 |  | √ | 0 |  |
| 20 | fperiodid | fperiodid | int8 | 64 |  | √ | 0 |  |
| 21 | fassgrpid | fassgrpid | int8 | 64 |  | √ | 0 |  |
| 22 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 23 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 24 | fbookid | fbookid | int8 | 64 |  | √ | 0 |  |
| 25 | fbooktypeid | fbooktypeid | int8 | 64 |  | √ | 0 |  |
| 26 | fvchentryid | fvchentryid | int8 | 64 |  | √ | 0 |  |
| 27 | fbizdate | fbizdate | timestamp | 0 |  |  | null |  |
| 28 | funeffectivedate | funeffectivedate | timestamp | 0 |  |  | null |  |
| 29 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 30 | faccountid | faccountid | int8 | 64 |  | √ | 0 |  |
| 31 | fwriteoffpersonid | fwriteoffpersonid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_acccurrent |  | forgid,fbooktypeid,fperiodid,faccountid,fassgrpid |
| 2 | idx_gl_acccurrent_2 |  | fbooktypeid,forgid,faccountid,fassgrpid |
| 3 | t_gl_acccurrent_pkey |  | fid |
| 4 | idx_gl_acccurrent_vchentryid |  | fvchentryid |
| 5 | idx_gl_acccurrent_vchid |  | fvoucherid |
| 6 | idx_gl_acccurrent_masterid |  | fmasterid |
