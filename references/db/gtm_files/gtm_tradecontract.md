# 贸易协议-gtm_tradecontract

## 协议条款-子表 t_gtm_tracontracttentry

- **表名称：** 协议条款-子表
- **表名：** t_gtm_tracontracttentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftermentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 3 | ftermgroupid | 分组 | int8 | 64 |  | √ | 0 | [合同条款分组 conm_termgroup](../conm_files/conm_termgroup.md) |
| 4 | ftermcontent | 条款内容 | varchar | 2000 |  | √ | ' ' | 条款内容 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ftermid | 协议条款 | int8 | 64 |  | √ | 0 | [合同条款 conm_term](../conm_files/conm_term.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_tracontracttentry |  | fentryid |
| 2 | idx_gtm_tracontracttentry |  | fid |

---

## 贸易协议-多语言表 t_gtm_tracontract_l

- **表名称：** 贸易协议-多语言表
- **表名：** t_gtm_tracontract_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fimpport | 目的地 | varchar | 770 |  | √ | ' ' | 目的地 |
| 3 | fcomment | 备注 | varchar | 770 |  | √ | ' ' | 备注 |
| 4 | fexpport | 交货地 | varchar | 770 |  | √ | ' ' | 交货地 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fbillname | 合同名称 | varchar | 155 |  | √ | ' ' | 合同名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_tracontract_l |  | fpkid |
| 2 | idx_gtm_tracontract_l |  | fid,flocaleid |
| 3 | idx_gtm_tracontract_name |  | fbillname,fid |

---

## 付款计划-子表 t_gtm_tracontractpentry

- **表名称：** 付款计划-子表
- **表名：** t_gtm_tracontractpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjoinpayamount | 关联付款金额 | numeric | 23 | 10 | √ | 0 | 关联付款金额 |
| 3 | fintervaltime | 间隔时间 | int8 | 64 |  | √ | 0 | 间隔时间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fpayentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 6 | fpayamount | 付款金额 | numeric | 23 | 10 | √ | 0 | 付款金额 |
| 7 | fisprepay | 是否预付 | bpchar | 1 |  | √ | '0' | 是否预付 |
| 8 | fpayrate | 付款比例(%) | numeric | 15 | 2 | √ | 0 | 付款比例(%) |
| 9 | ftimeunit | 时间单位 | varchar | 5 |  | √ | ' ' | 时间单位,枚举: A :工作日 B :自然日 C :月 |
| 10 | fpaidamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fpaynameid | 款项名称 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 13 | fpaydate | 计划付款日期 | timestamp | 0 |  |  | null | 计划付款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_tracontractpentry |  | fentryid |
| 2 | idx_gtm_tracontractpentry |  | fid |

---

## 贸易协议-分表 t_gtm_tracontract_s

- **表名称：** 贸易协议-分表
- **表名：** t_gtm_tracontract_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontactperson1st | 甲方联系人 | varchar | 60 |  | √ | ' ' | 甲方联系人 |
| 3 | fsigndate | 签章日期 | timestamp | 0 |  |  | null | 签章日期 |
| 4 | freviewdate | 评审日期 | timestamp | 0 |  |  | null | 评审日期 |
| 5 | fparty2nd | 乙方 | varchar | 255 |  | √ | ' ' | 乙方 |
| 6 | fpartbid | 合同乙方 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 7 | fsignerid | 签章人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fpartcid | 第三方 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 9 | femail2nd | 乙方邮箱 | varchar | 70 |  | √ | ' ' | 乙方邮箱 |
| 10 | fparty1st | 甲方 | varchar | 255 |  | √ | ' ' | 甲方 |
| 11 | fphone2nd | 乙方电话 | varchar | 50 |  | √ | ' ' | 乙方电话 |
| 12 | ffilingerid | 归档人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fpartaid | 合同甲方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fphone1st | 甲方电话 | varchar | 50 |  | √ | ' ' | 甲方电话 |
| 15 | femail1st | 甲方邮箱 | varchar | 70 |  | √ | ' ' | 甲方邮箱 |
| 16 | ffilingdate | 归档日期 | timestamp | 0 |  |  | null | 归档日期 |
| 17 | fcontactperson2nd | 乙方联系人 | varchar | 60 |  | √ | ' ' | 乙方联系人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_tracontract_s |  | fpartaid |
| 2 | pk_gtm_tracontract_s |  | fid |

---

## 贸易协议-分表 t_gtm_tracontract_f

- **表名称：** 贸易协议-分表
- **表名：** t_gtm_tracontract_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftotalygprofi | 预估利润 | numeric | 23 | 10 | √ | 0 | 预估利润 |
| 3 | ftotalcuramount | 采购金额(本位币) | numeric | 23 | 10 | √ | 0 | 采购金额(本位币) |
| 4 | ftotalamount | 采购金额 | numeric | 23 | 10 | √ | 0 | 采购金额 |
| 5 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 6 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 7 | fisentrysumamt | 明细金额汇总 | bpchar | 1 |  | √ | '1' | 明细金额汇总 |
| 8 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 9 | ftotalcurtaxamount | 采购税额(本位币) | numeric | 23 | 10 | √ | 0 | 采购税额(本位币) |
| 10 | fsmtotalamount | 销售金额 | numeric | 23 | 10 | √ | 0 | 销售金额 |
| 11 | ftotalcurallamount | 采购价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 采购价税合计(本位币) |
| 12 | fsmtotalcuramount | 销售金额(本位币) | numeric | 23 | 10 | √ | 0 | 销售金额(本位币) |
| 13 | fispayrate | 按比例(%) | bpchar | 1 |  | √ | '1' | 按比例(%) |
| 14 | fsmtotalallamount | 销售价税合计 | numeric | 23 | 10 | √ | 0 | 销售价税合计 |
| 15 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 16 | fsmtotalcurallamount | 销售价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 销售价税合计(本位币) |
| 17 | fsmtotaltaxamount | 销售税额 | numeric | 23 | 10 | √ | 0 | 销售税额 |
| 18 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 19 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 20 | fsmtotalcurtaxamount | 销售税额(本位币) | numeric | 23 | 10 | √ | 0 | 销售税额(本位币) |
| 21 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 22 | ftotalallamount | 采购价税合计 | numeric | 23 | 10 | √ | 0 | 采购价税合计 |
| 23 | ftotaltaxamount | 采购税额 | numeric | 23 | 10 | √ | 0 | 采购税额 |
| 24 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_tracontract_f |  | fid |
| 2 | idx_gtm_tracontract_f |  | fsettlecurrencyid |

---

## 贸易协议-主表 t_gtm_tracontract

- **表名称：** 贸易协议-主表
- **表名：** t_gtm_tracontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fterminatorid | 终止人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | forgid | 贸易组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcancelstatus | 作废状态 | varchar | 5 |  | √ | ' ' | 作废状态,枚举: A :未作废 B :已作废 |
| 5 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 6 | fimporgid | 进口组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | freviewstatus | 评审状态 | varchar | 5 |  | √ | ' ' | 评审状态,枚举: A :未评审 B :评审中 C :通过 D :不通过 E :未启用 |
| 9 | fimpdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fterminatestatus | 终止状态 | varchar | 5 |  | √ | ' ' | 终止状态,枚举: A :未终止 B :已终止 |
| 11 | ffreezerid | 冻结人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fexpcarrierid | 承运方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 13 | fcategoryid | 合同种类 | int8 | 64 |  | √ | 0 | [合同种类 conm_category](../conm_files/conm_category.md) |
| 14 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 15 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillno | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 17 | fframename | 框架协议名称 | varchar | 100 |  | √ | ' ' | 框架协议名称 |
| 18 | fversion | 版本号 | varchar | 30 |  | √ | ' ' | 版本号 |
| 19 | fconfirmdate | 确认日期 | timestamp | 0 |  |  | null | 确认日期 |
| 20 | fexporgid | 出口组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fimpport | 目的地 | varchar | 512 |  | √ | ' ' | 目的地 |
| 22 | ftemplateid | 合同模板 | int8 | 64 |  | √ | 0 | [合同模板 conm_template](../conm_files/conm_template.md) |
| 23 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fexpdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fexpcountryid | 装运国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 26 | fframeversion | 框架协议版本 | varchar | 30 |  | √ | ' ' | 框架协议版本 |
| 27 | fpayconditionid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 28 | fexplinkmanid | 联系人 | int8 | 64 |  | √ | 0 | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 29 | fimplinkmanid | 联系人 | int8 | 64 |  | √ | 0 | [供应商联系人 bd_supplierlinkman](../sbd_files/bd_supplierlinkman.md) |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 |
| 32 | fbiztimeend | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 33 | fbillname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |
| 34 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 35 | fimptradetermid | 贸易术语 | int8 | 64 |  | √ | 0 | [贸易术语 gtm_tradeterm](../gtm_files/gtm_tradeterm.md) |
| 36 | ftypeid | 合同类型 | int8 | 64 |  | √ | 0 | [合同类型 conm_type](../conm_files/conm_type.md) |
| 37 | fvalidstatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 C :已失效 |
| 38 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 39 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fisonlist | 基于清单 | bpchar | 1 |  | √ | '1' | 基于清单 |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 43 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 44 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fexptradetermid | 贸易术语 | int8 | 64 |  | √ | 0 | [贸易术语 gtm_tradeterm](../gtm_files/gtm_tradeterm.md) |
| 46 | fiselecsignature | 是否电子签章 | bpchar | 1 |  | √ | '0' | 是否电子签章 |
| 47 | fterminatedate | 终止日期 | timestamp | 0 |  |  | null | 终止日期 |
| 48 | fcontpartiesid | 合同主体 | int8 | 64 |  | √ | 0 | [合同主体 conm_contparties](../conm_files/conm_contparties.md) |
| 49 | fconfirmstatus | 确认状态 | varchar | 5 |  | √ | ' ' | 确认状态,枚举: A :未确认 B :已确认 |
| 50 | fexpport | 交货地 | varchar | 512 |  | √ | ' ' | 交货地 |
| 51 | fbiztime | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 52 | fimpcarrierid | 承运方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 53 | fchangestatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 54 | fexpoperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 55 | fcancelerid | 作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 57 | ffilingstatus | 归档状态 | varchar | 5 |  | √ | ' ' | 归档状态,枚举: A :未归档 B :已归档 C :未启用 |
| 58 | fsignstatus | 签章状态 | varchar | 5 |  | √ | ' ' | 签章状态,枚举: A :未签章 B :签章完成 C :未启用 D :乙方已签 E :甲方已签 F :上传完成 |
| 59 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 60 | ftradepattern | 贸易模式 | varchar | 5 |  | √ | ' ' | 贸易模式,枚举: 1 :双边贸易 2 :进口贸易 3 :出口贸易 |
| 61 | frecconditionid | 收款条件 | int8 | 64 |  | √ | 0 | [收款条件 bd_reccondition](../sbd_files/bd_reccondition.md) |
| 62 | ffreezedate | 冻结日期 | timestamp | 0 |  |  | null | 冻结日期 |
| 63 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 64 | fconmprop | 合同属性 | varchar | 5 |  | √ | ' ' | 合同属性,枚举: A :框架协议 B :合同 |
| 65 | fbizmode | 业务模式 | varchar | 5 |  | √ | ' ' | 业务模式,枚举: A :统谈统签 B :统谈分签 C :分谈分签 |
| 66 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 67 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 68 | fimpoperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 69 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 70 | fexpoperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 71 | fframenum | 框架协议编号 | varchar | 80 |  | √ | ' ' | 框架协议编号 |
| 72 | fexptransportmodeid | 运输方式 | int8 | 64 |  | √ | 0 | [运输方式 gtm_transportmode](../gtm_files/gtm_transportmode.md) |
| 73 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 74 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 75 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :未关闭 B :已关闭 |
| 76 | ffreezestatus | 冻结状态 | varchar | 5 |  | √ | ' ' | 冻结状态,枚举: A :未冻结 B :已冻结 |
| 77 | fsubversion | 子版本号 | varchar | 30 |  | √ | ' ' | 子版本号 |
| 78 | fimptransportmodeid | 运输方式 | int8 | 64 |  | √ | 0 | [运输方式 gtm_transportmode](../gtm_files/gtm_transportmode.md) |
| 79 | ftemplateentryid | 模板版本 | int8 | 64 |  | √ | 0 | [模板版本 conm_tempfileentry](../conm_files/conm_tempfileentry.md) |
| 80 | fimpoperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 81 | fconfirmerid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 82 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 83 | fimpcountryid | 目的国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 84 | fbiztimebegin | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_tracontract |  | fid |
| 2 | idx_gtm_tracontract_billno |  | fbillno |
| 3 | idx_gtm_tracontract_org |  | forgid,fbillno |

---

## 物料明细-分表 t_gtm_tracontractentry_r

- **表名称：** 物料明细-分表
- **表名：** t_gtm_tracontractentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 3 | fpurbaseqty | 已执行采购基本数量 | numeric | 23 | 10 | √ | 0 | 已执行采购基本数量 |
| 4 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 5 | fsalcuramount | 已执行销售金额（本位币） | numeric | 23 | 10 | √ | 0 | 已执行销售金额（本位币） |
| 6 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 7 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 8 | fpurqty | 已执行采购数量 | numeric | 23 | 10 | √ | 0 | 已执行采购数量 |
| 9 | fpurcuramount | 已执行采购金额（本位币） | numeric | 23 | 10 | √ | 0 | 已执行采购金额（本位币） |
| 10 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 11 | fsalbaseqty | 已执行销售基本数量 | numeric | 23 | 10 | √ | 0 | 已执行销售基本数量 |
| 12 | fsalqty | 已执行销售数量 | numeric | 23 | 10 | √ | 0 | 已执行销售数量 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_tracontractentry_r |  | fentryid |
| 2 | idx_gtm_tracontractentry_r |  | fid |

---

## 物料明细-分表 t_gtm_tracontractentry_f

- **表名称：** 物料明细-分表
- **表名：** t_gtm_tracontractentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsmtaxamount | 销售税额 | numeric | 23 | 10 | √ | 0 | 销售税额 |
| 3 | fsmtaxrate | 销售税率(%) | numeric | 23 | 10 | √ | 0 | 销售税率(%) |
| 4 | fdiscountrate | 采购单位折扣(率) | numeric | 23 | 6 | √ | 0 | 采购单位折扣(率) |
| 5 | ftaxrate | 采购税率(%) | numeric | 23 | 2 | √ | 0 | 采购税率(%) |
| 6 | fdiscountamount | 采购折扣额 | numeric | 23 | 10 | √ | 0 | 采购折扣额 |
| 7 | fsmdiscountrate | 销售单位折扣(率) | numeric | 23 | 10 | √ | 0 | 销售单位折扣(率) |
| 8 | famount | 采购金额 | numeric | 23 | 10 | √ | 0 | 采购金额 |
| 9 | fsmcuramountandtax | 销售价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 销售价税合计(本位币) |
| 10 | fprice | 采购单价 | numeric | 23 | 10 | √ | 0 | 采购单价 |
| 11 | fsmprice | 销售单价 | numeric | 23 | 10 | √ | 0 | 销售单价 |
| 12 | fygprofi | 预估利润 | numeric | 23 | 10 | √ | 0 | 预估利润 |
| 13 | fsmdiscounttype | 销售折扣方式 | varchar | 5 |  | √ | ' ' | 销售折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 14 | fcuramount | 采购金额(本位币) | numeric | 23 | 10 | √ | 0 | 采购金额(本位币) |
| 15 | ftaxrateid | 采购税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 16 | fpriceandtax | 采购含税单价 | numeric | 23 | 10 | √ | 0 | 采购含税单价 |
| 17 | ftaxamount | 采购税额 | numeric | 23 | 10 | √ | 0 | 采购税额 |
| 18 | fsmpriceandtax | 销售含税单价 | numeric | 23 | 10 | √ | 0 | 销售含税单价 |
| 19 | fdiscounttype | 采购折扣方式 | varchar | 5 |  | √ | ' ' | 采购折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 20 | famountandtax | 采购价税合计 | numeric | 23 | 10 | √ | 0 | 采购价税合计 |
| 21 | fsmamountandtax | 销售价税合计 | numeric | 23 | 10 | √ | 0 | 销售价税合计 |
| 22 | fcuramountandtax | 采购价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 采购价税合计(本位币) |
| 23 | fsmcuramount | 销售金额(本位币) | numeric | 23 | 10 | √ | 0 | 销售金额(本位币) |
| 24 | fsmamount | 销售金额 | numeric | 23 | 10 | √ | 0 | 销售金额 |
| 25 | fsmdiscountamount | 销售折扣额 | numeric | 23 | 10 | √ | 0 | 销售折扣额 |
| 26 | fcurtaxamount | 采购税额(本位币) | numeric | 23 | 10 | √ | 0 | 采购税额(本位币) |
| 27 | fsmtaxrateid | 销售税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 28 | fsmcurtaxamount | 销售税额(本位币) | numeric | 23 | 10 | √ | 0 | 销售税额(本位币) |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_tracontractentry_f |  | fid |
| 2 | pk_gtm_tracontractentry_f |  | fentryid |

---

## 其他方-多选基础资料表 t_gtm_contpartother

- **表名称：** 其他方-多选基础资料表
- **表名：** t_gtm_contpartother

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
| 1 | idx_gtm_contpartother |  | fid |
| 2 | pk_gtm_contpartother |  | fpkid |

---

## 物料明细-子表 t_gtm_tracontractentry

- **表名称：** 物料明细-子表
- **表名：** t_gtm_tracontractentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frowclosestatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 8 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 10 | fpurprogress | 采购执行进度 | numeric | 23 | 10 | √ | 0 | 采购执行进度 |
| 11 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 12 | fbillentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 13 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 15 | fsalprogress | 销售执行进度 | numeric | 23 | 10 | √ | 0 | 销售执行进度 |
| 16 | fmaterialmasterid | 主物料(废弃) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 17 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 18 | frowterminatestatus | 行终止状态 | varchar | 5 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 19 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 20 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 21 | fentrypurorgid | 所属组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 26 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_tracontractentry |  | fentryid |
| 2 | idx_gtm_tracontractentry |  | fid |
