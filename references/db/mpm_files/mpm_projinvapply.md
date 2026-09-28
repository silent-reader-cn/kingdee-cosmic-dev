# 项目开票申请单-mpm_projinvapply

## 关联子实体-子表 t_mpm_invapply_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpm_invapply_lk

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
| 1 | pk_mpm_invapply_lk |  | fpkid |
| 2 | idx_mpm_invapply_lk_fk |  | fid |

---

## 开票明细-分表 t_mpm_pinvaentry_r

- **表名称：** 开票明细-分表
- **表名：** t_mpm_pinvaentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | farrelamt | 关联应收价税合计 | numeric | 23 | 10 | √ | 0 | 关联应收价税合计 |
| 3 | fcursaleinvrelamt | 关联销售发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 关联销售发票价税合计(本位币) |
| 4 | fsrcentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 5 | fsrcbillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 6 | fcontractentity | 合同实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fredinvrelbaseqty | 关联红字开票申请基本数量 | numeric | 23 | 10 | √ | 0 | 关联红字开票申请基本数量 |
| 8 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fcontractid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 10 | fsaleinvrelamt | 关联销售发票价税合计 | numeric | 23 | 10 | √ | 0 | 关联销售发票价税合计 |
| 11 | fsrcentryseq | 来源单据行号 | int8 | 64 |  | √ | 0 | 来源单据行号 |
| 12 | fcontractseq | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 13 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 14 | fsaleinvrelbaseqty | 关联销售发票基本数量 | numeric | 23 | 10 | √ | 0 | 关联销售发票基本数量 |
| 15 | fcurincrelamt | 关联应收价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 关联应收价税合计(本位币) |
| 16 | fredinvrelqty | 关联红字开票申请数量 | numeric | 23 | 10 | √ | 0 | 关联红字开票申请数量 |
| 17 | fredinvdrelqty | 红字已申请开票数量 | numeric | 23 | 10 | √ | 0 | 红字已申请开票数量 |
| 18 | farrelbaseqty | 关联应收基本数量 | numeric | 23 | 10 | √ | 0 | 关联应收基本数量 |
| 19 | fsaleinvrelqty | 关联销售发票数量 | numeric | 23 | 10 | √ | 0 | 关联销售发票数量 |
| 20 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 21 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 22 | fcontractentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 23 | fredinvdrelbaseqty | 红字已申请开票基本数量 | numeric | 23 | 10 | √ | 0 | 红字已申请开票基本数量 |
| 24 | fmainentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 25 | farrelqty | 关联应收数量 | numeric | 23 | 10 | √ | 0 | 关联应收数量 |
| 26 | fmainbillno | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 27 | fcontractnum | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 29 | fmainentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_pinvappr_fid |  | fid |
| 2 | pk_mpm_pinvaentry_r |  | fentryid |

---

## 开票明细-多语言表 t_mpm_pinvaentry_l

- **表名称：** 开票明细-多语言表
- **表名：** t_mpm_pinvaentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_pinvaentry_l |  | fpkid |
| 2 | idx_mpm_pinvappl_fidflid |  | fentryid,flocaleid |

---

## 项目开票申请单-主表 t_mpm_invapply

- **表名称：** 项目开票申请单-主表
- **表名：** t_mpm_invapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | farrelamt | 关联应收价税合计 | numeric | 23 | 10 | √ | 0 | 关联应收价税合计 |
| 3 | fcursaleinvrelamt | 关联销售发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 关联销售发票价税合计(本位币) |
| 4 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsalegroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 6 | fsaleinvrelamt | 关联销售发票价税合计 | numeric | 23 | 10 | √ | 0 | 关联销售发票价税合计 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 9 | fistax | 录入含税单价 | bpchar | 1 |  | √ | '1' | 录入含税单价 |
| 10 | fapplyuserid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | finvtype | 发票类型 | bpchar | 1 |  | √ | ' ' | 发票类型,枚举: 0 :增值税专用发票 1 :增值税普通发票 |
| 12 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 13 | finvcustomerid | 开票客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 14 | fsaleuserid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 15 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 16 | finvctrlmode | 项目开票控制方式 | bpchar | 1 |  | √ | ' ' | 项目开票控制方式,枚举: A :按数量控制 B :按金额控制 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 19 | fpaycustomerid | 付款客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 20 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fisprojectbegin | 项目期初 | bpchar | 1 |  | √ | '0' | 项目期初 |
| 23 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fisredflush | 是否已红冲 | bpchar | 1 |  | √ | '0' | 是否已红冲 |
| 26 | famtandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 27 | fexchangetype | 换算方式 | bpchar | 1 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 28 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 31 | fsrcbillno | 来源单据号 | varchar | 80 |  | √ | ' ' | 来源单据号 |
| 32 | finvdirection | 发票方向 | varchar | 5 |  | √ | ' ' | 发票方向,枚举: blue :蓝字 red :红字 |
| 33 | fisinputamt | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 34 | fsaledeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fasstacttype | 往来单位类型 | varchar | 80 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 36 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 37 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fcurincrelamt | 关联应收价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 关联应收价税合计(本位币) |
| 39 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 40 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 43 | fcuramtandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 47 | fpaymode | 付款方式 | varchar | 10 |  | √ | 'CREDIT' | 付款方式,枚举: CASH :现销 CREDIT :赊销 |
| 48 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 49 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 50 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_invapply |  | fid |
| 2 | idx_mpm_invapply_fbillno |  | fbillno |

