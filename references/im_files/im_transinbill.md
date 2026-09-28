# 分步调入单-im_transinbill

## 分步调入单-反写记录表 t_im_transinbill_wb

- **表名称：** 分步调入单-反写记录表
- **表名：** t_im_transinbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_transinbill_wb_pkey |  | fentryid |
| 2 | idx_im_transinbill_wb_fk |  | fid |

---

## 分步调入单-多语言表 t_im_transinbill_l

- **表名称：** 分步调入单-多语言表
- **表名：** t_im_transinbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_transinbill_l_pkey |  | fpkid |
| 2 | idx_im_transinbill_l |  | fid,flocaleid |

---

## 关联子实体-子表 t_im_transinbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_transinbillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_transinbillentry_lk_fk |  | fentryid |
| 2 | t_im_transinbillentry_lk_pkey |  | fpkid |

---

## 分步调入单-关联追踪表 t_im_transinbill_tc

- **表名称：** 分步调入单-关联追踪表
- **表名：** t_im_transinbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_transin_tc_ftbidtid |  | ftbillid,ftid |
| 2 | idx_im_transinbill_tc_tbill |  | ftbillid |
| 3 | idx_im_transinbill_tc_tid |  | ftid |
| 4 | t_im_transinbill_tc_pkey |  | fid |

---

## 关联子实体-子表 t_im_transinbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_transinbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_transinbill_lk_pkey |  | fpkid |
| 2 | idx_im_transinbill_lk_fk |  | fid |

---

## 分步调入单-主表 t_im_transinbill

- **表名称：** 分步调入单-主表
- **表名：** t_im_transinbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvdc | finvdc | varchar | 5 |  | √ | ' ' |  |
| 3 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 4 | forgid | 调入组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 8 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 11 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 12 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 17 | frelroradamagebill | frelroradamagebill | int8 | 64 |  | √ | 0 |  |
| 18 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 21 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | froaddamageowner | froaddamageowner | varchar | 10 |  | √ | ' ' |  |
| 24 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 26 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 27 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 28 | ftransit | 在途归属 | varchar | 5 |  | √ | ' ' | 在途归属,枚举: A :调出货主 B :调入货主 |
| 29 | frevconfirmnode | 收入确认时点 | varchar | 50 |  | √ | ' ' | 收入确认时点,枚举: signIn :签收 saleOut :出库 |
| 30 | ftranstype | 调拨类型 | varchar | 5 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 31 | foutorgid | 调出组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 33 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 36 | fsettlescurrency | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_transinbill_org |  | forgid |
| 2 | idx_im_tibill_bktorgno |  | fbookdate,forgid,fbillno |
| 3 | idx_im_transinbill_forgbillno |  | fbillno,forgid |
| 4 | t_im_transinbill_pkey |  | fid |
| 5 | idx_im_transinbill_biztorgno |  | fbiztime,forgid,fbillno |
| 6 | idx_im_transinbill_oorg |  | foutorgid |
| 7 | idx_im_transinbill |  | fbilltypeid |

---

## 物料明细-分表 t_im_transinbillentry_x

- **表名称：** 物料明细-分表
- **表名：** t_im_transinbillentry_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutownertype | 调出货主类型 | varchar | 36 |  | √ | ' ' | 调出货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 3 | foutorgid | foutorgid | int8 | 64 |  | √ | 0 |  |
| 4 | foutinvtypeid | 调出库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 5 | foutwarehouseid | foutwarehouseid | int8 | 64 |  | √ | 0 |  |
| 6 | foutkeepertype | 调出保管者类型 | varchar | 36 |  | √ | ' ' | 调出保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | foutlocationid | foutlocationid | int8 | 64 |  | √ | 0 |  |
| 9 | foutinvstatusid | 调出库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 10 | foutprojectid | foutprojectid | int8 | 64 |  | √ | 0 |  |
| 11 | foutownerid | 调出货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | foutkeeperid | 调出保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_trainbillentry_x_id |  | fid |
| 2 | t_im_transinbillentry_x_pkey |  | fentryid |

---

