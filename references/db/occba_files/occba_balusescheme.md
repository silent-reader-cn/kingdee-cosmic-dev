# 资金池使用方案-occba_balusescheme

## 资金池使用方案-主表 t_occba_balusescheme

- **表名称：** 资金池使用方案-主表
- **表名：** t_occba_balusescheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseentity | 使用对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fuserecordentity | 使用记录 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | ffilterscheme | 自定义过滤条件 | varchar | 2000 |  | √ | ' ' | 自定义过滤条件 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fusetargetentity | 使用目标对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_balusescheme |  | fid |
| 2 | idx_occba_balusescheme_num |  | fnumber |

---

## 匹配条件配置-子表 t_occba_baluseschemee

- **表名称：** 匹配条件配置-子表
- **表名：** t_occba_baluseschemee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fusetargetcolname | 使用目标字段名称 | varchar | 100 |  | √ | ' ' | 使用目标字段名称 |
| 3 | fmatchmode | 匹配方式 | varchar | 5 |  | √ | ' ' | 匹配方式,枚举: = :等于 != :不等于 in :在…中 |
| 4 | ffieldformula | 常量 | varchar | 50 |  | √ | ' ' | 常量 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fvaluetype | 取值来源 | bpchar | 1 |  | √ | '0' | 取值来源,枚举: 0 :源单字段 1 :计算公式 2 :按条件取值 3 :常量 |
| 7 | fusetargetcol | 使用目标字段标识 | varchar | 50 |  | √ | ' ' | 使用目标字段标识 |
| 8 | ffieldformuladesc | 常量 | varchar | 50 |  | √ | ' ' | 常量 |
| 9 | fusetargetfullcol | 使用目标字段全标识 | varchar | 100 |  | √ | ' ' | 使用目标字段全标识 |
| 10 | fusecolname | 使用对象字段名称 | varchar | 100 |  | √ | ' ' | 使用对象字段名称 |
| 11 | fusecol | 使用对象字段标识 | varchar | 50 |  | √ | ' ' | 使用对象字段标识 |
| 12 | fusefullcol | 使用对象字段全标识 | varchar | 100 |  | √ | ' ' | 使用对象字段全标识 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_baluseschemee |  | fentryid |
| 2 | idx_occba_baluseschemee_id |  | fid |

---

## 资金池使用方案-多语言表 t_occba_balusescheme_l

- **表名称：** 资金池使用方案-多语言表
- **表名：** t_occba_balusescheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_balusescheme_l |  | fpkid |
| 2 | idx_occba_balusescheme_flid |  | fid,flocaleid |

---

## 使用对象反写映射-子表 t_occba_baluseschemewe

- **表名称：** 使用对象反写映射-子表
- **表名：** t_occba_baluseschemewe

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwusecolname | 使用对象字段名称 | varchar | 100 |  | √ | ' ' | 使用对象字段名称 |
| 3 | fwusecol | 使用对象字段标识 | varchar | 50 |  | √ | ' ' | 使用对象字段标识 |
| 4 | fwuserecordcolname | 使用记录字段名称 | varchar | 100 |  | √ | ' ' | 使用记录字段名称 |
| 5 | fwusefullcol | 使用对象字段全标识 | varchar | 100 |  | √ | ' ' | 使用对象字段全标识 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fwvalmode | 取值方式 | bpchar | 1 |  | √ | ' ' | 取值方式,枚举: A :源单字段 |
| 8 | fwuserecordfullcol | 使用记录字段全标识 | varchar | 100 |  | √ | ' ' | 使用记录字段全标识 |
| 9 | fwuserecordcol | 使用记录字段标识 | varchar | 50 |  | √ | ' ' | 使用记录字段标识 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_baluseschemewe_id |  | fid |
| 2 | pk_occba_baluseschemewe |  | fentryid |

---

## 使用记录映射规则-子表 t_occba_baluseschemeve

- **表名称：** 使用记录映射规则-子表
- **表名：** t_occba_baluseschemeve

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frecordcol | 使用记录字段标识 | varchar | 50 |  | √ | ' ' | 使用记录字段标识 |
| 3 | frecordfullcol | 使用记录字段全标识 | varchar | 100 |  | √ | ' ' | 使用记录字段全标识 |
| 4 | fsourcecol | 源单字段标识 | varchar | 50 |  | √ | ' ' | 源单字段标识 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | frecordcolname | 使用记录字段名称 | varchar | 100 |  | √ | ' ' | 使用记录字段名称 |
| 7 | fsourcecolname | 源单字段名称 | varchar | 100 |  | √ | ' ' | 源单字段名称 |
| 8 | fcalculatefield | 字段类型 | bpchar | 1 |  | √ | ' ' | 字段类型,枚举: A :合计字段 B :汇总维度 |
| 9 | fvalmode | 取值方式 | bpchar | 1 |  | √ | ' ' | 取值方式,枚举: A :源单字段 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fsourcefullcol | 源单字段全标识 | varchar | 100 |  | √ | ' ' | 源单字段全标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_baluseschemeve |  | fentryid |
| 2 | idx_occba_baluseschemeve_id |  | fid |
