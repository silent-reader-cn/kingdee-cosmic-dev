# 核算成本记录明细-cal_costdetail

## 核算成本记录明细-主表 t_cal_calcostrecordentry

- **表名称：** 核算成本记录明细-主表
- **表名：** t_cal_calcostrecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 所属成本记录 | int8 | 64 |  | √ | 0 | 核算成本记录表头 cal_costrecordhead |
| 2 | fsrcsystem | fsrcsystem | varchar | 100 |  | √ | ' ' |  |
| 3 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位实际成本 |
| 4 | fcaldimensionid | fcaldimensionid | int8 | 64 |  | √ | 0 |  |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fancestorid | fancestorid | int8 | 64 |  | √ | 0 |  |
| 7 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 8 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 9 | fbalancesupplierid | fbalancesupplierid | int8 | 64 |  | √ | 0 |  |
| 10 | fsrcsysbillno | fsrcsysbillno | varchar | 100 |  | √ | ' ' |  |
| 11 | flot | 批次 | varchar | 255 |  | √ | ' ' | 批次 |
| 12 | ftaxamt | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 13 | fassistpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fsrcbillnumber | fsrcbillnumber | varchar | 80 |  | √ | ' ' |  |
| 15 | fwriteoffid | 核销记录ID | int8 | 64 |  | √ | 0 | 核销记录ID |
| 16 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 17 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 18 | fmainbillnumber | fmainbillnumber | varchar | 80 |  | √ | ' ' |  |
| 19 | ftotalsharefee | 累计分摊费用 | numeric | 23 | 10 | √ | 0.0000000000 | 累计分摊费用 |
| 20 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 21 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 22 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fsrcsysbillentryid | fsrcsysbillentryid | varchar | 100 |  | √ | ' ' |  |
| 24 | fstepamtww | 本阶金额（委外） | numeric | 23 | 10 | √ | 0 | 本阶金额（委外） |
| 25 | fcostsource | fcostsource | varchar | 30 |  | √ | ' ' |  |
| 26 | fproductid | fproductid | int8 | 64 |  | √ | 0 |  |
| 27 | fisintransit | fisintransit | bpchar | 1 |  | √ | '0' |  |
| 28 | fstandardcost | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 29 | fsuitesettletype | fsuitesettletype | varchar | 50 |  | √ | ' ' |  |
| 30 | fentryid | 交易币别(模型冗余) | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fiscalculated | fiscalculated | bpchar | 1 |  | √ | '0' |  |
| 32 | freceiveprojectid | freceiveprojectid | int8 | 64 |  | √ | 0 |  |
| 33 | fmainbillentryseq | fmainbillentryseq | int8 | 64 |  | √ | 0 |  |
| 34 | fisallocate | fisallocate | bpchar | 1 |  | √ | '0' |  |
| 35 | ffatherentryid | ffatherentryid | int8 | 64 |  | √ | 0 |  |
| 36 | fgroupnumber | fgroupnumber | varchar | 100 |  | √ | ' ' |  |
| 37 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 38 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 39 | ffee | 采购成本 | numeric | 23 | 10 | √ | 0.0000000000 | 采购成本 |
| 40 | flocaltax | 税额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 税额本位币 |
| 41 | funitmanufacturecost | 单位制造费用 | numeric | 23 | 10 | √ | 0 | 单位制造费用 |
| 42 | fprojecttaskid | fprojecttaskid | int8 | 64 |  | √ | 0 |  |
| 43 | fdividebasisvalue | fdividebasisvalue | varchar | 500 |  | √ | ' ' |  |
| 44 | fsrcbillentity | fsrcbillentity | varchar | 80 |  | √ | ' ' |  |
| 45 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 46 | fcostsrc | fcostsrc | bpchar | 1 |  |  | ' ' |  |
| 47 | fislastentry | fislastentry | bpchar | 1 |  | √ | '0' |  |
| 48 | fproducttype | fproducttype | varchar | 50 |  | √ | ' ' |  |
| 49 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 50 | ffatherbillid | ffatherbillid | int8 | 64 |  | √ | 0 |  |
| 51 | flocationid | 库位 | int8 | 64 |  | √ | 0 | [库位 pur_location](../pbd_files/pur_location.md) |
| 52 | fprocesscost | 委外费用 | numeric | 23 | 10 | √ | 0.0000000000 | 委外费用 |
| 53 | fbizbillentryid | 业务单据分录ID | int8 | 64 |  | √ | 0 | 业务单据分录ID |
| 54 | fsrcsysbillid | fsrcsysbillid | varchar | 100 |  | √ | ' ' |  |
| 55 | fproductnum | fproductnum | varchar | 255 |  | √ | ' ' |  |
| 56 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 57 | fdevtrial | fdevtrial | bpchar | 1 |  | √ | '0' |  |
| 58 | fqueuetype | fqueuetype | bpchar | 1 |  | √ | '0' |  |
| 59 | fmainbillentity | fmainbillentity | varchar | 80 |  | √ | ' ' |  |
| 60 | fmversionid | fmversionid | int8 | 64 |  | √ | 0 |  |
| 61 | fbaseunit | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 62 | fsrcbillentryseq | fsrcbillentryseq | int8 | 64 |  | √ | 0 |  |
| 63 | funitresource | 单位人工费用 | numeric | 23 | 10 | √ | 0 | 单位人工费用 |
| 64 | fisrework | fisrework | bpchar | 1 |  | √ | '0' |  |
| 65 | fkitsettleway | fkitsettleway | varchar | 50 |  | √ | ' ' |  |
| 66 | fmainbillid | fmainbillid | int8 | 64 |  | √ | 0 |  |
| 67 | fdevcost | fdevcost | varchar | 10 |  | √ | '0' |  |
| 68 | fgroupseq | fgroupseq | varchar | 100 |  | √ | ' ' |  |
| 69 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 70 | floctaxamt | 价税合计本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计本位币 |
| 71 | funitprocesscost | 单位委外费用 | numeric | 23 | 10 | √ | 0.0000000000 | 单位委外费用 |
| 72 | fresource | 人工费用 | numeric | 23 | 10 | √ | 0 | 人工费用 |
| 73 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 74 | flicensenoid | flicensenoid | int8 | 64 |  | √ | 0 |  |
| 75 | froaddamageqty | froaddamageqty | numeric | 23 | 10 | √ | 0 |  |
| 76 | fbalancecustomerid | fbalancecustomerid | int8 | 64 |  | √ | 0 |  |
| 77 | fadjustamount | 调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整金额 |
| 78 | fecalstatus | fecalstatus | bpchar | 1 |  | √ | 'A' |  |
| 79 | fparentrowid | fparentrowid | int8 | 64 |  | √ | 0 |  |
| 80 | fcaldimensionvalue | fcaldimensionvalue | varchar | 100 |  | √ | ' ' |  |
| 81 | fcostdomainkey | fcostdomainkey | varchar | 50 |  | √ | ' ' |  |
| 82 | fsignnum | fsignnum | int4 | 32 |  | √ | 1 |  |
| 83 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 84 | fsuitegroupid | fsuitegroupid | int8 | 64 |  | √ | 0 |  |
| 85 | faccounttype | 计价方法 | varchar | 5 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 F :个别计价法 G :先进先出法 |
| 86 | fcostupdatedate | fcostupdatedate | timestamp | 0 |  |  | null |  |
| 87 | funitmaterialcost | 单位材料成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位材料成本 |
| 88 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 89 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | 'C' |  |
| 90 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | [核算范围 cal_bd_calrange](../cal_files/cal_bd_calrange.md) |
| 91 | fbonded | fbonded | bpchar | 1 |  | √ | '0' |  |
| 92 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 93 | fisspanorg | fisspanorg | bpchar | 1 |  | √ | '0' |  |
| 94 | fancestorentryid | fancestorentryid | int8 | 64 |  | √ | 0 |  |
| 95 | fmanufacturecost | 制造费用 | numeric | 23 | 10 | √ | 0 | 制造费用 |
| 96 | fcalentryid | 核算单分录ID | int8 | 64 |  | √ | 0 | 核算单分录ID |
| 97 | fmainbillentryid | fmainbillentryid | int8 | 64 |  | √ | 0 |  |
| 98 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 99 | fmaterialcost | 材料成本 | numeric | 23 | 10 | √ | 0.0000000000 | 材料成本 |
| 100 | funitstandardcost | 单位标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位标准成本 |
| 101 | funitfee | 单位采购成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位采购成本 |

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
