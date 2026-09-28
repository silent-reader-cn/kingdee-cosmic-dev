# 凭证结果-tdm_dc_voucher

## 凭证结果-主表 t_tdm_dc_voucher

- **表名称：** 凭证结果-主表
- **表名：** t_tdm_dc_voucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdebitbegin_dest | 期初借方金额（目标单据） | numeric | 23 | 10 | √ | 0 | 期初借方金额（目标单据） |
| 3 | fdebitbegin_src | 期初借方金额（源单据） | numeric | 23 | 10 | √ | 0 | 期初借方金额（源单据） |
| 4 | faccountnumber | 科目编码 | varchar | 100 |  | √ | ' ' | 科目编码 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fvoucherrow | 记账凭证行号 | varchar | 50 |  | √ | ' ' | 记账凭证行号 |
| 7 | faccountname | 科目名称 | varchar | 255 |  | √ | ' ' | 科目名称 |
| 8 | fperiodnumber | 会计期间 | int8 | 64 |  | √ | 0 | 会计期间 |
| 9 | fvouchercode | 记账凭证编号 | varchar | 100 |  | √ | ' ' | 记账凭证编号 |
| 10 | fcreditbegin_dest | 期初贷方金额（目标单据） | numeric | 23 | 10 | √ | 0 | 期初贷方金额（目标单据） |
| 11 | fdifftype | 差异类型 | varchar | 50 |  | √ | ' ' | 差异类型,枚举: A :目标数据未更新 B :目标数据不存在 C :原始数据不存在 |
| 12 | fstate | 比对结果 | varchar | 50 |  | √ | ' ' | 比对结果,枚举: A :无差异 B :异常 |
| 13 | faccountbookstype | 账簿类型 | varchar | 50 |  | √ | ' ' | 账簿类型 |
| 14 | fcreditbegin_src | 期初贷方金额（源单据） | numeric | 23 | 10 | √ | 0 | 期初贷方金额（源单据） |
| 15 | ftotalid | 汇总表ID | int8 | 64 |  | √ | 0 | 汇总表ID |
| 16 | fresultid | 结果表ID | int8 | 64 |  | √ | 0 | 结果表ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_dc_voucher |  | fid |
| 2 | idx_t_tdm_dc_voucher_1 |  | fresultid,ftotalid |
