# 申请资产基础资料-fa_apply_bill_detail_base

## 申请资产基础资料-主表 t_fa_apply_asseet_detail

- **表名称：** 申请资产基础资料-主表
- **表名：** t_fa_apply_asseet_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fassetname | 资产名称 | varchar | 60 |  | √ | ' ' | 资产名称 |
| 4 | fstoreplace | fstoreplace | int8 | 64 |  | √ | 0 |  |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fnumber | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 7 | fentryid | 长整数 | int8 | 64 |  | √ | 0 | 长整数 |
| 8 | fusestate | fusestate | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_apply_asseet_detail_pkey |  | fentryid |
| 2 | idx_fa_aad_fid |  | fid |
