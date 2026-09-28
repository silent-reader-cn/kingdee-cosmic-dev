# 变量映射-bos_variablemapping

## 变量映射-多语言表 t_bas_variablemapping_l

- **表名称：** 变量映射-多语言表
- **表名：** t_bas_variablemapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 256 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_variablemapping_l |  | fid,flocaleid |
| 2 | pk_t_bas_variablemapping_l |  | fpkid |

---

## 变量映射-主表 t_bas_variablemapping

- **表名称：** 变量映射-主表
- **表名：** t_bas_variablemapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | fname | varchar | 256 |  | √ | ' ' |  |
| 5 | fscriptplugin | 插件 | varchar | 2000 |  | √ | ' ' | 插件 |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 9 | fbusibill | 业务实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_variablemapping |  | fid |
| 2 | idx_variablemapping_n |  | fnumber |

---

## 单据体-多语言表 t_bas_mappinfield_l

- **表名称：** 单据体-多语言表
- **表名：** t_bas_mappinfield_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fvarfieldname | 映射字段名称 | varchar | 256 |  | √ | ' ' | 映射字段名称 |
| 2 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_mappingfield_l |  | fentryid,flocaleid |
| 2 | pk_t_bas_mappinfield_l |  | fpkid |

---

## 单据体-子表 t_bas_mappinfield

- **表名称：** 单据体-子表
- **表名：** t_bas_mappinfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsplitsymbol | 字段合并分隔符 | varchar | 20 |  | √ | ' ' | 字段合并分隔符,枚举: , :, ; :; \| :\| \& :\& _0D :_0D @ :@ |
| 3 | fvarfieldname | 映射字段名称 | varchar | 256 |  | √ | ' ' | 映射字段名称 |
| 4 | fvardatasource | 数据源 | varchar | 50 |  | √ | ' ' | 数据源,枚举: |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fvariable | 变量 | int8 | 64 |  | √ | 0 | [全局变量 bos_variable](../cts_files/bos_variable.md) |
| 7 | fvarfield | 映射字段编码 | varchar | 100 |  | √ | ' ' | 映射字段编码 |
| 8 | fnewlineidx | 换行位置 | int4 | 32 |  | √ | 0 | 换行位置 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_mappinfield |  | fentryid |
| 2 | idx_bas_mappingfield_id |  | fid |
