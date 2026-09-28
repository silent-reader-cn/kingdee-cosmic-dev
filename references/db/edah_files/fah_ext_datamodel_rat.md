# 异构数据对接模型关系-fah_ext_datamodel_rat

## 异构数据对接模型关系-主表 t_ai_preevent

- **表名称：** 异构数据对接模型关系-主表
- **表名：** t_ai_preevent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 异构数据对接模型 | int8 | 64 |  | √ | 0 | [异构数据对接模型 fah_ext_datamodel](../edah_files/fah_ext_datamodel.md) |
| 2 | fpreeventclass | 前置异构数据对接模型 | int8 | 64 |  | √ | 0 | [异构数据对接模型 fah_ext_datamodel](../edah_files/fah_ext_datamodel.md) |
| 3 | fprestatus | 前置异构数据状态 | bpchar | 1 |  | √ | ' ' | 前置异构数据状态,枚举: v :生成凭证 g :产生外部数据 |
| 4 | fpreevtfield | 前置外部数据字段 | varchar | 80 |  | √ | ' ' | 前置外部数据字段 |
| 5 | fevtfield | 外部数据字段 | varchar | 80 |  | √ | ' ' | 外部数据字段 |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_preevent |  | fentryid |
| 2 | idx_ai_preevent |  | fid |
