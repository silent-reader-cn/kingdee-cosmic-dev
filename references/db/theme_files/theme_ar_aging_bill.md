# 应收账款账龄结构分析表-theme_ar_aging_bill

## 应收账款账龄结构分析表-主表 t_theme_ar_aging

- **表名称：** 应收账款账龄结构分析表-主表
- **表名：** t_theme_ar_aging

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | faccrualtype | 计提类型 | varchar | 50 |  | √ | ' ' | 计提类型,枚举: 0 :单项计堤 1 :按账龄分组计提 |
| 7 | fitemname | 计提项名 | varchar | 50 |  | √ | ' ' | 计提项名 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_aging_item |  | fipoorgld,fitemname |
| 2 | pk_theme_ar_aging |  | fid |

---

## 报告数据-子表 t_theme_ar_aging_entity

- **表名称：** 报告数据-子表
- **表名：** t_theme_ar_aging_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbaddebtavgrate | 坏账准备平均计提率（%） | numeric | 23 | 10 |  | null | 坏账准备平均计提率（%） |
| 3 | fbaddebt | 坏账准备 | numeric | 23 | 10 |  | null | 坏账准备 |
| 4 | fbookbalance | 账面余额 | numeric | 23 | 10 |  | null | 账面余额 |
| 5 | fbookamount | 账面价值 | numeric | 23 | 10 |  | null | 账面价值 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 8 | fbbratio | 账面余额 占比 | numeric | 23 | 10 |  | null | 账面余额 占比 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_ar_aging_entity |  | fentryid |
| 2 | idx_ar_aging_entity_report |  | freportdate |
