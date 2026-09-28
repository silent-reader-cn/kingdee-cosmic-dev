# 退库查询-scp_return

## 退货查询分录-子表 t_pur_returnentry

- **表名称：** 退货查询分录-子表
- **表名：** t_pur_returnentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fproddate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 4 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 5 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 10 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 11 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 13 | fretreason | 退货原因 | varchar | 512 |  | √ | ' ' | 退货原因 |
| 14 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 15 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 16 | fqty | 退货数量 | numeric | 19 | 6 | √ | 0.000000 | 退货数量 |
| 17 | ftaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 18 | fdctrate | 单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 单位折扣(率) |
| 19 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 pur_trace |
| 21 | fmaterialnewid | 补货物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 22 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 23 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 24 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 26 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 27 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 pur_warehouse |
| 28 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | finvorgid | 库存方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 31 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 32 | flotid | 批号（废弃） | int8 | 64 |  | √ | 0 | 批号 pur_lot |
| 33 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 34 | fsuplot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 35 | freplenishqty | 补货数量 | numeric | 19 | 6 | √ | 0.000000 | 补货数量 |
| 36 | fmaterialnametext | 品类物料名称 | varchar | 255 |  | √ | ' ' | 品类物料名称 |
| 37 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 38 | fsettleorgid | 核算客户 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 42 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_returnentry_pkey |  | fentryid |
| 2 | idx_pur_returnentry_fid_fseq |  | fid,fseq |
| 3 | idx_pur_returnentry_fmatid |  | fmaterialid |

---

## 退货查询分录-分表 t_pur_returnentry_a

- **表名称：** 退货查询分录-分表
- **表名：** t_pur_returnentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 税额(本位币) |
| 3 | fsumcheckqty | 关联对账数量 | numeric | 19 | 6 | √ | 0.000000 | 关联对账数量 |
| 4 | fmatchqty | fmatchqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 5 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 6 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 7 | fsrcinsentryid | 来源单据入库行ID | varchar | 50 |  | √ | ' ' | 来源单据入库行ID |
| 8 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 9 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fpurtypeid | 采购类型 | int8 | 64 |  | √ | 0 | 协同辅助资料 pbd_mallextdata |
| 11 | fsumreturnqty | 关联退货数量 | numeric | 19 | 6 | √ | 0.000000 | 关联退货数量 |
| 12 | fsettlesupid | 结算供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 15 | floctaxamount | 价税合计(本位币) | numeric | 19 | 6 | √ | 0.000000 | 价税合计(本位币) |
| 16 | funmatchbaseqty | 未核销基本数量 | numeric | 23 | 10 | √ | 0 | 未核销基本数量 |
| 17 | funmatchqty | 未核销数量 | numeric | 23 | 10 | √ | 0 | 未核销数量 |
| 18 | finvoiceqty | 已开票数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票数量 |
| 19 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 20 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 21 | fsrcinsbillid | 来源单据入库ID | varchar | 50 |  | √ | ' ' | 来源单据入库ID |
| 22 | fischeckorinvoice | 对账/开票 | bpchar | 1 |  | √ | '0' | 对账/开票 |
| 23 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 24 | funmatchamt | funmatchamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 25 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 26 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 27 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 28 | fsuminvoiceqty | 关联数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联数量 |
| 29 | flocamount | 金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 金额(本位币) |
| 30 | finvoiceamt | 已开票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票金额 |
| 31 | fsaloutnum | fsaloutnum | varchar | 80 |  | √ | ' ' |  |
| 32 | fsumcheckamt | 关联对账金额 | numeric | 19 | 6 | √ | 0.000000 | 关联对账金额 |
| 33 | fsaloutid | fsaloutid | int8 | 64 |  | √ | 0 |  |
| 34 | fsaloutentryid | fsaloutentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 37 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 38 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |
| 39 | fmatchamt | fmatchamt | numeric | 19 | 6 | √ | 0.000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_returnentry_a_pkey |  | fentryid |
| 2 | idx_pur_returnentry_a_fpoid |  | fpoentryid |
| 3 | idx_pur_returnentry_a_fid |  | fid |

