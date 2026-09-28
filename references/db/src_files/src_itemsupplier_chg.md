# 标的供应商变更-src_itemsupplier_chg

## 标的供应商变更-主表 t_src_purlist

- **表名称：** 标的供应商变更-主表
- **表名：** t_src_purlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpickschemeld | 供应商抽取方案 | int8 | 64 |  | √ | 0 | [供应商抽取方案 src_supplierpick](../src_files/src_supplierpick.md) |
| 3 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsourceid | fsourceid | int8 | 64 |  | √ | 0 |  |
| 5 | fisbizitemcomp | fisbizitemcomp | bpchar | 1 |  | √ | '0' |  |
| 6 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 7 | fmaintainclause | fmaintainclause | varchar | 50 |  | √ | ' ' |  |
| 8 | forigin | 发起方 | varchar | 30 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 9 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 10 | fsumamount | fsumamount | numeric | 23 | 10 | √ | 0 |  |
| 11 | fbizschemeid | fbizschemeid | int8 | 64 |  | √ | 0 |  |
| 12 | fispurlistcomp | fispurlistcomp | bpchar | 1 |  | √ | '1' |  |
| 13 | fcondition | 邀请条件 | varchar | 2000 |  | √ | ' ' | 邀请条件 |
| 14 | ftaxtype | ftaxtype | bpchar | 1 |  | √ | ' ' |  |
| 15 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 16 | fparentid | 父单据ID | varchar | 30 |  | √ | ' ' | 父单据ID |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fentitykey | 组件标识 | varchar | 30 |  | √ | ' ' | 组件标识 |
| 19 | fexpertcount | 抽取供应商数 | int8 | 64 |  | √ | 0 | 抽取供应商数 |
| 20 | fdecisiontype | fdecisiontype | bpchar | 1 |  | √ | ' ' |  |
| 21 | fsumqty | fsumqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | [寻源项目变更F7 src_bidchangef7](../pds_files/src_bidchangef7.md) |
| 23 | fcosttypeid | fcosttypeid | int8 | 64 |  | √ | 0 |  |
| 24 | fpurtype | fpurtype | varchar | 30 |  | √ | ' ' |  |
| 25 | fsourcetypeid | fsourcetypeid | int8 | 64 |  | √ | 0 |  |
| 26 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 27 | fsumtax | fsumtax | numeric | 23 | 10 | √ | 0 |  |
| 28 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 29 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 30 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |

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
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
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
