# 公共单据映射-ai_billmapping

## 公共单据映射-主表 t_ai_billmapping

- **表名称：** 公共单据映射-主表
- **表名：** t_ai_billmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourcebillnumber | 公共表单 | varchar | 60 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | ftargetbillnumber | 源表单 | varchar | 60 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_billmapping_id |  | fsourcebillnumber |
| 2 | pk_t_ai_billmapping |  | fid |

---

## 单据体-子表 t_ai_mapping_body

- **表名称：** 单据体-子表
- **表名：** t_ai_mapping_body

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcefielddesc | 公共表单 | varchar | 60 |  | √ | ' ' | 公共表单 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsourcefieldfull | 公共表单字段 | varchar | 255 |  | √ | ' ' | 公共表单字段 |
| 5 | ftargetfieldfull | 源表单字段 | varchar | 255 |  | √ | ' ' | 源表单字段 |
| 6 | ftargetfielddesc | 源表单 | varchar | 60 |  | √ | ' ' | 源表单 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_mapping_body_id |  | fid |
| 2 | pk_t_ai_mapping_body |  | fentryid |
