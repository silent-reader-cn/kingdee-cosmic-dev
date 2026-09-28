# 匹配规则-ebg_judging_condition

## 匹配规则-主表 t_note_judging_condition

- **表名称：** 匹配规则-主表
- **表名：** t_note_judging_condition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 银行版本.应用 | int8 | 64 |  | √ | 0 | [银行应用列表 note_bank_app_list](../note_files/note_bank_app_list.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbiz_type_number | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: notePayable :应付票据 noteReceivable :应收票据 queryNoteDetail :待签收票据查询 queryNoteInfo :贴现试算查询 queryNoteSide :背面信息查询 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fbiz_type_new | 业务类型 | int8 | 64 |  |  | null | [低代码业务类型 note_codeless_type](../note_files/note_codeless_type.md) |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftype | 规则匹配类型 | varchar | 50 |  | √ | ' ' | 规则匹配类型,枚举: request :字段上传 out_stat :外层状态 inner_stat :内层状态 parse :解析 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fjudging_condition | fjudging_condition | varchar | 255 |  | √ | ' ' |  |
| 15 | fnumber | 规则编码 | varchar | 30 |  | √ | ' ' | 规则编码 |
| 16 | fcontent | 规则内容 | varchar | 1000 |  | √ | ' ' | 规则内容 |
| 17 | fjudging_condition_tag | fjudging_condition_tag | text | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_note_judging_condition |  | fid |
| 2 | idx_note_judging_condition |  | fnumber |

---

## 单据体-子表 t_note_judging_body

- **表名称：** 单据体-子表
- **表名：** t_note_judging_body

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | febgparam_source | 取值来源 | varchar | 50 |  | √ | ' ' | 取值来源,枚举: ebg_field :银企属性 node :报文节点 |
| 3 | ffilter_compare | 比较方式 | varchar | 50 |  | √ | ' ' | 比较方式,枚举: = :等于 != :不等于 is null :为空 is not null :不为空 contains :包含 not contains :不包含 in :在...中 not in :不在...中 start with :以...开始 end with :以...结束 > :大于 < :小于 >= :大于等于 <= :小于等于 |
| 4 | ffilter_link | 逻辑连接符 | varchar | 50 |  | √ | ' ' | 逻辑连接符,枚举: && :并且 \|\| :或者 |
| 5 | fcode_field | 状态码字段 | varchar | 50 |  | √ | ' ' | 状态码字段,枚举: out_code :外层状态码字段 inner_code :内层状态码字段 inner_code2 :内层状态码字段2 inner_code3 :内层状态码字段3 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ffilter_left_bracket | (隐藏)左括号 | varchar | 50 |  | √ | ' ' | (隐藏)左括号,枚举: ( :( (( :(( ((( :((( |
| 8 | fvalue | 值 | varchar | 50 |  | √ | ' ' | 值 |
| 9 | febgparam | （隐藏）银企属性字段 | varchar | 50 |  | √ | ' ' | （隐藏）银企属性字段 |
| 10 | ffilter_right_bracket | (隐藏)右括号 | varchar | 50 |  | √ | ' ' | (隐藏)右括号,枚举: ) :) )) :)) ))) :))) |
| 11 | febg_field_type | （隐藏）银企属性类型 | varchar | 50 |  | √ | ' ' | （隐藏）银企属性类型 |
| 12 | fnode | 报文节点 | varchar | 50 |  |  | ' ' | 报文节点 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | febg_field | 银企属性 | varchar | 200 |  | √ | ' ' | 银企属性 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_note_judging_body |  | fentryid |
| 2 | idx_note_judging_body_fk |  | fid |

---

## 匹配规则-多语言表 t_note_judging_condition_l

- **表名称：** 匹配规则-多语言表
- **表名：** t_note_judging_condition_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 1000 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_note_judging_condition_l |  | fpkid |
| 2 | idx_note_judging_condition_l_0 |  | fid,flocaleid |
