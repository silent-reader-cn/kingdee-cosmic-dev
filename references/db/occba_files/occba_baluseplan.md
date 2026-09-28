# 资金池使用方案-occba_baluseplan

## 输出收款明细表-子表 t_occba_userecentry

- **表名称：** 输出收款明细表-子表
- **表名：** t_occba_userecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fusebalcolname | 资金池使用方字段名称 | varchar | 100 |  | √ | ' ' | 资金池使用方字段名称 |
| 3 | fusecolname | 使用记录字段名称 | varchar | 100 |  | √ | ' ' | 使用记录字段名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fusecol | 使用记录字段标识 | varchar | 100 |  | √ | ' ' | 使用记录字段标识 |
| 6 | fvaluetype | 取值方式 | bpchar | 1 |  | √ | 'A' | 取值方式,枚举: 0 :源单字段 |
| 7 | fusefullcol | 使用记录字段全名称 | varchar | 100 |  | √ | ' ' | 使用记录字段全名称 |
| 8 | fusebalfullcol | 资金池使用方字段全标识 | varchar | 100 |  | √ | ' ' | 资金池使用方字段全标识 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fusebalcol | 资金池使用方字段标识 | varchar | 100 |  | √ | ' ' | 资金池使用方字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_userecentry |  | fentryid |
| 2 | idx_occba_userecentry_id |  | fid |

---

## 使用规则分录-子表 t_occba_useentity

- **表名称：** 使用规则分录-子表
- **表名：** t_occba_useentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatchmode | 条件 | varchar | 5 |  | √ | ' ' | 条件,枚举: = :等于 in :在…中 |
| 3 | ffieldformula | 常量 | varchar | 100 |  | √ | ' ' | 常量 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fvaluetype | 取值方式 | bpchar | 1 |  | √ | '0' | 取值方式,枚举: 0 :源单字段 3 :常量 |
| 6 | ffieldformuladesc | 常量 | varchar | 510 |  | √ | ' ' | 常量 |
| 7 | fusebalcolname | 资金池供应模型字段名称 | varchar | 100 |  | √ | ' ' | 资金池供应模型字段名称 |
| 8 | fusecolname | 资金池使用模型字段名称 | varchar | 100 |  | √ | ' ' | 资金池使用模型字段名称 |
| 9 | fusecol | 资金池使用模型字段标识 | varchar | 100 |  | √ | ' ' | 资金池使用模型字段标识 |
| 10 | fusefullcol | 资金池使用模型字段全标识 | varchar | 100 |  | √ | ' ' | 资金池使用模型字段全标识 |
| 11 | fusebalfullcol | 资金池供应模型字段全标识 | varchar | 100 |  | √ | ' ' | 资金池供应模型字段全标识 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fusebalcol | 资金池供应模型字段标识 | varchar | 100 |  | √ | ' ' | 资金池供应模型字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_useentity |  | fentryid |
| 2 | idx_occba_useentity_id |  | fid |

---

## 资金池使用方案-主表 t_occba_baluseplan

- **表名称：** 资金池使用方案-主表
- **表名：** t_occba_baluseplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseentity | 资金池使用方 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcomment | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 6 | fschemefilter | 执行条件存储字段 | text | 0 |  |  | null | 执行条件存储字段 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fentryname | 使用方单据体 | varchar | 80 |  | √ | ' ' | 使用方单据体,枚举: |
| 9 | fbalentity | 资金池供应方 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fbalfilter | 资金池供应方准入条件 | text | 0 |  |  | null | 资金池供应方准入条件 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fusefilter | 资金池使用方准入条件 | text | 0 |  |  | null | 资金池使用方准入条件 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 18 | fissyspreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_baluseplan_num |  | fnumber |
| 2 | pk_occba_baluseplan |  | fid |

---

## 资金池使用方案-多语言表 t_occba_baluseplan_l

- **表名称：** 资金池使用方案-多语言表
- **表名：** t_occba_baluseplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_baluseplan_flid |  | fid,flocaleid |
| 2 | pk_occba_baluseplan_l |  | fpkid |