## 物料明细-分表 t_im_transinbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_transinbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcrosslegalperson | 是否跨法人 | varchar | 5 |  | √ | '0' | 是否跨法人,枚举: 0 :否 1 :是 |
| 3 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 4 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 5 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 6 | fmainbillentity | 核心单据实体 | varchar | 100 |  | √ | ' ' | 核心单据实体 |
| 7 | freturnbaseqty | 已退回基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退回基本数量 |
| 8 | fgroupnumber | 成组号 | varchar | 50 |  | √ | ' ' | 成组号 |
| 9 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 10 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 11 | fgroupseq | 成组行号 | varchar | 50 |  | √ | ' ' | 成组行号 |
| 12 | fremainreturnbaseqty | 未退回基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未退回基本数量 |
| 13 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 14 | freloutqty | freloutqty | numeric | 23 | 10 | √ | 0 |  |
| 15 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 16 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 17 | fmainbillnumber | 核心单据编号 | varchar | 100 |  | √ | ' ' | 核心单据编号 |
| 18 | freturnqty | 已退回数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退回数量 |
| 19 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 20 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 21 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 22 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 23 | freloutbaseqty | freloutbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 24 | fremainreturnqty | 未退回数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未退回数量 |
| 25 | fisovertrans | 调拨完成 | bpchar | 1 |  | √ | '0' | 调拨完成 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 27 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_transinbillentry_r_pkey |  | fentryid |
| 2 | idx_im_trainentry_r_fid |  | fid |

---

## 物料明细-子表 t_im_transinbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_transinbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 3 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | foutownerid | foutownerid | int8 | 64 |  | √ | 0 |  |
| 6 | finvstatusid | 调入库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 7 | fkitsettleway | 套件内部结算方式 | varchar | 50 |  | √ | ' ' | 套件内部结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 8 | fparentproduct | 父项产品 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 9 | foutinvtypeid | foutinvtypeid | int8 | 64 |  | √ | 0 |  |
| 10 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fownertype | 调入货主类型 | varchar | 36 |  | √ | ' ' | 调入货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 12 | fkeeperid | 调入保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | foutkeeperid | foutkeeperid | int8 | 64 |  | √ | 0 |  |
| 15 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 16 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 17 | fprojectid | 调入项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 18 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fkeepertype | 调入保管者类型 | varchar | 36 |  | √ | ' ' | 调入保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 20 | froaddamageqty | froaddamageqty | numeric | 23 | 10 | √ | 0 |  |
| 21 | fwarehouseid | 调入仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 22 | foutinvstatusid | foutinvstatusid | int8 | 64 |  | √ | 0 |  |
| 23 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 24 | ftransitownertype | 在途货主类型 | varchar | 30 |  | √ | ' ' | 在途货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 25 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 26 | fownerid | 调入货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 28 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 29 | foutorgid | foutorgid | int8 | 64 |  | √ | 0 |  |
| 30 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 31 | froaddamagebaseqty | froaddamagebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 34 | foutmpmtaskno | 调出项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 35 | froaddamageqty2nd | froaddamageqty2nd | numeric | 23 | 10 | √ | 0 |  |
| 36 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 37 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 38 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 39 | fsettleroute | fsettleroute | int8 | 64 |  | √ | 0 |  |
| 40 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 41 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 42 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 43 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 44 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 45 | foutkeepertype | foutkeepertype | varchar | 36 |  | √ | ' ' |  |
| 46 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 47 | ftransitownerid | 在途货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 48 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 49 | foutlocationid | 调出仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 50 | foutownertype | foutownertype | varchar | 36 |  | √ | ' ' |  |
| 51 | finvtypeid | 调入库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 52 | fproducttype | 产品类别 | varchar | 50 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 53 | flocationid | 调入仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 54 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量(2) |
| 55 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 56 | fentrycomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 57 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 58 | fmpmtaskno | 调入项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 59 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 60 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 61 | foutprojectid | 调出项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 62 | froaddamageqty3rd | froaddamageqty3rd | numeric | 23 | 10 | √ | 0 |  |
| 63 | fisfreegift | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_transinbill_e_mmt |  | fmaterialmasterid |
| 2 | t_im_transinbillentry_pkey |  | fentryid |
| 3 | idx_im_transinbill_e_ow |  | fownerid |
| 4 | idx_im_transinbillentry |  | fid |
| 5 | idx_im_transinbill_e_wh |  | fwarehouseid |

---

## 物料明细-分表 t_im_transinbillentry_c

- **表名称：** 物料明细-分表
- **表名：** t_im_transinbillentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcurrencyid | 成本币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | foutcostcurrencyid | 调出成本币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | foutactualcost | 调出实际成本 | numeric | 23 | 10 | √ | 0 | 调出实际成本 |
| 5 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0 | 单位实际成本 |
| 6 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 7 | foutcostaccountid | 调出成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 8 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | foutunitactualcost | 调出单位实际成本 | numeric | 23 | 10 | √ | 0 | 调出单位实际成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_transinbillentry_c |  | fid |
| 2 | pk__im_transinbillentry_c |  | fentryid |
