# 销售出库单-im_saloutbill

## 关联子实体-子表 t_im_saloutbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_saloutbillentry_lk

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
| 1 | idx_im_saloutbillentry_lk_fk |  | fentryid |
| 2 | t_im_saloutbillentry_lk_pkey |  | fpkid |

---

## 销售出库单-多语言表 t_im_saloutbill_l

- **表名称：** 销售出库单-多语言表
- **表名：** t_im_saloutbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_saloutbill_l_fid |  | fid,flocaleid |
| 2 | t_im_saloutbill_l_pkey |  | fpkid |

---

## 物料明细-分表 t_im_saloutbillentry_c

- **表名称：** 物料明细-分表
- **表名：** t_im_saloutbillentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcurrencyid | 成本币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0 | 单位实际成本 |
| 4 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 5 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_saloutbillentry_c |  | fentryid |
| 2 | idx_im_saloutbillentry_c |  | fid |

---

## 销售出库单-反写记录表 t_im_saloutbill_wb

- **表名称：** 销售出库单-反写记录表
- **表名：** t_im_saloutbill_wb

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
| 1 | idx_im_saloutbill_wb_fk |  | fid |
| 2 | t_im_saloutbill_wb_pkey |  | fentryid |

---

## 物料明细-分表 t_im_saloutbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_saloutbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcrosslegalperson | 是否跨法人 | varchar | 5 |  | √ | '0' | 是否跨法人,枚举: 0 :否 1 :是 |
| 3 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 4 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 5 | fremaininvoicedbaseqty | 应收未关联销售发票基本数量 | numeric | 23 | 10 | √ | 0 | 应收未关联销售发票基本数量 |
| 6 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 7 | fentrustunverifybaseqty | 委托代销未结算基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 委托代销未结算基本数量 |
| 8 | freturnbaseqty | 已退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库基本数量 |
| 9 | funverifybaseqty | 未勾稽基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽基本数量 |
| 10 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 11 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 12 | fjoinpriceqty | 应收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应收数量 |
| 13 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 14 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 15 | fremaininvoicedqty | 应收未关联销售发票数量 | numeric | 23 | 10 | √ | 0 | 应收未关联销售发票数量 |
| 16 | fgroupseq | 成组行号 | varchar | 50 |  | √ | ' ' | 成组行号 |
| 17 | fsrcsysbillno | 来源系统单据编号 | varchar | 100 |  | √ | ' ' | 来源系统单据编号 |
| 18 | fremaincfmqty | 未确认数量 | numeric | 23 | 10 | √ | 0 | 未确认数量 |
| 19 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 20 | fjoincfmqty | 已确认数量 | numeric | 23 | 10 | √ | 0 | 已确认数量 |
| 21 | fwriteoffstockbaseqty | 冲销基本数量 | numeric | 23 | 10 | √ | 0 | 冲销基本数量 |
| 22 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 23 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 24 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 25 | fentrustunverifyqty | 委托代销未结算数量 | numeric | 23 | 10 | √ | 0.0000000000 | 委托代销未结算数量 |
| 26 | fverifybaseqty | 已勾稽基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽基本数量 |
| 27 | fwriteoffstockqty | 冲销数量 | numeric | 23 | 10 | √ | 0 | 冲销数量 |
| 28 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 29 | fremainjoinpricebaseqty | 剩余应收基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余应收基本数量 |
| 30 | fremainjoinpriceqty | 剩余应收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余应收数量 |
| 31 | finvoicedqty | 关联销售发票数量 | numeric | 23 | 10 | √ | 0 | 关联销售发票数量 |
| 32 | funverifyqty | 未勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽数量 |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 34 | fjoincfmbaseqty | 已确认基本数量 | numeric | 23 | 10 | √ | 0 | 已确认基本数量 |
| 35 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 36 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 37 | finvoicedbaseqty | 关联销售发票基本数量 | numeric | 23 | 10 | √ | 0 | 关联销售发票基本数量 |
| 38 | fconbillentity | 合同实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 39 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 40 | fjoinpricebaseqty | 应收基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应收基本数量 |
| 41 | fgroupnumber | 成组号 | varchar | 50 |  | √ | ' ' | 成组号 |
| 42 | fremaincfmbaseqty | 未确认基本数量 | numeric | 23 | 10 | √ | 0 | 未确认基本数量 |
| 43 | fremainreturnbaseqty | 未退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未退库基本数量 |
| 44 | fverifyqty | 已勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽数量 |
| 45 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 46 | fassociatedreturnqty | 关联退货数量 | numeric | 23 | 10 | √ | 0 | 关联退货数量 |
| 47 | fassociatedreturnbaseqty | 关联退货基本数量 | numeric | 23 | 10 | √ | 0 | 关联退货基本数量 |
| 48 | freturnqty | 已退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库数量 |
| 49 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 50 | fentrustverifyqty | 委托代销已结算数量 | numeric | 23 | 10 | √ | 0.0000000000 | 委托代销已结算数量 |
| 51 | fentrustverifybaseqty | 委托代销已结算基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 委托代销已结算基本数量 |
| 52 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 53 | finvoicedamountandtax | 关联销售发票价税合计 | numeric | 23 | 10 | √ | 0 | 关联销售发票价税合计 |
| 54 | fremainreturnqty | 未退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未退库数量 |
| 55 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_sobillentry_r_srceid |  | fsrcbillentryid |
| 2 | idx_im_sobillentry_r_mainid |  | fmainbillid |
| 3 | t_im_saloutbillentry_r_pkey |  | fentryid |
| 4 | idx_im_saloutbillentry_r_id |  | fid |
| 5 | idx_im_sobillentry_r_mainnum |  | fmainbillnumber |
| 6 | idx_im_sobillentry_r_srcid |  | fsrcbillid |
| 7 | idx_im_sobillentry_r_maineid |  | fmainbillentryid |

