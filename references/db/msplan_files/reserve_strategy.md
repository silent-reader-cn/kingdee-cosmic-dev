# 预留策略-reserve_strategy

## 预留策略-主表 t_reserve_stragtegy

- **表名称：** 预留策略-主表
- **表名：** t_reserve_stragtegy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | f_enable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 4 | f_number | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | f_require_bill_id | 需求单据 | varchar | 128 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | f_desc | 描述 | varchar | 80 |  | √ | ' ' | 描述 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | f_filter_value | 过滤器值 | varchar | 80 |  | √ | ' ' | 过滤器值 |
| 12 | f_filter_value_tag | 过滤器值_详情 | text | 0 |  |  | null | 过滤器值_详情 |
| 13 | f_name | 名称 | varchar | 510 |  | √ | ' ' | 名称 |
| 14 | f_creator_id | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | f_status | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reserve_stragtegy_fnum |  | f_number |
| 2 | pk_t_reserve_stragtegy |  | fid |

---

## 预留规则信息-子表 t_reserve_stragtegyentry

- **表名称：** 预留规则信息-子表
- **表名：** t_reserve_stragtegyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | f_pick_inv_rule | 预留规则 | varchar | 80 |  | √ | ' ' | 预留规则 |
| 3 | f_pick_inv_rule_id | 预留规则 | int8 | 64 |  | √ | 0 | [预留规则 reserve_rule](../msplan_files/reserve_rule.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | f_rule_result_plugin | 结果插件 | varchar | 512 |  | √ | ' ' | 结果插件 |
| 6 | f_rule_way | 结果取值方式 | bpchar | 1 |  | √ | '1' | 结果取值方式,枚举: 1 :尽量预留 2 :不足不预留 3 :按百分比预留 4 :插件预留 |
| 7 | f_rule_seq | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_reserve_stragtegyentry |  | fentryid |
| 2 | idx_reserve_stragtegy_efid |  | fid |

---

## 预留策略-多语言表 t_reserve_stragtegy_l

- **表名称：** 预留策略-多语言表
- **表名：** t_reserve_stragtegy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | f_name | 名称 | varchar | 510 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_reserve_stragtegy_l |  | fpkid |
| 2 | idx_reserve_stragtegy_l_fid |  | fid,flocaleid |
