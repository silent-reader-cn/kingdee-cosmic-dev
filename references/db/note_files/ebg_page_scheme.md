# 分页方案-ebg_page_scheme

## 分页方案-多语言表 t_ebg_page_scheme_l

- **表名称：** 分页方案-多语言表
- **表名：** t_ebg_page_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ebg_page_scheme_l_pkey |  | fpkid |

---

## 分页方案单据体-子表 t_ebg_page_entity

- **表名称：** 分页方案单据体-子表
- **表名：** t_ebg_page_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fparam_select | 参数选择 | int8 | 64 |  |  | null | [分页参数类型 ebg_page_param](../note_files/ebg_page_param.md) |
| 3 | foperator | 运算符设置 | varchar | 50 |  | √ | ' ' | 运算符设置,枚举: + :加 - :减 * :乘 / :除以 > :大于 < :小于 >= :大于等于 <= :小于等于 == :等于 != :不等于 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbracket | 是否加括号 | varchar | 50 |  | √ | ' ' | 是否加括号,枚举: 1 :是 0 :否 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ebg_page_entity_pkey |  | fentryid |

---

## 分页方案-主表 t_ebg_page_scheme

- **表名称：** 分页方案-主表
- **表名：** t_ebg_page_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fsheme_type | 方案类型 | varchar | 50 |  | √ | ' ' | 方案类型,枚举: next :下一页预制方案 last :最后页预制方案 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fdetail | 说明 | varchar | 300 |  | √ | ' ' | 说明 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 11 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 13 | fcontent | 配置内容 | varchar | 500 |  | √ | ' ' | 配置内容 |
| 14 | fcombofield1 | fcombofield1 | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ebg_page_scheme_pkey |  | fid |
