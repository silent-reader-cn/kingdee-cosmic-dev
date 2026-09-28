# 预留规则-reserve_rule

## 预留规则-主表 t_reserve_rule

- **表名称：** 预留规则-主表
- **表名：** t_reserve_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsupfilterval | 供应来源过滤值 | varchar | 255 |  | √ | ' ' | 供应来源过滤值 |
| 4 | f_number | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcrossprjsupply | 考虑跨项目供应 | bpchar | 1 |  | √ | '0' | 考虑跨项目供应 |
| 7 | f_use_plugin | 插件模式 | bpchar | 1 |  | √ | '0' | 插件模式 |
| 8 | f_rule_plugin | 规则插件 | varchar | 128 |  | √ | ' ' | 规则插件 |
| 9 | fsupsrcobj | 供应来源 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fdemandsrcobj | 需求单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fispredict | 预计入 | bpchar | 1 |  | √ | '0' | 预计入 |
| 17 | f_name | 规则 | varchar | 510 |  | √ | ' ' | 规则 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fmatverstructmatch | 物料版本严格匹配 | bpchar | 1 |  | √ | '0' | 物料版本严格匹配 |
| 20 | f_rule_desc | 规则名称 | varchar | 255 |  | √ | ' ' | 规则名称 |
| 21 | fsupfilterval_tag | 供应来源过滤值_详情 | text | 0 |  |  | null | 供应来源过滤值_详情 |
| 22 | fauxstructmatch | 辅助属性严格匹配 | bpchar | 1 |  | √ | '0' | 辅助属性严格匹配 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reserve_rule_fnum |  | f_number |
| 2 | pk_reserve_rule |  | fid |

---

## 预留规则-子表 t_reserve_ruleentry

- **表名称：** 预留规则-子表
- **表名：** t_reserve_ruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | f_right_bracket |  | varchar | 32 |  | √ | ' ' | ,枚举: A :) B :)) |
| 3 | f_std_inv_col | 供应来源字段 | varchar | 128 |  | √ | ' ' | 供应来源字段 |
| 4 | f_require_bill_date | 日期取值方式 | timestamp | 0 |  |  | null | 日期取值方式 |
| 5 | f_left_bracket |  | varchar | 32 |  | √ | ' ' | ,枚举: A :( B :(( |
| 6 | f_logic | 逻辑 | varchar | 120 |  | √ | ' ' | 逻辑,枚举: A :并且 B :或 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | f_std_inv_col_no | 字段标识 | varchar | 128 |  | √ | ' ' | 字段标识 |
| 10 | f_compare_type | 条件 | varchar | 64 |  | √ | ' ' | 条件,枚举: A :等于 H :不等于 B :大于 C :小于 D :在…中 I :不在...中 E :不为空 F :为空 G :字段等于或为空 = :字段等于 > :字段大于 < :字段小于 >= :字段大于等于 <= :字段小于等于 |
| 11 | f_require_bill_col | 取值方式 | varchar | 2000 |  | √ | ' ' | 取值方式 |
| 12 | f_require_bill_col_no | 取值方式标识 | varchar | 2000 |  | √ | ' ' | 取值方式标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reserve_rule_e_fid |  | fid |
| 2 | pk_t_reserve_ruleentry |  | fentryid |

---

## 预留规则-多语言表 t_reserve_rule_l

- **表名称：** 预留规则-多语言表
- **表名：** t_reserve_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | f_name | 规则 | varchar | 510 |  | √ | ' ' | 规则 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_reserve_rule_l_id |  | fid,flocaleid |
| 2 | pk_t_reserve_rule_l |  | fpkid |

---

## 预留顺序-子表 t_reserve_rulesortentry

- **表名称：** 预留顺序-子表
- **表名：** t_reserve_rulesortentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | f_sort_field | 排序字段 | varchar | 50 |  | √ | ' ' | 排序字段 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | f_sort_way | 排序方式 | varchar | 50 |  | √ | ' ' | 排序方式,枚举: asc :升序 desc :降序 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | f_sort_field_no | 排序字段标识 | varchar | 50 |  | √ | ' ' | 排序字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_reserve_rulesortentry |  | fentryid |
| 2 | idx_reserve_rule_se_fid |  | fid |
