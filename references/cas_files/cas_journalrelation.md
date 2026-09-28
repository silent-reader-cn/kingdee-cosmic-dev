# 日记账关系-cas_journalrelation

## 日记账关系-主表 t_cas_journalrelation

- **表名称：** 日记账关系-主表
- **表名：** t_cas_journalrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 3 | fbatchid | 批次ID | int8 | 64 |  | √ | 0 | 批次ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_jr_fbid |  | fbatchid |
| 2 | t_cas_journalrelation_pkey |  | fid |
