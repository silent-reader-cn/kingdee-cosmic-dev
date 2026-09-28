# 定标单-sou_compare

## 定标单-反写记录表 t_pur_compare_wb

- **表名称：** 定标单-反写记录表
- **表名：** t_pur_compare_wb

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
| 1 | t_pur_compare_wb_pkey |  | fentryid |

---

## 阶梯价子分录-子表 t_pur_soucompare_ladder

- **表名称：** 阶梯价子分录-子表
- **表名：** t_pur_soucompare_ladder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fladderqtyfrom | 阶梯数量从（>） | numeric | 23 | 10 | √ | 0 | 阶梯数量从（>） |
| 2 | fladderprice | 未税单价 | numeric | 23 | 10 | √ | 0 | 未税单价 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fladdercurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fladderremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fladderunitid | 阶梯价计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fladdertaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fladderqtyto | 阶梯数量至（<=） | numeric | 23 | 10 | √ | 0 | 阶梯数量至（<=） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_soucompare_ladder |  | fdetailid |
| 2 | idx_compare_ladderentry_entry |  | fentryid |

---

## 关联子实体-子表 t_pur_comparentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_comparentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 中标数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 中标数量_确认携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fqty_old | 中标数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 中标数量_原始携带值 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_comparentry_lk_pkey |  | fpkid |

---

## 关联子实体-子表 t_pur_compare_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_compare_lk

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
| 1 | t_pur_compare_lk_pkey |  | fpkid |
| 2 | idx_pur_compare_lk_fk |  | fid |

---

## 定标单-关联追踪表 t_pur_compare_tc

- **表名称：** 定标单-关联追踪表
- **表名：** t_pur_compare_tc

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
| 1 | idx_pur_compare_tc_tbill |  | ftbillid |
| 2 | idx_pur_compare_tc_tid |  | ftid |
| 3 | t_pur_compare_tc_pkey |  | fid |

---

## 报价详情信息-子表 t_pur_comparentry

- **表名称：** 报价详情信息-子表
- **表名：** t_pur_comparentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 3 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftaxrate | 中标税率(%) | numeric | 19 | 6 | √ | 0.000000 | 中标税率(%) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | finquiryqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 7 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 10 | ftaxprice | 中标含税单价（报价币） | numeric | 23 | 10 | √ | 0.0000000000 | 中标含税单价（报价币） |
| 11 | famount | 中标未税金额（报价币） | numeric | 19 | 6 | √ | 0.000000 | 中标未税金额（报价币） |
| 12 | fincludeunittax | 含税单价(结算币) | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价(结算币) |
| 13 | fprice | 中标未税单价（报价币） | numeric | 23 | 10 | √ | 0.0000000000 | 中标未税单价（报价币） |
| 14 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 15 | ftaxrateid | 中标税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 16 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 17 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 18 | fqty | 中标数量 | numeric | 19 | 6 | √ | 0.000000 | 中标数量 |
| 19 | ftaxamount | 中标价税合计（报价币） | numeric | 19 | 6 | √ | 0.000000 | 中标价税合计（报价币） |
| 20 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fdctrate | 单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 单位折扣(率) |
| 22 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 pur_trace](../pbd_files/pur_trace.md) |
| 24 | fmaintainladder | 是否已填写阶梯价 | varchar | 1 |  | √ | ' ' | 是否已填写阶梯价,枚举: 1 :是 0 :否 |
| 25 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fexcludeunittax | 未税单价（结算币） | numeric | 23 | 10 | √ | 0.0000000000 | 未税单价（结算币） |
| 27 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fpcbillno | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 29 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fquotecurr | 报价币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fsupplierid | 中标供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 32 | fdelitypeid | 交货方式 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 33 | ftax | 中标税额（报价币） | numeric | 19 | 6 | √ | 0.000000 | 中标税额（报价币） |
| 34 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 35 | fentryquotation | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 36 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 37 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fpobillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 41 | fvalidnum | 有效报价供应商数量 | int4 | 32 |  | √ | 0 | 有效报价供应商数量 |
| 42 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 43 | fisupdateasinfo | 是否已更新采购价目表 | bpchar | 1 |  | √ | '0' | 是否已更新采购价目表 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_comparentry_fid_fseq |  | fid,fseq |
| 2 | idx_pur_comparentry_fmatid |  | fmaterialid |
| 3 | t_pur_comparentry_pkey |  | fentryid |

