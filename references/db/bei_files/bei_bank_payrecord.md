# 银行提交记录-bei_bank_payrecord

## 银行提交记录-主表 t_bei_bank_payrecord

- **表名称：** 银行提交记录-主表
- **表名：** t_bei_bank_payrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsrcbillkey | 源单主键 | varchar | 50 |  | √ | ' ' | 源单主键 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fbillid | 单据标识 | int8 | 64 |  | √ | 0 | 单据标识 |
| 6 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: 1 :银行付款单 2 :银行代发单 3 :资金上划下拨 |
| 7 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_bankpayrecord_biz |  | fsrcbilltype,fsrcbillkey |
| 2 | pk_t_bei_bank_payrecord |  | fid |
