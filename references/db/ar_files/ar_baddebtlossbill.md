# 坏账损失单-ar_baddebtlossbill

## 收款计划-子表 t_ar_lossbillplanentry

- **表名称：** 收款计划-子表
- **表名：** t_ar_lossbillplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbaddebtcause | 坏账原因 | varchar | 30 |  | √ | ' ' | 坏账原因,枚举: overdue :逾期未还并明显超过规定账龄 bankrupt :债务人破产和死亡 other :其他原因 |
| 5 | fbaddebtlocamt | 损失金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 损失金额(本位币) |
| 6 | funlockamt | 未锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未锁定金额 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | funsettleamt | 未收回金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未收回金额 |
| 10 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fduedate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 13 | fsrcplanentryid | 源单计划分录ID | int8 | 64 |  | √ | 0 | 源单计划分录ID |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fsettledamt | 已收回金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已收回金额 |
| 16 | fbaddebtamt | 损失金额 | numeric | 23 | 10 | √ | 0.0000000000 | 损失金额 |
| 17 | flockedamt | 已锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已锁定金额 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | frecamt | 应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_lossbillplanentry_fid |  | fid |
| 2 | t_ar_lossbillplanentry_pkey |  | fentryid |

---

## 坏账损失单-关联追踪表 t_ar_baddebtlossbill_tc

- **表名称：** 坏账损失单-关联追踪表
- **表名：** t_ar_baddebtlossbill_tc

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
| 1 | idx_ar_baddebtlossbill_tc_tid |  | ftid |
| 2 | idx_ar_baddebtlossbill_tc_tbill |  | ftbillid |
| 3 | t_ar_baddebtlossbill_tc_pkey |  | fid |

---

## 坏账损失单-反写记录表 t_ar_baddebtlossbill_wb

- **表名称：** 坏账损失单-反写记录表
- **表名：** t_ar_baddebtlossbill_wb

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
| 1 | idx_ar_baddebtlossbill_wb_fk |  | fid |
| 2 | t_ar_baddebtlossbill_wb_pkey |  | fentryid |

---

## 关联子实体-子表 t_ar_lossbillplanentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_lossbillplanentry_lk

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
| 1 | idx_ar_lossbillplanentry_lk_fk |  | fentryid |
| 2 | t_ar_lossbillplanentry_lk_pkey |  | fpkid |

---

## 关联子实体-子表 t_ar_baddebtlossbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_baddebtlossbill_lk

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
| 1 | t_ar_baddebtlossbill_lk_pkey |  | fpkid |
| 2 | idx_ar_baddebtlossbill_lk_fk |  | fid |

---

## 坏账损失单-主表 t_ar_baddebtlossbill

- **表名称：** 坏账损失单-主表
- **表名：** t_ar_baddebtlossbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbaddebtlocamt | 损失金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 损失金额(本位币) |
| 3 | facctsysid | 会计核算体系 | int8 | 64 |  | √ | 0 | 核算体系 xkbd_accountingsys |
| 4 | fsalesmanid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 5 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsourcebilltypeid | 源单据类型ID | int8 | 64 |  | √ | 0 | 源单据类型ID |
| 7 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 8 | fsettlestatus | 核销状态 | varchar | 30 |  | √ | ' ' | 核销状态,枚举: unsettle :未核销 partsettle :部分核销 settled :全部核销 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 11 | fbiztype | 业务类型(预留字段) | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 12 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbaddebtamt | 损失金额 | numeric | 23 | 10 | √ | 0.0000000000 | 损失金额 |
| 15 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 16 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 17 | fsourcebillno | 源单编号 | varchar | 255 |  | √ | ' ' | 源单编号 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fsourcebizdate | 源单日期 | timestamp | 0 |  |  | null | 源单日期 |
| 20 | frecamt | 应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额 |
| 21 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fbaddebtcause | 坏账原因 | varchar | 30 |  | √ | ' ' | 坏账原因,枚举: overdue :逾期未还并明显超过规定账龄 bankrupt :债务人破产和死亡 other :其他原因 |
| 24 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 28 | funsettleamt | 未收回金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未收回金额 |
| 29 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 30 | fdepartmentid | 部门 | int8 | 64 |  | √ | 0 | 行政组织（部门） bos_adminorg |
| 31 | fimagenumber | fimagenumber | varchar | 80 |  | √ | ' ' |  |
| 32 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 33 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 34 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 35 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 37 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | ' ' | 已生成凭证 |
| 38 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 39 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 42 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_baddebtlossbill_org |  | forgid |
| 2 | t_ar_baddebtlossbill_pkey |  | fid |

---

## 应收明细-子表 t_ar_lossbillentry

- **表名称：** 应收明细-子表
- **表名：** t_ar_lossbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 3 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbaddebtcause | 坏账原因 | varchar | 30 |  | √ | ' ' | 坏账原因,枚举: overdue :逾期未还并明显超过规定账龄 bankrupt :债务人破产和死亡 other :其他原因 |
| 6 | fbaddebtlocamt | 损失金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 损失金额(本位币) |
| 7 | fsrcentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 8 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 9 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 10 | funlockamt | 未锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未锁定金额 |
| 11 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 13 | funsettleamt | 未收回金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未收回金额 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fsettledamt | 已收回金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已收回金额 |
| 17 | fbaddebtamt | 损失金额 | numeric | 23 | 10 | √ | 0.0000000000 | 损失金额 |
| 18 | flockedamt | 已锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已锁定金额 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | flinetypeid | 行类型(预留字段) | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 21 | fmaterialname | fmaterialname | varchar | 255 |  | √ | ' ' |  |
| 22 | frecamt | 应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_lossbillentry_pkey |  | fentryid |
| 2 | idx_ar_lossbillentry_fid |  | fid |

---

## 关联子实体-子表 t_ar_lossbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_lossbillentry_lk

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
| 1 | t_ar_lossbillentry_lk_pkey |  | fpkid |
| 2 | idx_ar_lossbillentry_lk_fk |  | fentryid |
