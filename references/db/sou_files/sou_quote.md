# 报价单-sou_quote

## 报价单分录-子表 t_pur_quotentry

- **表名称：** 报价单分录-子表
- **表名：** t_pur_quotentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 3 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | finquiryqty | 询价数量 | numeric | 19 | 6 | √ | 0.000000 | 询价数量 |
| 7 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 10 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 11 | famount | 未税金额 | numeric | 19 | 6 | √ | 0.000000 | 未税金额 |
| 12 | fprice | 未税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 未税单价 |
| 13 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 14 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 15 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 16 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 17 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 18 | ftaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 19 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fdctrate | 单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 单位折扣(率) |
| 21 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 pur_trace](../pbd_files/pur_trace.md) |
| 23 | fmaintainladder | 是否已填写阶梯价 | varchar | 1 |  | √ | ' ' | 是否已填写阶梯价,枚举: 1 :是 0 :否 |
| 24 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 25 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fpcbillno | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 27 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fquotecurr | 报价币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | fnewestturns | 询价轮次 | varchar | 10 |  | √ | ' ' | 询价轮次,枚举: 1 :首轮 2 :第二轮 3 :第三轮 4 :第四轮 5 :第五轮 6 :第六轮 7 :第七轮 8 :第八轮 9 :第九轮 10 :第十轮 11 :第十一轮 12 :第十二轮 13 :第十三轮 14 :第十四轮 15 :第十五轮 16 :第十六轮 18 :第十八轮 17 :第十七轮 19 :第十九轮 20 :第二十轮 |
| 30 | fquoturns | 报价轮次 | varchar | 10 |  | √ | ' ' | 报价轮次,枚举: 1 :第一次 2 :第二次 3 :第三次 4 :第四次 5 :第五次 6 :第六次 7 :第七次 8 :第八次 9 :第九次 10 :第十次 11 :第十一次 12 :第十二次 13 :第十三次 14 :第十四次 15 :第十五次 16 :第十六次 18 :第十八次 17 :第十七次 19 :第十九次 20 :第二十次 |
| 31 | fdelitypeid | 交货方式 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 32 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 33 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 34 | fentryquotation | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 35 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 36 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | fpobillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 40 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_quotentry_fid_fseq |  | fid,fseq |
| 2 | t_pur_quotentry_pkey |  | fentryid |
| 3 | idx_pur_quotentry_fmaterialid |  | fmaterialid |

---

## 报价单分录-分表 t_pur_quotentry_a

- **表名称：** 报价单分录-分表
- **表名：** t_pur_quotentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 税额(本位币) |
| 3 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 4 | fcfmtaxrateid | 中标税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 5 | fgoodsid | 供方物料编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 6 | flastwinbillid | 上次中标比价单id | varchar | 50 |  | √ | ' ' | 上次中标比价单id |
| 7 | fsumorderqty | 关联订单数量 | numeric | 19 | 6 | √ | 0.000000 | 关联订单数量 |
| 8 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 9 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fprbillid | 申请单id | varchar | 50 |  | √ | ' ' | 申请单id |
| 11 | fresult | 报价结果 | bpchar | 1 |  | √ | ' ' | 报价结果,枚举: 1 :中标 2 :未中标 |
| 12 | fcfmtaxprice | 中标含税单价 | numeric | 19 | 6 | √ | 0.000000 | 中标含税单价 |
| 13 | fcfmqty | 中标数量 | numeric | 19 | 6 | √ | 0.000000 | 中标数量 |
| 14 | fcfmtaxrate | 中标税率(%) | numeric | 19 | 6 | √ | 0.000000 | 中标税率(%) |
| 15 | flastwinprice | 上次中标含税单价 | numeric | 19 | 6 | √ | 0 | 上次中标含税单价 |
| 16 | fminorderqty | 最小起订量 | numeric | 19 | 6 | √ | 0.000000 | 最小起订量 |
| 17 | fcfmbaseqty | 确认基本数量 | numeric | 23 | 10 | √ | 0 | 确认基本数量 |
| 18 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 20 | floctaxamount | 价税合计(本位币) | numeric | 19 | 6 | √ | 0.000000 | 价税合计(本位币) |
| 21 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 22 | fsumcompareqty | 关联中标数量 | numeric | 19 | 6 | √ | 0.000000 | 关联中标数量 |
| 23 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 24 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 25 | fgoodsdesc | 供方物料描述 | varchar | 255 |  | √ | ' ' | 供方物料描述 |
| 26 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 27 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 28 | fcfmprice | 中标未税单价 | numeric | 19 | 6 | √ | 0.000000 | 中标未税单价 |
| 29 | fprbillno | 申请单编号 | varchar | 80 |  | √ | ' ' | 申请单编号 |
| 30 | fcfmnote | 定标意见 | varchar | 512 |  | √ | ' ' | 定标意见 |
| 31 | fpurleadday | 采购提前期 | int8 | 64 |  | √ | 0 | 采购提前期 |
| 32 | flocamount | 金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 金额(本位币) |
| 33 | fprentryid | 申请单分录id | varchar | 50 |  | √ | ' ' | 申请单分录id |
| 34 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 36 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 37 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_quotentry_a_pkey |  | fentryid |
| 2 | idx_pur_quotentry_a_srcentryid |  | fsrcentryid |
| 3 | idx_pur_quotentry_a_fid |  | fid |
| 4 | idx_pur_quotentry_a_fpoentryid |  | fpoentryid |

