# 对账数据基础资料-pur_thirdbasedata

## 对账数据基础资料-主表 t_pur_thirddata

- **表名称：** 对账数据基础资料-主表
- **表名：** t_pur_thirddata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 对账期间到 | timestamp | 0 |  |  | null | 对账期间到 |
| 3 | fcurrid | fcurrid | int8 | 64 |  | √ | 0 |  |
| 4 | floccurrid | floccurrid | int8 | 64 |  | √ | 0 |  |
| 5 | fstartdate | 对账期间从 | timestamp | 0 |  |  | null | 对账期间从 |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fnumber | 账单编码 | varchar | 80 |  | √ | ' ' | 账单编码 |
| 8 | fsource | 电商平台 | varchar | 10 |  | √ | ' ' | 电商平台,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_thirddata_pkey |  | fid |
| 2 | idx_pur_thirddata_fnumber |  | fnumber |
