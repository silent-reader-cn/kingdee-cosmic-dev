# 询价单-sou_inquiry

## 关联子实体-子表 t_pur_inquiryentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_inquiryentry_lk

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
| 1 | t_pur_inquiryentry_lk_fentryid |  | fentryid,fseq |
| 2 | t_pur_inquiryentry_lk_pkey |  | fpkid |

---

## 物料分录-分表 t_pur_inquiryentry_a

- **表名称：** 物料分录-分表
- **表名：** t_pur_inquiryentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 税额(本位币) |
| 3 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 4 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 5 | fgoodsid | 供方物料编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 6 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 7 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 8 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 9 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fprbillid | 申请单id | varchar | 50 |  | √ | ' ' | 申请单id |
| 11 | fgoodsdesc | 供方物料描述 | varchar | 255 |  | √ | ' ' | 供方物料描述 |
| 12 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 13 | fsumquoteqty | 关联报价数量 | numeric | 19 | 6 | √ | 0.000000 | 关联报价数量 |
| 14 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 15 | fprbillno | 采购申请单号 | varchar | 80 |  | √ | ' ' | 采购申请单号 |
| 16 | flocamount | 金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 金额(本位币) |
| 17 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 19 | floctaxamount | 价税合计(本位币) | numeric | 19 | 6 | √ | 0.000000 | 价税合计(本位币) |
| 20 | fprentryid | 申请单分录id | varchar | 50 |  | √ | ' ' | 申请单分录id |
| 21 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 23 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 24 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_inquiryentry_a_fid |  | fid |
| 2 | idx_inquiryentry_a_fpoentryid |  | fpoentryid |
| 3 | t_pur_inquiryentry_a_pkey |  | fentryid |

---

## 多轮报价面板分录-子表 t_pur_inquiryturnslog

- **表名称：** 多轮报价面板分录-子表
- **表名：** t_pur_inquiryturnslog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrylogscope | 询价范围 | bpchar | 1 |  | √ | ' ' | 询价范围,枚举: 1 :所有供应商 2 :指定供应商 |
| 3 | fturns | 询价轮次 | varchar | 10 |  | √ | ' ' | 询价轮次,枚举: 1 :首轮 2 :第二轮 3 :第三轮 4 :第四轮 5 :第五轮 6 :第六轮 7 :第七轮 8 :第八轮 9 :第九轮 10 :第十轮 11 :第十一轮 12 :第十二轮 13 :第十三轮 14 :第十四轮 15 :第十五轮 16 :第十六轮 17 :第十七轮 18 :第十八轮 19 :第十九轮 20 :第二十轮 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fnote | 原因说明 | varchar | 255 |  | √ | ' ' | 原因说明 |
| 6 | fhandlerid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | flogdeadline | 报价截止时间 | timestamp | 0 |  |  | null | 报价截止时间 |
| 9 | fhandletime | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_inquiryturnslog_fid |  | fid,fseq |
| 2 | t_pur_inquiryturnslog_pkey |  | fentryid |

---

## 关联子实体-子表 t_pur_inquiryn_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_inquiryn_lk

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
| 1 | t_pur_inquiryn_lk_pkey |  | fpkid |
| 2 | idx_pur_inquiryn_lk_fk |  | fid |

---

## 询价单-关联追踪表 t_pur_inquiry_tc

- **表名称：** 询价单-关联追踪表
- **表名：** t_pur_inquiry_tc

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
| 1 | t_pur_inquiry_tc_pkey |  | fid |
| 2 | idx_pur_inquiry_tc_tbill |  | ftbillid |
| 3 | idx_pur_inquiry_tc_tid |  | ftid |

---

## 询价单-分表 t_pur_inquiry_a

