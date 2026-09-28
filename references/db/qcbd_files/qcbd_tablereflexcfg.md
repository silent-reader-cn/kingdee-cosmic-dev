# 表映射配置_质量云-qcbd_tablereflexcfg

## 单据体-子表 t_qcbd_reflexentry

- **表名称：** 单据体-子表
- **表名：** t_qcbd_reflexentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | ffieldkey | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_reflexentry |  | fentryid |
| 2 | idx_qcbd_reflry_fid |  | fid |
| 3 | idx_qcbd_reflry_fseq |  | fseq |

---

## 表映射配置_质量云-主表 t_qcbd_reflexcfg

- **表名称：** 表映射配置_质量云-主表
- **表名：** t_qcbd_reflexcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 来源表名称 | varchar | 255 |  | √ | ' ' | 来源表名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdestabkey | 目标表编码 | varchar | 50 |  | √ | ' ' | 目标表编码 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fdestabname | 目标表名称 | varchar | 50 |  | √ | ' ' | 目标表名称 |
| 11 | ftype | 映射类型 | varchar | 5 |  | √ | ' ' | 映射类型,枚举: 1 :分应用分表 3 :设计器后缀分表 |
| 12 | fissys | 系统预制 | bpchar | 1 |  | √ | '0' | 系统预制 |
| 13 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 来源表编码 | varchar | 30 |  | √ | ' ' | 来源表编码 |
| 15 | fbilltypeid | 映射单据类型内码 | varchar | 50 |  | √ | ' ' | 映射单据类型内码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_reflfg_fcreatetime |  | fcreatetime |
| 2 | pk_qcbd_reflexcfg |  | fid |
| 3 | idx_qcbd_reflfg_fnumber |  | fnumber |

---

## 表映射配置_质量云-多语言表 t_qcbd_reflexcfg_l

- **表名称：** 表映射配置_质量云-多语言表
- **表名：** t_qcbd_reflexcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 来源表名称 | varchar | 255 |  | √ | ' ' | 来源表名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_reflfgl_fid |  | fid,flocaleid |
| 2 | pk_qcbd_reflexcfg_l |  | fpkid |
| 3 | idx_qcbd_reflfgl_fname |  | fname |
