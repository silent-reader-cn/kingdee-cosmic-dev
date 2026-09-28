# 关联方采购交易额分析表-theme_volume_trade_bill

## 关联方采购交易额分析表-主表 t_theme_volume_trade

- **表名称：** 关联方采购交易额分析表-主表
- **表名：** t_theme_volume_trade

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fratio | 关联采购占采购总金额比例（%） | numeric | 23 | 10 |  | null | 关联采购占采购总金额比例（%） |
| 6 | ftotal | 关联采购金额合计 | numeric | 23 | 10 |  | null | 关联采购金额合计 |
| 7 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcurrentamount | 当期采购总金额 | numeric | 23 | 10 |  | null | 当期采购总金额 |
| 10 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_volume_trade_report |  | freportdate,fipoorgld |
| 2 | pk_theme_volume_trade |  | fid |

---

## 单据体-子表 t_theme_vt_entryentity

- **表名称：** 单据体-子表
- **表名：** t_theme_vt_entryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | famount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | frdetermination | 关联方 | int8 | 64 |  | √ | 0 | [关联关系认定表 theme_rdetermination_bill](../theme_files/theme_rdetermination_bill.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_vt_entryentity_rdet |  | frdetermination |
| 2 | pk_theme_vt_entryentity |  | fentryid |