- **表名称：** 询价单-分表
- **表名：** t_pur_inquiry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdecider | 定标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fdecidedate | 定标时间 | timestamp | 0 |  |  | null | 定标时间 |
| 4 | fsupplierstatus | fsupplierstatus | bpchar | 1 |  | √ | ' ' |  |
| 5 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | favgsumamount | 平均价税合计 | numeric | 19 | 6 | √ | 0.000000 | 平均价税合计 |
| 10 | fmaxsupplierid | 最高价税合计供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | fmaxuntaxsumamount | 最高未税金额 | numeric | 23 | 10 | √ | 0 | 最高未税金额 |
| 12 | fminsupplierid | 最低价税合计供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 13 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fopener | 开标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fminuntaxamount | 最低未税金额 | numeric | 23 | 10 | √ | 0 | 最低未税金额 |
| 17 | fmaxuntaxsupplierid | 最高未税金额供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fterminate | 终止意见 | varchar | 255 |  | √ | ' ' | 终止意见 |
| 20 | fpushnotice | 是否已发布公告 | bpchar | 1 |  | √ | '0' | 是否已发布公告,枚举: 1 :是 0 :否 |
| 21 | fsupplierprostatus | fsupplierprostatus | bpchar | 1 |  | √ | ' ' |  |
| 22 | fopendate | 开标时间 | timestamp | 0 |  |  | null | 开标时间 |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | fminsumamount | 最低价税合计 | numeric | 19 | 6 | √ | 0.000000 | 最低价税合计 |
| 25 | fpush1688 | 是否发布1688 | bpchar | 1 |  | √ | '0' | 是否发布1688,枚举: 1 :是 0 :否 |
| 26 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fquotenum | 收到报价数 | int8 | 64 |  | √ | 0 | 收到报价数 |
| 28 | faudit | 定标意见 | varchar | 512 |  | √ | ' ' | 定标意见 |
| 29 | fmaxsumamount | 最高价税合计 | numeric | 19 | 6 | √ | 0.000000 | 最高价税合计 |
| 30 | fbuyofferid | 1688询价单ID | varchar | 50 |  | √ | ' ' | 1688询价单ID |
| 31 | fminuntaxsupplierid | 最低未税金额供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 32 | favgsumuntaxamount | 平均未税金额 | numeric | 23 | 10 | √ | 0 | 平均未税金额 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fisautofillprice | 自动携带上轮价格 | bpchar | 1 |  | √ | '0' | 自动携带上轮价格 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_inquiry_a_pkey |  | fid |
| 2 | idx_pur_inquiry_a_fcreatetime |  | fcreatetime |

---

## 询价单-主表 t_pur_inquiry

- **表名称：** 询价单-主表
- **表名：** t_pur_inquiry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcontrolqty | 控制中标物料数量 | varchar | 1 |  | √ | '1' | 控制中标物料数量,枚举: 1 :不控制 2 :严格控制 |
| 3 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 4 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 6 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 9 | ftitle | 询价标题 | varchar | 255 |  | √ | ' ' | 询价标题 |
| 10 | fenddate | 报价截止时间 | timestamp | 0 |  |  | null | 报价截止时间 |
| 11 | fbizmodel | 经营模式 | varchar | 50 |  | √ | ' ' | 经营模式,枚举: 1 :生产加工 2 :经销批发 3 :商业服务 4 :招商代理 |
| 12 | finvtype | 发票种类 | bpchar | 1 |  | √ | ' ' | 发票种类,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 9 :不需要发票 |
| 13 | fsumamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 14 | fdatefrom | 价格有效期从 | timestamp | 0 |  |  | null | 价格有效期从 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fsupquonum | 报价供应商数量 | int8 | 64 |  | √ | 0 | 报价供应商数量 |
| 17 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 |
| 19 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 20 | fopenladder | 启用阶梯价 | varchar | 1 |  | √ | '0' | 启用阶梯价,枚举: 1 :启用 0 :不启用 |
| 21 | fbizaddr | 经营地址 | varchar | 255 |  | √ | ' ' | 经营地址 |
| 22 | fadoptrule | 默认中标规则 | varchar | 1 |  | √ | '1' | 默认中标规则,枚举: 1 :含税单价最低 2 :未税单价最低 3 :含税总额最低 4 :未税总额最低 |
| 23 | fpersonid | 采购员（废弃） | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 24 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 26 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | '1270375173299638272' | 单据类型 bos_billtype |
| 27 | fcheckperm | 校验供应商用户采购组织权限 | bpchar | 1 |  | √ | '1' | 校验供应商用户采购组织权限 |
| 28 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 29 | fbizstatus | 项目状态 | bpchar | 1 |  | √ | ' ' | 项目状态,枚举: A :报价中 B :已开标 C :已定标 D :已执行 E :已终止 |
| 30 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 31 | ftotalinquiry | 供应商整单报价 | bpchar | 1 |  | √ | ' ' | 供应商整单报价 |
| 32 | fsupcurrtype | 供应商报价币选项 | bpchar | 1 |  | √ | '2' | 供应商报价币选项,枚举: 1 :按询价单结算币 2 :供应商自选币种 |
| 33 | fbiztype | 业务类型(作废) | bpchar | 1 |  | √ | ' ' | 业务类型(作废),枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 34 | fquotation | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 35 | fopentype | 开标方式 | bpchar | 1 |  | √ | ' ' | 开标方式,枚举: 1 :报价即可见自动开标（非密封） 4 :报价即可见手工开标（非密封） 2 :到截止时间自动开标（密封） 3 :到截止时间手工开标（密封） |
| 36 | fcertificate | 证照要求 | varchar | 50 |  | √ | ' ' | 证照要求,枚举: 1 :三/五证合一 2 :营业执照 3 :税务登记证 4 :组织机构代码证 5 :社会保险登记证 6 :一般纳税人证明材料 7 :统计登记证 8 :其他证照 |
| 37 | fenablemodify | 允许供应商修改阶梯 | varchar | 1 |  | √ | '0' | 允许供应商修改阶梯 |
| 38 | fturns | 询价轮次 | varchar | 10 |  | √ | ' ' | 询价轮次,枚举: 1 :首轮 2 :第二轮 3 :第三轮 4 :第四轮 5 :第五轮 6 :第六轮 7 :第七轮 8 :第八轮 9 :第九轮 10 :第十轮 11 :第十一轮 12 :第十二轮 13 :第十三轮 14 :第十四轮 15 :第十五轮 16 :第十六轮 17 :第十七轮 18 :第十八轮 19 :第十九轮 20 :第二十轮 |
| 39 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 40 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 41 | fpublisher | 发布人 | varchar | 255 |  | √ | ' ' | 发布人 |
| 42 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 44 | fcurrid | 结算币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 45 | fdateto | 价格有效期至 | timestamp | 0 |  |  | null | 价格有效期至 |
| 46 | fsupscope | 供应商范围 | bpchar | 1 |  | √ | ' ' | 供应商范围,枚举: 1 :所有供应商 2 :指定供应商 |
| 47 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 49 | fsumqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 50 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 51 | fregcapital | 注册资金(万元) | numeric | 19 | 6 | √ | 0.000000 | 注册资金(万元) |
| 52 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 53 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 54 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 |
| 55 | fsumtaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 56 | fsumtax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 57 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 0 | 汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_inquiry_pkey |  | fid |
| 2 | idx_pur_inquiry_fbilldate |  | fbilldate |
| 3 | idx_pur_inquiry_fbillno |  | fbillno |
| 4 | idx_pur_inquiry_fbizpartnerid |  | fbizpartnerid |
| 5 | idx_pur_inquiry_fenddate |  | fenddate |

