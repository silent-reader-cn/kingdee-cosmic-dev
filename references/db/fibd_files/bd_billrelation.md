# 单据关联关系-bd_billrelation

## 单据关联关系-主表 t_bd_relation

- **表名称：** 单据关联关系-主表
- **表名：** t_bd_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftargetbilltable | 目标表实体名 | varchar | 50 |  | √ | ' ' | 目标表实体名 |
| 3 | fsourcebillmeta | 源表元数据 | varchar | 50 |  | √ | ' ' | 源表元数据 |
| 4 | fisvehicle | 是否中间表 | bpchar | 1 |  | √ | '0' | 是否中间表,枚举: 1 :是 0 :否 |
| 5 | fsourcemetacol | 上游元数据关联 | varchar | 50 |  | √ | ' ' | 上游元数据关联 |
| 6 | fsourcebillcol | 源表关联字段 | varchar | 50 |  | √ | ' ' | 源表关联字段 |
| 7 | ftargetbillroute | 目标表路由字段 | varchar | 50 |  | √ | ' ' | 目标表路由字段 |
| 8 | fsourcebilltable | 源表实体名 | varchar | 50 |  | √ | ' ' | 源表实体名 |
| 9 | ftargetbillmeta | 目标表元数据 | varchar | 50 |  | √ | ' ' | 目标表元数据 |
| 10 | ftargetbillcol | 目标表关联字段 | varchar | 50 |  | √ | ' ' | 目标表关联字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_relation_ftargetsourcemeta |  | ftargetbillmeta |
| 2 | pk_t_bd_relation |  | fid |