---

## 物料明细-多语言表 t_im_saloutbillentry_l

- **表名称：** 物料明细-多语言表
- **表名：** t_im_saloutbillentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | freceiveaddress | 收货地址 | varchar | 512 |  | √ | ' ' | 收货地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_saloutbille_l_id_local |  | fentryid,flocaleid |
| 2 | t_im_saloutbillentry_l_pkey |  | fpkid |

---

## 销售出库单-关联追踪表 t_im_saloutbill_tc

- **表名称：** 销售出库单-关联追踪表
- **表名：** t_im_saloutbill_tc

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
| 1 | t_im_saloutbill_tc_pkey |  | fid |
| 2 | idx_im_saloutbill_tc_tbill |  | ftbillid |
| 3 | idx_im_saloutbill_tc_tid |  | ftid |
| 4 | idx_t_im_sobill_ftbidtid |  | ftbillid,ftid |

---

## 关联子实体-子表 t_im_saloutbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_saloutbill_lk

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
| 1 | t_im_saloutbill_lk_pkey |  | fpkid |
| 2 | idx_im_saloutbill_lk_fk |  | fid |

---

## 销售出库单-主表 t_im_saloutbill

- **表名称：** 销售出库单-主表
- **表名：** t_im_saloutbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 3 | fisredbill | 是否红字 | bpchar | 1 |  | √ | '0' | 是否红字 |
| 4 | finvdc | finvdc | varchar | 5 |  | √ | ' ' |  |
| 5 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 7 | ftransactepathid | 结算路径 | int8 | 64 |  | √ | 0 | 结算路径 ism_settlerelations |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 10 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 11 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 12 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 13 | fisdespatchcreate | 是否发运生成 | bpchar | 1 |  | √ | '0' | 是否发运生成 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 16 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 21 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 22 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 23 | fbizdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 27 | fcustomerid | 收货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 28 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 29 | fhasapbusbill | 是否生成暂估应收单 | bpchar | 1 |  | √ | '0' | 是否生成暂估应收单 |
| 30 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 31 | fbizoperatorid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 32 | fsupplytrans | 供应商直运 | bpchar | 1 |  | √ | '0' | 供应商直运 |
| 33 | finnerbilltype | 内部交易单据类别 | varchar | 10 |  | √ | ' ' | 内部交易单据类别,枚举: in :对内 out :对外 |
| 34 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 35 | fquotation | 换算方式 | varchar | 50 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 36 | fpricelistid | 价目表 | int8 | 64 |  | √ | 0 | 销售价目表 sm_salepricelist |
| 37 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fbizorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 40 | fiswholediscount | 录入整单折扣 | bpchar | 1 |  | √ | '0' | 录入整单折扣 |
| 41 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 42 | frecconditionid | 收款条件 | int8 | 64 |  | √ | 0 | 收款条件 bd_reccondition |
| 43 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 46 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 47 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | finternal | 内部购销 | bpchar | 1 |  | √ | '0' | 内部购销 |
| 49 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 50 | fwholediscountamount | 整单折扣额 | numeric | 23 | 10 | √ | 0 | 整单折扣额 |
| 51 | fbizoperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 52 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 53 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 54 | fpaymode | 付款方式 | varchar | 30 |  | √ | 'CREDIT' | 付款方式,枚举: CASH :现销 CREDIT :赊销 |
| 55 | frevconfirmnode | 收入确认时点 | varchar | 50 |  | √ | ' ' | 收入确认时点,枚举: signIn :签收 saleOut :出库 |
| 56 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 57 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_sobill_biztimeno |  | fbiztime,fbillno |
| 2 | idx_im_sobill_org |  | forgid |
| 3 | idx_im_sobill_bktorgno |  | fbookdate,forgid,fbillno |
| 4 | idx_im_saleoutbl_forgbillno |  | fbillno,forgid |
| 5 | idx_im_sobill_forfbizfno |  | forgid,fbiztime,fbillno |
| 6 | t_im_saloutbill_pkey |  | fid |
| 7 | idx_im_sobill_custm |  | fcustomerid |

