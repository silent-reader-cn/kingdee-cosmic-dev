# 指标展示配置-cbi_dataset_indexconfig

## 指标展示配置-主表 t_cbi_dataset_indexconfig

- **表名称：** 指标展示配置-主表
- **表名：** t_cbi_dataset_indexconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatasetid | 数据集 | int8 | 64 |  | √ | 0 | [数据集 gai_cbi_dataset](../chatbi_files/gai_cbi_dataset.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_ds_indexcf_fdatas |  | fdatasetid |
| 2 | pk_cbi_dataset_indexconfig |  | fid |

---

## 指标展示配置-子表 t_cbi_dataset_indexcfdata

- **表名称：** 指标展示配置-子表
- **表名：** t_cbi_dataset_indexcfdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 3 | fdisplayindex | 显示指标 | text | 0 |  |  | null | 显示指标,枚举: |
| 4 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | faskindex | 提问指标 | varchar | 255 |  | √ | ' ' | 提问指标,枚举: |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_ds_icfdata_fentryid |  | fid |
| 2 | pk_cbi_dataset_indexcfdata |  | fentryid |
