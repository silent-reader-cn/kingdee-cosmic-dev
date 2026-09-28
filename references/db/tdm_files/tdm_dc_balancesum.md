# 科目余额表汇总结果-tdm_dc_balancesum

## 科目余额表汇总结果-主表 t_tdm_dc_balancesum

- **表名称：** 科目余额表汇总结果-主表
- **表名：** t_tdm_dc_balancesum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdebitbegin_dest | 期初借方金额（目标单据） | numeric | 23 | 10 | √ | 0 | 期初借方金额（目标单据） |
| 3 | fdebitbegin_src | 期初借方金额（源单据） | numeric | 23 | 10 | √ | 0 | 期初借方金额（源单据） |
| 4 | fstate | 比对结果 | varchar | 50 |  | √ | ' ' | 比对结果,枚举: A :无差异 B :异常 |
| 5 | faccountnumber | 科目编码 | varchar | 100 |  | √ | ' ' | 科目编码 |
| 6 | faccountbookstype | 账簿类型 | varchar | 50 |  | √ | ' ' | 账簿类型 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | faccountname | 科目名称 | varchar | 255 |  | √ | ' ' | 科目名称 |
| 9 | fcreditbegin_src | 期初贷方金额（源单据） | numeric | 23 | 10 | √ | 0 | 期初贷方金额（源单据） |
| 10 | fperiodnumber | 会计期间 | int8 | 64 |  | √ | 0 | 会计期间 |
| 11 | fcreditbegin_dest | 期初贷方金额（目标单据） | numeric | 23 | 10 | √ | 0 | 期初贷方金额（目标单据） |
| 12 | fresultid | 结果表ID | int8 | 64 |  | √ | 0 | 结果表ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_dc_balancesum_1 |  | fresultid,forgid,fperiodnumber,faccountnumber |
| 2 | pk_tdm_dc_balancesum |  | fid |
