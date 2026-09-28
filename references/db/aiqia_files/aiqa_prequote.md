# 预报价单-aiqa_prequote

## 预报价单-主表 t_aiqa_prequote

- **表名称：** 预报价单-主表
- **表名：** t_aiqa_prequote

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 11 | fexchangetype | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 12 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 13 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fcustomerid | 客户名称 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aiqa_prequote |  | fid |
| 2 | idx_aiqa_prequote_m0 |  | fbillno |

---

## 物料明细-子表 t_aiqa_prequoteentry

- **表名称：** 物料明细-子表
- **表名：** t_aiqa_prequoteentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fcategory | 品类 | varchar | 200 |  | √ | ' ' | 品类 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | funitid | 单位id | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fbrand | 品牌 | varchar | 50 |  | √ | ' ' | 品牌 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fstock | 库存 | numeric | 23 | 10 | √ | 0 | 库存 |
| 9 | funicode | 国标码 | varchar | 50 |  | √ | ' ' | 国标码 |
| 10 | funitname | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 11 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 12 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fpicture | 物料图片 | varchar | 255 |  | √ | ' ' | 物料图片 |
| 14 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fyxdc | 以销定采 | bpchar | 1 |  | √ | '0' | 以销定采 |
| 16 | funitprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 17 | fstockupdatetime | 库存更新时间 | timestamp | 0 |  |  | null | 库存更新时间 |
| 18 | fspecification | 规格型号 | varchar | 250 |  | √ | ' ' | 规格型号 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fdeal | 已处理 | bpchar | 1 |  | √ | '0' | 已处理 |
| 21 | fmaterialname | 物料名称 | varchar | 200 |  | √ | ' ' | 物料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aiqa_prequoteentry_fk |  | fid |
| 2 | pk_aiqa_prequoteentry |  | fentryid |
