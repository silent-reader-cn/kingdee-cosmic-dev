# 匹配规则集合-ebg_judging_conditions

## 规则集合匹配时取值单据体-子表 t_note_judgings

- **表名称：** 规则集合匹配时取值单据体-子表
- **表名：** t_note_judgings

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | febgparam_source | 规则匹配时取值 | varchar | 50 |  | √ | ' ' | 规则匹配时取值,枚举: ebg_field :银企属性 default :固定值 abs :取绝对值 origin :原值 pass :跳过 |
| 3 | fjudging_name | （废弃）判断条件名称 | varchar | 200 |  |  | ' ' | （废弃）判断条件名称 |
| 4 | fjudging_condition_desc | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fin_ebgfield | 填入银企字段 | varchar | 50 |  |  | ' ' | 填入银企字段,枚举: |
| 7 | fvalue | 固定值 | varchar | 50 |  | √ | ' ' | 固定值 |
| 8 | febgparam | （隐藏）银企属性字段 | varchar | 50 |  | √ | ' ' | （隐藏）银企属性字段 |
| 9 | frsp_judging | （废弃）匹配规则 | varchar | 50 |  | √ | ' ' | （废弃）匹配规则 |
| 10 | febg_field_type | （隐藏）银企属性类型 | varchar | 50 |  | √ | ' ' | （隐藏）银企属性类型 |
| 11 | fcondition | 匹配规则 | int8 | 64 |  | √ | 0 | [匹配规则 ebg_judging_condition](../note_files/ebg_judging_condition.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | febg_field | 银企属性 | varchar | 200 |  | √ | ' ' | 银企属性 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_note_judgings_fk |  | fid |
| 2 | pk_note_judgings |  | fentryid |

---

## 匹配规则集合-多语言表 t_note_judging_conditions_l

- **表名称：** 匹配规则集合-多语言表
- **表名：** t_note_judging_conditions_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则集合名称 | varchar | 1000 |  | √ | ' ' | 规则集合名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_note_judging_conds_l_0 |  | fid,flocaleid |
| 2 | pk_note_judging_conditions_l |  | fpkid |

---

## 规则集合不匹配时取值单据体-子表 t_note_judgings_n

- **表名称：** 规则集合不匹配时取值单据体-子表
- **表名：** t_note_judgings_n

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | febgparam_source | 规则集合不匹配时取值 | varchar | 50 |  | √ | ' ' | 规则集合不匹配时取值,枚举: ebg_field :银企属性 default :固定值 error :抛出异常 |
| 3 | fvalue | 固定值 | varchar | 50 |  | √ | ' ' | 固定值 |
| 4 | febgparam | （隐藏）银企属性字段 | varchar | 50 |  | √ | ' ' | （隐藏）银企属性字段 |
| 5 | febg_field_type | （隐藏）银企属性类型 | varchar | 50 |  | √ | ' ' | （隐藏）银企属性类型 |
| 6 | fjudging_condition_desc | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | febg_field | 银企属性 | varchar | 200 |  | √ | ' ' | 银企属性 |
| 10 | fin_ebgfield2 | 填入银企字段 | varchar | 50 |  |  | ' ' | 填入银企字段,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_note_judgings_n_fk |  | fid |
| 2 | pk_note_judgings_n |  | fentryid |

---

## 匹配规则集合-主表 t_note_judging_conditions

- **表名称：** 匹配规则集合-主表
- **表名：** t_note_judging_conditions

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 规则集合名称 | varchar | 50 |  | √ | ' ' | 规则集合名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 银行版本.应用 | int8 | 64 |  | √ | 0 | [银行应用列表 note_bank_app_list](../note_files/note_bank_app_list.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbiz_type_number | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: notePayable :应付票据 noteReceivable :应收票据 queryNoteDetail :待签收票据查询 queryNoteInfo :贴现试算查询 queryNoteSide :背面信息查询 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fbiz_type_new | 业务类型 | int8 | 64 |  |  | null | [低代码业务类型 note_codeless_type](../note_files/note_codeless_type.md) |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fjudge_type | 匹配规则类型 | varchar | 50 |  |  | ' ' | 匹配规则类型,枚举: request :请求 parse :解析 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 规则集合编码 | varchar | 50 |  | √ | ' ' | 规则集合编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_note_judging_conditions |  | fid |
| 2 | idx_note_judging_conditions |  | fnumber |
