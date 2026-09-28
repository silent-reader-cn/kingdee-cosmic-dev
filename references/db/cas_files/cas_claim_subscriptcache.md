# 通知单角标缓存表-cas_claim_subscriptcache

## 通知单角标缓存表-主表 t_cas_claim_subscript

- **表名称：** 通知单角标缓存表-主表
- **表名：** t_cas_claim_subscript

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flastestid | 最新记录ID | int8 | 64 |  | √ | 0 | 最新记录ID |
| 3 | ftype | 类型 | int2 | 16 |  | √ | 0 | 类型 |
| 4 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_subscript_l |  | flastestid |
| 2 | idx_cas_subscript_ult |  | fuserid,ftype,flastestid |
| 3 | pk_t_cas_claim_subscript |  | fid |
