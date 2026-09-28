# 开票申请单-sim_original_bill

## 关联子实体-子表 t_sim_original_bill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sim_original_bill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_original_bill_lk_fk |  | fid |
| 2 | pk_sim_original_bill_lk |  | fpkid |

---

## 开票申请单-分表 t_sim_original_bill_e

- **表名称：** 开票申请单-分表
- **表名：** t_sim_original_bill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdrawer | 开票人 | varchar | 50 |  | √ | ' ' | 开票人 |
| 3 | fcapitalorg | 资金组织 | varchar | 100 |  | √ | ' ' | 资金组织 |
| 4 | fbillcomplete | 单据完整 | varchar | 10 |  | √ | '0' | 单据完整,枚举: 0 :完整 1 :待补充 |
| 5 | ftextfield5 | 扩展字段5 | varchar | 150 |  | √ | ' ' | 扩展字段5 |
| 6 | fsettlementorgbase | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | foriginbillseq | 批次序号 | varchar | 30 |  | √ | ' ' | 批次序号 |
| 8 | ftextfield4 | 扩展字段4 | varchar | 150 |  | √ | ' ' | 扩展字段4 |
| 9 | fsalesorg | 销售组织 | varchar | 100 |  | √ | ' ' | 销售组织 |
| 10 | fcustomname | 客户名称 | varchar | 200 |  | √ | ' ' | 客户名称 |
| 11 | finvoicedamount | 发票金额 | numeric | 23 | 10 | √ | 0 | 发票金额 |
| 12 | foribuyeraddr | 原购方地址电话 | varchar | 150 |  | √ | ' ' | 原购方地址电话 |
| 13 | foribuyername | 原购方名称 | varchar | 100 |  | √ | ' ' | 原购方名称 |
| 14 | feditable | 可编辑 | varchar | 10 |  | √ | ' ' | 可编辑,枚举: 0 :可编辑 1 :不可编辑 |
| 15 | fsalesorgbase | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fredflushblue | 红冲蓝票源单 | varchar | 50 |  | √ | ' ' | 红冲蓝票源单 |
| 17 | fbatchbelong | 所属批次 | varchar | 50 |  | √ | ' ' | 所属批次 |
| 18 | fexchangerate | 汇率（文本） | varchar | 50 |  | √ | ' ' | 汇率（文本） |
| 19 | fblueinvoicecode | 待冲蓝票代码 | varchar | 200 |  | √ | ' ' | 待冲蓝票代码 |
| 20 | fbotpparamconfig | 下推参数配置 | varchar | 1000 |  | √ | ' ' | 下推参数配置 |
| 21 | finvoicecode | 发票代码 | varchar | 20 |  | √ | ' ' | 发票代码 |
| 22 | fsplitrule | 拆分规则 | varchar | 10 |  | √ | ' ' | 拆分规则,枚举: |
| 23 | fspecialtype | 特殊票种 | varchar | 50 |  | √ | ' ' | 特殊票种,枚举: 00 :非特殊票种 02 :收购 06 :抵扣通行费 07 :不抵扣通行费 08 :成品油 11 :卷烟 18 :机动车 |
| 24 | fgoodstype | 物料分类 | varchar | 100 |  | √ | ' ' | 物料分类 |
| 25 | finvoiceno | 发票号码 | varchar | 20 |  | √ | ' ' | 发票号码 |
| 26 | finvoicedtax | 发票税额 | numeric | 23 | 10 | √ | 0 | 发票税额 |
| 27 | fblueinvoiceno | 待冲蓝票号码 | varchar | 200 |  | √ | ' ' | 待冲蓝票号码 |
| 28 | fbillstatus | 单据审批状态 | varchar | 50 |  | √ | ' ' | 单据审批状态,枚举: A :暂存 B :已提交 C :已审核 D :无需审批 |
| 29 | finvoicedtotalamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 30 | fredreason | 冲红原因 | varchar | 50 |  | √ | ' ' | 冲红原因,枚举: 1 :销货退回 2 :开票有误 3 :服务中止 4 :销售折让 |
| 31 | fdeduction | 扣除额(差额) | numeric | 23 | 10 | √ | 0.0000000000 | 扣除额(差额) |
| 32 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 33 | fcustomnameid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 34 | fabolishreason | 作废原因 | varchar | 50 |  | √ | ' ' | 作废原因 |
| 35 | fmergelable | 当前处理人(合并标识) | varchar | 50 |  | √ | ' ' | 当前处理人(合并标识) |
| 36 | fsurplustax | 剩余可开税额 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余可开税额 |
| 37 | fbillsource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :excel导入 2 :业务系统 3 :单据下推 4 :其他 5 :扫码开票 6 :手工新增 7 :应收单下推 |
| 38 | fbotptype | 下推类型 | varchar | 10 |  | √ | ' ' | 下推类型,枚举: 01 :按物料匹配 03 :按物料分类匹配 00 :按优先级匹配 04 :按物料分类匹配，取物料分类名称开票 |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fplanamount | 参考金额 | numeric | 23 | 10 | √ | 0 | 参考金额 |
| 41 | fmainissuedtax | 已开税额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开税额 |
| 42 | fbuyertype | fbuyertype | varchar | 10 |  | √ | ' ' |  |
| 43 | foribuyerbank | 原购方开户行电话 | varchar | 150 |  | √ | ' ' | 原购方开户行电话 |
| 44 | fexchangedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 45 | finvoicestatus | 发票状态 | varchar | 10 |  | √ | ' ' | 发票状态,枚举: 0 :正常 3 :红冲 6 :作废 |
| 46 | fplantaxamount | 参考含税金额 | numeric | 23 | 10 | √ | 0 | 参考含税金额 |
| 47 | fsalerorbuyer | 购销身份 | varchar | 10 |  | √ | ' ' | 购销身份,枚举: 0 :我是销方 1 :我是购方 |
| 48 | fsplitormergeflag | 是否合并拆分标志 | varchar | 50 |  | √ | ' ' | 是否合并拆分标志,枚举: 0 :不拆分不合并 1 :要拆分不合并 2 :不拆分要合并 3 :要拆分要合并 |
| 49 | fsurplusamount | 剩余可开金额 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余可开金额 |
| 50 | fbillsourcetype | 单据类型 | varchar | 30 |  | √ | 'A' | 单据类型,枚举: A :普通单 B :红冲单 C :作废单 D :重开单 |
| 51 | fmergekey | 合并key | varchar | 50 |  | √ | ' ' | 合并key |
| 52 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: 01 :01 |
| 53 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 54 | fissuetime | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 55 | fauditsuggestion | 审核意见 | varchar | 200 |  | √ | ' ' | 审核意见 |
| 56 | fpushbillname | 下推单据名称 | varchar | 50 |  | √ | ' ' | 下推单据名称 |
| 57 | foperator | 经办人 | int8 | 64 |  | √ | 0 | 经办人信息 bdm_operator_info |
| 58 | fmaintaxdeviation | 税额误差 | numeric | 23 | 10 | √ | 0.0000000000 | 税额误差 |
| 59 | fsettlementorg | 结算组织 | varchar | 100 |  | √ | ' ' | 结算组织 |
| 60 | fcurrency | 币别 | varchar | 50 |  | √ | ' ' | 币别 |
| 61 | finfocode | 红字信息表编号/红字确认单编号 | varchar | 800 |  | √ | ' ' | 红字信息表编号/红字确认单编号 |
| 62 | ftaxadjust | 税额微调 | varchar | 4 |  | √ | ' ' | 税额微调 |
| 63 | fmaterialtypebase | 物料分类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 64 | fapplicant | 申请方 | varchar | 50 |  | √ | ' ' | 申请方,枚举: 2 :销方申请 1 :购方申请-未抵扣 0 :购方申请-已抵扣 |
| 65 | fbilltypebase | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 66 | fmainissuedamount | 已开金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开金额 |
| 67 | fproducttype | 商品类型 | varchar | 10 |  | √ | ' ' | 商品类型,枚举: 1 :开票项 2 :物料 3 :费用项目 |
| 68 | fclosestatus | 关闭状态 | varchar | 10 |  | √ | ' ' | 关闭状态,枚举: 0 :未关闭 1 :关闭 |
| 69 | foriginalissuetime | 待冲蓝票开票日期 | timestamp | 0 |  |  | null | 待冲蓝票开票日期 |
| 70 | fblueinvoicetype | 待冲发票种类 | varchar | 10 |  | √ | ' ' | 待冲发票种类,枚举: 026 :电子普通发票 007 :纸质普通发票 025 :增值税普通发票（卷票） 08xdp :全电发票（增值税专用发票） 10xdp :全电发票（普通发票） |
| 71 | fcapitalorgbase | 资金组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 72 | fwxid | 微信id(扫码二次校验使用) | varchar | 50 |  | √ | ' ' | 微信id(扫码二次校验使用) |
| 73 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型,枚举: 01 :应收单 50 :业务单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_original_bill_e |  | fid |
| 2 | idx_sim_original_bill_e |  | fdeduction |

