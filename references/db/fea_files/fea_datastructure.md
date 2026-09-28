# 数据结构-fea_datastructure

## 树形单据体-子表 t_fea_structureentry

- **表名称：** 树形单据体-子表
- **表名：** t_fea_structureentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue | 表达式值 | text | 0 |  |  | ' ' | 表达式值 |
| 3 | ftype | 分录类型 | bpchar | 1 |  | √ | '1' | 分录类型,枚举: 1 :数据元素 2 :数据结构 |
| 4 | fpid | fpid | int8 | 64 |  | √ | 0 | pid |
| 5 | fmultype | 类别 | varchar | 30 |  | √ | ' ' | 类别,枚举: fea_element :数据元素 fea_datastructure :数据结构 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fvaluedesc | 表达式 | varchar | 255 |  |  | ' ' | 表达式 |
| 8 | frefid | 数据元素/子结构 | int8 | 64 |  | √ | 0 | 数据元素 fea_element |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | frefentryid | refentryid | int8 | 64 |  | √ | 0 | refentryid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fea_structureentry |  | fentryid |
| 2 | idx_fea_structureentry_fid |  | fid |

---

## 数据结构-主表 t_fea_structure

- **表名称：** 数据结构-主表
- **表名：** t_fea_structure

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fdescription | 注释 | varchar | 255 |  | √ | ' ' | 注释 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fctrlstrategy | fctrlstrategy | bpchar | 1 |  | √ | '5' |  |
| 10 | fentity | 业务对象标志 | varchar | 100 |  | √ | ' ' | 业务对象标志 |
| 11 | fiscommon | 是否可被引用 | bpchar | 1 |  | √ | '1' | 是否可被引用 |
| 12 | fstandardid | 文件标准 | int8 | 64 |  | √ | 0 | [文件标准 fea_standard](../fea_files/fea_standard.md) |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | fentitydesc | 业务对象 | varchar | 100 |  | √ | ' ' | 业务对象 |
| 19 | fcommonfilter | 通用过滤 | text | 0 |  |  | ' ' | 通用过滤 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fea_structure |  | fid |
| 2 | idx_fea_stru_masterid |  | fmasterid |
| 3 | idx_fea_stru_createorg |  | fctrlstrategy,fcreateorgid,forgid |

---

## 数据结构-多语言表 t_fea_structure_l

- **表名称：** 数据结构-多语言表
- **表名：** t_fea_structure_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fea_structure_l |  | fpkid |
| 2 | idx_fea_structure_l |  | fid,flocaleid |
