# 竞价发布-sou_bidbill

## 竞价发布-反写记录表 t_pur_bidbill_wb

- **表名称：** 竞价发布-反写记录表
- **表名：** t_pur_bidbill_wb

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
| 1 | t_pur_bidbill_wb_pkey |  | fentryid |

---

## 物料明细-子表 t_pur_bidbillentry

- **表名称：** 物料明细-子表
- **表名：** t_pur_bidbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 3 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 8 | ftaxprice | 基准含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 基准含税单价 |
| 9 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 10 | fprice | 基准单价 | numeric | 23 | 10 | √ | 0.0000000000 | 基准单价 |
| 11 | fwinoption | 中标意见 | varchar | 512 |  | √ | ' ' | 中标意见 |
| 12 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 13 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 14 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 15 | fwinamount | 中标金额 | numeric | 19 | 6 | √ | 0.000000 | 中标金额 |
| 16 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 17 | ftaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 18 | fwinprice | 中标单价 | numeric | 23 | 10 | √ | 0.0000000000 | 中标单价 |
| 19 | fdctrate | 折扣率(%) | numeric | 19 | 6 | √ | 0.000000 | 折扣率(%) |
| 20 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 pur_trace |
| 21 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | fpcbillno | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 24 | fislarge | 允许报价高于基准价 | bpchar | 1 |  | √ | '0' | 允许报价高于基准价 |
| 25 | fwinsupplierid | 中标供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 26 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 27 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 28 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 29 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 30 | fwintaxprice | 中标含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 中标含税单价 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fpobillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 33 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 34 | fisupdateasinfo | fisupdateasinfo | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_bidbillentry_pkey |  | fentryid |
| 2 | idx_pur_bidbillentry_fmatid |  | fmaterialid |
| 3 | idx_pur_bidbillentry_fid_fseq |  | fid,fseq |

---

## 附件-附件表 t_pur_bidbillsupplier_att

- **表名称：** 附件-附件表
- **表名：** t_pur_bidbillsupplier_att

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
| 1 | pk_pur_bidbill_att_feid |  | fentryid |
| 2 | pk_t_pur_bidbillsupplier_att |  | fpkid |
| 3 | pk_pur_bidbill_att_fbdid |  | fbasedataid |

---

## 竞价发布-分表 t_pur_bidbill_a

- **表名称：** 竞价发布-分表
- **表名：** t_pur_bidbill_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdecider | 定标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbidprofit | 竞价利润 | numeric | 19 | 6 | √ | 0.000000 | 竞价利润 |
| 4 | fdecidedate | 定标时间 | timestamp | 0 |  |  | null | 定标时间 |
| 5 | fsupplierstatus | fsupplierstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | famount | 中标金额 | numeric | 19 | 6 | √ | 0.000000 | 中标金额 |
| 7 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fpauseamt | 竞价暂停最新报价 | numeric | 19 | 6 | √ | 0.000000 | 竞价暂停最新报价 |
| 12 | fpushresult | 是否发布结果公告 | bpchar | 1 |  | √ | '0' | 是否发布结果公告,枚举: 1 :是 0 :否 |
| 13 | fpausetime | 竞价暂停时间 | timestamp | 0 |  |  | null | 竞价暂停时间 |
| 14 | fsupplierid1 | fsupplierid1 | int8 | 64 |  | √ | 0 |  |
| 15 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbidnum | 参与竞价数 | int8 | 64 |  | √ | 0 | 参与竞价数 |
| 18 | fenrollnum | 报名/确认数 | int8 | 64 |  | √ | 0 | 报名/确认数 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fterminate | 异常处理意见 | varchar | 255 |  | √ | ' ' | 异常处理意见 |
| 21 | fpushnotice | 是否发布公告 | bpchar | 1 |  | √ | '0' | 是否发布公告,枚举: 0 :否 1 :是 |
| 22 | fpushprice | fpushprice | int8 | 64 |  | √ | 0 |  |
| 23 | fbidrestoftime | 竞价剩余时长(毫秒) | int8 | 64 |  | √ | 0 | 竞价剩余时长(毫秒) |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fsupplierid | 中标供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 27 | faudit | 定标意见 | varchar | 512 |  | √ | ' ' | 定标意见 |
| 28 | fpushsouce | fpushsouce | int8 | 64 |  | √ | 0 |  |
| 29 | famount1 | famount1 | numeric | 19 | 6 | √ | 0.000000 |  |
| 30 | fpausestarttime | 竞价暂停开始时间 | timestamp | 0 |  |  | null | 竞价暂停开始时间 |
| 31 | fisfreequote | 供应商自由报价 | bpchar | 1 |  | √ | '0' | 供应商自由报价 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_bidbill_a_pkey |  | fid |
| 2 | idx_pur_bidbill_a_ftime |  | fcreatetime |

