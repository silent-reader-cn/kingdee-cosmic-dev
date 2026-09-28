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
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 8 | ftaxprice | 基准含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 基准含税单价 |
| 9 | famount | 基准不含税金额 | numeric | 19 | 6 | √ | 0.000000 | 基准不含税金额 |
| 10 | fprice | 基准单价 | numeric | 23 | 10 | √ | 0.0000000000 | 基准单价 |
| 11 | fwinoption | 中标意见 | varchar | 512 |  | √ | ' ' | 中标意见 |
| 12 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 13 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 14 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 15 | fwinamount | 中标金额 | numeric | 19 | 6 | √ | 0.000000 | 中标金额 |
| 16 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 17 | ftaxamount | 基准含税金额 | numeric | 19 | 6 | √ | 0.000000 | 基准含税金额 |
| 18 | fwinprice | 中标单价 | numeric | 23 | 10 | √ | 0.0000000000 | 中标单价 |
| 19 | fdctrate | 折扣率(%) | numeric | 19 | 6 | √ | 0.000000 | 折扣率(%) |
| 20 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 pur_trace](../pbd_files/pur_trace.md) |
| 21 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fpcbillno | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 24 | fislarge | 允许报价高于基准价 | bpchar | 1 |  | √ | '0' | 允许报价高于基准价 |
| 25 | fwinsupplierid | 中标供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 26 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 27 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 28 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 29 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 30 | fwintaxprice | 中标含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 中标含税单价 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fpobillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 33 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
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
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
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
| 2 | fdecider | 定标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbidprofit | 竞价利润 | numeric | 19 | 6 | √ | 0.000000 | 竞价利润 |
| 4 | fdecidedate | 定标时间 | timestamp | 0 |  |  | null | 定标时间 |
| 5 | fsupplierstatus | fsupplierstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | famount | 定标金额 | numeric | 19 | 6 | √ | 0.000000 | 定标金额 |
| 7 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fpauseamt | 竞价暂停最新报价 | numeric | 19 | 6 | √ | 0.000000 | 竞价暂停最新报价 |
| 12 | fpushresult | 是否发布结果公告 | bpchar | 1 |  | √ | '0' | 是否发布结果公告,枚举: 1 :是 0 :否 |
| 13 | fpausetime | 竞价暂停时间 | timestamp | 0 |  |  | null | 竞价暂停时间 |
| 14 | fsupplierid1 | fsupplierid1 | int8 | 64 |  | √ | 0 |  |
| 15 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbidnum | 竞价供应商数 | int8 | 64 |  | √ | 0 | 竞价供应商数 |
| 18 | fpicture5 | 竞价图片5 | varchar | 255 |  | √ | ' ' | 竞价图片5 |
| 19 | fenrollnum | 报名供应商数 | int8 | 64 |  | √ | 0 | 报名供应商数 |
| 20 | fpicture4 | 竞价图片4 | varchar | 255 |  | √ | ' ' | 竞价图片4 |
| 21 | fpicture3 | 竞价图片3 | varchar | 255 |  | √ | ' ' | 竞价图片3 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fpicture2 | 竞价图片2 | varchar | 255 |  | √ | ' ' | 竞价图片2 |
| 24 | fterminate | 结束竞价原因 | varchar | 255 |  | √ | ' ' | 结束竞价原因 |
| 25 | fpushnotice | 是否发布公告 | bpchar | 1 |  | √ | '0' | 是否发布公告,枚举: 0 :否 1 :是 |
| 26 | fpicture1 | 竞价图片1 | varchar | 255 |  | √ | ' ' | 竞价图片1 |
| 27 | fpushprice | fpushprice | int8 | 64 |  | √ | 0 |  |
| 28 | fbidrestoftime | 竞价剩余时长(毫秒) | int8 | 64 |  | √ | 0 | 竞价剩余时长(毫秒) |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fsupplierid | 中标供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 32 | faudit | 定标意见 | varchar | 512 |  | √ | ' ' | 定标意见 |
| 33 | fpushsouce | fpushsouce | int8 | 64 |  | √ | 0 |  |
| 34 | famount1 | famount1 | numeric | 19 | 6 | √ | 0.000000 |  |
| 35 | fpausestarttime | 竞价暂停开始时间 | timestamp | 0 |  |  | null | 竞价暂停开始时间 |
| 36 | fisfreequote | 供应商自由报价 | bpchar | 1 |  | √ | '0' | 供应商自由报价 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

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