---

## 开票申请单-关联追踪表 t_sim_original_bill_tc

- **表名称：** 开票申请单-关联追踪表
- **表名：** t_sim_original_bill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_original_bill_tc_tid |  | ftid |
| 2 | pk_sim_original_bill_tc |  | fid |
| 3 | idx_sim_original_bill_tc_tbill |  | ftbillid |

---

## 单据体-子表 t_sim_original_bill_item

- **表名称：** 单据体-子表
- **表名：** t_sim_original_bill_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率 | varchar | 30 |  | √ | ' ' | 税率,枚举: 0 :0% 0.01 :1% 0.015 :减按1.5% 0.03 :3% 0.04 :4% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.16 :16% 0.17 :17% |
| 3 | fdiscountrate | 折扣率 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣率 |
| 4 | frowtype | 行性质 | varchar | 30 |  | √ | ' ' | 行性质,枚举: 1 :折扣行 2 :商品行 |
| 5 | foriissuednum | 原始已开数量 | numeric | 23 | 10 | √ | 0 | 原始已开数量 |
| 6 | ffromissuedamount | 原币已开金额(不含税) | numeric | 23 | 10 | √ | 0 | 原币已开金额(不含税) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fblueinvoiceitemid | 红冲单对应蓝票明细id | int8 | 64 |  | √ | 0 | 红冲单对应蓝票明细id |
| 9 | funitprice | 单价(不含税) | numeric | 23 | 10 | √ | 0.0000000000 | 单价(不含税) |
| 10 | fspecification | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 11 | ftaxratecodeid | 税收分类编码名称 | int8 | 64 |  | √ | 0 | 税收分类编码 er_taxclasscode |
| 12 | fbillsourceid | billsourceid | varchar | 50 |  | √ | ' ' | billsourceid |
| 13 | fissuednum | 已开数量 | numeric | 23 | 10 | √ | 0 | 已开数量 |
| 14 | fextrafield3 | 明细扩展字段3 | varchar | 150 |  | √ | ' ' | 明细扩展字段3 |
| 15 | fextrafield2 | 明细扩展字段2 | varchar | 150 |  | √ | ' ' | 明细扩展字段2 |
| 16 | fgoodstype | fgoodstype | int8 | 64 |  | √ | 0 |  |
| 17 | fextrafield5 | 明细扩展字段5 | varchar | 150 |  | √ | ' ' | 明细扩展字段5 |
| 18 | fspbm | 商品编码 | varchar | 50 |  | √ | ' ' | 商品编码 |
| 19 | fextrafield4 | 明细扩展字段4 | varchar | 150 |  | √ | ' ' | 明细扩展字段4 |
| 20 | fnumdeviation | 数量尾差 | numeric | 23 | 10 | √ | 0 | 数量尾差 |
| 21 | ftaxamount | 金额(含税) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(含税) |
| 22 | fremainvalidnum | 剩余可申请数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余可申请数量 |
| 23 | ffromtaxamount | 原币金额(含税) | numeric | 23 | 10 | √ | 0 | 原币金额(含税) |
| 24 | fdeduction | fdeduction | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 25 | fcustomnameid | fcustomnameid | int8 | 64 |  | √ | 0 |  |
| 26 | famountdeviation | 金额尾差 | numeric | 23 | 10 | √ | 0 | 金额尾差 |
| 27 | fcombinelocalamount | 关联本币金额 | numeric | 23 | 10 | √ | 0 | 关联本币金额 |
| 28 | ftaxdeviation | 税额尾差 | numeric | 23 | 10 | √ | 0.0000000000 | 税额尾差 |
| 29 | foritaxamount | 原始金额(含税) | numeric | 23 | 10 | √ | 0 | 原始金额(含税) |
| 30 | ffromtaxdeviation | 原币税额尾差 | numeric | 23 | 10 | √ | 0 | 原币税额尾差 |
| 31 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 32 | ffromdiscountamount | 原币折扣额 | numeric | 23 | 10 | √ | 0 | 原币折扣额 |
| 33 | fissuedtax | 已开税额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开税额 |
| 34 | ffromtaxprice | 原币单价(含税) | numeric | 23 | 10 | √ | 0 | 原币单价(含税) |
| 35 | ffromissuedtax | 原币已开税额 | numeric | 23 | 10 | √ | 0 | 原币已开税额 |
| 36 | fremainvalidamount | 剩余可申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余可申请金额 |
| 37 | ffromprice | 原币单价(不含税) | numeric | 23 | 10 | √ | 0 | 原币单价(不含税) |
| 38 | fissuedamount | 已开金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开金额 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | funit | 计量单位 | varchar | 50 |  | √ | ' ' | 计量单位 |
| 41 | fextrafield | 明细扩展字段1 | varchar | 200 |  | √ | ' ' | 明细扩展字段1 |
| 42 | fcombineamount | 关联金额 | numeric | 23 | 10 | √ | 0 | 关联金额 |
| 43 | fbenchmark | 基准类型 | varchar | 10 |  | √ | ' ' | 基准类型,枚举: 0 :数量基准 1 :金额基准 |
| 44 | ffromissuedtaxamount | 原币已开价税合计 | numeric | 23 | 10 | √ | 0 | 原币已开价税合计 |
| 45 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 开票项管理 bdm_goods_info |
| 46 | fpolicycontants | 优惠政策内容 | varchar | 200 |  | √ | ' ' | 优惠政策内容 |
| 47 | fdiscountamount | 折扣金额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣金额 |
| 48 | forispecification | 原始规格型号 | varchar | 50 |  | √ | ' ' | 原始规格型号 |
| 49 | fmaterielfield | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 50 | forifromtaxamount | forifromtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 51 | famount | 金额(不含税) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(不含税) |
| 52 | fzeropushflag | 0金额下推标识 | varchar | 30 |  | √ | '0' | 0金额下推标识,枚举: 0 :未下推 1 :已下推 |
| 53 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 54 | ffromtax | 原币税额 | numeric | 23 | 10 | √ | 0 | 原币税额 |
| 55 | fcombinenum | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 56 | fgoodsname | 商品名称 | varchar | 100 |  | √ | ' ' | 商品名称 |
| 57 | fgoodssimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 58 | foriunit | 原始计量单位 | varchar | 50 |  | √ | ' ' | 原始计量单位 |
| 59 | ffromamount | 原币金额(不含税) | numeric | 23 | 10 | √ | 0 | 原币金额(不含税) |
| 60 | forinum | 原始数量 | numeric | 23 | 10 | √ | 0.0000000000 | 原始数量 |
| 61 | fgift | 是否赠品 | varchar | 4 |  | √ | '0' | 是否赠品 |
| 62 | fremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 63 | fitemdeduction | 明细扣除额 | numeric | 23 | 10 | √ | 0 | 明细扣除额 |
| 64 | fsourceinfodetailid | 原红字信息明细id | varchar | 50 |  | √ | ' ' | 原红字信息明细id |
| 65 | fissuedtotaltaxamount | 已开价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 已开价税合计 |
| 66 | fpolicylogo | 是否享受优惠 | varchar | 10 |  | √ | ' ' | 是否享受优惠,枚举: 0 :不享受 1 :享受 |
| 67 | fexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 68 | fmaterialtype | 物料分类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 69 | ftaxunitprice | 单价(含税) | numeric | 23 | 10 | √ | 0.0000000000 | 单价(含税) |
| 70 | fsourceinfocode | 原红字信息表编号 | varchar | 50 |  | √ | ' ' | 原红字信息表编号 |
| 71 | fgoodscode | 税收分类编码 | varchar | 50 |  | √ | ' ' | 税收分类编码 |
| 72 | fmodelnumrate | 单位换算率 | numeric | 23 | 10 | √ | 1 | 单位换算率 |
| 73 | fremainvalidtax | 剩余可申请税额 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余可申请税额 |
| 74 | forigoodsname | 原始商品名称 | varchar | 150 |  | √ | ' ' | 原始商品名称 |
| 75 | fdeductedpk | 被折扣行主键（折扣行存值） | int8 | 64 |  | √ | 0 | 被折扣行主键（折扣行存值） |
| 76 | fgoodsno | fgoodsno | varchar | 50 |  | √ | ' ' |  |
| 77 | foriunitprice | 原始单价 | numeric | 23 | 10 | √ | 0.0000000000 | 原始单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_original_bill_item |  | fentryid |
| 2 | idx_sim_original_bill_item_fk |  | fid |