---

## 关联子实体-子表 t_pur_quotentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_quotentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 数量_确认携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fqty_old | 数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 数量_原始携带值 |
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
| 1 | t_pur_quotentry_lk_fidseq |  | fentryid,fseq |
| 2 | t_pur_quotentry_lk_pkey |  | fpkid |

---

## 关联子实体-子表 t_pur_quoten_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_quoten_lk

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
| 1 | idx_pur_quoten_lk_fk |  | fid |
| 2 | t_pur_quoten_lk_pkey |  | fpkid |

---

## 报价单-反写记录表 t_pur_quote_wb

- **表名称：** 报价单-反写记录表
- **表名：** t_pur_quote_wb

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
| 1 | t_pur_quote_wb_pkey |  | fentryid |

---

## 报价单-多语言表 t_pur_quote_l

- **表名称：** 报价单-多语言表
- **表名：** t_pur_quote_l

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
| 1 | t_pur_quote_l_pkey |  | fpkid |
| 2 | idx_pur_quote_l_fid_flocaleid |  | fid,flocaleid |

---

## 报价单-分表 t_pur_quote_a

- **表名称：** 报价单-分表
- **表名：** t_pur_quote_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontactway | 联系方式 | varchar | 50 |  | √ | ' ' | 联系方式 |
| 3 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fquotefrom | 报价来源 | bpchar | 1 |  | √ | ' ' | 报价来源,枚举: A :协同平台 B :1688平台 |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 9 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | forigin | 报价录入方 | bpchar | 1 |  | √ | ' ' | 报价录入方,枚举: 1 :供应商 2 :采购方 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fopentype | 开标方式 | bpchar | 1 |  | √ | ' ' | 开标方式,枚举: 1 :报价即可见自动开标（非密封） 4 :报价即可见手工开标（非密封） 2 :到截止时间自动开标（密封） 3 :到截止时间手工开标（密封） |
| 14 | fsupname | 供应商名称 | varchar | 100 |  | √ | ' ' | 供应商名称 |
| 15 | fcontactor | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_quote_a_pkey |  | fid |
| 2 | idx_pur_quote_a_fcreatetime |  | fcreatetime |

---

## 报价单-主表 t_pur_quote