---

## 询价单-反写记录表 t_pur_inquiry_wb

- **表名称：** 询价单-反写记录表
- **表名：** t_pur_inquiry_wb

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
| 1 | t_pur_inquiry_wb_pkey |  | fentryid |

---

## 询价单-多语言表 t_pur_inquiry_l

- **表名称：** 询价单-多语言表
- **表名：** t_pur_inquiry_l

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
| 1 | t_pur_inquiry_l_pkey |  | fpkid |
| 2 | idx_pur_inquiry_l_fid |  | fid,flocaleid |

---

## 报价范围分录-子表 t_pur_inquiryturns

- **表名称：** 报价范围分录-子表
- **表名：** t_pur_inquiryturns

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fturns | 询价轮次 | varchar | 10 |  | √ | ' ' | 询价轮次,枚举: 1 :首轮 2 :第二轮 3 :第三轮 4 :第四轮 5 :第五轮 6 :第六轮 7 :第七轮 8 :第八轮 9 :第九轮 10 :第十轮 11 :第十一轮 12 :第十二轮 13 :第十三轮 14 :第十四轮 15 :第十五轮 16 :第十六轮 17 :第十七轮 18 :第十八轮 19 :第十九轮 20 :第二十轮 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_inquiryturns_pkey |  | fentryid |
| 2 | idx_pur_inquiryturns_fturns |  | fturns,fsupplierid,fmaterialid |
| 3 | idx_pur_inquiryturns_fidseq |  | fid,fseq |

---

## 阶梯价子分录-子表 t_pur_inquiry_ladderentry

- **表名称：** 阶梯价子分录-子表
- **表名：** t_pur_inquiry_ladderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fladderqtyfrom | 阶梯数量从（>） | numeric | 23 | 10 |  | null | 阶梯数量从（>） |
| 2 | fladderprice | 未税单价 | numeric | 23 | 10 |  | null | 未税单价 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fladderremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fladderunitid | 阶梯价计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | null | id |
| 7 | fladdertaxprice | 含税单价 | numeric | 23 | 10 |  | null | 含税单价 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 9 | fladderqtyto | 阶梯数量至（<=） | numeric | 23 | 10 |  | null | 阶梯数量至（<=） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_inquiry_ladderentry |  | fdetailid |
| 2 | idx_inquiry_ladderentry_entry |  | fentryid |

