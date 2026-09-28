# 标的供应商-src_itemsupplier

## 标的供应商-主表 t_src_purlist

- **表名称：** 标的供应商-主表
- **表名：** t_src_purlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 3 | fsourceid | fsourceid | int8 | 64 |  | √ | 0 |  |
| 4 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 5 | fmaintainclause | fmaintainclause | varchar | 50 |  | √ | ' ' |  |
| 6 | forigin | 发起方 | varchar | 30 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 7 | fchgsrcbillid | fchgsrcbillid | int8 | 64 |  | √ | 0 |  |
| 8 | fsumamount | fsumamount | numeric | 23 | 10 | √ | 0 |  |
| 9 | fbizschemeid | fbizschemeid | int8 | 64 |  | √ | 0 |  |
| 10 | fispurlistcomp | fispurlistcomp | bpchar | 1 |  | √ | '1' |  |
| 11 | fcondition | 邀请条件 | varchar | 2000 |  | √ | ' ' | 邀请条件 |
| 12 | ftaxtype | ftaxtype | bpchar | 1 |  | √ | ' ' |  |
| 13 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 14 | fparentid | 父单据ID | varchar | 30 |  | √ | ' ' | 父单据ID |
| 15 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 16 | fentitykey | 组件标识 | varchar | 30 |  | √ | ' ' | 组件标识 |
| 17 | fdecisiontype | fdecisiontype | bpchar | 1 |  | √ | ' ' |  |
| 18 | fsumqty | fsumqty | numeric | 23 | 10 | √ | 0 |  |
| 19 | fbidchangeid | fbidchangeid | int8 | 64 |  | √ | 0 |  |
| 20 | fcosttypeid | fcosttypeid | int8 | 64 |  | √ | 0 |  |
| 21 | fpurtype | fpurtype | varchar | 30 |  | √ | ' ' |  |
| 22 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 23 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 24 | fsumtax | fsumtax | numeric | 23 | 10 | √ | 0 |  |
| 25 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 26 | fcompbillno | fcompbillno | varchar | 30 |  | √ | ' ' |  |
| 27 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_purlist_fentitykey |  | fentitykey |
| 2 | idx_src_purlist_fparentid |  | fparentid |
| 3 | pk_src_purlist |  | fid |

---

## 供应商-多选基础资料表 t_src_itemsupentry_sup

- **表名称：** 供应商-多选基础资料表
- **表名：** t_src_itemsupentry_sup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_itemsupentry_sup_fid |  | fentryid |
| 2 | pk_src_itemsupentry_sup |  | fpkid |

---

## 标的供应商分录-子表 t_src_itemsupentry

- **表名称：** 标的供应商分录-子表
- **表名：** t_src_itemsupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fpurlistid | 标的名称 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_itemsupentry_fid |  | fid |
| 2 | pk_src_itemsupentry |  | fentryid |