---

## 竞价发布-关联追踪表 t_pur_bidbill_tc

- **表名称：** 竞价发布-关联追踪表
- **表名：** t_pur_bidbill_tc

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
| 1 | idx_pur_bidbill_tc_tbill |  | ftbillid |
| 2 | idx_pur_bidbill_tc_tid |  | ftid |
| 3 | t_pur_bidbill_tc_pkey |  | fid |

---

## 关联子实体-子表 t_pur_bidbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_bidbillentry_lk

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
| 1 | t_pur_bidbillentry_lk_pkey |  | fpkid |

---

## 关联子实体-子表 t_pur_bidbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_bidbill_lk

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
| 1 | t_pur_bidbill_lk_pkey |  | fpkid |
| 2 | idx_pur_bidbill_lk_fk |  | fid |

---

## 竞价发布-多语言表 t_pur_bidbill_l

- **表名称：** 竞价发布-多语言表
- **表名：** t_pur_bidbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fname | 项目名称 | varchar | 100 |  | √ | ' ' | 项目名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_bidbill_l_pkey |  | fpkid |
| 2 | idx_pur_bidbill_l_fid |  | fid,flocaleid |

---

## 供应商分录-子表 t_pur_bidbillsupplier

- **表名称：** 供应商分录-子表
- **表名：** t_pur_bidbillsupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 附件备注 | varchar | 255 |  |  | ' ' | 附件备注 |
| 3 | freturnid | 退保证金人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fentrystatus | 当前状态 | bpchar | 1 |  | √ | ' ' | 当前状态,枚举: A :待资审 B :资审通过 C :资审未通过 D :保证金已收 H :保证金未通过 J :未竞价 F :已中标 G :未中标 E :保证金已退 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fnote | 供应商备注 | varchar | 255 |  | √ | ' ' | 供应商备注 |
| 7 | fauditdate | 资审时间 | timestamp | 0 |  |  | null | 资审时间 |
| 8 | famount | 竞价报价 | numeric | 19 | 6 | √ | 0.000000 | 竞价报价 |
| 9 | fallowbid | 允许竞价 | bpchar | 1 |  | √ | ' ' | 允许竞价 |
| 10 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 11 | franking | 竞价排名 | int8 | 64 |  | √ | 0 | 竞价排名 |
| 12 | fenrollid | 报名人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fpayid | 收保证金人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fenrolldate | 报名时间 | timestamp | 0 |  |  | null | 报名时间 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fauditid | 资审人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | freturndate | 退保证金时间 | timestamp | 0 |  |  | null | 退保证金时间 |
| 18 | fpaydate | 收保证金时间 | timestamp | 0 |  |  | null | 收保证金时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_bidbillsupplier_pkey |  | fentryid |
| 2 | idx_pur_bidbillsup_fid |  | fid,fseq |
| 3 | idx_pur_bidbillsup_fsupplierid |  | fsupplierid |

---

## 报价分录-子表 t_pur_bidbillquote

- **表名称：** 报价分录-子表
- **表名：** t_pur_bidbillquote

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fquotedate | 报价时间 | timestamp | 0 |  |  | null | 报价时间 |
| 3 | fmaterialrowid | 物料分录ID | int8 | 64 |  | √ | 0 | 物料分录ID |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | famount | 报价金额 | numeric | 19 | 6 | √ | 0.000000 | 报价金额 |
| 6 | fquotetaxprice | 报价含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 报价含税单价 |
| 7 | fquoteprice | 报价未税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 报价未税单价 |
| 8 | fsupplierid | 供应商编码 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 9 | fquocurrencyid | 报价币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | fquotaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 11 | fexchange | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |
| 12 | fquosuppamount | 报价金额 | numeric | 19 | 6 | √ | 0.000000 | 报价金额 |
| 13 | fquotematerial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 14 | freduceamt | 降价额度 | numeric | 19 | 2 | √ | 0.00 | 降价额度 |
| 15 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 16 | fentryquotation | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 17 | fsuppreduceamt | 降价额度 | numeric | 19 | 6 | √ | 0.000000 | 降价额度 |
| 18 | fquotaxrate | 税率(%) | numeric | 19 | 6 | √ | 0 | 税率(%) |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_bidbillquote_pkey |  | fentryid |
| 2 | idx_pur_bidbillquote_fid_fseq |  | fid,fseq |
| 3 | idx_pur_bidbillquote_fsupid |  | fsupplierid |

