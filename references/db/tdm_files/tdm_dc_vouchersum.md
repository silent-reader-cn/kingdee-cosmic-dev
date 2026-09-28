# 凭证汇总结果-tdm_dc_vouchersum

## 凭证汇总结果-主表 t_tdm_dc_vouchersum

- **表名称：** 凭证汇总结果-主表
- **表名：** t_tdm_dc_vouchersum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdebitbegin_dest | 期初借方金额（目标单据） | numeric | 23 | 10 | √ | 0 | 期初借方金额（目标单据） |
| 3 | fdebitbegin_src | 期初借方金额（源单据） | numeric | 23 | 10 | √ | 0 | 期初借方金额（源单据） |
| 4 | faccountnumber | 科目编码 | varchar | 100 |  | √ | ' ' | 科目编码 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | faccountname | 科目名称 | varchar | 255 |  | √ | ' ' | 科目名称 |
| 7 | fperiodnumber | 会计期间 | int8 | 64 |  | √ | 0 | 会计期间 |
| 8 | fcreditbegin_dest | 期初贷方金额（目标单据） | numeric | 23 | 10 | √ | 0 | 期初贷方金额（目标单据） |
| 9 | ftar_count | 目标凭证行数 | int8 | 64 |  | √ | 0 | 目标凭证行数 |
| 10 | fstate | 比对结果 | varchar | 50 |  | √ | ' ' | 比对结果,枚举: A :无差异 B :异常 |
| 11 | fsource_count | 原始凭证行数 | int8 | 64 |  | √ | 0 | 原始凭证行数 |
| 12 | faccountbookstype | 账簿类型 | varchar | 50 |  | √ | ' ' | 账簿类型 |
| 13 | fcreditbegin_src | 期初贷方金额（源单据） | numeric | 23 | 10 | √ | 0 | 期初贷方金额（源单据） |
| 14 | fresultid | 结果表ID | int8 | 64 |  | √ | 0 | 结果表ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idex_t_tdm_dc_vouchersum_1 |  | fresultid,forgid,fperiodnumber,faccountnumber |
| 2 | pk_tdm_dc_vouchersum |  | fid |