---

## 供应商分录-子表 t_pur_inquirysupplier

- **表名称：** 供应商分录-子表
- **表名：** t_pur_inquirysupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fquotedate | 参与时间 | timestamp | 0 |  |  | null | 参与时间 |
| 3 | fentrycount | 供应商实际报价轮次 | varchar | 10 |  | √ | ' ' | 供应商实际报价轮次,枚举: 1 :第一轮 2 :第二轮 3 :第三轮 4 :第四轮 5 :第五轮 6 :第六轮 7 :第七轮 8 :第八轮 9 :第九轮 10 :第十轮 11 :第十一轮 12 :第十二轮 13 :第十三轮 14 :第十四轮 15 :第十五轮 16 :第十六轮 17 :第十七轮 18 :第十八轮 19 :第十九轮 20 :第二十轮 |
| 4 | fsupplierbizstatus | 供应商轮次状态 | bpchar | 1 |  | √ | ' ' | 供应商轮次状态,枚举: A :待报价 B :已报价 C :不报价 D :未参与 E :已终止 |
| 5 | fentrystatus | 中标结果 | bpchar | 1 |  | √ | ' ' | 中标结果,枚举: A :已报价 B :已开标 C :中标 D :部分中标 E :未中标 F :不报价 |
| 6 | fdeadline | 报价截止时间 | timestamp | 0 |  |  | null | 报价截止时间 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fquoterid | 参与人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fentryturns | 询价轮次 | varchar | 10 |  | √ | ' ' | 询价轮次,枚举: 1 :第一轮 2 :第二轮 3 :第三轮 4 :第四轮 5 :第五轮 6 :第六轮 7 :第七轮 8 :第八轮 9 :第九轮 10 :第十轮 11 :第十一轮 12 :第十二轮 13 :第十三轮 14 :第十四轮 15 :第十五轮 16 :第十六轮 17 :第十七轮 18 :第十八轮 19 :第十九轮 20 :第二十轮 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fcanshow | 是否显示可选 | bpchar | 1 |  | √ | '1' | 是否显示可选 |
| 12 | fsupplierid | 供应商编码 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_inquirysup_fid_fseq |  | fid,fseq |
| 2 | idx_pur_inquirysup_fsupid |  | fsupplierid |
| 3 | t_pur_inquirysupplier_pkey |  | fentryid |

---

## 物料分录-子表 t_pur_inquiryentry

- **表名称：** 物料分录-子表
- **表名：** t_pur_inquiryentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flatestpricingnotes | 最新议价备注 | varchar | 512 |  | √ | ' ' | 最新议价备注 |
| 3 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 4 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fblueprintstatus | 图纸获取状态 | bpchar | 1 |  |  | ' ' | 图纸获取状态,枚举: A :下载中 B :无图纸 C :已获取 D :获取失败 E :未获取 |
| 6 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 7 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 11 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 12 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 13 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 14 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 15 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 16 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 17 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 18 | ftaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 19 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fdctrate | 单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 单位折扣(率) |
| 21 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 pur_trace](../pbd_files/pur_trace.md) |
| 23 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 24 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fpcbillno | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 26 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fnewestturns | 询价轮次 | varchar | 10 |  | √ | ' ' | 询价轮次,枚举: 1 :首轮 2 :第二轮 3 :第三轮 4 :第四轮 5 :第五轮 6 :第六轮 7 :第七轮 8 :第八轮 9 :第九轮 10 :第十轮 11 :第十一轮 12 :第十二轮 13 :第十三轮 14 :第十四轮 15 :第十五轮 16 :第十六轮 18 :第十八轮 17 :第十七轮 19 :第十九轮 20 :第二十轮 |
| 28 | fdelitypeid | 交货方式 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 29 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 30 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 31 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 32 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fpobillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 36 | fvalidnum | 有效报价供应商数量 | int4 | 32 |  | √ | 0 | 有效报价供应商数量 |
| 37 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_inquiryentry_pkey |  | fentryid |
| 2 | idx_inquiryentry_fmaterialid |  | fmaterialid |
| 3 | idx_inquiryentry_fid_fseq |  | fid,fseq |
