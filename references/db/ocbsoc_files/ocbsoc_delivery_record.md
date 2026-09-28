# 发货记录-ocbsoc_delivery_record

## 发货记录-关联追踪表 t_ocbsoc_deliveryrecord_tc

- **表名称：** 发货记录-关联追踪表
- **表名：** t_ocbsoc_deliveryrecord_tc

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
| 1 | idx_ocbsoc_deliveryrecord_tc_tbill |  | ftbillid |
| 2 | idx_ocbsoc_deliveryrecord_tc_tid |  | ftid |
| 3 | pk_ocbsoc_deliveryrecord_tc |  | fid |

---

## 发货记录-主表 t_ocbsoc_deliveryrecord

- **表名称：** 发货记录-主表
- **表名：** t_ocbsoc_deliveryrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fautosignfailreson | 自动签收失败原因 | varchar | 255 |  | √ | ' ' | 自动签收失败原因 |
| 2 | fdistributionchannelid | 配送渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 3 | flogisticcompid | 物流公司 | int8 | 64 |  | √ | 0 | 物流公司 bd_logisticcomp |
| 4 | freceivechannelid | 收货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 5 | fdistributiondate | 配送时间 | timestamp | 0 |  |  | null | 配送时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fclosetime | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 8 | fsigntime | 签收时间 | timestamp | 0 |  |  | null | 签收时间 |
| 9 | fdeliverdate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fsignstatus | 签收状态(废弃) | varchar | 100 |  | √ | ' ' | 签收状态(废弃),枚举: 1 :已签收 0 :待签收 2 :部分签收 |
| 12 | flogisticno | 物流单号 | varchar | 80 |  | √ | ' ' | 物流单号 |
| 13 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fsourcebillno | fsourcebillno | varchar | 80 |  | √ | ' ' |  |
| 15 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 16 | fpursalemodel | 购销模式 | bpchar | 1 |  | √ | ' ' | 购销模式,枚举: A :普通外销 B :内销分步结算 C :内部调拨 D :寄售外销 E :渠道购销 F :内销同步结算 |
| 17 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fsigner | 签收人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fphone | 收寄件电话号码 | varchar | 80 |  | √ | ' ' | 收寄件电话号码 |
| 21 | fdistributionstatus | 配送状态 | varchar | 10 |  | √ | '0' | 配送状态,枚举: 0 :无 1 :待配送 2 :已配送 |
| 22 | fsourcebilltype | 来源单据 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 23 | fbillstatus | 单据状态 | varchar | 100 |  | √ | ' ' | 单据状态,枚举: B :待签收 C :已签收 D :部分签收 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fsigndesc | 签收说明 | varchar | 255 |  | √ | ' ' | 签收说明 |
| 28 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | 'A' | 关闭状态,枚举: A :未关闭 B :已关闭 |
| 29 | fownerid | 销售渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 30 | frecordid | frecordid | int8 | 64 |  | √ | 0 | id |
| 31 | fsourcebillid | fsourcebillid | varchar | 100 |  | √ | ' ' |  |
| 32 | fisautosign | 是否自动签收 | bpchar | 1 |  | √ | '0' | 是否自动签收 |
| 33 | fhastax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 34 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 35 | fsignimgurl | 签收图片地址 | text | 0 |  |  | ' ' | 签收图片地址 |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fdistributorid | 配送人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fcustomerid | 订货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | frecordid | frecordid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_dlr_fsbid |  | fsourcebillid |
| 2 | pk_ocbsoc_deliveryrecord |  | frecordid |

---

## 关联子实体-子表 t_ocbsoc_deliveryrecord_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocbsoc_deliveryrecord_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frecordid | frecordid | int8 | 64 |  | √ | null |  |
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
| 1 | idx_ocbsoc_deliveryrecord_lk_fk |  | frecordid |
| 2 | pk_ocbsoc_deliveryrecord_lk |  | fpkid |

---

## 商品分录-子表 t_ocbsoc_deli_detail

- **表名称：** 商品分录-子表
- **表名：** t_ocbsoc_deli_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fjoinrefusebaseqty | 关联拒收基本数量 | numeric | 23 | 10 | √ | 0 | 关联拒收基本数量 |
| 2 | fsignqty | 累计签收入库数量 | numeric | 23 | 10 | √ | 0 | 累计签收入库数量 |
| 3 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 4 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | frefuseqty | 累计拒收数量 | numeric | 23 | 10 | √ | 0 | 累计拒收数量 |
| 7 | fdeliverassitqty | 发货辅助数量 | numeric | 23 | 10 | √ | 0 | 发货辅助数量 |
| 8 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fserialqty | 序列号数量 | numeric | 23 | 10 | √ | 0 | 序列号数量 |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | fdeliverqty | 发货数量 | numeric | 23 | 10 | √ | 0 | 发货数量 |
| 13 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 14 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 15 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 17 | fassistunit | 辅助计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fscmlotid | 批号ID | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 19 | fsignassitqty | 累计签收入库辅助数量 | numeric | 23 | 10 | √ | 0 | 累计签收入库辅助数量 |
| 20 | fthissignbotpqty | 本次签收数量 | numeric | 23 | 10 | √ | 0 | 本次签收数量 |
| 21 | fsignbaseqty | 累计签收入库基本数量 | numeric | 23 | 10 | √ | 0 | 累计签收入库基本数量 |
| 22 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 23 | fociclotid | 商品批号 | int8 | 64 |  | √ | 0 | 商品批号 ococic_lot |
| 24 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 25 | frefuseassitqty | 累计拒收辅助数量 | numeric | 23 | 10 | √ | 0 | 累计拒收辅助数量 |
| 26 | fserialunitid | 序列号单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :单位折扣率％ B :单位折扣额 |
| 28 | fjoinrefuseassistqty | 关联拒收辅助数量 | numeric | 23 | 10 | √ | 0 | 关联拒收辅助数量 |
| 29 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 30 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 31 | fdeliverbaseqty | 发货基本数量 | numeric | 23 | 10 | √ | 0 | 发货基本数量 |
| 32 | frefuseinfo | 拒收原因 | varchar | 255 |  | √ | ' ' | 拒收原因 |
| 33 | fjoinrefuseqty | 关联拒收数量 | numeric | 23 | 10 | √ | 0 | 关联拒收数量 |
| 34 | fdiscount | 单位折扣（率） | numeric | 23 | 10 | √ | 0 | 单位折扣（率） |
| 35 | frecordid | frecordid | int8 | 64 |  | √ | 0 |  |
| 36 | frefusebaseqty | 累计拒收基本数量 | numeric | 23 | 10 | √ | 0 | 累计拒收基本数量 |
| 37 | fitem | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 38 | fexpirydate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 39 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_deli_detail |  | fentryid |
| 2 | idx_ocbsoc_dld_frid |  | frecordid |

