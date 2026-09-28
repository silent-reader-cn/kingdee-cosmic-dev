# 营业成本构成分析表-theme_operating_cost_bill

## 单据体-子表 t_theme_oc_entryentity

- **表名称：** 单据体-子表
- **表名：** t_theme_oc_entryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fratio | 占比 | numeric | 23 | 10 |  | null | 占比 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | famount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 5 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_oc_entryentity_report |  | freportdate |
| 2 | pk_theme_oc_entryentity |  | fentryid |

---

## 营业成本构成分析表-主表 t_theme_operating_cost

- **表名称：** 营业成本构成分析表-主表
- **表名：** t_theme_operating_cost

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fisleaf | 是否叶子节点 | bpchar | 1 |  | √ | ' ' | 是否叶子节点 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fccounttype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型,枚举: 0 :主营业务成本 1 :其他业务成本 2 :合计 3 :主营业务成本构成 4 :主营业务成本构成合计 |
| 7 | fitemname | 项目名 | varchar | 50 |  | √ | ' ' | 项目名 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_operating_cost_item |  | fitemname |
| 2 | pk_theme_operating_cost |  | fid |
