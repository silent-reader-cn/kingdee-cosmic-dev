# 发货单-ocococ_deliveryorder

## 商品明细-子表 t_ocococ_delorder_det

- **表名称：** 商品明细-子表
- **表名：** t_ocococ_delorder_det

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstockstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 3 | fremake | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | freceivedate | 签收日期 | timestamp | 0 |  |  | null | 签收日期 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | ffrozentime | 冻结日期 | timestamp | 0 |  |  | null | 冻结日期 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fsalerid | 销售员 | int8 | 64 |  | √ | 0 | [渠道用户(已废弃) ocdbd_channeluser](../ocdbd_files/ocdbd_channeluser.md) |
| 9 | fclosetime | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 10 | fbusinesswayid | 经营方式 | int8 | 64 |  | √ | 0 | [商品经营方式 ocdbd_item_businesstype](../ocdpm_files/ocdbd_item_businesstype.md) |
| 11 | fstocktypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 12 | fmaterialassid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | fitemsaleattrid | 销售属性 | int8 | 64 |  | √ | 0 | [商品销售属性 ocdbd_item_saleattr](../ocdbd_files/ocdbd_item_saleattr.md) |
| 14 | fsignstatus | 签收状态 | bpchar | 1 |  | √ | 'A' | 签收状态,枚举: A :未开始 B :待签收 C :部分签收 D :已签收 |
| 15 | fpayingcustomerid | 付款方 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 16 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 17 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fassistunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 21 | fserialunitid | 序列号单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | flotnum | 批号 | varchar | 200 |  | √ | ' ' | 批号 |
| 23 | ffrozenstatus | 冻结状态 | bpchar | 1 |  | √ | '1' | 冻结状态,枚举: 1 :未冻结 2 :已冻结 |
| 24 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 26 | fstockid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 27 | fkeepertype | 保管者类型 | varchar | 30 |  | √ | ' ' | 保管者类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 28 | fdeliverystatusid | 发货状态 | int8 | 64 |  | √ | 0 | [发货状态 ococic_deliverstatus](../ococic_files/ococic_deliverstatus.md) |
| 29 | fserialnumber | 序列号 | varchar | 80 |  | √ | ' ' | 序列号 |
| 30 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 31 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | '1' | 关闭状态,枚举: 1 :未关闭 2 :手工关闭 3 :自动关闭 |
| 32 | finstalldate | 要求安装时间 | timestamp | 0 |  |  | null | 要求安装时间 |
| 33 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fassistattrid | fassistattrid | int8 | 64 |  | √ | 0 |  |
| 35 | fchannelwarehouseid | 渠道仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 36 | fisnegativesell | 是否负卖 | bpchar | 1 |  | √ | '0' | 是否负卖 |
| 37 | finstallstatus | 安装状态 | bpchar | 1 |  | √ | 'A' | 安装状态,枚举: A :未开始 B :部分安装 C :已安装 |
| 38 | fexpirydate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 39 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 40 | fassistqty | 辅助单位数量 | numeric | 23 | 10 | √ | 0 | 辅助单位数量 |
| 41 | fsettlecustomerid | 收票方 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 42 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 43 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 44 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | farrivaldate | 要求到货时间 | timestamp | 0 |  |  | null | 要求到货时间 |
| 46 | fisneedinstall | 是否需要安装 | bpchar | 1 |  | √ | '0' | 是否需要安装 |
| 47 | fsaledepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocococ_delorderdet_fid |  | fid |
| 2 | pk_ocococ_delorder_det |  | fentryid |

---

## 发货单-主表 t_ocococ_deliveryorder

