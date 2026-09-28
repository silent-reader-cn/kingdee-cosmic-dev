# 预留记录传递记录-sbs_entry_reserve

## 预留记录传递记录-主表 t_sbs_entryreserve

- **表名称：** 预留记录传递记录-主表
- **表名：** t_sbs_entryreserve

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentity | 实体名称 | varchar | 50 |  | √ | ' ' | 实体名称 |
| 3 | ftype | 记录类型 | bpchar | 1 |  | √ | '2' | 记录类型,枚举: 1 :原单 2 :下游单 |
| 4 | freserveid | 预留记录ID | int8 | 64 |  | √ | 0 | 预留记录ID |
| 5 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 6 | fentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_ev_feid |  | fentryid |
| 2 | idx_sbs_ev_fbid |  | fbillid |
| 3 | t_sbs_entryreserve_pkey |  | fid |
