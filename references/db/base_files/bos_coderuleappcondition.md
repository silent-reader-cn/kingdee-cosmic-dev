# 编码规则适用条件基础资料-bos_coderuleappcondition

## 编码规则适用条件基础资料-主表 t_cr_appcondition

- **表名称：** 编码规则适用条件基础资料-主表
- **表名：** t_cr_appcondition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 编码规则 | varchar | 36 |  | √ | ' ' | [编码规则 bos_coderule](../base_files/bos_coderule.md) |
| 2 | fpropertyvalue | 属性值 | varchar | 100 |  | √ | ' ' | 属性值 |
| 3 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 4 | fproperty | 属性 | varchar | 100 |  | √ | ' ' | 属性 |
| 5 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cr_appcondition_fcrid |  | fid |
| 2 | t_cr_appcondition_pkey |  | fentryid |