- **表名称：** 发货单-主表
- **表名：** t_ocococ_deliveryorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ftradetype | 购销模式 | bpchar | 1 |  | √ | ' ' | 购销模式,枚举: A :普通外销 B :内销分步结算 C :内部调拨 D :寄售外销 E :渠道购销 F :内销同步结算 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fdeliverystatusid | 发货状态 | int8 | 64 |  | √ | 0 | [发货状态 ococic_deliverstatus](../ococic_files/ococic_deliverstatus.md) |
| 8 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fdistributionmodeid | 配送模式 | int8 | 64 |  | √ | 0 | [配送模式 ocdbd_distributionmode](../ococic_files/ocdbd_distributionmode.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 13 | fsignstatus | 签收状态 | bpchar | 1 |  | √ | 'A' | 签收状态,枚举: A :未开始 B :待签收 C :部分签收 D :已签收 |
| 14 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocococ_delorder_bno |  | fbillno |
| 2 | pk_ocococ_deliveryorder |  | fid |

---

## 商品明细-分表 t_ocococ_delorder_det_x

- **表名称：** 商品明细-分表
- **表名：** t_ocococ_delorder_det_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstockstatusid | fstockstatusid | int8 | 64 |  | √ | 0 |  |
| 3 | fsrcbillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 4 | fsumsalereturnassistqty | 累计销售退货辅助数量 | numeric | 23 | 10 | √ | 0 | 累计销售退货辅助数量 |
| 5 | fsrcbilleid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 6 | finvbaseqty | 已出库基本数量 | numeric | 23 | 10 | √ | 0 | 已出库基本数量 |
| 7 | finstallbaseqty | 已安装基本数量 | numeric | 23 | 10 | √ | 0 | 已安装基本数量 |
| 8 | fcorebillno | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 9 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 10 | ftotalinvbaseqty | 累计已出库基本数量 | numeric | 23 | 10 | √ | 0 | 累计已出库基本数量 |
| 11 | fjoinsalereturnassistqty | 关联销售退货辅助数量 | numeric | 23 | 10 | √ | 0 | 关联销售退货辅助数量 |
| 12 | finstallassistqty | 已安装辅助数量 | numeric | 23 | 10 | √ | 0 | 已安装辅助数量 |
| 13 | fjoinsalereturnbaseqty | 关联销售退货基本数量 | numeric | 23 | 10 | √ | 0 | 关联销售退货基本数量 |
| 14 | fdeliveredassistqty | 已发货辅助数量 | numeric | 23 | 10 | √ | 0 | 已发货辅助数量 |
| 15 | fownertype | fownertype | varchar | 30 |  | √ | ' ' |  |
| 16 | fkeeperid | fkeeperid | int8 | 64 |  | √ | 0 |  |
| 17 | fjoindeliverrecordbaseqty | 关联发货记录基本数量 | numeric | 23 | 10 | √ | 0 | 关联发货记录基本数量 |
| 18 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 19 | fdeliveredbaseqty | 已发货基本数量 | numeric | 23 | 10 | √ | 0 | 已发货基本数量 |
| 20 | fdeliveredqty | 已发货数量 | numeric | 23 | 10 | √ | 0 | 已发货数量 |
| 21 | fserialunitid | fserialunitid | int8 | 64 |  | √ | 0 |  |
| 22 | flotnum | flotnum | varchar | 200 |  | √ | ' ' |  |
| 23 | fcorebillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 24 | fsumpurreturnassistqty | 累计采购退货辅助数量 | numeric | 23 | 10 | √ | 0 | 累计采购退货辅助数量 |
| 25 | finvqty | 已出库数量 | numeric | 23 | 10 | √ | 0 | 已出库数量 |
| 26 | fsumsalereturnbaseqty | 累计销售退货基本数量 | numeric | 23 | 10 | √ | 0 | 累计销售退货基本数量 |
| 27 | fsumpurreturnbaseqty | 累计采购退货基本数量 | numeric | 23 | 10 | √ | 0 | 累计采购退货基本数量 |
| 28 | finvassistqty | 已出库辅助数量 | numeric | 23 | 10 | √ | 0 | 已出库辅助数量 |
| 29 | finstallqty | 已安装数量 | numeric | 23 | 10 | √ | 0 | 已安装数量 |
| 30 | fkeepertype | fkeepertype | varchar | 30 |  | √ | ' ' |  |
| 31 | ftotalinvqty | 累计已出库数量 | numeric | 23 | 10 | √ | 0 | 累计已出库数量 |
| 32 | fcorebillentity | 核心单据实体 | varchar | 80 |  | √ | ' ' | 核心单据实体 |
| 33 | fserialnumber | fserialnumber | varchar | 80 |  | √ | ' ' |  |
| 34 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 35 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 36 | ftotalinvassistqty | 累计已出库辅助数量 | numeric | 23 | 10 | √ | 0 | 累计已出库辅助数量 |
| 37 | fjoinpurreturnbaseqty | 关联采购退货基本数量 | numeric | 23 | 10 | √ | 0 | 关联采购退货基本数量 |
| 38 | fcorebillentryseq | 核心单据分录序号 | int4 | 32 |  | √ | 0 | 核心单据分录序号 |
| 39 | fexpirydate | fexpirydate | timestamp | 0 |  |  | null |  |
| 40 | fjoinpurreturnassistqty | 关联采购退货辅助数量 | numeric | 23 | 10 | √ | 0 | 关联采购退货辅助数量 |
| 41 | fproducedate | fproducedate | timestamp | 0 |  |  | null |  |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 43 | fcorebillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocococ_delorder_det_x |  | fentryid |
| 2 | idx_ocococ_delorderdetx_fid |  | fid |

---

## 关联子实体-子表 t_ocococ_deliveryorder_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocococ_deliveryorder_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocococ_deliveryorder_lk |  | fpkid |
| 2 | idx_ocococ_deliveryorder_lk_fk |  | fid |

---

## 发货单-分表 t_ocococ_deliveryorder_x

- **表名称：** 发货单-分表
- **表名：** t_ocococ_deliveryorder_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | finvgroupid | 库存组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 4 | faddress | 国家/省/市/区 | varchar | 36 |  | √ | ' ' | 国家/省/市/区 |
| 5 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | [渠道用户(已废弃) ocdbd_channeluser](../ocdbd_files/ocdbd_channeluser.md) |
| 6 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 7 | fconsignee | 收货人 | varchar | 80 |  | √ | ' ' | 收货人 |
| 8 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fconsigneechannelid | 收货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 11 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 12 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 13 | fconsigneephone | 联系电话 | varchar | 30 |  | √ | ' ' | 联系电话 |
| 14 | fpurchannelid | 订货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 15 | fdeliverdeptid | 发货部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | falladdress | 完整地址 | varchar | 255 |  | √ | ' ' | 完整地址 |
| 17 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fpurcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 19 | fdeliveroperatorid | 仓管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 20 | fmemberinfoid | 会员 | int8 | 64 |  | √ | 0 | [顾客信息 ocdbd_user](../ocdbd_files/ocdbd_user.md) |
| 21 | freccustomerid | 收货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 22 | fstockorgid | 发货库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fdeliverychannelid | 发货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 24 | fdetailaddress | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocococ_delorderx_orgid |  | forgid |
| 2 | pk_ocococ_deliveryorder_x |  | fid |
| 3 | idx_ocococ_delorderx_storgid |  | fstockorgid |

---

## 物流信息-子表 t_ocococ_delorder_lsc

- **表名称：** 物流信息-子表
- **表名：** t_ocococ_delorder_lsc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcarno | 车牌号 | varchar | 30 |  | √ | ' ' | 车牌号 |
| 3 | flogisticsbill | 物流单号 | varchar | 80 |  | √ | ' ' | 物流单号 |
| 4 | flogisticcompid | 物流公司 | int8 | 64 |  | √ | 0 | [物流公司 bd_logisticcomp](../sbd_files/bd_logisticcomp.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | finfodescription | 信息说明 | varchar | 255 |  | √ | ' ' | 信息说明 |
| 7 | fdriverid | 配送司机 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fdriver | 配送司机 | varchar | 80 |  | √ | ' ' | 配送司机 |
| 9 | flogisticscompany | 物流公司 | varchar | 80 |  | √ | ' ' | 物流公司 |
| 10 | fsignstatus | 签收状态 | bpchar | 1 |  | √ | 'A' | 签收状态,枚举: A :未开始 B :待签收 C :部分签收 D :已签收 |
| 11 | freceivingdate | 签收日期 | timestamp | 0 |  |  | null | 签收日期 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | farrivaldate | 发货时间 | timestamp | 0 |  |  | null | 发货时间 |
| 14 | fdrivertel | 司机电话 | varchar | 30 |  | √ | ' ' | 司机电话 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocococ_delorderlsc_fid |  | fid |
| 2 | pk_ocococ_delorder_lsc |  | fentryid |

---

## 发货单-关联追踪表 t_ocococ_deliveryord_tc

- **表名称：** 发货单-关联追踪表
- **表名：** t_ocococ_deliveryord_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocococ_deliveryord_tc_tid |  | ftid |
| 2 | idx_ocococ_deliveryord_tc_tbill |  | ftbillid |
| 3 | pk_ocococ_deliveryord_tc |  | fid |

---

## 发货单-分表 t_ocococ_deliveryorder_f

- **表名称：** 发货单-分表
- **表名：** t_ocococ_deliveryorder_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxallamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 3 | fcurtotalallamount | 价税合计本位币 | numeric | 23 | 10 | √ | 0 | 价税合计本位币 |
| 4 | fcurtotaltaxamount | 税额本位币 | numeric | 23 | 10 | √ | 0 | 税额本位币 |
| 5 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 6 | fpaytype | 付款方式 | bpchar | 1 |  | √ | '1' | 付款方式,枚举: 1 :赊销 2 :现销 |
| 7 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 8 | fistax | 是否含税 | bpchar | 1 |  | √ | '1' | 是否含税 |
| 9 | fcurtotalamount | 金额本位币 | numeric | 23 | 10 | √ | 0 | 金额本位币 |
| 10 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 11 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 12 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 13 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocococ_deliveryorder_f |  | fid |
| 2 | idx_ocococ_delorderf_setid |  | fsettlecurrencyid |

---

## 序列号-子表 t_ocococ_delorder_ser

- **表名称：** 序列号-子表
- **表名：** t_ocococ_delorder_ser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fiscorrect | 是否补录 | bpchar | 1 |  | √ | '0' | 是否补录 |
| 2 | fitemserialid | 商品序列号 | int8 | 64 |  | √ | 0 | [商品序列号 ococic_snmainfile](../ococic_files/ococic_snmainfile.md) |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fserialno | 序列号 | varchar | 80 |  | √ | ' ' | 序列号 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fscmserialid | 供应链序列号 | int8 | 64 |  | √ | 0 | [序列号主档 bd_snmainfile](../sbd_files/bd_snmainfile.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocococ_delorder_ser |  | fdetailid |
| 2 | idx_ocococ_delorder_ser_eid |  | fentryid |

---

## 发货单-反写记录表 t_ocococ_deliveryord_wb

- **表名称：** 发货单-反写记录表
- **表名：** t_ocococ_deliveryord_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocococ_deliveryord_wb |  | fentryid |
| 2 | idx_ocococ_deliveryord_wb_fk |  | fid |

---

## 商品明细-分表 t_ocococ_delorder_det_f

- **表名称：** 商品明细-分表
- **表名：** t_ocococ_delorder_det_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 3 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 4 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :单位折扣率（%） B :单位折扣额 NULL :无 |
| 5 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 6 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 7 | fdiscount | 单位折扣（率） | numeric | 23 | 10 | √ | 0 | 单位折扣（率） |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 9 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 10 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 11 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 12 | fcurtaxamount | 税额本位币 | numeric | 23 | 10 | √ | 0 | 税额本位币 |
| 13 | fcuramount | 金额本位币 | numeric | 23 | 10 | √ | 0 | 金额本位币 |
| 14 | fcurallamount | 价税合计本位币 | numeric | 23 | 10 | √ | 0 | 价税合计本位币 |
| 15 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 16 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocococ_delorderdetf_fid |  | fid |
| 2 | pk_ocococ_delorder_det_f |  | fentryid |

---

## 关联子实体-子表 t_ocococ_order_detail_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocococ_order_detail_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocococ_order_detail_lk |  | fpkid |
| 2 | idx_ocococ_order_detail_lk_fk |  | fentryid |