---

## 报价汇总分录-子表 t_pur_comparquoentry

- **表名称：** 报价汇总分录-子表
- **表名：** t_pur_comparquoentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrysupplierid | 供应商名称 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 3 | fqoutaxamount | 报价价税合计(结算币) | numeric | 19 | 6 | √ | 0.000000 | 报价价税合计(结算币) |
| 4 | fqouamount | 报价未税金额（结算币） | numeric | 23 | 10 | √ | 0 | 报价未税金额（结算币） |
| 5 | fpayconditionid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 6 | fquobillno | 报价单号 | varchar | 80 |  | √ | ' ' | 报价单号 |
| 7 | fremarks | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 8 | fipaddress | 供应商IP地址 | varchar | 50 |  | √ | ' ' | 供应商IP地址 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fisadopt | 是否中标 | bpchar | 1 |  | √ | ' ' | 是否中标 |
| 11 | fdeliverdate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 12 | fquotebillid | 报价单ID | int8 | 64 |  | √ | 0 | 报价单ID |
| 13 | frate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fadoptamount | 中标价税合计（结算币） | numeric | 19 | 6 | √ | 0.000000 | 中标价税合计（结算币） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_comparquoentry_pkey |  | fentryid |
| 2 | idx_pur_comparquoentry_fid |  | fid,fseq |

---

## 定标单-分表 t_pur_compare_a

- **表名称：** 定标单-分表
- **表名：** t_pur_compare_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fpushprice | 下推价目表否 | int8 | 64 |  | √ | 0 | 下推价目表否 |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 8 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 11 | fpushsouce | 下推货源清单否 | int8 | 64 |  | √ | 0 | 下推货源清单否 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fpushresult | 是否发布结果公告 | bpchar | 1 |  | √ | ' ' | 是否发布结果公告,枚举: 1 :是 0 :否 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_compare_a_pkey |  | fid |
| 2 | idx_pur_compare_a_fcreatetime |  | fcreatetime |

---

## 定标单-主表 t_pur_compare

- **表名称：** 定标单-主表
- **表名：** t_pur_compare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcontrolqty | 控制中标物料数量 | varchar | 1 |  | √ | '1' | 控制中标物料数量,枚举: 1 :不控制 2 :严格控制 |
| 3 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 5 | fratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 6 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 8 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fqtysource | 下游单据默认数量来源 | bpchar | 1 |  | √ | '2' | 下游单据默认数量来源,枚举: 1 :定标单 2 :采购申请单 |
| 10 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 11 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 12 | fsupcurrtype | 报价币选项 | bpchar | 1 |  | √ | '2' | 报价币选项,枚举: 1 :按询价单结算币 2 :供应商自选币种 |
| 13 | fbiztype | 业务类型(废弃) | bpchar | 1 |  | √ | ' ' | 业务类型(废弃),枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 14 | fquotation | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 15 | fsumamount | 未税金额 | numeric | 19 | 6 | √ | 0.000000 | 未税金额 |
| 16 | fdatefrom | 价格有效期从 | timestamp | 0 |  |  | null | 价格有效期从 |
| 17 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 18 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 22 | fcurrid | 结算币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 23 | fdateto | 价格有效期至 | timestamp | 0 |  |  | null | 价格有效期至 |
| 24 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 |
| 25 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 26 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fsumqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 29 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 30 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 31 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 32 | fopenladder | 启用阶梯价 | varchar | 1 |  | √ | '0' | 启用阶梯价,枚举: 1 :启用 0 :不启用 |
| 33 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 |
| 34 | fcomparerange | 比价范围 | bpchar | 1 |  | √ | 'B' | 比价范围,枚举: A :集团比价 B :组织比价 |
| 35 | fpersonid | 采购员（废弃） | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 36 | finquiryno | 询价单号 | varchar | 80 |  | √ | ' ' | 询价单号 |
| 37 | fsumtaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 38 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fsumtax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 40 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 41 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |
| 42 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_compare_pkey |  | fid |
| 2 | idx_pur_compare_fbizpartnerid |  | fbizpartnerid |
| 3 | idx_pur_compare_fbilldate |  | fbilldate |
| 4 | idx_pur_compare_fbillno |  | fbillno |
| 5 | idx_pur_compare_finquiryno |  | finquiryno |

