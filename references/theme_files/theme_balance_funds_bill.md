# 往来款项余额分析表-theme_balance_funds_bill

## 单据体-子表 t_balance_funds_entryent

- **表名称：** 单据体-子表
- **表名：** t_balance_funds_entryent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | famount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 4 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_balance_funds_entryent |  | fentryid |
| 2 | idx_funds_entryent_report |  | freportdate |

---

## 往来款项余额分析表-主表 t_theme_balance_funds

- **表名称：** 往来款项余额分析表-主表
- **表名：** t_theme_balance_funds

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fisleaf | 是否叶子节点 | bpchar | 1 |  | √ | '1' | 是否叶子节点 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fccounttype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型,枚举: 0 :应收款项合计 1 :应付款项合计 2 :应收账款 3 :应付账款 4 :合同资产 5 :其他应收款 6 :其他应付款 7 :预付账款 8 :预收账款 |
| 7 | frdetermination | 关联方 | int8 | 64 |  | √ | 0 | 关联关系认定表 theme_rdetermination_bill |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_balance_funds_rdete |  | fipoorgld,frdetermination |
| 2 | pk_theme_balance_funds |  | fid |
