# 维度层级配置-chatbi_dataset_demconfig

## 维度层级配置-主表 t_cbi_dataset_dmcf

- **表名称：** 维度层级配置-主表
- **表名：** t_cbi_dataset_dmcf

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
| 1 | pk_cbi_dataset_dmcf |  | fid |

---

## 单据体-子表 t_cbi_dataset_dmdetails

- **表名称：** 单据体-子表
- **表名：** t_cbi_dataset_dmdetails

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffirstlevel | 一级维度 | varchar | 50 |  | √ | ' ' | 一级维度,枚举: |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fmulcombo | 下钻维度 | varchar | 2000 |  | √ | ' ' | 下钻维度,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_dataser_dmdetails |  | fentryid |
| 2 | idx_cbi_dataset_dmdetails_fk |  | fid |
