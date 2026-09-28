# 资金池使用记录-occba_rebateacctuse_rd

## 资金池使用记录-主表 t_occba_rbtacctuse

- **表名称：** 资金池使用记录-主表
- **表名：** t_occba_rbtacctuse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsettlecust_s | 供应方结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 3 | fgroupuseableamt_u | 使用方分组总可用金额 | numeric | 23 | 10 | √ | 0 | 使用方分组总可用金额 |
| 4 | fbaluseplanid | 资金池使用方案 | int8 | 64 |  | √ | 0 | [资金池使用方案 occba_baluseplan](../occba_files/occba_baluseplan.md) |
| 5 | fentryid_u | 使用方单据行ID | int8 | 64 |  | √ | 0 | 使用方单据行ID |
| 6 | fsettlechannelid_s | 供应方结算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 7 | fsettlechannelid_u | 使用方结算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 8 | faccountid_s | 供应方账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 9 | faccountid_u | 使用方账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 10 | fsrcbillid_s | 供应方来源单据ID | int8 | 64 |  | √ | 0 | 供应方来源单据ID |
| 11 | fsettlecustid_u | 使用方结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 12 | fmaterielid_u | 使用方物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | ftaxrateid_s | 供应方税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 14 | fbillno_u | 使用方单据编码 | varchar | 80 |  | √ | ' ' | 使用方单据编码 |
| 15 | fbaseunitqty_u | 使用方基本单位数量 | numeric | 23 | 10 | √ | 0 | 使用方基本单位数量 |
| 16 | ftaxrateid_u | 使用方税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 17 | fbaseusedamt_u | 使用方基本单位总使用金额 | numeric | 23 | 10 | √ | 0 | 使用方基本单位总使用金额 |
| 18 | fbillno_s | 供应方单据编码 | varchar | 80 |  | √ | ' ' | 供应方单据编码 |
| 19 | fitemid_u | 使用方商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 20 | fcloseretamt_s | fcloseretamt_s | numeric | 23 | 10 | √ | 0 |  |
| 21 | funitqtyusedamt_s | 供应方单位数量使用金额 | numeric | 23 | 10 | √ | 0 | 供应方单位数量使用金额 |
| 22 | fgroupno_u | 使用方组号 | int4 | 32 |  | √ | 0 | 使用方组号 |
| 23 | fsettlecurrencyid_s | 供应方结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 24 | fsettlecurrencyid_u | 使用方结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fsettleorgid_u | 使用方结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fentryseq_u | 使用方单据行号 | int4 | 32 |  | √ | 0 | 使用方单据行号 |
| 27 | fsettleorgid_s | 供应方结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fitembrandid_u | 使用方商品品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 29 | fitembrandid_s | 供应方商品品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 30 | ftips | 提示消息 | varchar | 200 |  | √ | ' ' | 提示消息 |
| 31 | fusableamount_s | 供应方可用余额 | numeric | 23 | 10 | √ | 0 | 供应方可用余额 |
| 32 | fusedamount_u | 使用方总使用金额 | numeric | 23 | 10 | √ | 0 | 使用方总使用金额 |
| 33 | fusedamount_s | 供应方使用金额 | numeric | 23 | 10 | √ | 0 | 供应方使用金额 |
| 34 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fuserentryseq_s | 使用记录行序号 | int4 | 32 |  | √ | 0 | 使用记录行序号 |
| 36 | fsrcbillobjid_s | 供应方来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 37 | factlusedamt_s | factlusedamt_s | numeric | 23 | 10 | √ | 0 |  |
| 38 | fbillobjid_u | 使用方单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 39 | fbillobjid_s | 供应方单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 40 | fitemclassid_u | 使用方商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | fbillid_s | 供应方单据ID | int8 | 64 |  | √ | 0 | 供应方单据ID |
| 43 | fbillid_u | 使用方单据ID | int8 | 64 |  | √ | 0 | 使用方单据ID |
| 44 | fuserate_u | 使用方使用比例 | numeric | 23 | 10 | √ | 0 | 使用方使用比例 |
| 45 | fismoneyoffset_u | 使用方计资金池抵扣 | bpchar | 1 |  | √ | '0' | 使用方计资金池抵扣 |
| 46 | fsalechannelid_u | 使用方销售渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 47 | fsalechannelid_s | 供应方销售渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 48 | fsrcentryid_s | 供应方来源单据行ID | int8 | 64 |  | √ | 0 | 供应方来源单据行ID |
| 49 | forderlinetypeid_u | 使用方行类型 | int8 | 64 |  | √ | 0 | [订单行类型 ocdbd_orderlinetype](../ocbsoc_files/ocdbd_orderlinetype.md) |
| 50 | fsrcbillno_s | 供应方来源单据编码 | varchar | 80 |  | √ | ' ' | 供应方来源单据编码 |
| 51 | fbillamount_s | 供应方指定抵扣 | numeric | 23 | 10 | √ | 0 | 供应方指定抵扣 |
| 52 | fbaseunitid_u | 使用方基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 53 | fitemclassid_s | 供应方商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 54 | fbillamount_u | 使用方指定抵扣 | numeric | 23 | 10 | √ | 0 | 使用方指定抵扣 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_rbtause_bno_u |  | fbillno_u |
| 2 | idx_occba_rbtause_bobj_u |  | fbillobjid_u |
| 3 | pk_t_occba_rbtacctuse |  | fid |