- **表名称：** 报价单-主表
- **表名：** t_pur_quote

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 4 | fratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 5 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | ftotalamount | 总价 | numeric | 19 | 6 | √ | 0.000000 | 总价 |
| 8 | fsumcost | 费用合计 | numeric | 19 | 6 | √ | 0.000000 | 费用合计 |
| 9 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 10 | fenddate | 报价截止时间 | timestamp | 0 |  |  | null | 报价截止时间 |
| 11 | finvtype | 发票种类 | bpchar | 1 |  | √ | ' ' | 发票种类,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 9 :不需要发票 |
| 12 | fsumamount | 未税金额 | numeric | 19 | 6 | √ | 0.000000 | 未税金额 |
| 13 | fdatefrom | 价格有效期从 | timestamp | 0 |  |  | null | 价格有效期从 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 16 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 17 | fipaddress | 供应商IP地址 | varchar | 50 |  | √ | ' ' | 供应商IP地址 |
| 18 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 19 | fopenladder | 启用阶梯价 | varchar | 1 |  | √ | '0' | 启用阶梯价,枚举: 1 :启用 0 :不启用 |
| 20 | fpersonid | 采购员(废弃) | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 21 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 23 | fcontacterid | 供应商联系人 | int8 | 64 |  | √ | 0 | [协同业务员 scp_bizperson](../scp_files/scp_bizperson.md) |
| 24 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 25 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 26 | fbizstatus | 中标结果 | bpchar | 1 |  | √ | ' ' | 中标结果,枚举: A :已报价 B :已开标 C :已中标 D :部分中标 E :未中标 |
| 27 | fbilldate | 报价日期 | timestamp | 0 |  |  | null | 报价日期 |
| 28 | ftotalinquiry | 整单询价 | bpchar | 1 |  | √ | '0' | 整单询价 |
| 29 | fsupcurrtype | 报价币选项 | bpchar | 1 |  | √ | '2' | 报价币选项,枚举: 1 :按询价单结算币 2 :供应商自选币 |
| 30 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 31 | fquotation | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 32 | fenablemodify | 允许供应商修改阶梯 | varchar | 1 |  | √ | '0' | 允许供应商修改阶梯 |
| 33 | fturns | 询价轮次 | varchar | 10 |  | √ | ' ' | 询价轮次,枚举: 1 :首轮 2 :第二轮 3 :第三轮 4 :第四轮 5 :第五轮 6 :第六轮 7 :第七轮 8 :第八轮 9 :第九轮 10 :第十轮 11 :第十一轮 12 :第十二轮 13 :第十三轮 14 :第十四轮 15 :第十五轮 16 :第十六轮 17 :第十七轮 18 :第十八轮 19 :第十九轮 20 :第二十轮 |
| 34 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 35 | fturnscount | 实际报价轮次 | varchar | 10 |  | √ | ' ' | 实际报价轮次,枚举: 1 :第一次 2 :第二次 3 :第三次 4 :第四次 5 :第五次 6 :第六次 7 :第七次 8 :第八次 9 :第九次 10 :第十次 11 :第十一次 12 :第十二次 13 :第十三次 14 :第十四次 15 :第十五次 16 :第十六次 17 :第十七次 18 :第十八次 19 :第十九次 20 :第二十次 |
| 36 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 37 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 39 | fdateto | 价格有效期至 | timestamp | 0 |  |  | null | 价格有效期至 |
| 40 | fcurrid | 结算币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 41 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | fsumqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 44 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 45 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 46 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 47 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 |
| 48 | finquiryno | 询价单号 | varchar | 80 |  | √ | ' ' | 询价单号 |
| 49 | fsumtaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 50 | fsumtax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 51 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_quote_fbilldate |  | fbilldate |
| 2 | idx_pur_quote_fbizpartnerid |  | fbizpartnerid |
| 3 | idx_pur_quote_fbillno |  | fbillno |
| 4 | idx_pur_quote_finquiryno |  | finquiryno |
| 5 | idx_pur_quote_forgid |  | forgid |
| 6 | t_pur_quote_pkey |  | fid |

---

## 阶梯价子分录-子表 t_pur_quotentry_ladder

- **表名称：** 阶梯价子分录-子表
- **表名：** t_pur_quotentry_ladder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fladderqtyfrom | 阶梯数量从（>） | numeric | 23 | 10 |  | null | 阶梯数量从（>） |
| 2 | fladderprice | 未税单价 | numeric | 23 | 10 |  | null | 未税单价 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fladdercurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fladderremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fladderunitid | 阶梯价计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | null | id |
| 8 | fladdertaxprice | 含税单价 | numeric | 23 | 10 |  | null | 含税单价 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fladderqtyto | 阶梯数量至（<=） | numeric | 23 | 10 |  | null | 阶梯数量至（<=） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_quotentry_ladder |  | fdetailid |
| 2 | idx_quote_ladderentry_entry |  | fentryid |

---

## 报价单-关联追踪表 t_pur_quote_tc

- **表名称：** 报价单-关联追踪表
- **表名：** t_pur_quote_tc

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
| 1 | t_pur_quote_tc_pkey |  | fid |
| 2 | idx_pur_quote_tc_tbill |  | ftbillid |
| 3 | idx_pur_quote_tc_tid |  | ftid |
