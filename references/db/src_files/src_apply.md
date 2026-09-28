# 寻源申请-src_apply

## 关联子实体-子表 t_src_applyentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_src_applyentry_lk

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
| 1 | pk_src_applyentry_lk |  | fpkid |
| 2 | idx_src_applyentry_lk_fk |  | fentryid |

---

## 供应商分录-子表 t_src_applysupplier

- **表名称：** 供应商分录-子表
- **表名：** t_src_applysupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispuragent | 代理投标/报价 | bpchar | 1 |  | √ | '0' | 代理投标/报价 |
| 3 | fphone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 4 | faddress | 地址 | varchar | 100 |  | √ | ' ' | 地址 |
| 5 | fsocietycreditcode | 统一社会信用代码 | varchar | 255 |  | √ | ' ' | 统一社会信用代码 |
| 6 | fisfeeagent | 代理缴费 | bpchar | 1 |  | √ | '0' | 代理缴费 |
| 7 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fsupplierid | 供应商编码 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 11 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 12 | fsuppliertype | 供应商类别 | varchar | 50 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 13 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 14 | fsupname | 供应商名称 | varchar | 255 |  | √ | ' ' | 供应商名称 |
| 15 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_applysupplier_fid |  | fid |
| 2 | idx_src_applysupplier_fpag |  | fpackageid |
| 3 | idx_src_applysupplier_fsup |  | fsupplierid |
| 4 | pk_src_applysupplier |  | fentryid |

---

## 寻源申请-多语言表 t_src_apply_l

- **表名称：** 寻源申请-多语言表
- **表名：** t_src_apply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 申请名称 | varchar | 300 |  | √ | ' ' | 申请名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_apply_l |  | fpkid |
| 2 | idx_src_apply_l_flocaleid |  | fid,flocaleid |

---

## 附件-附件表 t_src_applyattachment

- **表名称：** 附件-附件表
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

## 限定供应商用户-多选基础资料表 t_src_supplierusers

- **表名称：** 限定供应商用户-多选基础资料表
- **表名：** t_src_supplierusers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 供应商用户 pur_supuser |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_supplierusers |  | fpkid |
| 2 | idx_src_supplierusers_eid |  | fentryid |
| 3 | idx_src_supplierusers_bid |  | fbasedataid |

---

## 申请信息-子表 t_src_applyentry

- **表名称：** 申请信息-子表
- **表名：** t_src_applyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faddress | faddress | varchar | 200 |  | √ | ' ' |  |
| 3 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fcategorysmall | fcategorysmall | int8 | 64 |  | √ | 0 |  |
| 5 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 6 | fordernub | fordernub | int8 | 64 |  | √ | 0 |  |
| 7 | fiscontrolqty | 是否控制数量 | bpchar | 1 |  | √ | '1' | 是否控制数量 |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fentryrcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | faccount | faccount | varchar | 50 |  | √ | ' ' |  |
| 12 | fsrctypeid | 寻源流程 | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 13 | fapplicationdeptid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fsourseno | 项目立项编号 | varchar | 100 |  | √ | ' ' | 项目立项编号 |
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
| 30 | fprice3 | 最近含税交易单价 | numeric | 23 | 10 | √ | 0 | 最近含税交易单价 |
| 31 | fprojectid | 寻源项目编号 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 32 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 33 | fcaruse | fcaruse | varchar | 50 |  | √ | ' ' |  |
| 34 | fwarehouse | fwarehouse | int8 | 64 |  | √ | 0 |  |
| 35 | freqqty2 | 关联项目立项数量(废弃) | varchar | 50 |  | √ | ' ' | 关联项目立项数量(废弃) |
| 36 | fminiorderqty | 最小起订量 | numeric | 23 | 10 | √ | 0 | 最小起订量 |
| 37 | freqtype | freqtype | int8 | 64 |  | √ | 0 |  |
| 38 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 39 | freqqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 40 | fpurchasersld | 需求人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | flinenumber | flinenumber | varchar | 50 |  | √ | ' ' |  |
| 42 | fbiginsmallld | fbiginsmallld | int8 | 64 |  | √ | 0 |  |
| 43 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 44 | freqdescribe | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 45 | fbudget | fbudget | varchar | 50 |  | √ | ' ' |  |
| 46 | frowtypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 47 | fprice2 | 最近未税交易单价 | numeric | 23 | 10 | √ | 0 | 最近未税交易单价 |
| 48 | fmaterialname | 标的名称 | varchar | 255 |  | √ | ' ' | 标的名称 |
| 49 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 50 | fpurchaserid | 采购人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
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
| 63 | fdemandstatus | 项目立项状态 | bpchar | 1 |  | √ | ' ' | 项目立项状态,枚举: A :未立项 B :已立项 C :已变更 D :终止 Z :作废 E :转订单 |
| 64 | fnotaxprice | 未税单价 | numeric | 23 | 10 | √ | 0 | 未税单价 |
| 65 | foriginpurbillno | foriginpurbillno | varchar | 50 |  | √ | ' ' |  |
| 66 | fentryorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 67 | fcategorybig | fcategorybig | int8 | 64 |  | √ | 0 |  |
| 68 | fpoline | fpoline | varchar | 50 |  | √ | ' ' |  |
| 69 | ftaxitemid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 70 | fprice12 | 上次定标未税单价 | numeric | 23 | 10 | √ | 0 | 上次定标未税单价 |
| 71 | fprice13 | 上次定标含税单价 | numeric | 23 | 10 | √ | 0 | 上次定标含税单价 |
| 72 | fprice14 | 历史最优未税)单价 | numeric | 23 | 10 | √ | 0 | 历史最优未税)单价 |
| 73 | fcategoryer | fcategoryer | int8 | 64 |  | √ | 0 |  |
| 74 | fprice15 | 历史最优含税单价 | numeric | 23 | 10 | √ | 0 | 历史最优含税单价 |
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

