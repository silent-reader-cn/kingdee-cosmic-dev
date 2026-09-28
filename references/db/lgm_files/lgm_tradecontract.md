# 运输协议-lgm_tradecontract

## 费用明细-子表 t_lgm_tracontractentry

- **表名称：** 费用明细-子表
- **表名：** t_lgm_tracontractentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funitld | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | froutedistance | 运输距离 | numeric | 23 | 10 | √ | 0.0 | 运输距离 |
| 4 | fexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcosttaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0 | 含税单价 |
| 7 | fcostprice | 单价 | numeric | 23 | 10 | √ | 0.0 | 单价 |
| 8 | fqtyto | 至 | numeric | 23 | 10 | √ | 0.0 | 至 |
| 9 | fshipunittype | 运输单元类型 | int8 | 64 |  | √ | 0 | [运输单元类型 lgm_shipunittype](../lgm_files/lgm_shipunittype.md) |
| 10 | fcosttaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0 | 税率(%) |
| 11 | fqtyfrom | 从 | numeric | 23 | 10 | √ | 0.0 | 从 |
| 12 | fcostcurrency | 费用币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 13 | fcosttaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 14 | ftransportroute | 运输路线 | int8 | 64 |  | √ | 0 | [运输路线 lgm_transportroute](../lgm_files/lgm_transportroute.md) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lgm_tracontractentry |  | fentryid |
| 2 | idx_lgm_tracontractentry_fid |  | fid |

---

## 协议条款-子表 t_lgm_termsentry

