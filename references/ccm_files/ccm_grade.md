# 信用等级-ccm_grade

## 信用等级-多语言表 t_ccm_grade_l

- **表名称：** 信用等级-多语言表
- **表名：** t_ccm_grade_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 说明 | varchar | 600 |  | √ | ' ' | 说明 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_grade_l_0 |  | fid,flocaleid |
| 2 | t_ccm_grade_l_pkey |  | fpkid |

---

## 等级详情-子表 t_ccm_gradeentry

- **表名称：** 等级详情-子表
- **表名：** t_ccm_gradeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbalance | 信用额度 | numeric | 23 | 10 | √ | 0.0000000000 | 信用额度 |
| 3 | fformula | 信用公式 | varchar | 510 |  |  | ' ' | 信用公式 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fday | 信用期限（天） | int8 | 64 |  | √ | 0 | 信用期限（天） |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ccm_gradeentry_pkey |  | fentryid |
| 2 | idx_ccm_gradeentity_fk |  | fid |

---

## 信用等级-主表 t_ccm_grade

- **表名称：** 信用等级-主表
- **表名：** t_ccm_grade

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | frange_value_from | 分值范围从 | numeric | 23 | 10 | √ | 0.0000000000 | 分值范围从 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdescription | 说明 | varchar | 600 |  | √ | ' ' | 说明 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 60 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | frange_value_to | 分值范围至 | numeric | 23 | 10 | √ | 0.0000000000 | 分值范围至 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | varchar | 60 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 120 |  | √ | ' ' | 编码 |
| 14 | fisdefault | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ccm_grade_pkey |  | fid |
| 2 | idx_ccm_grade_fnumber |  | fnumber |