---

## 定标单-多语言表 t_pur_compare_l

- **表名称：** 定标单-多语言表
- **表名：** t_pur_compare_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 定标意见 | varchar | 512 |  | √ | ' ' | 定标意见 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_compare_l_pkey |  | fpkid |
| 2 | idx_pur_compare_l_fid |  | fid,flocaleid |

---

## 报价详情信息-分表 t_pur_comparentry_a

- **表名称：** 报价详情信息-分表
- **表名：** t_pur_comparentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 税额(本位币) |
| 3 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 4 | fgoodsid | 供方物料编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 5 | fnewprice | 最新报价 | numeric | 19 | 6 | √ | 0.000000 | 最新报价 |
| 6 | flastwinbillid | 上次中标比价单id | varchar | 50 |  | √ | ' ' | 上次中标比价单id |
| 7 | favgprice | 报价平均价 | numeric | 19 | 6 | √ | 0.000000 | 报价平均价 |
| 8 | fsumorderqty | 关联订单数量 | numeric | 19 | 6 | √ | 0.000000 | 关联订单数量 |
| 9 | flastcompareid | 上次定标单id | varchar | 50 |  | √ | ' ' | 上次定标单id |
| 10 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 11 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fprbillid | 申请单id | varchar | 50 |  | √ | ' ' | 申请单id |
| 13 | fmaxprice | 最高报价 | numeric | 19 | 6 | √ | 0.000000 | 最高报价 |
| 14 | fhisminprice | 历史最低价 | numeric | 19 | 6 | √ | 0.000000 | 历史最低价 |
| 15 | fquote6 | 报价六 | numeric | 19 | 6 | √ | 0.000000 | 报价六 |
| 16 | flastwinprice | 上次中标含税单价 | numeric | 19 | 6 | √ | 0 | 上次中标含税单价 |
| 17 | fquote7 | 报价七 | numeric | 19 | 6 | √ | 0.000000 | 报价七 |
| 18 | fminorderqty | 确认最小起订量 | numeric | 19 | 6 | √ | 0.000000 | 确认最小起订量 |
| 19 | fquote8 | 报价八 | numeric | 19 | 6 | √ | 0.000000 | 报价八 |
| 20 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 22 | floctaxamount | 价税合计(本位币) | numeric | 19 | 6 | √ | 0.000000 | 价税合计(本位币) |
| 23 | fsupname | 临时供应商 | varchar | 100 |  | √ | ' ' | 临时供应商 |
| 24 | fsumcontractqty | 关联合同数量 | numeric | 19 | 6 | √ | 0.000000 | 关联合同数量 |
| 25 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 26 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 27 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 28 | fquote2 | 报价二 | numeric | 19 | 6 | √ | 0.000000 | 报价二 |
| 29 | fquote3 | 报价三 | numeric | 19 | 6 | √ | 0.000000 | 报价三 |
| 30 | fquote4 | 报价四 | numeric | 19 | 6 | √ | 0.000000 | 报价四 |
| 31 | fgoodsdesc | 供方物料描述 | varchar | 255 |  | √ | ' ' | 供方物料描述 |
| 32 | fquote5 | 报价五 | numeric | 19 | 6 | √ | 0.000000 | 报价五 |
| 33 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 34 | fquote1 | 报价一 | numeric | 19 | 6 | √ | 0.000000 | 报价一 |
| 35 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 36 | fprbillno | 采购申请单号 | varchar | 80 |  | √ | ' ' | 采购申请单号 |
| 37 | fpurleadday | 确认采购提前期 | int8 | 64 |  | √ | 0 | 确认采购提前期 |
| 38 | flocamount | 未税金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 未税金额(本位币) |
| 39 | fprentryid | 申请单分录id | varchar | 50 |  | √ | ' ' | 申请单分录id |
| 40 | fminprice | 最低报价 | numeric | 19 | 6 | √ | 0.000000 | 最低报价 |
| 41 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 43 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 44 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |
| 45 | flastcompareprice | 上次定标单价格 | numeric | 19 | 6 | √ | 0.000000 | 上次定标单价格 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_comparentry_a_pkey |  | fentryid |
| 2 | idx_pur_comparentry_a_fpoid |  | fpoentryid |
| 3 | idx_pur_comparentry_a_fid |  | fid |
