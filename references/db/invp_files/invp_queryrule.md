# 因子取数规则-invp_queryrule

## 匹配规则-子表 t_invp_queryrule_match

- **表名称：** 匹配规则-子表
- **表名：** t_invp_queryrule_match

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fleftbracket | 左括号 | varchar | 50 |  | √ | ' ' | 左括号,枚举: :空 :空 : : ( :( (( :(( ((( :((( |
| 3 | fsrcmatchfield | 来源实体字段 | varchar | 100 |  | √ | ' ' | 来源实体字段 |
| 4 | fmatchtype | 匹配类型 | varchar | 50 |  | √ | ' ' | 匹配类型,枚举: A :直接匹配 B :分组匹配 |
| 5 | frightbracket | 右括号 | varchar | 50 |  | √ | ' ' | 右括号,枚举: :空 :空 : : ) :) )) :)) ))) :))) |
| 6 | fsrcmatchfieldkey | 来源实体字段（标识） | varchar | 255 |  | √ | ' ' | 来源实体字段（标识） |
| 7 | fldmatchfield | 库存水位维度字段 | varchar | 100 |  | √ | ' ' | 库存水位维度字段 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fmatchgroup | 分组关系 | int8 | 64 |  | √ | 0 | [数据分组关系 msmod_datagrouprelation](../mscommon_files/msmod_datagrouprelation.md) |
| 10 | flogic | 逻辑 | varchar | 50 |  | √ | ' ' | 逻辑,枚举: and :并且 or :或者 |
| 11 | fldmatchfieldkey | 库存水位维度字段（标识） | varchar | 255 |  | √ | ' ' | 库存水位维度字段（标识） |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_queryrule_match_fid |  | fid |
| 2 | pk_invp_queryrule_match |  | fentryid |

---

## 因子取数规则-主表 t_invp_queryrule

- **表名称：** 因子取数规则-主表
- **表名：** t_invp_queryrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fsrcfilterjson | 来源实体过滤条件（json） | varchar | 255 |  | √ | ' ' | 来源实体过滤条件（json） |
| 5 | fsrcfilterformula_tag | 来源实体过滤条件（表达式）_详情 | text | 0 |  |  | null | 来源实体过滤条件（表达式）_详情 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fleveldimension | 库存水位维度 | int8 | 64 |  | √ | 0 | [库存水位维度 msplan_plan_dimension](../msplan_files/msplan_plan_dimension.md) |
| 8 | fsrcentity | 来源实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fsrcfield | 来源字段 | varchar | 50 |  | √ | ' ' | 来源字段 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsrcfieldkey | 来源字段（标识） | varchar | 50 |  | √ | ' ' | 来源字段（标识） |
| 15 | fsrcfilterjson_tag | 来源实体过滤条件（json）_详情 | text | 0 |  |  | null | 来源实体过滤条件（json）_详情 |
| 16 | fsrcfilterformula | 来源实体过滤条件（表达式） | varchar | 255 |  | √ | ' ' | 来源实体过滤条件（表达式） |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fsrcfiltercondition | 来源实体过滤条件 | varchar | 255 |  | √ | ' ' | 来源实体过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_queryrule_fnum |  | fnumber |
| 2 | pk_invp_queryrule |  | fid |

---

## 取数优先级-子表 t_invp_queryrule_order

- **表名称：** 取数优先级-子表
- **表名：** t_invp_queryrule_order

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forderfield | 排序字段 | varchar | 100 |  | √ | ' ' | 排序字段 |
| 3 | forder | 排序方式 | varchar | 50 |  | √ | ' ' | 排序方式,枚举: asc :升序 desc :降序 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | forderfieldkey | 排序字段（标识） | varchar | 255 |  | √ | ' ' | 排序字段（标识） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invp_queryrule_order |  | fentryid |
| 2 | idx_invp_queryrule_order_fid |  | fid |

---

## 因子取数规则-多语言表 t_invp_queryrule_l

- **表名称：** 因子取数规则-多语言表
- **表名：** t_invp_queryrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_queryrule_l |  | fid,flocaleid |
| 2 | pk_invp_queryrule_l |  | fpkid |
