# 成本明细分析-src_costdetailentryanaly

## 成本明细分析-主表 t_pds_costdetailentry

- **表名称：** 成本明细分析-主表
- **表名：** t_pds_costdetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | ftaxamount | 含税成本额 | numeric | 23 | 10 | √ | 0 | 含税成本额 |
| 4 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 5 | fchildcount | fchildcount | int4 | 32 |  | √ | 0 |  |
| 6 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 7 | fischanged | fischanged | bpchar | 1 |  | √ | '1' |  |
| 8 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fratio | fratio | numeric | 19 | 6 | √ | 0 |  |
| 10 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 11 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 12 | fcostitemid | 成本项目编号 | int8 | 64 |  | √ | 0 | 成本项目 pds_costitem |
| 13 | ftaxprice | 含税成本 | numeric | 23 | 10 | √ | 0 | 含税成本 |
| 14 | fdescription | 成本项目名称 | varchar | 510 |  | √ | ' ' | 成本项目名称 |
| 15 | famount | 未税成本额 | numeric | 23 | 10 | √ | 0 | 未税成本额 |
| 16 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 17 | fprice | 未税成本 | numeric | 23 | 10 | √ | 0 | 未税成本 |
| 18 | fparententryid | 父分录ID | int8 | 64 |  | √ | 0 | 父分录ID |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_costdetailentry_purid |  | fpurlistid |
| 2 | idx_pds_costdetailentry_fid |  | fid |
| 3 | idx_pds_costdetailentry_pid |  | fprojectid |
| 4 | idx_pds_costdetailentry_cosid |  | fcostitemid |
| 5 | pk_pds_costdetailentry |  | fentryid |

---

## 成本明细分析-多语言表 t_pds_costdetailentry_l

- **表名称：** 成本明细分析-多语言表
- **表名：** t_pds_costdetailentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_costdetailentry_l |  | fpkid |
| 2 | idx_pds_costdetailentry_l_fentryid |  | fentryid,flocaleid |

---

## 成本明细分录-子表 t_pds_costdetailsubentry

- **表名称：** 成本明细分录-子表
- **表名：** t_pds_costdetailsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 明细数量 | numeric | 23 | 10 | √ | 0 | 明细数量 |
| 2 | ftaxamount | 明细含税成本额 | numeric | 23 | 10 | √ | 0 | 明细含税成本额 |
| 3 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 4 | fischanged | fischanged | bpchar | 1 |  | √ | '1' |  |
| 5 | funitid | 明细计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 6 | fratio | 明细系数 | numeric | 19 | 6 | √ | 0 | 明细系数 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fnote | 明细备注 | varchar | 255 |  | √ | ' ' | 明细备注 |
| 9 | fcostitemid | 明细成本项目编码 | int8 | 64 |  | √ | 0 | 成本项目 pds_costitem |
| 10 | ftaxprice | 明细含税成本 | numeric | 23 | 10 | √ | 0 | 明细含税成本 |
| 11 | fdescription | 明细成本项目名称 | varchar | 510 |  | √ | ' ' | 明细成本项目名称 |
| 12 | famount | 明细未税成本额 | numeric | 23 | 10 | √ | 0 | 明细未税成本额 |
| 13 | fpurlistid | fpurlistid | int8 | 64 |  | √ | 0 |  |
| 14 | fprice | 明细未税成本 | numeric | 23 | 10 | √ | 0 | 明细未税成本 |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_costdetailsubentry |  | fdetailid |
| 2 | idx_pds_costdetailsubentry_eid |  | fentryid |
