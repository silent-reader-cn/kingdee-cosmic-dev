# 上市条件类型-ipo_list_conditions_type

## 上市条件类型-多语言表 t_ipo_lconditions_type_l

- **表名称：** 上市条件类型-多语言表
- **表名：** t_ipo_lconditions_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 50 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ipo_lconditions_type_l_0 |  | fid |
| 2 | pk_ipo_lconditions_type_l |  | fpkid |

---

## 上市条件类型-主表 t_ipo_lconditions_type

- **表名称：** 上市条件类型-主表
- **表名：** t_ipo_lconditions_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmarket_position | 板块定位 | varchar | 3000 |  | √ | ' ' | 板块定位 |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 4 | fpublish_condition_tag | 发行条件_详情 | text | 0 |  |  | null | 发行条件_详情 |
| 5 | fpublish_condition | 发行条件 | varchar | 3000 |  | √ | ' ' | 发行条件 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fstandard_content_tag | 标准内容_详情 | text | 0 |  |  | null | 标准内容_详情 |
| 11 | fipo_condition_tag | 上市条件_详情 | text | 0 |  |  | null | 上市条件_详情 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 14 | fshowrows | 报表显示行次 | int8 | 64 |  | √ | 0 | 报表显示行次 |
| 15 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [上市条件类型 ipo_list_conditions_type](../ipobase_files/ipo_list_conditions_type.md) |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fstandard_content | 标准内容 | varchar | 3000 |  | √ | ' ' | 标准内容 |
| 18 | fmarket_position_tag | 板块定位_详情 | text | 0 |  |  | null | 板块定位_详情 |
| 19 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 20 | fsummary_tag | 标准摘要_详情 | text | 0 |  |  | null | 标准摘要_详情 |
| 21 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 22 | fipo_condition | 上市条件 | varchar | 3000 |  | √ | ' ' | 上市条件 |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fsummary | 标准摘要 | varchar | 3000 |  | √ | ' ' | 标准摘要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lconditions_type_name |  | fname |
| 2 | pk_ipo_lconditions_type |  | fid |
| 3 | idx_lconditions_type_number |  | fnumber |
