# 主营业务收入构成分析表（按业务板块）-theme_mb_service_bill

## 主营业务收入构成分析表（按业务板块）-主表 t_theme_mb_service

- **表名称：** 主营业务收入构成分析表（按业务板块）-主表
- **表名：** t_theme_mb_service

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fccounttype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型,枚举: 0 :合计 |
| 6 | fitemname | 项目名 | varchar | 50 |  | √ | ' ' | 项目名 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_mb_service |  | fid |
| 2 | idx_mb_service_item |  | fitemname |

---

## 单据体-子表 t_theme_mbs_entryentity

- **表名称：** 单据体-子表
- **表名：** t_theme_mbs_entryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgrossprofitrate | 毛利率 | numeric | 23 | 10 |  | null | 毛利率 |
| 3 | fcostsales | 销售成本 | numeric | 23 | 10 |  | null | 销售成本 |
| 4 | fratio | 占比 | numeric | 23 | 10 |  | null | 占比 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fcostgrossprofit | 销售毛利 | numeric | 23 | 10 |  | null | 销售毛利 |
| 7 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 8 | fsalesrevenue | 销售收入 | numeric | 23 | 10 |  | null | 销售收入 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbs_entryentity_report |  | freportdate |
| 2 | pk_theme_mbs_entryentity |  | fentryid |