---

## 竞价发布-主表 t_pur_bidbill

- **表名称：** 竞价发布-主表
- **表名：** t_pur_bidbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 3 | fratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 4 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fbidstatus | 项目状态 | bpchar | 1 |  | √ | ' ' | 项目状态,枚举: A :报名中 I :报名截止 B :已资审 C :竞价中 D :评标中 E :已定标 F :已执行 G :已终止 H :已暂停 |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcashdeposit | 竞价保证金 | numeric | 19 | 6 | √ | 0.000000 | 竞价保证金 |
| 8 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 9 | fchecktype | 资审方式 | bpchar | 1 |  | √ | ' ' | 资审方式,枚举: 1 :资格预审 2 :资格后审 3 :资格免审 |
| 10 | fquotemode | 竞价模式 | bpchar | 1 |  | √ | '1' | 竞价模式,枚举: 1 :总额竞价 2 :行项目竞价 |
| 11 | fbizmodel | 经营模式 | varchar | 50 |  | √ | ' ' | 经营模式,枚举: 1 :生产加工 2 :经销批发 3 :商业服务 4 :招商代理 |
| 12 | finvtype | 发票种类 | bpchar | 1 |  | √ | ' ' | 发票种类,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 9 :不需要发票 |
| 13 | fsumamount | 汇总金额 | numeric | 19 | 6 | √ | 0.000000 | 汇总金额 |
| 14 | fbidtime | 竞价时长(分钟) | int8 | 64 |  | √ | 0 | 竞价时长(分钟) |
| 15 | flasttime | 倒计时内有报价/分钟 | int8 | 64 |  | √ | 0 | 倒计时内有报价/分钟 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 18 | fresultdate | 预计公布结果时间 | timestamp | 0 |  |  | null | 预计公布结果时间 |
| 19 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 |
| 21 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 22 | fbidcount | 最多报价次数 | int8 | 64 |  | √ | 0 | 最多报价次数 |
| 23 | freducetype | 每次降/加价方式 | bpchar | 1 |  | √ | ' ' | 每次降/加价方式,枚举: A :按比例(%) B :按金额 |
| 24 | fbizaddr | 经营地址 | varchar | 255 |  | √ | ' ' | 经营地址 |
| 25 | fislargebase | 允许报价高于基准价 | bpchar | 1 |  | √ | '0' | 允许报价高于基准价 |
| 26 | fpersonid | 采购员（废弃） | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 27 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 28 | fenrolldate | 报名截止时间 | timestamp | 0 |  |  | null | 报名截止时间 |
| 29 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | '1270377872653029376' | 单据类型 bos_billtype |
| 30 | fcheckperm | 校验供应商用户采购组织权限 | bpchar | 1 |  | √ | '1' | 校验供应商用户采购组织权限 |
| 31 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 32 | fmaxamount | 报价最高限额 | numeric | 19 | 6 | √ | 0.000000 | 报价最高限额 |
| 33 | fqtysource | 下游单据默认数量来源 | bpchar | 1 |  | √ | '2' | 下游单据默认数量来源,枚举: 1 :竞价定标单 2 :采购申请单 |
| 34 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 35 | fbiztype | 竞价范围 | bpchar | 1 |  | √ | ' ' | 竞价范围,枚举: 1 :所有供应商 2 :指定供应商 |
| 36 | fcertificate | 证照要求 | varchar | 50 |  | √ | ' ' | 证照要求,枚举: 1 :三/五证合一 2 :营业执照 3 :税务登记证 4 :组织机构代码证 5 :社会保险登记证 6 :一般纳税人证明材料 7 :统计登记证 8 :其他证照 |
| 37 | freducepct | 每次降/加价幅度 | numeric | 19 | 6 | √ | 0.000000 | 每次降/加价幅度 |
| 38 | fquotationtrend | 报价趋势 | bpchar | 1 |  | √ | '1' | 报价趋势,枚举: 1 :不限制 2 :仅允许降价 3 :仅允许加价 |
| 39 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 40 | fopen4 | 竞价后公布胜出价格 | bpchar | 1 |  | √ | '0' | 竞价后公布胜出价格 |
| 41 | faddremark | 补充说明 | varchar | 255 |  | √ | ' ' | 补充说明 |
| 42 | fopen2 | 竞价中公开竞价排名 | bpchar | 1 |  | √ | '0' | 竞价中公开竞价排名 |
| 43 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 44 | fopen3 | 竞价后公布胜出公司 | bpchar | 1 |  | √ | '0' | 竞价后公布胜出公司 |
| 45 | fautoconfirm | 自动定标 | bpchar | 1 |  | √ | '0' | 自动定标 |
| 46 | fpublisher | 发布人 | varchar | 255 |  | √ | ' ' | 发布人 |
| 47 | fopen1 | 竞价中公开竞价公司 | bpchar | 1 |  | √ | '0' | 竞价中公开竞价公司 |
| 48 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 49 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 50 | fopendate | 预计竞价开始时间 | timestamp | 0 |  |  | null | 预计竞价开始时间 |
| 51 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 52 | fsumqty | 合计数量 | numeric | 19 | 6 | √ | 0.000000 | 合计数量 |
| 53 | fminamount | 报价最低限额 | numeric | 19 | 6 | √ | 0.000000 | 报价最低限额 |
| 54 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 55 | fregcapital | 注册资金(万元) | numeric | 19 | 6 | √ | 0.000000 | 注册资金(万元) |
| 56 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 57 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 58 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 59 | fdelaytime | 竞价自动延时/分钟 | int8 | 64 |  | √ | 0 | 竞价自动延时/分钟 |
| 60 | fbidnumber | 参与竞价至少应有几家 | int8 | 64 |  | √ | 0 | 参与竞价至少应有几家 |
| 61 | fsumtaxamount | 竞价基准金额 | numeric | 19 | 6 | √ | 0.000000 | 竞价基准金额 |
| 62 | fsumtax | 汇总税额 | numeric | 19 | 6 | √ | 0.000000 | 汇总税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_bidbill_fbilldate |  | fbilldate |
| 2 | idx_pur_bidbill_fbillno |  | fbillno |
| 3 | t_pur_bidbill_pkey |  | fid |