---

## 寻源申请-反写记录表 t_src_apply_wb

- **表名称：** 寻源申请-反写记录表
- **表名：** t_src_apply_wb

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
| 1 | pk_src_apply_wb |  | fentryid |
| 2 | idx_src_apply_wb_fk |  | fid |

---

## 寻源申请-关联追踪表 t_src_apply_tc

- **表名称：** 寻源申请-关联追踪表
- **表名：** t_src_apply_tc

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
| 1 | pk_src_apply_tc |  | fid |
| 2 | idx_src_apply_tc_tid |  | ftid |
| 3 | idx_src_apply_tc_tbill |  | ftbillid |

---

## 寻源申请-主表 t_src_apply

- **表名称：** 寻源申请-主表
- **表名：** t_src_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freqdatetime | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 3 | fdemandaffiliateid | fdemandaffiliateid | int8 | 64 |  | √ | 0 |  |
| 4 | fisproject | 下推方式 | bpchar | 1 |  | √ | '0' | 下推方式,枚举: 0 :手工下推项目立项 1 :手工下推项目启动 2 :审核自动下推项目启动 |
| 5 | forgid | 需求组织(有效) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fspecialreason | fspecialreason | varchar | 300 |  |  | ' ' |  |
| 7 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 8 | fsrctypeid | 寻源流程 | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | freqsource | 需求来源 | varchar | 30 |  | √ | ' ' | 需求来源,枚举: 1 :需求新增 2 :外部导入 3 :寻源新增 |
| 11 | ftitle | 申请名称 | varchar | 300 |  | √ | ' ' | 申请名称 |
| 12 | fattachurl | fattachurl | varchar | 500 |  | √ | ' ' |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fsuppliernoid | fsuppliernoid | int8 | 64 |  | √ | 0 |  |
| 15 | fsumamount | 预估未税金额 | numeric | 23 | 10 | √ | 0 | 预估未税金额 |
| 16 | fisdecision | fisdecision | bpchar | 1 |  | √ | '0' |  |
| 17 | freqclass | freqclass | varchar | 3 |  | √ | 'A' |  |
| 18 | fprojectno | fprojectno | varchar | 100 |  | √ | ' ' |  |
| 19 | frentsupplierid | frentsupplierid | int8 | 64 |  | √ | 0 |  |
| 20 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 21 | ftaxtype | 价格录入方式 | bpchar | 1 |  | √ | '1' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 22 | fbillno | 申请编号 | varchar | 60 |  | √ | ' ' | 申请编号 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fecpno | fecpno | varchar | 100 |  | √ | ' ' |  |
| 25 | fserviceattributes | fserviceattributes | varchar | 50 |  | √ | ' ' |  |
| 26 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已终止 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fsuppliernametext | fsuppliernametext | varchar | 50 |  | √ | ' ' |  |
| 29 | fcostattribution | fcostattribution | int8 | 64 |  | √ | 0 |  |
| 30 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fisspecial | fisspecial | bpchar | 1 |  | √ | '0' |  |
| 33 | fdepartmentid | fdepartmentid | int8 | 64 |  | √ | 0 |  |
| 34 | fsumqty | 合计数量 | numeric | 23 | 10 | √ | 0 | 合计数量 |
| 35 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 36 | fyearcomment | fyearcomment | varchar | 255 |  | √ | ' ' |  |
| 37 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 38 | ftype | ftype | varchar | 30 |  | √ | ' ' |  |
| 39 | fbasedatafield | fbasedatafield | int8 | 64 |  | √ | 0 |  |
| 40 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 41 | fsumtaxamount | 预估价税合计 | numeric | 23 | 10 | √ | 0 | 预估价税合计 |
| 42 | fsumtax | 合计税额 | numeric | 23 | 10 | √ | 0 | 合计税额 |
| 43 | fisannual | fisannual | varchar | 30 |  | √ | '0' |  |
| 44 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 45 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_apply_fecpno |  | fecpno |
| 2 | idx_src_apply_fbillno |  | fbillno |
| 3 | pk_src_apply |  | fid |
