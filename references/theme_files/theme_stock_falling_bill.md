# 存货构成与跌价分析表-theme_stock_falling_bill

## 存货构成与跌价分析表-主表 t_theme_stock_falling

- **表名称：** 存货构成与跌价分析表-主表
- **表名：** t_theme_stock_falling

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fstockgrowthrate | 存货增长率（%） | numeric | 23 | 10 |  | null | 存货增长率（%） |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fflowproperty | 流动资产 | numeric | 23 | 10 |  | null | 流动资产 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsfratio | 存货占流动资产比例（%） | numeric | 23 | 10 |  | null | 存货占流动资产比例（%） |
| 8 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_stock_falling |  | fid |
| 2 | idx_stock_falling_report |  | fipoorgld,freportdate |

---

## 存货单据体-子表 t_theme_sf_entity

- **表名称：** 存货单据体-子表
- **表名：** t_theme_sf_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 3 | fbookbalance | 账面余额 | numeric | 23 | 10 |  | null | 账面余额 |
| 4 | fitemratio | 占比 | numeric | 23 | 10 |  | null | 占比 |
| 5 | ffailingprepare | 跌价准备 | numeric | 23 | 10 |  | null | 跌价准备 |
| 6 | fbookamount | 账面价值 | numeric | 23 | 10 |  | null | 账面价值 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | faccrualratio | 计提比例 | numeric | 23 | 10 |  | null | 计提比例 |
| 9 | fitemname | 项目名 | varchar | 50 |  | √ | ' ' | 项目名 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sf_entity_item |  | fitemname |
| 2 | pk_theme_sf_entity |  | fentryid |
