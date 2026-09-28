# 自定义导入方案实体-bos_multi_import_scheme

## 单据体-子表 t_bas_mul_scheme_set

- **表名称：** 单据体-子表
- **表名：** t_bas_mul_scheme_set

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnodetype | 节点类型 | int4 | 32 |  | √ | 0 | 节点类型 |
| 3 | fdetailsheet | 对应的sheet页签 | int4 | 32 |  | √ | '-1' | 对应的sheet页签 |
| 4 | fsheetname | sheet页签名称 | varchar | 255 |  | √ | ' ' | sheet页签名称 |
| 5 | fstartcol | 起始列 | int4 | 32 |  | √ | '-1' | 起始列 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentitynumber | 实体编码 | varchar | 100 |  | √ | ' ' | 实体编码 |
| 8 | flowerconcatefield | 与下级实体关联的字段 | int4 | 32 |  | √ | '-1' | 与下级实体关联的字段 |
| 9 | fdatareplacenumber | 数据替换规则的唯一值编码 | varchar | 50 |  | √ | ' ' | 数据替换规则的唯一值编码 |
| 10 | fdatareplacename | 数据替换规则的唯一值名称 | varchar | 50 |  | √ | ' ' | 数据替换规则的唯一值名称 |
| 11 | fpnodeid | 父节点编码 | int4 | 32 |  | √ | 0 | 父节点编码 |
| 12 | fnodeid | 节点编码 | int4 | 32 |  | √ | 0 | 节点编码 |
| 13 | fmainnumber | 主实体编码 | varchar | 100 |  | √ | ' ' | 主实体编码 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fsuperconcatefield | 与上级实体关联的字段 | int4 | 32 |  | √ | '-1' | 与上级实体关联的字段 |
| 16 | fimporttype | 导入方式 | bpchar | 1 |  | √ | ' ' | 导入方式,枚举: |
| 17 | fstartrow | 起始行 | int4 | 32 |  | √ | '-1' | 起始行 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_mul_scheme_set |  | fentryid |
| 2 | idx_mul_scheme_set_pid |  | fid |

---

## 子单据体-子表 t_bas_mul_scheme_map

- **表名称：** 子单据体-子表
- **表名：** t_bas_mul_scheme_map

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fexcelfieldname | excel字段名称 | varchar | 255 |  | √ | ' ' | excel字段名称 |
| 2 | ffieldtype | 字段类型 | int4 | 32 |  | √ | 0 | 字段类型 |
| 3 | fbasedatatype | 基础资料类型 | int4 | 32 |  | √ | 0 | 基础资料类型 |
| 4 | fentityfieldname | 实体字段名称 | varchar | 100 |  | √ | ' ' | 实体字段名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fismapping | 映射关系 | bpchar | 1 |  | √ | '0' | 映射关系,枚举: |
| 7 | fexcelfield | Excel字段 | int4 | 32 |  | √ | '-1' | Excel字段 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fentityfieldnumber | 实体字段编码 | varchar | 50 |  | √ | ' ' | 实体字段编码 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fpropseq | 字段导入顺序 | int4 | 32 |  | √ | 0 | 字段导入顺序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mul_scheme_map_pid |  | fentryid |
| 2 | pk_t_bas_mul_scheme_map |  | fdetailid |

---

## 自定义导入方案实体-主表 t_bas_mulimport_scheme

- **表名称：** 自定义导入方案实体-主表
- **表名：** t_bas_mulimport_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | ffirstimportform | 首先导入的单据 | varchar | 50 |  | √ | ' ' | 首先导入的单据 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | ffilename | 文件名 | varchar | 200 |  | √ | ' ' | 文件名 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | ffilesize | 文件大小 | int4 | 32 |  | √ | 0 | 文件大小 |
| 13 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 14 | ffirstimportsheet | 首先导入的工作表页签 | int4 | 32 |  | √ | '-1' | 首先导入的工作表页签 |
| 15 | fschemedesc | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 16 | ffilepath | 文件路径 | varchar | 500 |  | √ | ' ' | 文件路径 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mulimport_scheme_number |  | fnumber |
| 2 | pk_t_bas_mulimport_scheme |  | fid |

---

## 将数据导入到-多选基础资料表 t_bas_mulimport_entity

- **表名称：** 将数据导入到-多选基础资料表
- **表名：** t_bas_mulimport_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mulimport_entity_fid |  | fid |
| 2 | pk_t_bas_mulimport_entity |  | fpkid |

---

## 自定义导入方案实体-多语言表 t_bas_mulimport_scheme_l

- **表名称：** 自定义导入方案实体-多语言表
- **表名：** t_bas_mulimport_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fschemedesc | 描述 | varchar | 200 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_mulimport_scheme_l |  | fpkid |
| 2 | idx_mulimport_scheme_l_fid |  | fid |
