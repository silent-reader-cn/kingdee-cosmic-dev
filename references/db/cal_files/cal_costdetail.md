# 核算成本记录明细-cal_costdetail

## 核算成本记录明细-主表 t_cal_calcostrecordentry

- **表名称：** 核算成本记录明细-主表
- **表名：** t_cal_calcostrecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 所属成本记录 | int8 | 64 |  | √ | 0 | 核算成本记录表头 cal_costrecordhead |
| 2 | fsrcsystem | fsrcsystem | varchar | 100 |  | √ | ' ' |  |
| 3 | fproductnum | fproductnum | varchar | 255 |  | √ | ' ' |  |
| 4 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位实际成本 |
| 5 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 6 | fqueuetype | fqueuetype | bpchar | 1 |  | √ | '0' |  |
| 7 | fmainbillentity | fmainbillentity | varchar | 80 |  | √ | ' ' |  |
| 8 | fcaldimensionid | fcaldimensionid | int8 | 64 |  | √ | 0 |  |
| 9 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 10 | fmversionid | fmversionid | int8 | 64 |  | √ | 0 |  |
| 11 | fbaseunit | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fancestorid | fancestorid | int8 | 64 |  | √ | 0 |  |
| 13 | fsrcbillentryseq | fsrcbillentryseq | int8 | 64 |  | √ | 0 |  |
| 14 | funitresource | 单位人工费用 | numeric | 23 | 10 | √ | 0 | 单位人工费用 |
| 15 | fisrework | fisrework | bpchar | 1 |  | √ | '0' |  |
| 16 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 17 | fmainbillid | fmainbillid | int8 | 64 |  | √ | 0 |  |
| 18 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 19 | fgroupseq | fgroupseq | varchar | 100 |  | √ | ' ' |  |
| 20 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 21 | fbalancesupplierid | fbalancesupplierid | int8 | 64 |  | √ | 0 |  |
| 22 | floctaxamt | 价税合计本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计本位币 |
| 23 | fsrcsysbillno | fsrcsysbillno | varchar | 100 |  | √ | ' ' |  |
| 24 | funitprocesscost | 单位委外费用 | numeric | 23 | 10 | √ | 0.0000000000 | 单位委外费用 |
| 25 | flot | 批次 | varchar | 50 |  | √ | ' ' | 批次 |
| 26 | fresource | 人工费用 | numeric | 23 | 10 | √ | 0 | 人工费用 |
| 27 | ftaxamt | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 28 | fassistpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 29 | fsrcbillnumber | fsrcbillnumber | varchar | 80 |  | √ | ' ' |  |
| 30 | fwriteoffid | 核销记录ID | int8 | 64 |  | √ | 0 | 核销记录ID |
| 31 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 32 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 33 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 34 | fmainbillnumber | fmainbillnumber | varchar | 80 |  | √ | ' ' |  |
| 35 | ftotalsharefee | 累计分摊费用 | numeric | 23 | 10 | √ | 0.0000000000 | 累计分摊费用 |
| 36 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 37 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 38 | fbalancecustomerid | fbalancecustomerid | int8 | 64 |  | √ | 0 |  |
| 39 | fadjustamount | 调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整金额 |
| 40 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fsrcsysbillentryid | fsrcsysbillentryid | varchar | 100 |  | √ | ' ' |  |
| 42 | fecalstatus | fecalstatus | bpchar | 1 |  | √ | 'A' |  |
| 43 | fparentrowid | fparentrowid | int8 | 64 |  | √ | 0 |  |
| 44 | fcostdomainkey | fcostdomainkey | varchar | 50 |  | √ | ' ' |  |
| 45 | fcostsource | fcostsource | varchar | 30 |  | √ | ' ' |  |
| 46 | fsignnum | fsignnum | int4 | 32 |  | √ | 1 |  |
| 47 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 48 | fproductid | fproductid | int8 | 64 |  | √ | 0 |  |
| 49 | faccounttype | 计价方法 | varchar | 5 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 F :个别计价法 G :先进先出法 |
| 50 | fstandardcost | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 51 | fcostupdatedate | fcostupdatedate | timestamp | 0 |  |  | null |  |
| 52 | funitmaterialcost | 单位材料成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位材料成本 |
| 53 | fentryid | 交易币别(模型冗余) | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 54 | fiscalculated | fiscalculated | bpchar | 1 |  | √ | '0' |  |
| 55 | fmainbillentryseq | fmainbillentryseq | int8 | 64 |  | √ | 0 |  |
| 56 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 57 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | 'C' |  |
| 58 | fisallocate | fisallocate | bpchar | 1 |  | √ | '0' |  |
| 59 | ffatherentryid | ffatherentryid | int8 | 64 |  | √ | 0 |  |
| 60 | fgroupnumber | fgroupnumber | varchar | 100 |  | √ | ' ' |  |
| 61 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 62 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 63 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | 核算范围 cal_bd_calrange |
| 64 | ffee | 采购成本 | numeric | 23 | 10 | √ | 0.0000000000 | 采购成本 |
| 65 | flocaltax | 税额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 税额本位币 |
| 66 | funitmanufacturecost | 单位制造费用 | numeric | 23 | 10 | √ | 0 | 单位制造费用 |
| 67 | fprojecttaskid | fprojecttaskid | int8 | 64 |  | √ | 0 |  |
| 68 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 69 | fsrcbillentity | fsrcbillentity | varchar | 80 |  | √ | ' ' |  |
| 70 | fisspanorg | fisspanorg | bpchar | 1 |  | √ | '0' |  |
| 71 | fancestorentryid | fancestorentryid | int8 | 64 |  | √ | 0 |  |
| 72 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 73 | fcostsrc | fcostsrc | bpchar | 1 |  |  | ' ' |  |
| 74 | fislastentry | fislastentry | bpchar | 1 |  | √ | '0' |  |
| 75 | fmanufacturecost | 制造费用 | numeric | 23 | 10 | √ | 0 | 制造费用 |
| 76 | fproducttype | fproducttype | varchar | 50 |  | √ | ' ' |  |
| 77 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 78 | ffatherbillid | ffatherbillid | int8 | 64 |  | √ | 0 |  |
| 79 | fcalentryid | 核算单分录ID | int8 | 64 |  | √ | 0 | 核算单分录ID |
| 80 | flocationid | 库位 | int8 | 64 |  | √ | 0 | 库位 pur_location |
| 81 | fmainbillentryid | fmainbillentryid | int8 | 64 |  | √ | 0 |  |
| 82 | fprocesscost | 委外费用 | numeric | 23 | 10 | √ | 0.0000000000 | 委外费用 |
| 83 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 84 | fmaterialcost | 材料成本 | numeric | 23 | 10 | √ | 0.0000000000 | 材料成本 |
| 85 | fbizbillentryid | 业务单据分录ID | int8 | 64 |  | √ | 0 | 业务单据分录ID |
| 86 | funitstandardcost | 单位标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位标准成本 |
| 87 | funitfee | 单位采购成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位采购成本 |
| 88 | fsrcsysbillid | fsrcsysbillid | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_costrecorde_bizeid |  | fbizbillentryid |
| 2 | idx_cal_calcostrecordentry |  | fid |
| 3 | idx_cal_calrecordet_owner |  | fownerid |
| 4 | t_cal_calcostrecordentry_pkey |  | fentryid |
| 5 | idx_cal_costrecorde_mat |  | fmaterialid |
| 6 | idx_cal_costrecorde_balsupid |  | fbalancesupplierid |
| 7 | idx_cal_costrecorde_caleid |  | fcalentryid |
| 8 | idx_cal_costrecorde_writeid |  | fwriteoffid |
| 9 | idx_cal_calrecordet_wh |  | fwarehouseid,fid |
| 10 | idx_cal_costreea_ancestoreid |  | fancestorentryid |
| 11 | idx_cal_costrecorde_cdkey |  | fcostdomainkey,fid |
| 12 | idx_cal_costreea_ancestorid |  | fancestorid |
| 13 | idx_cal_costrecorde_calrid |  | fcalrangeid |
