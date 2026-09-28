# 采购合同-conm_purcontract

## 合同条款-子表 t_conm_purcontracttentry

- **表名称：** 合同条款-子表
- **表名：** t_conm_purcontracttentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftermgroupid | 分组 | int8 | 64 |  | √ | 0 | [合同条款分组 conm_termgroup](../conm_files/conm_termgroup.md) |
| 3 | ftermentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 4 | ftermcontent | 条款内容 | varchar | 2000 |  |  | ' ' | 条款内容 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ftermid | 合同条款 | int8 | 64 |  | √ | 0 | [合同条款 conm_term](../conm_files/conm_term.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_purcontracttentry |  | fid |
| 2 | t_conm_purcontracttentry_pkey |  | fentryid |

---

## 采购合同-分表 t_conm_purcontract_f

- **表名称：** 采购合同-分表
- **表名：** t_conm_purcontract_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpaidallamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 3 | fispayrate | 按比例(%) | bpchar | 1 |  | √ | '1' | 按比例(%) |
| 4 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 5 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 7 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 8 | fisentrysumamt | 明细金额汇总 | bpchar | 1 |  | √ | '1' | 明细金额汇总 |
| 9 | fpaidpreallamount | 已预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预付金额 |
| 10 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 11 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 12 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 13 | forderallamount | 已采购价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 已采购价税合计 |
| 14 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 16 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 17 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_purcontract_f |  | fsettlecurrencyid |
| 2 | t_conm_purcontract_f_pkey |  | fid |

---

## 采购合同-反写记录表 t_conm_purcontract_wb

- **表名称：** 采购合同-反写记录表
- **表名：** t_conm_purcontract_wb

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
| 1 | t_conm_purcontract_wb_pkey |  | fentryid |
| 2 | idx_conm_purcontract_wb_fk |  | fid |

---

## 采购合同-分表 t_conm_purcontract_s

- **表名称：** 采购合同-分表
- **表名：** t_conm_purcontract_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faddress | faddress | varchar | 512 |  |  | ' ' |  |
| 3 | fterminatorid | 终止人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fproviderlinkmanid | 供货联系人 | int8 | 64 |  | √ | 0 | [供应商联系人 bd_supplierlinkman](../sbd_files/bd_supplierlinkman.md) |
| 5 | fterminatedate | 终止日期 | timestamp | 0 |  |  | null | 终止日期 |
| 6 | fcontpartiesid | 合同主体 | int8 | 64 |  | √ | 0 | [合同主体 conm_contparties](../conm_files/conm_contparties.md) |
| 7 | fsigndate | 签章日期 | timestamp | 0 |  |  | null | 签章日期 |
| 8 | freviewdate | 评审日期 | timestamp | 0 |  |  | null | 评审日期 |
| 9 | fparty2nd | 乙方 | varchar | 255 |  | √ | ' ' | 乙方 |
| 10 | fprovideraddress | 供货联系地址 | varchar | 512 |  |  | ' ' | 供货联系地址 |
| 11 | femail2nd | 乙方邮箱 | varchar | 100 |  | √ | ' ' | 乙方邮箱 |
| 12 | fphone2nd | 乙方电话 | varchar | 255 |  |  | null | 乙方电话 |
| 13 | ffilingerid | 归档人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | finvoicesupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 15 | fframename | 框架协议名称 | varchar | 100 |  | √ | ' ' | 框架协议名称 |
| 16 | fcontactperson1st | 甲方联系人 | varchar | 60 |  | √ | ' ' | 甲方联系人 |
| 17 | fframeversion | 框架协议版本 | varchar | 30 |  | √ | ' ' | 框架协议版本 |
| 18 | fframenum | 框架协议编号 | varchar | 80 |  | √ | ' ' | 框架协议编号 |
| 19 | fprovidersupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 20 | fsupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 21 | freceivesupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 22 | fpartcid | 第三方 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 23 | fsignerid | 签章人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fparty1st | 甲方 | varchar | 255 |  | √ | ' ' | 甲方 |
| 25 | flinkmanid | flinkmanid | int8 | 64 |  | √ | 0 |  |
| 26 | fphone1st | 甲方电话 | varchar | 255 |  |  | null | 甲方电话 |
| 27 | ffilingdate | 归档日期 | timestamp | 0 |  |  | null | 归档日期 |
| 28 | femail1st | 甲方邮箱 | varchar | 100 |  | √ | ' ' | 甲方邮箱 |
| 29 | fcontactperson2nd | 乙方联系人 | varchar | 60 |  | √ | ' ' | 乙方联系人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_purcontract_s |  | fsupplierid |
| 2 | t_conm_purcontract_s_pkey |  | fid |

---

## 采购合同-多语言表 t_conm_purcontract_l

- **表名称：** 采购合同-多语言表
- **表名：** t_conm_purcontract_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 2000 |  |  | ' ' | 备注 |
| 3 | fdesport | 目的地 | varchar | 512 |  | √ | ' ' | 目的地 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fsrcport | 交货地 | varchar | 512 |  | √ | ' ' | 交货地 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fbillname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_purcontract_l_name |  | fbillname,fid |
| 2 | idx_conm_purcontract_l |  | fid,flocaleid |
| 3 | t_conm_purcontract_l_pkey |  | fpkid |

---

## 付款计划-子表 t_conm_purcontractpentry

- **表名称：** 付款计划-子表
- **表名：** t_conm_purcontractpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanprojrecamount | 已确认项目结算额 | numeric | 23 | 10 | √ | 0 | 已确认项目结算额 |
| 3 | fplanprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 4 | fplanmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 5 | fintervaltime | 间隔时间 | int8 | 64 |  | √ | 0 | 间隔时间 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fpayamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 8 | fplanprojectassamount | 关联项目结算额 | numeric | 23 | 10 | √ | 0 | 关联项目结算额 |
| 9 | fplanmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 10 | fisprepay | 是否预付 | bpchar | 1 |  | √ | '0' | 是否预付 |
| 11 | fplanentrysettleorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fplanbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 13 | fpayprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 14 | fplanexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 15 | fplanmilestone | 里程碑 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 16 | fjoinpayamount | 关联付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 关联付款金额 |
| 17 | fpaypriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 18 | fplanconbillnumber | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 19 | fplanentrycomment | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 20 | fplanlicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 21 | fpayentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 22 | fpayrate | 应付比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 应付比例(%) |
| 23 | ftimeunit | 时间单位 | varchar | 5 |  | √ | ' ' | 时间单位,枚举: A :工作日 B :自然日 C :月 |
| 24 | fpaidamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fpaynameid | 款项名称 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 27 | fpaydate | 到期日 | timestamp | 0 |  |  | null | 到期日 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_purcontractpentry |  | fid |
| 2 | t_conm_purcontractpentry_pkey |  | fentryid |

---

## 关联子实体-子表 t_conm_purcontractentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_conm_purcontractentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbaseqty_old | 基本数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量_原始携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fbaseqty | 基本数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量_确认携带值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_purcontractentry_lk_pkey |  | fpkid |
| 2 | idx_conm_purcontractentry_lk_fk |  | fentryid |

---

## 采购合同-主表 t_conm_purcontract

- **表名称：** 采购合同-主表
- **表名：** t_conm_purcontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmpmpaymethod | 项目支出确认方式 | varchar | 5 |  | √ | ' ' | 项目支出确认方式,枚举: D :按交付物 M :按里程碑 P :按项目进度 |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 5 | fcancelstatus | 作废状态 | varchar | 5 |  | √ | ' ' | 作废状态,枚举: A :未作废 B :已作废 |
| 6 | fsplitschemeid | 付款计划方案 | int8 | 64 |  | √ | 0 | [付款计划方案 ap_plansplit_scheme](../ap_files/ap_plansplit_scheme.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | freviewstatus | 评审状态 | varchar | 5 |  | √ | ' ' | 评审状态,枚举: A :未评审 B :评审中 C :通过 D :不通过 E :未启用 |
| 9 | fterminatestatus | 终止状态 | varchar | 5 |  | √ | ' ' | 终止状态,枚举: A :未终止 B :已终止 |
| 10 | ffreezerid | 冻结人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcategoryid | 合同种类 | int8 | 64 |  | √ | 0 | [合同种类 conm_category](../conm_files/conm_category.md) |
| 12 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 13 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillno | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 15 | fversion | 版本号 | varchar | 30 |  | √ | '1' | 版本号 |
| 16 | fconfirmdate | 确认日期 | timestamp | 0 |  |  | null | 确认日期 |
| 17 | ftotalamountcn | 金额（大写） | varchar | 50 |  | √ | ' ' | 金额（大写） |
| 18 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | ftemplateid | 合同模板 | int8 | 64 |  | √ | 0 | [合同模板 conm_template](../conm_files/conm_template.md) |
| 20 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fpayconditionid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 22 | ftrdbillno | 第三方业务编码 | varchar | 50 |  | √ | ' ' | 第三方业务编码 |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 9 :迁移生成 |
| 25 | fbiztimeend | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 26 | fbillname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |
| 27 | ftypeid | 合同类型 | int8 | 64 |  | √ | 0 | [合同类型 conm_type](../conm_files/conm_type.md) |
| 28 | fdescountryid | 目的国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 29 | fvalidstatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 C :已失效 |
| 30 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 31 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fpartaid | 合同甲方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | fisonlist | 基于清单 | bpchar | 1 |  | √ | '0' | 基于清单 |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 36 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fiselecsignature | 是否电子签章 | bpchar | 1 |  | √ | '0' | 是否电子签章 |
| 38 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 39 | fconfirmstatus | 确认状态 | varchar | 5 |  | √ | ' ' | 确认状态,枚举: A :未确认 B :已确认 |
| 40 | ftradetermid | 贸易术语 | int8 | 64 |  | √ | 0 | [贸易术语 gtm_tradeterm](../gtm_files/gtm_tradeterm.md) |
| 41 | fbiztime | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 42 | fchangestatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 43 | fdocumentid | 电签合同ID | varchar | 50 |  | √ | ' ' | 电签合同ID |
| 44 | fcancelerid | 作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fsrccountryid | 装运国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 47 | ffilingstatus | 归档状态 | varchar | 5 |  | √ | ' ' | 归档状态,枚举: A :未归档 B :已归档 C :未启用 |
| 48 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 49 | fsignstatus | 签章状态 | varchar | 5 |  | √ | ' ' | 签章状态,枚举: A :未签章 B :签章完成 C :未启用 D :乙方已签 E :甲方已签 F :上传完成 |
| 50 | ffreezedate | 冻结日期 | timestamp | 0 |  |  | null | 冻结日期 |
| 51 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 52 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 53 | fbizmode | 业务模式 | varchar | 5 |  | √ | ' ' | 业务模式,枚举: A :统谈统签 B :统谈分签 C :分谈分签 |
| 54 | fconmprop | 合同属性 | varchar | 5 |  | √ | ' ' | 合同属性,枚举: A :框架协议 B :合同 |
| 55 | ftotaltaxamountcn | 税额（大写） | varchar | 50 |  | √ | ' ' | 税额（大写） |
| 56 | fcomment | 备注 | varchar | 2000 |  |  | ' ' | 备注 |
| 57 | fdesport | 目的地 | varchar | 512 |  | √ | ' ' | 目的地 |
| 58 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 59 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 60 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 61 | fsrcport | 交货地 | varchar | 512 |  | √ | ' ' | 交货地 |
| 62 | ftotalallamountcn | 价税合计（大写） | varchar | 50 |  | √ | ' ' | 价税合计（大写） |
| 63 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 64 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :未关闭 B :已关闭 |
| 65 | ffreezestatus | 冻结状态 | varchar | 5 |  | √ | ' ' | 冻结状态,枚举: A :未冻结 B :已冻结 |
| 66 | fpartbid | 合同乙方 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 67 | fsubversion | 子版本号 | varchar | 30 |  | √ | '1' | 子版本号 |
| 68 | fconfirmerid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 69 | ftemplateentryid | 模板版本 | int8 | 64 |  | √ | 0 | [模板版本 conm_tempfileentry](../conm_files/conm_tempfileentry.md) |
| 70 | ftransportmodeid | 运输方式 | int8 | 64 |  | √ | 0 | [运输方式 gtm_transportmode](../gtm_files/gtm_transportmode.md) |
| 71 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 72 | fbiztimebegin | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 73 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 74 | fcarrierid | 承运方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_purcontract_pkey |  | fid |
| 2 | idx_conm_purcontract_biztime |  | fbiztime |
| 3 | idx_conm_purcontract_org |  | forgid,fbiztime,fbillno,fid |
| 4 | idx_conm_purcontract_billno |  | fbillno |

---

## 关联子实体-子表 t_conm_purcontract_lk

- **表名称：** 关联子实体-子表
- **表名：** t_conm_purcontract_lk

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
| 1 | idx_conm_purcontract_lk_fk |  | fid |
| 2 | t_conm_purcontract_lk_pkey |  | fpkid |

---

## 采购合同-关联追踪表 t_conm_purcontract_tc

- **表名称：** 采购合同-关联追踪表
- **表名：** t_conm_purcontract_tc

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
| 1 | idx_conm_purcontract_tc_tbill |  | ftbillid |
| 2 | idx_conm_purcontract_tc_tid |  | ftid |
| 3 | t_conm_purcontract_tc_pkey |  | fid |

---

## 物料明细-分表 t_conm_purcontractentry_f

- **表名称：** 物料明细-分表
- **表名：** t_conm_purcontractentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 4 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 5 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 6 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 7 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 9 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 10 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 11 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 12 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 13 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 15 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_purcontractentry_f_pkey |  | fentryid |
| 2 | idx_conm_purcontractentry_f |  | fid |

---

## 物料明细-分表 t_conm_purcontractentry_r

- **表名称：** 物料明细-分表
- **表名：** t_conm_purcontractentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrmsrcbillno | 来源SRM单据编号 | varchar | 100 |  | √ | ' ' | 来源SRM单据编号 |
| 3 | fjoinpayablebaseqty | 关联应付基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联应付基本数量 |
| 4 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 5 | fpayablebaseqty | 应付基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应付基本数量 |
| 6 | fdeliverdate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 7 | fexecutedamountandtax | 已执行价税合计 | numeric | 23 | 10 | √ | 0 | 已执行价税合计 |
| 8 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | forderqty | 已采购数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已采购数量 |
| 10 | fpayableamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 11 | fsrmsrcbillentryseq | 来源SRM单据行号 | int8 | 64 |  | √ | 0 | 来源SRM单据行号 |
| 12 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 13 | fsrmsrcbillid | 来源SRM单据ID | int8 | 64 |  | √ | 0 | 来源SRM单据ID |
| 14 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 15 | fdeliveraddress | 交货地址 | varchar | 512 |  |  | ' ' | 交货地址 |
| 16 | fsrmsrcbillentryid | 来源SRM单据行ID | int8 | 64 |  | √ | 0 | 来源SRM单据行ID |
| 17 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 18 | forderbaseqty | 已采购基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已采购基本数量 |
| 19 | fsrmsrcbillentity | 来源SRM单据标识 | varchar | 50 |  | √ | ' ' | 来源SRM单据标识 |
| 20 | fwarehouseid | 收货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 21 | fpayablepriceqty | 应付数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应付数量 |
| 22 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 23 | fentryinvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fjoinpushamountandtax | 关联下推价税合计 | numeric | 23 | 10 | √ | 0 | 关联下推价税合计 |
| 25 | fjoinpayablepriceqty | 关联应付数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联应付数量 |
| 26 | fjoinorderbaseqty | 关联采购基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联采购基本数量 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 28 | fjoinorderqty | 关联采购数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联采购数量 |
| 29 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_purcontractentry_r |  | fid |
| 2 | t_conm_purcontractentry_r_pkey |  | fentryid |

---

## 物料明细-子表 t_conm_purcontractentry

- **表名称：** 物料明细-子表
- **表名：** t_conm_purcontractentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frowclosestatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 3 | fsupplierlot | fsupplierlot | varchar | 80 |  | √ | ' ' |  |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | frownum | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 8 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 9 | fprojectconfqty | 已确认项目服务数量 | numeric | 23 | 10 | √ | 0 | 已确认项目服务数量 |
| 10 | fconbillnumber | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 11 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 16 | fprojectassqty | 关联项目服务数量 | numeric | 23 | 10 | √ | 0 | 关联项目服务数量 |
| 17 | fprojectassbaseqty | 关联项目服务基本数量 | numeric | 23 | 10 | √ | 0 | 关联项目服务基本数量 |
| 18 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 19 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 20 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 21 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | fbizunitid | fbizunitid | int8 | 64 |  | √ | 0 |  |
| 23 | fmpmtasknoid | fmpmtasknoid | int8 | 64 |  | √ | 0 |  |
| 24 | fbillentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 25 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 27 | fprojectassamount | 关联项目结算额 | numeric | 23 | 10 | √ | 0 | 关联项目结算额 |
| 28 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 29 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 30 | fmaterialmasterid | 主物料(废弃) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 31 | frowterminatestatus | 行终止状态 | varchar | 5 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 32 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 33 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 34 | fentrypurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fentrycomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 36 | fprojrecamount | 已确认项目结算额 | numeric | 23 | 10 | √ | 0 | 已确认项目结算额 |
| 37 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 38 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 39 | fprojectconfbaseqty | 已确认项目服务基本数量 | numeric | 23 | 10 | √ | 0 | 已确认项目服务基本数量 |
| 40 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | fbizunitrate | fbizunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 43 | fentrychangetype | fentrychangetype | varchar | 5 |  | √ | ' ' |  |
| 44 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 45 | fmaterialname | 物料名称(历史) | varchar | 255 |  |  | ' ' | 物料名称(历史) |
| 46 | fqtybizunit | fqtybizunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 47 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_purcontractentry |  | fid |
| 2 | t_conm_purcontractentry_pkey |  | fentryid |

---

## 其他方-多选基础资料表 t_conm_contpartother

- **表名称：** 其他方-多选基础资料表
- **表名：** t_conm_contpartother

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_contpartother_pkey |  | fpkid |
| 2 | idx_conm_contpartother_fid |  | fid |
