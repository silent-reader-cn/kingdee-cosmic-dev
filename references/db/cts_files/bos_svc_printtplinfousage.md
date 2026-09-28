# 打印模板组织隔离-bos_svc_printtplinfousage

## 打印模板组织隔离-主表 t_bas_printtplinfousage

- **表名称：** 打印模板组织隔离-主表
- **表名：** t_bas_printtplinfousage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | FID | int8 | 64 |  | √ | 0 | FID |
| 2 | fcreateorgid | FCREATEORGID | int8 | 64 |  | √ | '-1' | FCREATEORGID |
| 3 | fisassign | FISASSIGN | bpchar | 1 |  | √ | ' ' | FISASSIGN |
| 4 | fassignorgid | fassignorgid | int8 | 64 |  | √ | '-1' |  |
| 5 | fdataid | FDATAID | int8 | 64 |  | √ | 0 | FDATAID |
| 6 | fuseorgid | FUSEORGID | int8 | 64 |  | √ | 0 | FUSEORGID |
| 7 | fctrlstrategy | FCTRLSTRATEGY | bpchar | 1 |  | √ | ' ' | FCTRLSTRATEGY |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_printtplinfous_idx_data |  | fdataid |
| 2 | t_bas_printtplinfous_idx_mul |  | fuseorgid,fdataid |
| 3 | pk_t_bas_printtplinfousage |  | fid |
