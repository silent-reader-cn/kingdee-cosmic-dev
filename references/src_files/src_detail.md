# 寻源申请分录F7-src_detail

## 标的附件-附件表 t_src_applyattachment

- **表名称：** 标的附件-附件表
- **表名：** t_src_applyattachment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_applyattachment_eid |  | fentryid |
| 2 | pk_src_applyattachment |  | fpkid |
| 3 | idx_src_applyattachment_bid |  | fbasedataid |

---

## 寻源申请分录F7-主表 t_src_applyentry

- **表名称：** 寻源申请分录F7-主表
- **表名：** t_src_applyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 寻源申请 | int8 | 64 |  | √ | 0 | 寻源申请F7 src_applyf7 |
| 2 | faddress | faddress | varchar | 200 |  | √ | ' ' |  |
| 3 | freqorgid | freqorgid | int8 | 64 |  | √ | 0 |  |
| 4 | fcategorysmall | fcategorysmall | int8 | 64 |  | √ | 0 |  |
| 5 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 6 | fordernub | fordernub | int8 | 64 |  | √ | 0 |  |
| 7 | fiscontrolqty | 是否控制数量 | bpchar | 1 |  | √ | '1' | 是否控制数量 |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fseq | 分录序号 | int4 | 32 |  | √ | 0 | 分录序号 |
| 10 | fentryrcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | faccount | faccount | varchar | 50 |  | √ | ' ' |  |
| 12 | fsrctypeid | 寻源流程 | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 13 | fapplicationdeptid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fsourseno | 项目编号 | varchar | 100 |  | √ | ' ' | 项目编号 |
| 15 | ftitle | 标的描述 | varchar | 1024 |  | √ | ' ' | 标的描述 |
| 16 | fcategorymid | fcategorymid | int8 | 64 |  | √ | 0 |  |
| 17 | fprnumber | fprnumber | varchar | 50 |  | √ | ' ' |  |
| 18 | fapplicationdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 19 | fmonth | fmonth | timestamp | 0 |  |  | null |  |
| 20 | fionumber | fionumber | varchar | 50 |  | √ | ' ' |  |
| 21 | fponumber | fponumber | varchar | 50 |  | √ | ' ' |  |
| 22 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | fapplicantid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fmaterialmodel | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |
| 25 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 26 | fqty | 核准数量 | numeric | 23 | 10 | √ | 0 | 核准数量 |
| 27 | fcontactmobile | fcontactmobile | varchar | 50 |  | √ | ' ' |  |
| 28 | fcategory | 品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 29 | fseeprocess | fseeprocess | varchar | 50 |  | √ | ' ' |  |
| 30 | fprice3 | fprice3 | numeric | 23 | 10 | √ | 0 |  |
| 31 | fprojectid | 寻源项目ID | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 32 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 33 | fcaruse | fcaruse | varchar | 50 |  | √ | ' ' |  |
| 34 | fwarehouse | fwarehouse | int8 | 64 |  | √ | 0 |  |
| 35 | freqqty2 | 立项数量(废弃) | varchar | 50 |  | √ | ' ' | 立项数量(废弃) |
| 36 | fminiorderqty | 最小起订量 | numeric | 23 | 10 | √ | 0 | 最小起订量 |
| 37 | freqtype | freqtype | int8 | 64 |  | √ | 0 |  |
| 38 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 39 | freqqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 40 | fpurchasersld | fpurchasersld | int8 | 64 |  | √ | 0 |  |
| 41 | flinenumber | flinenumber | varchar | 50 |  | √ | ' ' |  |
| 42 | fbiginsmallld | fbiginsmallld | int8 | 64 |  | √ | 0 |  |
| 43 | fentryid | 明细分录ID | int8 | 64 |  | √ | 0 | 明细分录ID |
| 44 | freqdescribe | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 45 | fbudget | fbudget | varchar | 50 |  | √ | ' ' |  |
| 46 | frowtypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 47 | fprice2 | fprice2 | numeric | 23 | 10 | √ | 0 |  |
| 48 | fmaterialname | 标的名称 | varchar | 255 |  | √ | ' ' | 标的名称 |
| 49 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 50 | fpurchaserid | fpurchaserid | int8 | 64 |  | √ | 0 |  |
| 51 | fprbillstatus | fprbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 52 | fsrcentryid | 源单分录ID | varchar | 50 |  | √ | ' ' | 源单分录ID |
| 53 | fsrcbillno | 源单单号 | varchar | 50 |  | √ | ' ' | 源单单号 |
| 54 | fmaterialid | 标的编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 55 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 56 | famount | 未税金额 | numeric | 23 | 10 | √ | 0 | 未税金额 |
| 57 | fminipackqty | 最小包装量 | numeric | 23 | 10 | √ | 0 | 最小包装量 |
| 58 | findicateld | findicateld | varchar | 30 |  | √ | ' ' |  |
| 59 | farrivedate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 60 | fuse | fuse | int8 | 64 |  | √ | 0 |  |
| 61 | fprofitcostcenter | fprofitcostcenter | int8 | 64 |  | √ | 0 |  |
| 62 | fbdprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 63 | fdemandstatus | 立项状态 | bpchar | 1 |  | √ | ' ' | 立项状态,枚举: A :未立项 B :已立项 C :已变更 D :终止 Z :作废 E :转订单 |
| 64 | fnotaxprice | 未税单价 | numeric | 23 | 10 | √ | 0 | 未税单价 |
| 65 | foriginpurbillno | foriginpurbillno | varchar | 50 |  | √ | ' ' |  |
| 66 | fentryorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 67 | fcategorybig | fcategorybig | int8 | 64 |  | √ | 0 |  |
| 68 | fpoline | fpoline | varchar | 50 |  | √ | ' ' |  |
| 69 | ftaxitemid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 70 | fprice12 | fprice12 | numeric | 23 | 10 | √ | 0 |  |
| 71 | fprice13 | fprice13 | numeric | 23 | 10 | √ | 0 |  |
| 72 | fprice14 | fprice14 | numeric | 23 | 10 | √ | 0 |  |
| 73 | fcategoryer | fcategoryer | int8 | 64 |  | √ | 0 |  |
| 74 | fprice15 | fprice15 | numeric | 23 | 10 | √ | 0 |  |
| 75 | foriginpurrownum | foriginpurrownum | int8 | 64 |  | √ | 0 |  |
| 76 | fareaid | fareaid | int8 | 64 |  | √ | 0 |  |
| 77 | fcontactno | fcontactno | int8 | 64 |  | √ | 0 |  |
| 78 | fdemandqty | 关联项目立项数量 | numeric | 23 | 10 | √ | 0 | 关联项目立项数量 |
| 79 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_applyentry_fid |  | fid |
| 2 | pk_src_applyentry |  | fentryid |
| 3 | idx_src_applyentry_pid |  | fprojectid |