---

## 项目开票申请单-多语言表 t_mpm_invapply_l

- **表名称：** 项目开票申请单-多语言表
- **表名：** t_mpm_invapply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_invappl_fidflid |  | fid,flocaleid |
| 2 | pk_mpm_invapply_l |  | fpkid |

---

## 项目开票申请单-反写记录表 t_mpm_invapply_wb

- **表名称：** 项目开票申请单-反写记录表
- **表名：** t_mpm_invapply_wb

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
| 1 | idx_mpm_invapply_wb_fk |  | fid |
| 2 | pk_mpm_invapply_wb |  | fentryid |

---

## 关联子实体-子表 t_mpm_pinvaentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpm_pinvaentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量_确认携带值 | numeric | 23 | 10 |  | null | 数量_确认携带值 |
| 2 | famtandtax | 价税合计_确认携带值 | numeric | 23 | 10 |  | null | 价税合计_确认携带值 |
| 3 | fbaseqty_old | 基本数量_原始携带值 | numeric | 23 | 10 |  | null | 基本数量_原始携带值 |
| 4 | famtandtax_old | 价税合计_原始携带值 | numeric | 23 | 10 |  | null | 价税合计_原始携带值 |
| 5 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 6 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 7 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 8 | fqty_old | 数量_原始携带值 | numeric | 23 | 10 |  | null | 数量_原始携带值 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fbaseqty | 基本数量_确认携带值 | numeric | 23 | 10 |  | null | 基本数量_确认携带值 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 12 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_pinvaentry_lk |  | fpkid |
| 2 | idx_mpm_pinvaentry_lk_fk |  | fentryid |

---

## 项目开票申请单-关联追踪表 t_mpm_invapply_tc

- **表名称：** 项目开票申请单-关联追踪表
- **表名：** t_mpm_invapply_tc

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
| 1 | idx_mpm_invapply_tc_tbill |  | ftbillid |
| 2 | pk_mpm_invapply_tc |  | fid |
| 3 | idx_mpm_invapply_tc_tid |  | ftid |

---

## 开票明细-子表 t_mpm_pinvaentry

- **表名称：** 开票明细-子表
- **表名：** t_mpm_pinvaentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 3 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 9 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 10 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 11 | fmtrlversionid | 物料/费用项目版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 12 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 13 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | freccustomerid | 收货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 16 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 17 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 18 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 19 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 20 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 21 | fdiscounttype | 折扣方式 | varchar | 10 |  | √ | ' ' | 折扣方式,枚举: NULL :无 A :折扣率(%) B :单位折扣额 TOTAL :固定折扣额 |
| 22 | fcuramtandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 23 | funitid | 开票单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 25 | fconfigcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 26 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 27 | famtandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 28 | fcurdiscountamt | 折扣额(本位币) | numeric | 23 | 10 | √ | 0 | 折扣额(本位币) |
| 29 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 30 | finvclassify | 开票分类 | bpchar | 1 |  | √ | ' ' | 开票分类,枚举: P :产品类 N :非产品类 |
| 31 | ftaskid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 32 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 35 | fcurtaxamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 36 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_pinvaentry_fid |  | fid |
| 2 | pk_mpm_pinvaentry |  | fentryid |
