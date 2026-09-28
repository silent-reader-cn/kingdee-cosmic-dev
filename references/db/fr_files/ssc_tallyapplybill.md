# 记账申请单-ssc_tallyapplybill

## 记账申请单-主表 t_tk_tallyapplybill

- **表名称：** 记账申请单-主表
- **表名：** t_tk_tallyapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freversalmark | 冲销标识 | bpchar | 1 |  | √ | '1' | 冲销标识,枚举: 1 :未冲销单 2 :冲销单 3 :已冲销单 |
| 3 | fmainbiztype | 报账业务类型 | int8 | 64 |  | √ | 0 | [报账业务类型 bd_businessitem](../fibd_files/bd_businessitem.md) |
| 4 | fcompany | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | ftallyamounttotal | 记账金额合计(本位币) | numeric | 23 | 10 | √ | 0.00 | 记账金额合计(本位币) |
| 8 | fdepartment | 部门名称 | varchar | 60 |  | √ | ' ' | 部门名称 |
| 9 | fposition | 职位 | varchar | 60 |  | √ | ' ' | 职位 |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fvoucherid | 凭证id | varchar | 60 |  | √ | ' ' | 凭证id |
| 13 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核通过 E :审核不通过 F :废弃 |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fdept | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fvouchernumber | 凭证号 | varchar | 60 |  | √ | ' ' | 凭证号 |
| 17 | fiscurrency | 多币别 | bpchar | 1 |  | √ | '0' | 多币别 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fdescription | 事由 | varchar | 2000 |  | √ | ' ' | 事由 |
| 20 | fisgenvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 21 | ftallydate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 22 | fapplierid | fapplierid | int8 | 64 |  | √ | 0 |  |
| 23 | fattachmentacount | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 24 | fimagenumber | 影像编码 | varchar | 60 |  | √ | ' ' | 影像编码 |
| 25 | forgcurrency | 组织本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 27 | ftallycompany | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fnextauditor | 下一步审核人 | varchar | 60 |  | √ | ' ' | 下一步审核人 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_tallyapplyapl |  | fauditorid |
| 2 | t_tk_tallyapplybill_pkey |  | fid |

---

## 记账申请单-关联追踪表 t_tk_tallyapplybill_tc

- **表名称：** 记账申请单-关联追踪表
- **表名：** t_tk_tallyapplybill_tc

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
| 1 | idx_tk_tallyapplybill_tc_tid |  | ftid |
| 2 | idx_tk_tallyapplybill_tc_tbill |  | ftbillid |
| 3 | t_tk_tallyapplybill_tc_pkey |  | fid |

---

## 记账明细-子表 t_tk_tallydetail

- **表名称：** 记账明细-子表
- **表名：** t_tk_tallydetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | ftaxamount | numeric | 23 | 10 | √ | 0.00 |  |
| 3 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 4 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 5 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fstardandtaxamount | fstardandtaxamount | numeric | 23 | 10 | √ | 0.00 |  |
| 7 | fstandardtallyamount | 记账金额(本位币) | numeric | 23 | 10 | √ | 0.00 | 记账金额(本位币) |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fexchangerate | 汇率 | numeric | 19 | 4 | √ | 0.0000 | 汇率 |
| 10 | fbizdetailtype | 业务项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 11 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 12 | ftallydeptid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 14 | fcostcenter | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 15 | ftallyamount | 记账金额 | numeric | 23 | 10 | √ | 0.00 | 记账金额 |
| 16 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 17 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 18 | ftallyexplanation | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_tallydetail_billid |  | fid |
| 2 | t_tk_tallydetail_pkey |  | fdetailid |

---

## 记账申请单-多语言表 t_tk_tallyapplybill_l

- **表名称：** 记账申请单-多语言表
- **表名：** t_tk_tallyapplybill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fposition | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc__tallyapplybill_l |  | fid,flocaleid |
| 2 | pk_t_tk_tallyapplybill_l |  | fpkid |

---

## 关联子实体-子表 t_tk_tallyentity_lk

- **表名称：** 关联子实体-子表
- **表名：** t_tk_tallyentity_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_tallyentity_lk_fk |  | fdetailid |
| 2 | t_tk_tallyentity_lk_pkey |  | fpkid |

---

## 记账申请单-反写记录表 t_tk_tallyapplybill_wb

- **表名称：** 记账申请单-反写记录表
- **表名：** t_tk_tallyapplybill_wb

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
| 1 | t_tk_tallyapplybill_wb_pkey |  | fentryid |
| 2 | idx_tk_tallyapplybill_wb_fk |  | fid |
