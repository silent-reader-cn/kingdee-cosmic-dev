# 信用等级-ccm_newgrade

## 信用等级-多语言表 t_ccm_grade_l

- **表名称：** 信用等级-多语言表
- **表名：** t_ccm_grade_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 信用等级名称 | varchar | 80 |  | √ | ' ' | 信用等级名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 信用等级说明 | varchar | 600 |  | √ | ' ' | 信用等级说明 |
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

## 等级标准详情-子表 t_ccm_gradeentry

- **表名称：** 等级标准详情-子表
- **表名：** t_ccm_gradeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | fsinglecurcontrol | 币种隔离 | bpchar | 1 |  | √ | '0' | 币种隔离 |
| 4 | forgid | 授信组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fschemeid | 信用控制方案 | int8 | 64 |  | √ | 0 | [信用控制方案 ccm_schemes](../ccm_files/ccm_schemes.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | foveramount | 信用逾期额度 | numeric | 23 | 10 | √ | 0 | 信用逾期额度 |
| 8 | fsingleamount | 单笔限额 | numeric | 23 | 10 | √ | 0 | 单笔限额 |
| 9 | fbalance | 信用额度 | numeric | 23 | 10 | √ | 0.0000000000 | 信用额度 |
| 10 | fformula | 信用公式 | varchar | 510 |  |  | ' ' | 信用公式 |
| 11 | fday | 信用天数 | int8 | 64 |  | √ | 0 | 信用天数 |
| 12 | fpresscontrol | 压批批数 | int8 | 64 |  | √ | 0 | 压批批数 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fcheckstatus | 信用检查状态 | varchar | 50 |  | √ | ' ' | 信用检查状态,枚举: CHECKED :信用检查 UNCHECKED :信用免检 |

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
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 信用等级名称 | varchar | 80 |  | √ | ' ' | 信用等级名称 |
| 4 | fgroupid | 信用等级方案 | int8 | 64 |  | √ | 0 | [信用等级方案 ccm_newgradegroup](../ccm_files/ccm_newgradegroup.md) |
| 5 | frange_value_from | 分值范围从 | numeric | 23 | 10 | √ | 0.0000000000 | 分值范围从 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdescription | 信用等级说明 | varchar | 600 |  | √ | ' ' | 信用等级说明 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fisgroup | 类别指标 | bpchar | 1 |  | √ | '0' | 类别指标 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 60 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | frange_value_to | 分值范围至(小于) | numeric | 23 | 10 | √ | 0.0000000000 | 分值范围至(小于) |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fenable | 使用状态 | varchar | 60 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fnumber | 信用等级编码 | varchar | 120 |  | √ | ' ' | 信用等级编码 |
| 19 | fisdefault | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ccm_grade_pkey |  | fid |
| 2 | idx_ccm_grade_fnumber |  | fnumber |
