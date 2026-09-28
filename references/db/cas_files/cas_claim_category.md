# 通知个性缓存表-cas_claim_category

## 通知个性缓存表-主表 t_cas_claim_category

- **表名称：** 通知个性缓存表-主表
- **表名：** t_cas_claim_category

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 整数 | int2 | 16 |  | √ | 0 | 整数 |
| 3 | fnoticeid | 通知单ID | int8 | 64 |  | √ | 0 | 通知单ID |
| 4 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_claim_category |  | fid |
| 2 | idx_cas_category_unt |  | fuserid,ftype,fnoticeid |
| 3 | idx_cas_category_n |  | fnoticeid |
