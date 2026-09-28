# 内部单据字段重置-ism_settleparam

## 内部单据字段重置-多语言表 t_ism_settleparam_l

- **表名称：** 内部单据字段重置-多语言表
- **表名：** t_ism_settleparam_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | '' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ism_settleparam_l |  | fpkid |
| 2 | idx_t_ism_settleparam_l_id |  | fid,flocaleid |

---

## 业务参数信息-子表 t_ism_settleparam_e

- **表名称：** 业务参数信息-子表
- **表名：** t_ism_settleparam_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconstantsdesc | 常量 | varchar | 50 |  | √ | ' ' | 常量 |
| 3 | ftargetfieldkey | 通用目标字段标识 | varchar | 50 |  | √ | ' ' | 通用目标字段标识 |
| 4 | ftargetfieldname | 通用目标字段名称 | varchar | 50 |  | √ | ' ' | 通用目标字段名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcolumntype | 项类型 | bpchar | 3 |  | √ | ' ' | 项类型,枚举: com :通用 sup :供应 dem :需求 |
| 7 | fvaluetype | 取值方式 | bpchar | 1 |  | √ | 'e' | 取值方式,枚举: e :常量值 c :按条件取值 |
| 8 | fconstants_tag | 常量值_详情 | text | 0 |  |  | null | 常量值_详情 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fconstants | 常量值 | varchar | 255 |  | √ | ' ' | 常量值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ism_settleparam_e |  | fentryid |
| 2 | idx_t_ism_settleparam_e_id |  | fid,fentryid |

---

## 内部单据字段重置-主表 t_ism_settleparam

- **表名称：** 内部单据字段重置-主表
- **表名：** t_ism_settleparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | '' | 描述 |
| 6 | fsettleorg | 供应方业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fowner | 需求方业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fstatus | 数据状态 | varchar | 60 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | varchar | 60 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 120 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ism_settleparam |  | fid |
| 2 | idx_fsettleorg_fowner |  | fsettleorg,fowner |

---

## 匹配条件单据体-子表 t_ism_settleparam_mc

- **表名称：** 匹配条件单据体-子表
- **表名：** t_ism_settleparam_mc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fright |  | varchar | 10 |  | √ | ' ' | ,枚举: ) :) )) :)) ))) :))) |
| 3 | fconditionvalue | 条件值 | varchar | 2000 |  | √ | ' ' | 条件值 |
| 4 | fconditionvaluestr | 条件值内容 | varchar | 255 |  | √ | ' ' | 条件值内容 |
| 5 | fleft |  | varchar | 10 |  | √ | ' ' | ,枚举: ( :( (( :(( ((( :((( |
| 6 | fconditiondimkey | 条件维度标识 | varchar | 100 |  | √ | ' ' | 条件维度标识 |
| 7 | fcomparison | 比较符 | varchar | 10 |  | √ | 'in' | 比较符,枚举: in :在…中 not in :不在...中 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fconditondimtext | 条件维度 | varchar | 100 |  | √ | ' ' | 条件维度 |
| 10 | flogic | 逻辑 | varchar | 5 |  | √ | 'and' | 逻辑,枚举: and :并且 or :或者 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fconditionvaluestr_tag | 条件值内容_详情 | text | 0 |  |  | null | 条件值内容_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ism_settleparam_mc |  | fentryid |
| 2 | idx_t_ism_settleparam_mc_id |  | fid,fentryid |
