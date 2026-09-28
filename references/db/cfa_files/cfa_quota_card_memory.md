# 指标卡片页面记忆-cfa_quota_card_memory

## 指标卡片页面记忆-主表 t_cfa_quota_card_memory

- **表名称：** 指标卡片页面记忆-主表
- **表名：** t_cfa_quota_card_memory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fpagetag | 页面标识 | varchar | 50 |  | √ | ' ' | 页面标识 |
| 5 | fquotaids | 指标id列表 | varchar | 650 |  | √ | ' ' | 指标id列表 |
| 6 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | ffiltercondition | 筛选条件 | varchar | 300 |  |  | ' ' | 筛选条件 |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfa_quota_card_memory |  | fid |
| 2 | uq_cfa_quota_card_memory |  | fpagetag |
