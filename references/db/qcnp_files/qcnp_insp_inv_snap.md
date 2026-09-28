# 检验计划明细库存快照-qcnp_insp_inv_snap

## 检验计划明细库存快照-主表 t_qcnp_insp_inv_snap

- **表名称：** 检验计划明细库存快照-主表
- **表名：** t_qcnp_insp_inv_snap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | finvbalanceid | 库存余额分录行ID | int8 | 64 |  | √ | 0 | 库存余额分录行ID |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | finbounddate | 入库日期 | timestamp | 0 |  |  | null | 入库日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcnp_snap_finvbalanceid |  | finvbalanceid |
| 2 | pk_t_qcnp_insp_inv_snap |  | fid |