---

## 关联子实体-子表 t_sim_original_bill_item_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sim_original_bill_item_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fnum | 数量_确认携带值 | numeric | 23 | 10 |  | null | 数量_确认携带值 |
| 2 | ftaxamount | 金额(含税)_确认携带值 | numeric | 23 | 10 |  | null | 金额(含税)_确认携带值 |
| 3 | fnum_old | 数量_原始携带值 | numeric | 23 | 10 |  | null | 数量_原始携带值 |
| 4 | ftaxamount_old | 金额(含税)_原始携带值 | numeric | 23 | 10 |  | null | 金额(含税)_原始携带值 |
| 5 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 6 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 7 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_original_bill_item_lk_fk |  | fentryid |
| 2 | pk_sim_original_bill_item_lk |  | fpkid |

---

## 开票申请单-反写记录表 t_sim_original_bill_wb

- **表名称：** 开票申请单-反写记录表
- **表名：** t_sim_original_bill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_original_bill_wb_fk |  | fid |
| 2 | pk_sim_original_bill_wb |  | fentryid |

---

## 开票申请单-主表 t_sim_original_bill

- **表名称：** 开票申请单-主表
- **表名：** t_sim_original_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuyeraddr | 地址及电话 | varchar | 100 |  | √ | ' ' | 地址及电话 |
| 3 | ftextfield2 | 扩展字段2 | varchar | 150 |  | √ | ' ' | 扩展字段2 |
| 4 | fsuppliercontact | 供应商联系人 | varchar | 50 |  | √ | ' ' | 供应商联系人 |
| 5 | ftextfield1 | 扩展字段1 | varchar | 150 |  | √ | ' ' | 扩展字段1 |
| 6 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 7 | fcontractdate | 合同日期 | timestamp | 0 |  |  | null | 合同日期 |
| 8 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fbilltaxrate | 单据税率 | varchar | 50 |  | √ | ' ' | 单据税率,枚举: 0 :0% 0.01 :1% 0.015 :1.5% 0.03 :3% 0.04 :4% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.16 :16% 0.17 :17% |
| 10 | ftotalamount | 申请价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 申请价税合计 |
| 11 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | ftextfield3 | 扩展字段3 | varchar | 150 |  | √ | ' ' | 扩展字段3 |
| 13 | fforeigntax | 原币税额 | numeric | 23 | 10 | √ | 0 | 原币税额 |
| 14 | fpurchasername | 采购商名称 | varchar | 50 |  | √ | ' ' | 采购商名称 |
| 15 | foldtotalamount | 原始价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 原始价税合计 |
| 16 | fbillremark | 开票说明 | varchar | 90 |  | √ | ' ' | 开票说明 |
| 17 | fsaleraddr | 地址及电话 | varchar | 100 |  | √ | ' ' | 地址及电话 |
| 18 | fbuyername | 购方名称 | varchar | 100 |  | √ | ' ' | 购方名称 |
| 19 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 20 | fbillno | 业务单据编号 | varchar | 50 |  | √ | ' ' | 业务单据编号 |
| 21 | fsalertaxno | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 22 | fbillcontaintax | fbillcontaintax | varchar | 30 |  | √ | ' ' |  |
| 23 | fforeigntaxdifference | 原币税额误差 | numeric | 23 | 10 | √ | 0 | 原币税额误差 |
| 24 | ftaxationstyle | 征税方式 | varchar | 30 |  | √ | ' ' | 征税方式,枚举: 0 :普通征税 2 :差额征税 1 :减按计征 |
| 25 | fbillproperties | 单据性质 | varchar | 30 |  | √ | ' ' | 单据性质,枚举: -1 :负数 1 :正数 |
| 26 | fbuyerphone | 交付手机 | varchar | 50 |  | √ | ' ' | 交付手机 |
| 27 | finvoicetype | 发票种类 | varchar | 30 |  | √ | ' ' | 发票种类,枚举: 026 :电子普通发票 028 :电子专用发票 007 :纸质普通发票 004 :纸质专用发票 025 :增值税普通发票（卷票） 08xdp :全电发票（增值税专用发票） 10xdp :全电发票（普通发票） |
| 28 | fbuyerbank | 开户行及账号 | varchar | 100 |  | √ | ' ' | 开户行及账号 |
| 29 | fsalername | 销方名称 | varchar | 100 |  | √ | ' ' | 销方名称 |
| 30 | fbuyeremail | 交付邮箱 | varchar | 100 |  | √ | ' ' | 交付邮箱 |
| 31 | finvoiceremark | 发票备注 | varchar | 255 |  | √ | ' ' | 发票备注 |
| 32 | fterminalno | 终端号 | varchar | 50 |  | √ | ' ' | 终端号,枚举: |
| 33 | fconfirmamount | 已申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已申请金额 |
| 34 | fpayee | 收款人 | varchar | 50 |  | √ | ' ' | 收款人 |
| 35 | fmergerule | 合并规则 | int8 | 64 |  | √ | 0 | 合并配置 bdm_merge_rule |
| 36 | fpriority | 优先级 | varchar | 30 |  | √ | ' ' | 优先级,枚举: 0 :正常 1 :加急 |
| 37 | fhsbz | 是否含税 | varchar | 50 |  | √ | ' ' | 是否含税,枚举: 0 :不含税 1 :含税 |
| 38 | fforeignissuedamount | 原币已开不含税金额 | numeric | 23 | 10 | √ | 0 | 原币已开不含税金额 |
| 39 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 40 | fpurchasercontact | 采购商联系人 | varchar | 50 |  | √ | ' ' | 采购商联系人 |
| 41 | ftotaltax | 申请税额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请税额 |
| 42 | fquotation | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 43 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | freviewer | 复核人 | varchar | 50 |  | √ | ' ' | 复核人 |
| 45 | ffromcurr | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 46 | fbuyertaxno | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 47 | fsalerbank | 开户行及账号 | varchar | 100 |  | √ | ' ' | 开户行及账号 |
| 48 | fforeignissuedtotalamount | 原币已开价税合计 | numeric | 23 | 10 | √ | 0 | 原币已开价税合计 |
| 49 | fsplit | 是否拆分 | varchar | 30 |  | √ | ' ' | 是否拆分,枚举: 0 :已拆 1 :未拆 |
| 50 | fpurchaserphone | 采购商电话 | varchar | 50 |  | √ | ' ' | 采购商电话 |
| 51 | fconfirmstate | 申请状态 | varchar | 30 |  | √ | ' ' | 申请状态,枚举: 0 :未申请 1 :部分申请 2 :已申请 |
| 52 | fsuppliername | 供应商名称 | varchar | 50 |  | √ | ' ' | 供应商名称 |
| 53 | fcontractamount | 合同金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合同金额 |
| 54 | fforeigninvoiceamount | 原币不含税金额 | numeric | 23 | 10 | √ | 0 | 原币不含税金额 |
| 55 | ftocurr | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 56 | fcontractno | 合同编号 | varchar | 50 |  | √ | ' ' | 合同编号 |
| 57 | fforeignissuedtax | 原币已开税额 | numeric | 23 | 10 | √ | 0 | 原币已开税额 |
| 58 | fsupplierphone | 供应商电话 | varchar | 50 |  | √ | ' ' | 供应商电话 |
| 59 | fbuyerproperty | 购方企业类型 | varchar | 30 |  | √ | ' ' | 购方企业类型,枚举: 0 :企业 1 :个人 |
| 60 | fforeigntotalamount | 原币价税合计 | numeric | 23 | 10 | √ | 0 | 原币价税合计 |
| 61 | finvoiceamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 62 | fbuyerpersonname | 收票人名称 | varchar | 100 |  | √ | ' ' | 收票人名称 |
| 63 | fsystemsource | 数据来源系统 | varchar | 50 |  | √ | ' ' | 数据来源系统 |
| 64 | fjqbh | 设备编号 | varchar | 50 |  | √ | ' ' | 设备编号,枚举: |
| 65 | fvalidstate | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: 0 :正常 1 :搁置 2 :开票结束 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_original_bill |  | fbillno |
| 2 | pk_sim_original_bill |  | fid |
| 3 | idx_sim_original_bill_org |  | forgid |