- **表名称：** 协议条款-子表
- **表名：** t_lgm_termsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftermentrychangetype | 变更方式 | varchar | 50 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 3 | ftermgroupid | 分组 | int8 | 64 |  | √ | 0 | [合同条款分组 conm_termgroup](../conm_files/conm_termgroup.md) |
| 4 | ftermcontent | 条款内容 | varchar | 2000 |  | √ | ' ' | 条款内容 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ftermid | 协议条款 | int8 | 64 |  | √ | 0 | [合同条款 conm_term](../conm_files/conm_term.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_lgm_termsentry_fid |  | fid |
| 2 | pk_t_lgm_termsentry |  | fentryid |

---

## 运输协议-分表 t_lgm_tracontract_f

- **表名称：** 运输协议-分表
- **表名：** t_lgm_tracontract_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispayrate | 按比例(%) | bpchar | 1 |  | √ | ' ' | 按比例(%) |
| 3 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0.0 | 金额 |
| 4 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 5 | fistax | 含税 | bpchar | 1 |  | √ | ' ' | 含税 |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0 | 汇率 |
| 7 | fisentrysumamt | 明细金额汇总 | bpchar | 1 |  | √ | ' ' | 明细金额汇总 |
| 8 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 9 | fexchangetype | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 10 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 11 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 12 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 13 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0.0 | 税额 |
| 14 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0.0 | 价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lgm_tracontract_f |  | fid |
| 2 | idx_lgm_tracontract_f |  | fcurrencyid |

---

## 运输协议-主表 t_lgm_tracontract

- **表名称：** 运输协议-主表
- **表名：** t_lgm_tracontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fforwarder | 货运代理 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 3 | fiselecsignature | 是否电子签章 | bpchar | 1 |  | √ | '0' | 是否电子签章 |
| 4 | forgid | 运输组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcontpartiesid | 协议主体 | int8 | 64 |  | √ | 0 | [合同主体 conm_contparties](../conm_files/conm_contparties.md) |
| 6 | fbiztime | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fparty2nd | 乙方 | varchar | 255 |  | √ | ' ' | 乙方 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | femail2nd | 乙方邮箱 | varchar | 254 |  | √ | ' ' | 乙方邮箱 |
| 11 | fphone2nd | 乙方电话 | varchar | 50 |  | √ | ' ' | 乙方电话 |
| 12 | fcategoryid | 合同种类 | int8 | 64 |  | √ | 0 | [合同种类 conm_category](../conm_files/conm_category.md) |
| 13 | fbillno | 协议编号 | varchar | 80 |  | √ | ' ' | 协议编号 |
| 14 | fversion | 版本号 | varchar | 30 |  | √ | ' ' | 版本号 |
| 15 | fframename | 框架协议名称 | varchar | 100 |  | √ | ' ' | 框架协议名称 |
| 16 | funitsrctype | 计量单位来源 | varchar | 50 |  | √ | ' ' | 计量单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbizmode | 业务模式 | varchar | 50 |  | √ | ' ' | 业务模式,枚举: A :统谈统签 B :统谈分签 C :分谈分签 |
| 19 | fconmprop | 合同属性 | varchar | 50 |  | √ | ' ' | 合同属性,枚举: A :框架协议 B :合同 |
| 20 | ftemplateid | 协议模板 | int8 | 64 |  | √ | 0 | [合同模板 conm_template](../conm_files/conm_template.md) |
| 21 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 23 | fcontactperson1st | 甲方联系人 | varchar | 60 |  | √ | ' ' | 甲方联系人 |
| 24 | ftransportmode | 运输方式 | int8 | 64 |  | √ | 0 | [运输方式 gtm_transportmode](../gtm_files/gtm_transportmode.md) |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fframeversion | 框架协议版本 | varchar | 30 |  | √ | ' ' | 框架协议版本 |
| 27 | fframenum | 框架协议编号 | varchar | 80 |  | √ | ' ' | 框架协议编号 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fbiztimeend | 协议截止日期 | timestamp | 0 |  |  | null | 协议截止日期 |
| 30 | fbillname | 协议名称 | varchar | 100 |  | √ | ' ' | 协议名称 |
| 31 | fpartbid | 合同乙方 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 32 | ftypeid | 合同类型 | int8 | 64 |  | √ | 0 | [合同类型 conm_type](../conm_files/conm_type.md) |
| 33 | fpartcid | 第三方 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 34 | fsubversion | 子版本号 | varchar | 30 |  | √ | ' ' | 子版本号 |
| 35 | fparty1st | 甲方 | varchar | 255 |  | √ | ' ' | 甲方 |
| 36 | ftemplateentryid | 模板版本 | int8 | 64 |  | √ | 0 | [模板版本 conm_tempfileentry](../conm_files/conm_tempfileentry.md) |
| 37 | fpartaid | 合同甲方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 39 | fbiztimebegin | 协议起始日期 | timestamp | 0 |  |  | null | 协议起始日期 |
| 40 | fisonlist | 基于清单 | bpchar | 1 |  | √ | '0' | 基于清单 |
| 41 | ftransporttype | 运输类型 | varchar | 50 |  | √ | ' ' | 运输类型,枚举: seaship :海运 road :公路 railway :铁路 airlift :航空 delivery :快递 theother :其他 |
| 42 | fphone1st | 甲方电话 | varchar | 50 |  | √ | ' ' | 甲方电话 |
| 43 | femail1st | 甲方邮箱 | varchar | 254 |  | √ | ' ' | 甲方邮箱 |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fcontactperson2nd | 乙方联系人 | varchar | 60 |  | √ | ' ' | 乙方联系人 |
| 46 | fbilltypeid | 协议类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_lgm_tracontract_fbillno |  | fbillno |
| 2 | pk_t_lgm_tracontract |  | fid |

---

## 运输协议-多语言表 t_lgm_tracontract_l

- **表名称：** 运输协议-多语言表
- **表名：** t_lgm_tracontract_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fbillname | 协议名称 | varchar | 100 |  | √ | ' ' | 协议名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lgm_tracontract_l_0 |  | fid,flocaleid |
| 2 | pk_t_lgm_tracontract_l |  | fpkid |

---

## 运输协议-分表 t_lgm_tracontract_s

- **表名称：** 运输协议-分表
- **表名：** t_lgm_tracontract_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fterminatorid | 终止人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fterminatedate | 终止日期 | timestamp | 0 |  |  | null | 终止日期 |
| 5 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 6 | fcancelstatus | 作废状态 | varchar | 50 |  | √ | ' ' | 作废状态,枚举: A :未作废 B :已作废 |
| 7 | fconfirmstatus | 确认状态 | varchar | 50 |  | √ | ' ' | 确认状态,枚举: A :未确认 B :已确认 |
| 8 | fsigndate | 签章日期 | timestamp | 0 |  |  | null | 签章日期 |
| 9 | freviewdate | 评审日期 | timestamp | 0 |  |  | null | 评审日期 |
| 10 | fchangestatus | 变更状态 | varchar | 50 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 11 | freviewstatus | 评审状态 | varchar | 50 |  | √ | ' ' | 评审状态,枚举: A :未评审 B :评审中 C :通过 D :不通过 E :未启用 |
| 12 | fcancelerid | 作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fterminatestatus | 终止状态 | varchar | 50 |  | √ | ' ' | 终止状态,枚举: A :未终止 B :已终止 |
| 14 | ffreezerid | 冻结人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | ffilingstatus | 归档状态 | varchar | 50 |  | √ | ' ' | 归档状态,枚举: A :未归档 B :已归档 C :未启用 |
| 16 | ffilingerid | 归档人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 18 | fsignstatus | 签章状态 | varchar | 50 |  | √ | ' ' | 签章状态,枚举: A :未签章 B :签章完成 C :未启用 D :乙方已签 E :甲方已签 F :上传完成 |
| 19 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 20 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fconfirmdate | 确认日期 | timestamp | 0 |  |  | null | 确认日期 |
| 22 | ffreezedate | 冻结日期 | timestamp | 0 |  |  | null | 冻结日期 |
| 23 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fbillcretype | 单据生成类型 | varchar | 50 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 |
| 25 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 26 | fclosestatus | 关闭状态 | varchar | 50 |  | √ | ' ' | 关闭状态,枚举: A :未关闭 B :已关闭 |
| 27 | ffreezestatus | 冻结状态 | varchar | 50 |  | √ | ' ' | 冻结状态,枚举: A :未冻结 B :已冻结 |
| 28 | fsignerid | 签章人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fvalidstatus | 生效状态 | varchar | 50 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 C :已失效 |
| 30 | fconfirmerid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 32 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | ffilingdate | 归档日期 | timestamp | 0 |  |  | null | 归档日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lgm_tracontract_s |  | fid |
| 2 | idx_t_lgm_tracontract_s_status |  | fvalidstatus |

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