---

## 物料明细-子表 t_im_saloutbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_saloutbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率% | numeric | 23 | 10 | √ | 0.0000000000 | 税率% |
| 3 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 4 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | flocation | 交货地点 | varchar | 255 |  | √ | ' ' | 交货地点 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fmatchpricelistid | 行价目表 | int8 | 64 |  | √ | 0 | 销售价目表 sm_salepricelist |
| 9 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 11 | fkitsettleway | 套件内部结算方式 | varchar | 50 |  | √ | ' ' | 套件内部结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 12 | fparentproduct | 父项产品 | int8 | 64 |  | √ | 0 | 物料销售信息 bd_materialsalinfo |
| 13 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 14 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 16 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fownertype | 入库货主类型 | varchar | 36 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 18 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | freccustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 21 | fdeliveraddressf7 | 收货地点 | int8 | 64 |  | √ | 0 | 地址 bd_address |
| 22 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 23 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 25 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 26 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 27 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 28 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 29 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 30 | fkeepertype | 入库保管者类型 | varchar | 36 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 31 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 32 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 33 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 34 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 35 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 36 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | freturntype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: 1 :退货 2 :退补货 |
| 38 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 39 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 40 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 41 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 42 | funitmaterialcost | 单位材料成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位材料成本 |
| 43 | fsuitesettletype | 套件结算方式 | varchar | 50 |  | √ | ' ' | 套件结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 44 | fbaseunitdenominator | 基本单位用量：分母 | numeric | 23 | 10 | √ | 1 | 基本单位用量：分母 |
| 45 | fcusmatid | 客户物料编码 | int8 | 64 |  | √ | 0 | 客户物料对应表明细信息 bd_customermaterialinfo |
| 46 | fisnotupdate | 不更新库存 | bpchar | 1 |  | √ | '0' | 不更新库存 |
| 47 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 48 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 49 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 50 | fbaseunitnumerator | 基本单位用量：分子 | numeric | 23 | 10 | √ | 1 | 基本单位用量：分子 |
| 51 | freceiveprojectid | 领用项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 52 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 53 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 54 | fsettleroute | fsettleroute | int8 | 64 |  | √ | 0 |  |
| 55 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 56 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 57 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 58 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 59 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 60 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 61 | foutkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 62 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 63 | finwarehouseid | 入库仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 64 | fpayingcustomerid | 付款客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 65 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 66 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 67 | fbomentryid | BOM分录ID | int8 | 64 |  | √ | 0 | BOM分录ID |
| 68 | freceiveaddress_bak | 发货明细执行地址(后台用) | varchar | 512 |  | √ | ' ' | 发货明细执行地址(后台用) |
| 69 | fsuitepricepercent | 套件价格拆分比例% | numeric | 23 | 10 | √ | 0 | 套件价格拆分比例% |
| 70 | foutownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 71 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 72 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 73 | freturnpath | 退回路径 | bpchar | 1 |  | √ | ' ' | 退回路径,枚举: 1 :供应商 2 :企业 |
| 74 | finlocationid | 入库仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 75 | fentryorgid | fentryorgid | int8 | 64 |  | √ | 0 |  |
| 76 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 77 | fdeliverywayid | 交货方式 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 78 | fqualitytype | 质量类型 | bpchar | 1 |  | √ | ' ' | 质量类型,枚举: A :合格出库 B :不合格出库 C :合格退货 D :不合格退货 E :报废退货 |
| 79 | fproducttype | 产品类别 | varchar | 50 |  | √ | 'standard' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 80 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 81 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量(2) |
| 82 | freceivecontactid | 收货联系人 | int8 | 64 |  | √ | 0 | 客户联系人 bd_customerlinkman |
| 83 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 84 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 85 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 86 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 87 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 88 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 89 | fsettlecustomerid | 结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 90 | fmaterialcost | 材料成本 | numeric | 23 | 10 | √ | 0.0000000000 | 材料成本 |
| 91 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 92 | fhasvirtualbill | 已生成内部单据 | bpchar | 1 |  | √ | '0' | 已生成内部单据 |
| 93 | fsuitedeliverytype | 套件发货方式 | varchar | 50 |  | √ | ' ' | 套件发货方式,枚举: kitdeliver :成套发货 nonkitdeliver :非成套发货 kitreturn :成套退货 nonkitreturn :非成套退货 |
| 94 | freceiveaddress | 收货地址 | varchar | 512 |  | √ | ' ' | 收货地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_sobill_e_oow |  | foutownerid |
| 2 | t_im_saloutbillentry_pkey |  | fentryid |
| 3 | idx_im_saloutbillentry_billid |  | fid |
| 4 | idx_im_sobill_e_mmt |  | fmaterialmasterid |
| 5 | idx_im_sobill_e_wh |  | fwarehouseid |
| 6 | idx_im_sobill_e_ow |  | fownerid |
