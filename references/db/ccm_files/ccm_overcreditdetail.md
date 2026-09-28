# 信用超标记录更新明细-ccm_overcreditdetail

## 信用超标记录更新明细-主表 t_ccm_overcreditdetail

- **表名称：** 信用超标记录更新明细-主表
- **表名：** t_ccm_overcreditdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | farchiveid | 信用档案ID | int8 | 64 |  | √ | 0 | 信用档案ID |
| 3 | foccupyamount | 占用额度 | numeric | 23 | 10 | √ | 0 | 占用额度 |
| 4 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 5 | fbalance | 余额 | numeric | 23 | 10 | √ | 0 | 余额 |
| 6 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 7 | fquotatype | 额度类型 | varchar | 50 |  | √ | ' ' | 额度类型 |
| 8 | fentitykey | 单据标识 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 9 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 10 | fquota | 额度 | numeric | 23 | 10 | √ | 0 | 额度 |
| 11 | ftempquota | 临时额度 | numeric | 23 | 10 | √ | 0 | 临时额度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_ovcredet_time |  | fcreatetime |
| 2 | pk_ccm_overcreditdetail |  | fid |
