# 信用更新明细-ccm_usedetail

## 信用更新明细-主表 t_ccm_usedetail

- **表名称：** 信用更新明细-主表
- **表名：** t_ccm_usedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | freduceamount | 本单占用额度 | numeric | 23 | 10 | √ | 0 | 本单占用额度 |
| 4 | farchiveid | 信用档案ID | int8 | 64 |  | √ | 0 | 信用档案ID |
| 5 | fcreatetime | 操作日期 | timestamp | 0 |  |  | null | 操作日期 |
| 6 | fop | 操作 | varchar | 30 |  | √ | ' ' | 操作 |
| 7 | farchiveamount | 档案金额 | numeric | 23 | 10 | √ | 0 | 档案金额 |
| 8 | funitid | 单位 | int8 | 64 |  | √ | 0 | 单位 |
| 9 | ftempamount | 临时档案金额 | numeric | 23 | 10 | √ | 0 | 临时档案金额 |
| 10 | fentitykey | 实体对象 | varchar | 30 |  | √ | ' ' | 实体对象 |
| 11 | fnote | 说明 | varchar | 2000 |  | √ | ' ' | 说明 |
| 12 | fbalance | 更新后余额 | numeric | 23 | 10 | √ | 0 | 更新后余额 |
| 13 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 14 | fincreaseamount | 本单返还额度 | numeric | 23 | 10 | √ | 0 | 本单返还额度 |
| 15 | flogtype | 日志类型 | varchar | 30 |  | √ | ' ' | 日志类型,枚举: 1 :正常日志 9 :其他日志 |
| 16 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_usedetail_time |  | fcreatetime |
| 2 | pk_ccm_usedetail |  | fid |
