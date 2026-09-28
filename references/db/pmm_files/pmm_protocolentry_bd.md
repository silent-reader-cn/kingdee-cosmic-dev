# 协议清单基础资料-pmm_protocolentry_bd

## 协议清单基础资料-主表 t_mal_protocolentry

- **表名称：** 协议清单基础资料-主表
- **表名：** t_mal_protocolentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 2 | fmaterialgroup | 产品分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fpriceinvaliddate | 价格失效日期 | timestamp | 0 |  |  | null | 价格失效日期 |
| 7 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 8 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 9 | fpurplanid | 采买方案 | int8 | 64 |  | √ | 0 | [采买方案 pmm_purchaseplan](../pmm_files/pmm_purchaseplan.md) |
| 10 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 11 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 12 | fsrcbillentryseq | fsrcbillentryseq | int8 | 64 |  | √ | 0 |  |
| 13 | fminorderqty | 起订量 | numeric | 19 | 6 | √ | 0 | 起订量 |
| 14 | fabandonstatus | fabandonstatus | bpchar | 1 |  | √ | ' ' |  |
| 15 | fentrypricetype | 价格类型 | bpchar | 1 |  | √ | 'A' | 价格类型,枚举: |
| 16 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 17 | fdctamount | fdctamount | numeric | 23 | 10 | √ | 0 |  |
| 18 | fleadtime | 供货周期（天） | int8 | 64 |  | √ | 0 | 供货周期（天） |
| 19 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 20 | fsrcbillentity | fsrcbillentity | varchar | 50 |  | √ | ' ' |  |
| 21 | fqty | fqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | ftaxamount | ftaxamount | numeric | 23 | 10 | √ | 0 |  |
| 23 | fdctrate | fdctrate | numeric | 23 | 10 | √ | 0 |  |
| 24 | fpurorgid | 采买组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fdiscounttype | fdiscounttype | varchar | 5 |  | √ | ' ' |  |
| 26 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 27 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fsrcbillentryid | fsrcbillentryid | int8 | 64 |  | √ | 0 |  |
| 29 | ftax | ftax | numeric | 23 | 10 | √ | 0 |  |
| 30 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 31 | fpriceeffectdate | 价格生效日期 | timestamp | 0 |  |  | null | 价格生效日期 |
| 32 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 33 | fentryid | 分录id | int8 | 64 |  | √ | 0 | 分录id |
| 34 | fmaterialname | 产品名称 | varchar | 255 |  | √ | ' ' | 产品名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_protocolentry_matid |  | fmaterialid |
| 2 | pk_t_mal_protocolentry |  | fentryid |
| 3 | idx_mal_protocolentry_id |  | fid |