---

## 关联子实体-子表 t_ocbsoc_deliverydetail_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocbsoc_deliverydetail_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fsignbaseqty | 累计签收入库基本数量_确认携带值 | numeric | 23 | 10 |  | null | 累计签收入库基本数量_确认携带值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsignbaseqty_old | 累计签收入库基本数量_原始携带值 | numeric | 23 | 10 |  | null | 累计签收入库基本数量_原始携带值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_deliverydetail_lk_fk |  | fentryid |
| 2 | pk_ocbsoc_deliverydetail_lk |  | fpkid |

---

## 商品分录-分表 t_ocbsoc_deli_detail_x

- **表名称：** 商品分录-分表
- **表名：** t_ocbsoc_deli_detail_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsumpurinassistqty | 累计入库辅助数量 | numeric | 23 | 10 | √ | 0 | 累计入库辅助数量 |
| 2 | fjoinoutbaseqty | fjoinoutbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | fstockaddrid | 仓位 | int8 | 64 |  | √ | 0 | 渠道仓位 ococic_location |
| 4 | fdistributionchannelid | 配送渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 5 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 6 | fmainbillentity | 核心单据实体 | varchar | 80 |  | √ | ' ' | 核心单据实体 |
| 7 | fjoinpurinbaseqty | 已关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 已关联入库基本数量 |
| 8 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 9 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 10 | fsumpurinqty | 累计入库数量 | numeric | 23 | 10 | √ | 0 | 累计入库数量 |
| 11 | fjoininassistqty | fjoininassistqty | numeric | 23 | 10 | √ | 0 |  |
| 12 | forderchannelid | 订货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 13 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 14 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 15 | fjoinpurinqty | 已关联入库数量 | numeric | 23 | 10 | √ | 0 | 已关联入库数量 |
| 16 | fjoinpurinassistqty | 已关联入库辅助数量 | numeric | 23 | 10 | √ | 0 | 已关联入库辅助数量 |
| 17 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 18 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 19 | fjoinoutassistqty | fjoinoutassistqty | numeric | 23 | 10 | √ | 0 |  |
| 20 | fstockid | 仓库 | int8 | 64 |  | √ | 0 | 渠道仓库 ococic_warehouse |
| 21 | fentryclosestatus | 行关闭状态 | bpchar | 1 |  | √ | 'A' | 行关闭状态,枚举: A :未关闭 B :已关闭 |
| 22 | fwarehouseid | 发货仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 23 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 24 | finvorgid | 发货库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fsumpurinbaseqty | 累计入库基本数量 | numeric | 23 | 10 | √ | 0 | 累计入库基本数量 |
| 26 | fjoininbaseqty | fjoininbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | frecordid | frecordid | int8 | 64 |  | √ | 0 |  |
| 28 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 29 | fenquirychannelid | 收货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_deli_srcbillid |  | fsrcbillid |
| 2 | pk_ocbsoc_deli_detail_x |  | fentryid |
| 3 | idx_ocbsoc_deli_mbillid |  | fmainbillid |
| 4 | idx_ocbsoc_dldx_frid |  | frecordid |

---

## 序列号-子表 t_ocbsoc_deliveryserial

- **表名称：** 序列号-子表
- **表名：** t_ocbsoc_deliveryserial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fisselect |  | bpchar | 1 |  | √ | '0' |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fsignremark | 签收备注 | varchar | 255 |  | √ | ' ' | 签收备注 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fserialnumber | 序列号 | varchar | 80 |  | √ | ' ' | 序列号 |
| 7 | fisreplenish | 是否补录 | bpchar | 1 |  | √ | '0' | 是否补录 |
| 8 | focicserialid | 商品序列号 | int8 | 64 |  | √ | 0 | 商品序列号 ococic_snmainfile |
| 9 | fscmserialid | 供应链序列号 | int8 | 64 |  | √ | 0 | 序列号主档 bd_snmainfile |
| 10 | fissign | 是否签收 | bpchar | 1 |  | √ | '0' | 是否签收 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_deliveryserial |  | fdetailid |
| 2 | idx_ocbsoc_deliveryserial_ent |  | fentryid |

---

## 发货记录-反写记录表 t_ocbsoc_deliveryrecord_wb

- **表名称：** 发货记录-反写记录表
- **表名：** t_ocbsoc_deliveryrecord_wb

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
| 1 | pk_ocbsoc_deliveryrecord_wb |  | fentryid |
| 2 | idx_ocbsoc_deliveryrecord_wb_fk |  | fid |