---

## 退库查询-关联追踪表 t_pur_return_tc

- **表名称：** 退库查询-关联追踪表
- **表名：** t_pur_return_tc

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
| 1 | t_pur_return_tc_pkey |  | fid |
| 2 | idx_pur_return_tc_tid |  | ftid |
| 3 | idx_pur_return_tc_tbill |  | ftbillid |

---

## 退库查询-分表 t_pur_return_a

- **表名称：** 退库查询-分表
- **表名：** t_pur_return_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fisinitial | fisinitial | bpchar | 1 |  | √ | ' ' |  |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 8 | fchkbillno | 对账单号 | varchar | 80 |  | √ | ' ' | 对账单号 |
| 9 | fpricetime | fpricetime | bpchar | 1 |  | √ | ' ' |  |
| 10 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fiscentersettle | 集中结算 | bpchar | 1 |  | √ | ' ' | 集中结算 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fsupaddr | 销售方地址 | varchar | 255 |  | √ | ' ' | 销售方地址 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fischeck | 已对账 | bpchar | 1 |  | √ | ' ' | 已对账 |
| 18 | fisvirtual | fisvirtual | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_return_a_pkey |  | fid |
| 2 | idx_pur_return_a_fcreatetime |  | fcreatetime |

---

## 退库查询-多语言表 t_pur_return_l

- **表名称：** 退库查询-多语言表
- **表名：** t_pur_return_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fsupaddr | fsupaddr | varchar | 255 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_return_l_pkey |  | fpkid |
| 2 | idx_pur_return_l_fid_flocaleid |  | fid,flocaleid |

---

## 退库查询-反写记录表 t_pur_return_wb

- **表名称：** 退库查询-反写记录表
- **表名：** t_pur_return_wb

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
| 1 | t_pur_return_wb_pkey |  | fentryid |

---

## 退库查询-主表 t_pur_return

- **表名称：** 退库查询-主表
- **表名：** t_pur_return

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | foperatorid | 联系人 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 5 | frettype | 退货类型(废弃) | bpchar | 1 |  | √ | ' ' | 退货类型(废弃),枚举: 1 :库存退货 2 :暂收退货 |
| 6 | fwriteoffflag | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 7 | forgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 10 | freplenishtype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: 1 :退货需补 2 :创建补货订单 3 :退货不补 |
| 11 | fpayeesupid | 收款方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 12 | fbiztype | 业务类型(作废) | bpchar | 1 |  | √ | ' ' | 业务类型(作废),枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 13 | fsumamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 14 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 17 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 20 | finvoicesupid | 开票方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 21 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 22 | fvmisettle | VMI结算 | bpchar | 1 |  | √ | '0' | VMI结算 |
| 23 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fdelisupid | 送货方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 25 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fsumqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 27 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 28 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 29 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 30 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 31 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 |
| 32 | fpersonid | 联系人（废弃） | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 33 | fsumtaxamount | 退货金额 | numeric | 19 | 6 | √ | 0.000000 | 退货金额 |
| 34 | fsettleorgid | 核算客户 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fsumtax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 36 | fsupaddr | fsupaddr | varchar | 255 |  | √ | ' ' |  |
| 37 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 38 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |
| 39 | fcontacterid | 销售员 | int8 | 64 |  | √ | 0 | 协同业务员 scp_bizperson |
| 40 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_return_fbizpartnerid |  | fbilldate,fbizpartnerid |
| 2 | t_pur_return_pkey |  | fid |
| 3 | idx_pur_return_fbillno |  | fbillno |

---

## 关联子实体-子表 t_pur_returnentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_returnentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 退货数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 退货数量_确认携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fqty_old | 退货数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 退货数量_原始携带值 |
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
| 1 | t_pur_returnentry_lk_pkey |  | fpkid |
