# 科目余额初始化-gl_initbalance

## 科目余额初始化-主表 t_gl_initbalance

- **表名称：** 科目余额初始化-主表
- **表名：** t_gl_initbalance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbegincreditfor | 期初余额贷方原币 | numeric | 19 | 6 | √ | 0.000000 | 期初余额贷方原币 |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fyearprofitdebitfor | 本年实际损益借方原币 | numeric | 19 | 6 | √ | 0.000000 | 本年实际损益借方原币 |
| 5 | fyearprofitdebitlocal | 本年实际损益借方本位币 | numeric | 19 | 6 | √ | 0.000000 | 本年实际损益借方本位币 |
| 6 | fbegindebitfor | 期初余额借方原币 | numeric | 19 | 6 | √ | 0.000000 | 期初余额借方原币 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fyearprofitcreditqty | 本年实际损益贷方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年实际损益贷方数量 |
| 9 | fcurlocalid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fyearprofitcreditlocal | 本年实际损益贷方本位币 | numeric | 19 | 6 | √ | 0.000000 | 本年实际损益贷方本位币 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbeginlocal | fbeginlocal | numeric | 19 | 6 | √ | 0.000000 |  |
| 13 | fbeginqty | fbeginqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | fyeardebitqty | 本年累计借方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计借方数量 |
| 15 | fyearcreditfor | 本年累计贷方原币 | numeric | 19 | 6 | √ | 0.000000 | 本年累计贷方原币 |
| 16 | fyeardebitlocal | 本年累计借方本位币 | numeric | 19 | 6 | √ | 0.000000 | 本年累计借方本位币 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbegindebitlocal | 期初余额借方本位币 | numeric | 19 | 6 | √ | 0.000000 | 期初余额借方本位币 |
| 19 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fbegindebitqty | 期初余额借方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期初余额借方数量 |
| 22 | fyearcreditqty | 本年累计贷方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计贷方数量 |
| 23 | fbegincreditlocal | 期初余额贷方本位币 | numeric | 19 | 6 | √ | 0.000000 | 期初余额贷方本位币 |
| 24 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 25 | fisdeleted | 是否已删除 | bpchar | 1 |  | √ | '0' | 是否已删除 |
| 26 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 27 | fbeginfor | fbeginfor | numeric | 19 | 6 | √ | 0.000000 |  |
| 28 | fyearprofitcreditfor | 本年实际损益贷方原币 | numeric | 19 | 6 | √ | 0.000000 | 本年实际损益贷方原币 |
| 29 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 30 | fyearprofitdebitqty | 本年实际损益借方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年实际损益借方数量 |
| 31 | fbegincreditqty | 期初余额贷方数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期初余额贷方数量 |
| 32 | fyeardebitfor | 本年累计借方原币 | numeric | 19 | 6 | √ | 0.000000 | 本年累计借方原币 |
| 33 | fyearcreditlocal | 本年累计贷方本位币 | numeric | 19 | 6 | √ | 0.000000 | 本年累计贷方本位币 |
| 34 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 35 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 36 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |

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
