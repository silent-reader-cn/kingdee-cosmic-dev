# 担保额度占用-gm_guaranteequotause

## 担保额度占用-主表 t_gm_guaranteequotause

- **表名称：** 担保额度占用-主表
- **表名：** t_gm_guaranteequotause

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fguaranteequotaid | 担保额度 | int8 | 64 |  | √ | 0 | [担保额度 gm_guaranteequota](../gm_files/gm_guaranteequota.md) |
| 6 | fbegindate | 担保开始日期 | timestamp | 0 |  |  | null | 担保开始日期 |
| 7 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 8 | fadvancequota | 预占额度 | numeric | 23 | 10 | √ | 0 | 预占额度 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | famount | 担保金额 | numeric | 23 | 10 | √ | 0 | 担保金额 |
| 11 | forgtype | 组织类型 | varchar | 80 |  | √ | ' ' | 组织类型 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fenddate | 担保结束日期 | timestamp | 0 |  |  | null | 担保结束日期 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 16 | forgname | 组织名称 | varchar | 80 |  | √ | ' ' | 组织名称 |
| 17 | fcurrencyid | 担保币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | factualquota | 实际占用额度 | numeric | 23 | 10 | √ | 0 | 实际占用额度 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fbilltype | 单据类型 | varchar | 80 |  | √ | ' ' | 单据类型,枚举: guarantee_apply :担保申请 guarantee_contract :担保合同 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_quotause_quotaid |  | fguaranteequotaid |
| 2 | idx_gm_quotause_bill |  | fbilltype,fbillid |
| 3 | pk_t_gm_guaranteequotause |  | fid |
| 4 | idx_gm_quotause_org |  | forgtype,forgid |
