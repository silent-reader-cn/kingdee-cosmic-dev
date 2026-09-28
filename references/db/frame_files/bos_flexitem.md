# bos_flexitem-bos_flexitem

## 单据体-子表 t_bas_flex_property

- **表名称：** 单据体-子表
- **表名：** t_bas_flex_property

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffiltercondition_tag | ffiltercondition_tag | text | 0 |  |  | null |  |
| 3 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 4 | fdisprops | fdisprops | varchar | 200 |  | √ | ' ' |  |
| 5 | fispreset | fispreset | bpchar | 1 |  | √ | '0' |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fassistanttype | fassistanttype | int8 | 64 |  |  | null |  |
| 8 | fdatamaxlen | fdatamaxlen | int8 | 64 |  | √ | 20 |  |
| 9 | fstatus | fstatus | bpchar | 1 |  | √ | ' ' |  |
| 10 | fvaluesource | 值来源 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 13 | fflexfield | 弹性域字段 | varchar | 30 |  | √ | ' ' | 弹性域字段 |
| 14 | fissystem | fissystem | bpchar | 1 |  | √ | '0' |  |
| 15 | fforbidderid | fforbidderid | int8 | 64 |  | √ | 0 |  |
| 16 | ffiltercondition | ffiltercondition | varchar | 512 |  | √ | ' ' |  |
| 17 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 18 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 19 | fname | fname | varchar | 30 |  | √ | ' ' |  |
| 20 | fcreatetime | fcreatetime | timestamp | 0 |  | √ | LOCALTIMESTAMP |  |
| 21 | findex | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 22 | fvaluetype | 值类型 | bpchar | 1 |  | √ | ' ' | 值类型,枚举: |
| 23 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 24 | forgfunc | forgfunc | int8 | 64 |  | √ | 0 |  |
| 25 | fctrlstrategy | fctrlstrategy | varchar | 10 |  | √ | ' ' |  |
| 26 | fenable | fenable | bpchar | 1 |  | √ | '0' |  |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | fforbiddate | fforbiddate | timestamp | 0 |  |  | null |  |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 31 | fdatatype | 字段类型 | varchar | 200 |  | √ | ' ' | 字段类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_flex_property_fid_fnumber_key |  | fid,fnumber |
| 2 | t_bas_flex_property_pkey |  | fentryid |
| 3 | t_bas_flex_property_fflexfield_key |  | fflexfield |
| 4 | idx_bas_flex_prop_fidfnumber |  | fid,fnumber |

---

## bos_flexitem-主表 t_bas_flex

- **表名称：** bos_flexitem-主表
- **表名：** t_bas_flex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fseparator | fseparator | varchar | 10 |  | √ | ' ' |  |
| 3 | fdisplayproperty | fdisplayproperty | bpchar | 1 |  | √ | '2' |  |
| 4 | ftable | 数据表 | varchar | 25 |  | √ | ' ' | 数据表 |
| 5 | fdisplayformat | fdisplayformat | int8 | 64 |  | √ | 0 |  |
| 6 | fnumber | 编码 | varchar | 10 |  | √ | ' ' | 编码 |
| 7 | fformid | 表单标识 | varchar | 36 |  | √ | ' ' | 表单标识 |
| 8 | fbasedataservice | fbasedataservice | varchar | 200 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_flex_pkey |  | fid |
| 2 | idx_bas_flex_fnumber |  | fnumber |

---

## bos_flexitem-多语言表 t_bas_flex_l

- **表名称：** bos_flexitem-多语言表
- **表名：** t_bas_flex_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 200 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_flex_l_fid |  | fid,flocaleid |
| 2 | t_bas_flex_l_pkey |  | fpkid |

---

## 单据体-多语言表 t_bas_flex_property_l

- **表名称：** 单据体-多语言表
- **表名：** t_bas_flex_property_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 60 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | fdescription | varchar | 200 |  | √ | ' ' |  |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_flex_property_fentryid |  | fentryid,flocaleid |
| 2 | t_bas_flex_property_l_pkey |  | fpkid |
