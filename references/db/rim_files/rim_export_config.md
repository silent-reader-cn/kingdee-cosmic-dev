# 导出字段配置-rim_export_config

## 单据体-子表 t_rim_export_config_item

- **表名称：** 单据体-子表
- **表名：** t_rim_export_config_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexportpropkey | 导出属性 | varchar | 300 |  | √ | ' ' | 导出属性 |
| 3 | ffield_key | 字段编码 | varchar | 50 |  | √ | ' ' | 字段编码 |
| 4 | fentity_key | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 5 | ffield_name | 字段名称 | varchar | 80 |  | √ | ' ' | 字段名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcolwidth | 整数 | int8 | 64 |  | √ | 0 | 整数 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_export_config_item_fk |  | fid |
| 2 | pk_rim_export_config_item |  | fentryid |

---

## 导出字段配置-主表 t_rim_export_config

- **表名称：** 导出字段配置-主表
- **表名：** t_rim_export_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | finvoice_type | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型 |
| 5 | fquery_type | 菜单类型 | varchar | 50 |  | √ | ' ' | 菜单类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_export_config |  | fid |
| 2 | idx_rim_export_config |  | fquery_type,fcreater,finvoice_type |
