# 余额重算操作记录-im_invbal_oplog

## 余额重算操作记录-主表 t_im_invbal_oplog

- **表名称：** 余额重算操作记录-主表
- **表名：** t_im_invbal_oplog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 3 | fopuser | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fop | 操作 | varchar | 30 |  | √ | ' ' | 操作 |
| 5 | fopdesc | 操作描述 | varchar | 30 |  | √ | ' ' | 操作描述 |
| 6 | fparams | 关键参数 | varchar | 2000 |  | √ | ' ' | 关键参数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_invbal_oplog |  | fid |
| 2 | idx_im_recal_op |  | fop |
| 3 | idx_im_recal_time |  | foptime |
