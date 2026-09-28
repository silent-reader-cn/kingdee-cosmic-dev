# 票据池票据加解锁记录-cdm_pooldraft_log

## 票据池票据加解锁记录-主表 t_cdm_pooldraftlocklog

- **表名称：** 票据池票据加解锁记录-主表
- **表名：** t_cdm_pooldraftlocklog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | foperatetype | 操作类型 | varchar | 20 |  | √ | ' ' | 操作类型,枚举: lock :加锁 unlock :解锁 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fbillpoolid | 票据池 | int8 | 64 |  | √ | 0 | [票据池维护 cdm_billpool](../cdm_files/cdm_billpool.md) |
| 6 | fpoollockorgid | 锁票人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fpooldraftid | 票据ID | int8 | 64 |  | √ | 0 | 票据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_pooldraftlocklog |  | fpoollockorgid,fbillpoolid,fcreatetime |
| 2 | pk_cdm_pooldraftlocklog |  | fid |