---

## 物料明细-分表 t_pur_bidbillentry_a

- **表名称：** 物料明细-分表
- **表名：** t_pur_bidbillentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 本位币税额 | numeric | 19 | 6 | √ | 0.000000 | 本位币税额 |
| 3 | fsrcentryid | 源单分录ID | varchar | 50 |  | √ | ' ' | 源单分录ID |
| 4 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fgoodsid | 供方物料编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 6 | fsumorderqty | fsumorderqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 7 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 8 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fprbillid | 申请单id | varchar | 50 |  | √ | ' ' | 申请单id |
| 10 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 12 | floctaxamount | 本位币价税合计 | numeric | 19 | 6 | √ | 0.000000 | 本位币价税合计 |
| 13 | fsumcontractqty | fsumcontractqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 14 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 16 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 17 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 18 | fgoodsdesc | 供方物料描述 | varchar | 255 |  | √ | ' ' | 供方物料描述 |
| 19 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 20 | fpoentryid | 订单分录ID | varchar | 50 |  | √ | ' ' | 订单分录ID |
| 21 | fprbillno | 采购申请单号 | varchar | 80 |  | √ | ' ' | 采购申请单号 |
| 22 | flocamount | 本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 本位币金额 |
| 23 | fprentryid | 申请单分录id | varchar | 50 |  | √ | ' ' | 申请单分录id |
| 24 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 26 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 27 | fpcentryid | 合同分录ID | varchar | 50 |  | √ | ' ' | 合同分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_bidbillentry_a_pkey |  | fentryid |
| 2 | idx_pur_bidbillentry_a_fid |  | fid |