## 参与供应商-子表 t_pur_bidbillsupplier

- **表名称：** 参与供应商-子表
- **表名：** t_pur_bidbillsupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 附件备注 | varchar | 255 |  |  | ' ' | 附件备注 |
| 3 | freturnid | 保证金退还人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fentrystatus | 当前状态 | bpchar | 1 |  | √ | ' ' | 当前状态,枚举: A :待资审 B :资审通过 C :资审未通过 D :保证金已收 H :保证金未通过 J :未竞价 F :已中标 G :未中标 E :保证金已退 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fnote | 供应商备注 | varchar | 255 |  | √ | ' ' | 供应商备注 |
| 7 | fsupamountextax | 报价总金额(不含税) | numeric | 23 | 10 | √ | 0 | 报价总金额(不含税) |
| 8 | fauditdate | 资审时间 | timestamp | 0 |  |  | null | 资审时间 |
| 9 | famount | 竞价报价 | numeric | 23 | 10 | √ | 0.000000 | 竞价报价 |
| 10 | fallowbid | 允许竞价 | bpchar | 1 |  | √ | ' ' | 允许竞价 |
| 11 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 12 | fsignuser | 签到人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fsigntime | 签到时间 | timestamp | 0 |  |  | null | 签到时间 |
| 14 | franking | 竞价排名 | int8 | 64 |  | √ | 0 | 竞价排名 |
| 15 | fenrollid | 报名人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fsignin | 是否签到 | bpchar | 1 |  | √ | '0' | 是否签到 |
| 17 | fpayid | 保证金收取人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fenrolldate | 报名时间 | timestamp | 0 |  |  | null | 报名时间 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fauditid | 资审人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | freturndate | 保证金退还时间 | timestamp | 0 |  |  | null | 保证金退还时间 |
| 22 | fpaydate | 保证金收取时间 | timestamp | 0 |  |  | null | 保证金收取时间 |

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
| 2 | fdelaybidendtime | 延迟后新结束时间 | timestamp | 0 |  |  | null | 延迟后新结束时间 |
| 3 | fisdelayedtriggered | 本次报价是否触发延迟 | bpchar | 1 |  | √ | '0' | 本次报价是否触发延迟,枚举: 1 :是 |
| 4 | fcurrentbidcount | 供应商本次竞价报价次数 | int4 | 32 |  | √ | 0 | 供应商本次竞价报价次数 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | famount | 报价金额 | numeric | 19 | 6 | √ | 0.000000 | 报价金额 |
| 7 | fquoteprice | 报价未税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 报价未税单价 |
| 8 | fquocurrencyid | 报价币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fexchange | 汇率 | numeric | 19 | 6 | √ | 0 | 汇率 |
| 10 | fquosuppamount | 报价金额 | numeric | 19 | 6 | √ | 0.000000 | 报价金额 |
| 11 | fquotematerial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 12 | fquotedelaynumber | 报价时当前已延迟次数 | int4 | 32 |  | √ | 0 | 报价时当前已延迟次数 |
| 13 | fquotaxrate | 税率(%) | numeric | 19 | 6 | √ | 0 | 税率(%) |
| 14 | fquotedate | 报价时间 | timestamp | 0 |  |  | null | 报价时间 |
| 15 | fmaterialrowid | 物料分录ID | int8 | 64 |  | √ | 0 | 物料分录ID |
| 16 | fipaddress | 供应商IP地址 | varchar | 50 |  | √ | ' ' | 供应商IP地址 |
| 17 | fquotetaxprice | 报价含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 报价含税单价 |
| 18 | fsupplierid | 供应商编码 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 19 | fquotaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 20 | fbidendtime | 初始竞价结束时间 | timestamp | 0 |  |  | null | 初始竞价结束时间 |
| 21 | freduceamt | 降价额度 | numeric | 19 | 2 | √ | 0.00 | 降价额度 |
| 22 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 23 | fentryquotation | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 24 | fsuppreduceamt | 降价额度 | numeric | 19 | 6 | √ | 0.000000 | 降价额度 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fremaintime | 报价时剩余时间(秒) | int4 | 32 |  | √ | 0 | 报价时剩余时间(秒) |

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
| 4 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fbidstatus | 项目状态 | bpchar | 1 |  | √ | ' ' | 项目状态,枚举: A :报名中 I :报名截止 B :已资审 C :竞价中 D :评标中 E :已定标 F :已执行 G :流标 H :已暂停 |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcashdeposit | 竞价保证金 | numeric | 19 | 6 | √ | 0.000000 | 竞价保证金 |
| 8 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 9 | ftotalquote | 整单报价 | bpchar | 1 |  | √ | '0' | 整单报价 |
| 10 | fchecktype | 资审方式 | bpchar | 1 |  | √ | ' ' | 资审方式,枚举: 1 :资格预审 2 :资格后审 3 :资格免审 |
| 11 | fquotemode | 竞价模式 | bpchar | 1 |  | √ | '1' | 竞价模式,枚举: 1 :总额竞价 2 :按行竞价 |
| 12 | fbizmodel | 经营模式 | varchar | 50 |  | √ | ' ' | 经营模式,枚举: 1 :生产加工 2 :经销批发 3 :商业服务 4 :招商代理 |
| 13 | finvtype | 发票种类 | bpchar | 1 |  | √ | ' ' | 发票种类,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 9 :不需要发票 |
| 14 | fdelaynumber | 当前已延迟次数 | int4 | 32 |  | √ | 0 | 当前已延迟次数 |
| 15 | fsumamount | 汇总金额 | numeric | 19 | 6 | √ | 0.000000 | 汇总金额 |
| 16 | fbidtime | 竞价时长(分钟) | int8 | 64 |  | √ | 0 | 竞价时长(分钟) |
| 17 | flasttime | 倒计时内有报价(分钟) | int8 | 64 |  | √ | 0 | 倒计时内有报价(分钟) |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 20 | fresultdate | 预计公布结果时间 | timestamp | 0 |  |  | null | 预计公布结果时间 |
| 21 | fname | 项目名称 | varchar | 100 |  | √ | ' ' | 项目名称 |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 |
| 23 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 24 | fbidcount | 最多报价次数 | int8 | 64 |  | √ | 0 | 最多报价次数 |
| 25 | freducetype | 每次降/加价方式 | bpchar | 1 |  | √ | ' ' | 每次降/加价方式,枚举: A :按比例(%) B :按金额 |
| 26 | fbizaddr | 经营地址 | varchar | 255 |  | √ | ' ' | 经营地址 |
| 27 | fislargebase | 允许报价高于基准价 | bpchar | 1 |  | √ | '0' | 允许报价高于基准价 |
| 28 | fpersonid | 采购员（废弃） | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 29 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 30 | fenrolldate | 报名截止时间 | timestamp | 0 |  |  | null | 报名截止时间 |
| 31 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | '1270377872653029376' | 单据类型 bos_billtype |
| 32 | fcheckperm | 校验供应商用户采购组织权限 | bpchar | 1 |  | √ | '1' | 校验供应商用户采购组织权限 |
| 33 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 34 | fmaxamount | 报价最高限额 | numeric | 19 | 6 | √ | 0.000000 | 报价最高限额 |
| 35 | fqtysource | 下游单据默认数量来源 | bpchar | 1 |  | √ | '2' | 下游单据默认数量来源,枚举: 1 :竞价发布 2 :采购申请单 |
| 36 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 37 | fbiztype | 供应商范围 | bpchar | 1 |  | √ | ' ' | 供应商范围,枚举: 1 :所有供应商 2 :指定供应商 |
| 38 | fcertificate | 证照要求 | varchar | 50 |  | √ | ' ' | 证照要求,枚举: 1 :三/五证合一 2 :营业执照 3 :税务登记证 4 :组织机构代码证 5 :社会保险登记证 6 :一般纳税人证明材料 7 :统计登记证 8 :其他证照 |
| 39 | freducepct | 每次降/加价幅度 | numeric | 19 | 6 | √ | 0.000000 | 每次降/加价幅度 |
| 40 | fquotationtrend | 报价趋势 | bpchar | 1 |  | √ | '1' | 报价趋势,枚举: 1 :不限制 2 :降价（竞价） 3 :加价（拍卖） |
| 41 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 42 | fopen4 | 竞价后公布胜出价格 | bpchar | 1 |  | √ | '0' | 竞价后公布胜出价格 |
| 43 | faddremark | 补充说明 | varchar | 255 |  | √ | ' ' | 补充说明 |
| 44 | fopen2 | 竞价中公开竞价排名 | bpchar | 1 |  | √ | '0' | 竞价中公开竞价排名 |
| 45 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 46 | fopen3 | 竞价后公布胜出公司 | bpchar | 1 |  | √ | '0' | 竞价后公布胜出公司 |
| 47 | fautoconfirm | 自动定标 | bpchar | 1 |  | √ | '0' | 自动定标 |
| 48 | fpublisher | 发布人 | varchar | 255 |  | √ | ' ' | 发布人 |
| 49 | fopen1 | 竞价中公开竞价公司 | bpchar | 1 |  | √ | '0' | 竞价中公开竞价公司 |
| 50 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 51 | fcurrid | 结算币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 52 | fopendate | 预计竞价开始时间 | timestamp | 0 |  |  | null | 预计竞价开始时间 |
| 53 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 54 | fsumqty | 合计数量 | numeric | 19 | 6 | √ | 0.000000 | 合计数量 |
| 55 | fminamount | 报价最低限额 | numeric | 19 | 6 | √ | 0.000000 | 报价最低限额 |
| 56 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 57 | fregcapital | 注册资金(万元) | numeric | 19 | 6 | √ | 0.000000 | 注册资金(万元) |
| 58 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 59 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 60 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 61 | fdelaytime | 竞价自动延时(分钟) | int8 | 64 |  | √ | 0 | 竞价自动延时(分钟) |
| 62 | fbidnumber | 最少参与供应商数量 | int8 | 64 |  | √ | 0 | 最少参与供应商数量 |
| 63 | fsumtaxamount | 竞价基准金额 | numeric | 19 | 6 | √ | 0.000000 | 竞价基准金额 |
| 64 | fsumtax | 汇总税额 | numeric | 19 | 6 | √ | 0.000000 | 汇总税额 |
| 65 | fmaxdelaynumber | 最多延迟次数 | int4 | 32 |  | √ | 0 | 最多延迟次数 |

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
| 4 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fgoodsid | 供方物料编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 6 | fsumorderqty | fsumorderqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 7 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 8 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fprbillid | 申请单id | varchar | 50 |  | √ | ' ' | 申请单id |
| 10 | fpicture | 图片 | varchar | 255 |  | √ | ' ' | 图片 |
| 11 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 13 | floctaxamount | 本位币价税合计 | numeric | 19 | 6 | √ | 0.000000 | 本位币价税合计 |
| 14 | fsumcontractqty | fsumcontractqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 15 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 17 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 18 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 19 | fgoodsdesc | 供方物料描述 | varchar | 255 |  | √ | ' ' | 供方物料描述 |
| 20 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 21 | fpoentryid | 订单分录ID | varchar | 50 |  | √ | ' ' | 订单分录ID |
| 22 | fprbillno | 采购申请单号 | varchar | 80 |  | √ | ' ' | 采购申请单号 |
| 23 | flocamount | 本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 本位币金额 |
| 24 | fprentryid | 申请单分录id | varchar | 50 |  | √ | ' ' | 申请单分录id |
| 25 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 27 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 28 | fpcentryid | 合同分录ID | varchar | 50 |  | √ | ' ' | 合同分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_bidbillentry_a_pkey |  | fentryid |
| 2 | idx_pur_bidbillentry_a_fid |  | fid |
