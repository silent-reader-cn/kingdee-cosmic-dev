# 成本明细组件(二级)-pds_costdetailcomp2

## 成本明细分录-子表 t_pds_costdetailentry

- **表名称：** 成本明细分录-子表
- **表名：** t_pds_costdetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | ftaxamount | 含税成本额 | numeric | 23 | 10 | √ | 0 | 含税成本额 |
| 4 | fname | fname | varchar | 300 |  | √ | ' ' |  |
| 5 | fchildcount | fchildcount | int4 | 32 |  | √ | 0 |  |
| 6 | fprojectid | 寻源项目ID | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 7 | fischanged | 允许供应商修改 | bpchar | 1 |  | √ | '1' | 允许供应商修改 |
| 8 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fratio | 系数 | numeric | 19 | 6 | √ | 0 | 系数 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 12 | fcostitemid | 成本项目编码 | int8 | 64 |  | √ | 0 | [成本项目 pds_costitem](../pds_files/pds_costitem.md) |
| 13 | ftaxprice | 含税成本 | numeric | 23 | 10 | √ | 0 | 含税成本 |
| 14 | fdescription | 成本项目名称 | varchar | 510 |  | √ | ' ' | 成本项目名称 |
| 15 | famount | 未税成本额 | numeric | 23 | 10 | √ | 0 | 未税成本额 |
| 16 | fpurlistid | 标的ID | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 17 | fprice | 未税成本 | numeric | 23 | 10 | √ | 0 | 未税成本 |
| 18 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
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

## 成本明细分录-多语言表 t_pds_costdetailentry_l

- **表名称：** 成本明细分录-多语言表
- **表名：** t_pds_costdetailentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | fname | varchar | 300 |  | √ | ' ' |  |
| 2 | fnote | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 成本项目名称 | varchar | 510 |  | √ | ' ' | 成本项目名称 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

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

## 成本明细组件(二级)-主表 t_pds_costdetail

- **表名称：** 成本明细组件(二级)-主表
- **表名：** t_pds_costdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 3 | ftype | 组件类型 | bpchar | 1 |  | √ | '1' | 组件类型,枚举: 1 :一级 2 :二级 3 :多级 |
| 4 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 5 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 6 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_costdetail_pid |  | fparentid |
| 2 | pk_pds_costdetail |  | fid |

---

## 成本明细子分录-多语言表 t_pds_costdetailsubentry_l

- **表名称：** 成本明细子分录-多语言表
- **表名：** t_pds_costdetailsubentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fnote | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 成本项目名称 | varchar | 510 |  | √ | ' ' | 成本项目名称 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_costdetailsub_l |  | fpkid |
| 2 | idx_pds_costdetailsub_l_fid |  | fdetailid,flocaleid |

---

## 成本明细子分录-子表 t_pds_costdetailsubentry

- **表名称：** 成本明细子分录-子表
- **表名：** t_pds_costdetailsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 2 | ftaxamount | 含税成本额 | numeric | 23 | 10 | √ | 0 | 含税成本额 |
| 3 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 4 | fischanged | 允许供应商修改 | bpchar | 1 |  | √ | '1' | 允许供应商修改 |
| 5 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fratio | 系数 | numeric | 19 | 6 | √ | 0 | 系数 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fcostitemid | 成本项目编码 | int8 | 64 |  | √ | 0 | [成本项目 pds_costitem](../pds_files/pds_costitem.md) |
| 10 | ftaxprice | 含税成本 | numeric | 23 | 10 | √ | 0 | 含税成本 |
| 11 | fdescription | 成本项目名称 | varchar | 510 |  | √ | ' ' | 成本项目名称 |
| 12 | famount | 未税成本额 | numeric | 23 | 10 | √ | 0 | 未税成本额 |
| 13 | fpurlistid | fpurlistid | int8 | 64 |  | √ | 0 |  |
| 14 | fprice | 未税成本 | numeric | 23 | 10 | √ | 0 | 未税成本 |
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
