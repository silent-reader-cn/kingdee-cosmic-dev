# 变更单分录实体-fa_chgbillentry_entity

## 变更单分录实体-主表 t_fa_changebillentry

- **表名称：** 变更单分录实体-主表
- **表名：** t_fa_changebillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | FID | int8 | 64 |  | √ | 0 | FID |
| 2 | fperiodid | 变更期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 3 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 4 | fnumber | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fassetbookid | 资产账簿 | int8 | 64 |  | √ | 0 | [启用期间设置 fa_assetbook](../fa_files/fa_assetbook.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_chabilent_fid |  | fid |
| 2 | t_fa_changebillentry_pkey |  | fentryid |
