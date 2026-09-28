# 核算成本记录（后台）-cal_costrecord

## 核算成本记录（后台）-多语言表 t_cal_calcostrecord_l

- **表名称：** 核算成本记录（后台）-多语言表
- **表名：** t_cal_calcostrecord_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_calcostrecord_l |  | fid,flocaleid |
| 2 | pk_cal_calcostrecord_l |  | fpkid |

---

## 暂估分摊明细-子表 t_cal_esbilldetailentry

- **表名称：** 暂估分摊明细-子表
- **表名：** t_cal_esbilldetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsharedetailamt | 本次分摊金额(单据) | numeric | 23 | 10 | √ | 0.0000000000 | 本次分摊金额(单据) |
| 2 | fexitemseq | 费用项目序号 | int8 | 64 |  | √ | 0 | 费用项目序号 |
| 3 | fsharedetailamount | 本次分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次分摊金额 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsharedetailatype | 往来类型 | varchar | 30 |  | √ | 'bd_supplier' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | festimatebillid | 费用暂估单id | int8 | 64 |  | √ | 0 | 费用暂估单id |
| 8 | fsharedetailasstactid | 往来户 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fsharedetailexitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_esbillde_cre |  | fentryid |
| 2 | t_cal_esbilldetailentry_pkey |  | fdetailid |

---

## 单据体-子表 t_cal_calcostrecordentry

- **表名称：** 单据体-子表
- **表名：** t_cal_calcostrecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 3 | fproductnum | 生产编号 | varchar | 255 |  | √ | ' ' | 生产编号 |
| 4 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位实际成本 |
| 5 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 6 | fqueuetype | 序列类型 | bpchar | 1 |  | √ | '0' | 序列类型,枚举: 0 :入库 1 :出库 |
| 7 | fmainbillentity | 业务单核心单据实体 | varchar | 80 |  | √ | ' ' | 业务单核心单据实体 |
| 8 | fcaldimensionid | 核算维度 | int8 | 64 |  | √ | 0 | 核算维度 cal_bd_caldimension |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 11 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fancestorid | 原单单据id | int8 | 64 |  | √ | 0 | 原单单据id |
| 13 | fsrcbillentryseq | 业务单来源单据分录序号 | int8 | 64 |  | √ | 0 | 业务单来源单据分录序号 |
| 14 | funitresource | 单位人工费用 | numeric | 23 | 10 | √ | 0 | 单位人工费用 |
| 15 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 16 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 17 | fmainbillid | 业务单核心单据ID | int8 | 64 |  | √ | 0 | 业务单核心单据ID |
| 18 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 19 | fgroupseq | 成组行号 | varchar | 100 |  | √ | ' ' | 成组行号 |
| 20 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 21 | fbalancesupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 22 | floctaxamt | 价税合计本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计本位币 |
| 23 | fsrcsysbillno | 来源系统单据编号 | varchar | 100 |  | √ | ' ' | 来源系统单据编号 |
| 24 | funitprocesscost | 单位委外费用 | numeric | 23 | 10 | √ | 0.0000000000 | 单位委外费用 |
| 25 | flot | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 26 | fresource | 人工费用 | numeric | 23 | 10 | √ | 0 | 人工费用 |
| 27 | ftaxamt | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 28 | fassistpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 29 | fsrcbillnumber | 业务单来源单据编号 | varchar | 80 |  | √ | ' ' | 业务单来源单据编号 |
| 30 | fwriteoffid | 勾稽记录ID | int8 | 64 |  | √ | 0 | 勾稽记录ID |
| 31 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 32 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 33 | fsrcbillid | 业务单来源单据ID | int8 | 64 |  | √ | 0 | 业务单来源单据ID |
| 34 | fmainbillnumber | 业务单核心单据编号 | varchar | 80 |  | √ | ' ' | 业务单核心单据编号 |
| 35 | ftotalsharefee | 累计分摊费用 | numeric | 23 | 10 | √ | 0.0000000000 | 累计分摊费用 |
| 36 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 37 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 38 | fbalancecustomerid | 结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 39 | fadjustamount | 调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整金额 |
| 40 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 42 | fecalstatus | 分录核算处理状态 | bpchar | 1 |  | √ | 'A' | 分录核算处理状态,枚举: A :成功 B :失败 C :处理中 |
| 43 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 44 | fcostdomainkey | 成本域维度 | varchar | 50 |  | √ | ' ' | 成本域维度 |
| 45 | fcostsource | 成本来源 | varchar | 30 |  | √ | ' ' | 成本来源,枚举: 31 :入库成本汇总维护 32 :出库成本汇总维护 33 :入库成本维护 34 :出库成本维护 35 :其他存货核算 351 :其他存货核算（权重和费用） 36 :委外入库成本维护 |
| 46 | fsignnum | 数值方向 | int4 | 32 |  | √ | 1 | 数值方向 |
| 47 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 48 | fproductid | 产品 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 49 | faccounttype | 计价方法 | varchar | 5 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 G :先进先出法 C :即时移动平均法 E :即时先进先出法 D :标准成本法 |
| 50 | fstandardcost | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 51 | fcostupdatedate | 成本更新时间 | timestamp | 0 |  |  | null | 成本更新时间 |
| 52 | funitmaterialcost | 单位材料成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位材料成本 |
| 53 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 54 | fiscalculated | 是否已参与出库核算 | bpchar | 1 |  | √ | '0' | 是否已参与出库核算 |
| 55 | fmainbillentryseq | 业务单核心单据分录序号 | int8 | 64 |  | √ | 0 | 业务单核心单据分录序号 |
| 56 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 57 | fentrystatus | 分录状态 | bpchar | 1 |  | √ | 'C' | 分录状态,枚举: A :暂存 B :已提交 C :已审核 |
| 58 | fisallocate | 是否分摊 | bpchar | 1 |  | √ | '0' | 是否分摊 |
| 59 | ffatherentryid | 父分录id | int8 | 64 |  | √ | 0 | 父分录id |
| 60 | fgroupnumber | 成组号 | varchar | 100 |  | √ | ' ' | 成组号 |
| 61 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 62 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 63 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | 核算范围 cal_bd_calrange |
| 64 | ffee | 采购成本 | numeric | 23 | 10 | √ | 0.0000000000 | 采购成本 |
| 65 | flocaltax | 税额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 税额本位币 |
| 66 | funitmanufacturecost | 单位制造费用 | numeric | 23 | 10 | √ | 0 | 单位制造费用 |
| 67 | fprojecttaskid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 68 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 69 | fsrcbillentity | 业务单来源单据实体 | varchar | 80 |  | √ | ' ' | 业务单来源单据实体 |
| 70 | fisspanorg | 是否跨核算组织 | bpchar | 1 |  | √ | '0' | 是否跨核算组织 |
| 71 | fancestorentryid | 原单分录id | int8 | 64 |  | √ | 0 | 原单分录id |
| 72 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 73 | fcostsrc | fcostsrc | bpchar | 1 |  |  | ' ' |  |
| 74 | fislastentry | 是否全部结转 | bpchar | 1 |  | √ | '0' | 是否全部结转 |
| 75 | fmanufacturecost | 制造费用 | numeric | 23 | 10 | √ | 0 | 制造费用 |
| 76 | fproducttype | 产品类别 | varchar | 50 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 77 | fsrcbillentryid | 业务单来源单据行ID | int8 | 64 |  | √ | 0 | 业务单来源单据行ID |
| 78 | ffatherbillid | 父单据id | int8 | 64 |  | √ | 0 | 父单据id |
| 79 | fcalentryid | 核算单分录ID | int8 | 64 |  | √ | 0 | 核算单分录ID |
| 80 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 81 | fmainbillentryid | 业务单核心单据行ID | int8 | 64 |  | √ | 0 | 业务单核心单据行ID |
| 82 | fprocesscost | 委外费用 | numeric | 23 | 10 | √ | 0.0000000000 | 委外费用 |
| 83 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 84 | fmaterialcost | 材料成本 | numeric | 23 | 10 | √ | 0.0000000000 | 材料成本 |
| 85 | fbizbillentryid | 业务单据分录ID | int8 | 64 |  | √ | 0 | 业务单据分录ID |
| 86 | funitstandardcost | 单位标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位标准成本 |
| 87 | funitfee | 单位采购成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位采购成本 |
| 88 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

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

---

## 核算成本记录（后台）-主表 t_cal_calcostrecord

- **表名称：** 核算成本记录（后台）-主表
- **表名：** t_cal_calcostrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouchertype | 凭证类型 | varchar | 5 |  | √ | ' ' | 凭证类型,枚举: A :正式凭证 B :暂估凭证 C :冲回凭证 |
| 3 | fwriteoffdate | 勾稽日期 | timestamp | 0 |  |  | null | 勾稽日期 |
| 4 | fbizentityobjectid | 业务对象 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fcarryovervouchernum | 结转凭证号 | varchar | 80 |  | √ | ' ' | 结转凭证号 |
| 6 | ffivoucherid | 正式凭证id | int8 | 64 |  | √ | 0 | 正式凭证id |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 10 | flocalcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 11 | fbizdirection | 业务方向 | varchar | 5 |  | √ | ' ' | 业务方向,枚举: A :正向 B :反向 |
| 12 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 13 | fistempvoucher | 是否生成暂估凭证 | bpchar | 1 |  | √ | '0' | 是否生成暂估凭证 |
| 14 | ffeevoucherid | 费用凭证id | int8 | 64 |  | √ | 0 | 费用凭证id |
| 15 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 16 | fiscostcarryover | 是否生成成本结转凭证 | bpchar | 1 |  | √ | '0' | 是否生成成本结转凭证 |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fwriteoffperiodid | 勾稽期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 19 | fwriteofftype | 勾稽类型 | varchar | 5 |  | √ | ' ' | 勾稽类型,枚举: A :红蓝核销 B :发票核销 C :费用分摊 |
| 20 | fisfivoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 21 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 22 | fwriteoffendperiodid | 勾稽完成期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 23 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 24 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fissubbillinvoiceverify | 子单已发票勾稽 | bpchar | 1 |  | √ | '0' | 子单已发票勾稽 |
| 26 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 27 | fdischargevoucherid | 冲回凭证id | int8 | 64 |  | √ | 0 | 冲回凭证id |
| 28 | fcarryovervoucherid | 结转凭证id | int8 | 64 |  | √ | 0 | 结转凭证id |
| 29 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 30 | fisinnervirtualbill | fisinnervirtualbill | bpchar | 1 |  | √ | '0' |  |
| 31 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 32 | finvorgid | 对方公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fbillnumber | 业务单据编号 | varchar | 50 |  | √ | ' ' | 业务单据编号 |
| 34 | fcostcenterorgid | 成本中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fdischargevouchernum | 冲回凭证号 | varchar | 80 |  | √ | ' ' | 冲回凭证号 |
| 36 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 37 | fcostsource | fcostsource | varchar | 30 |  | √ | ' ' |  |
| 38 | ftranstype | 调拨类型 | varchar | 5 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 39 | fcostupdatedate | fcostupdatedate | timestamp | 0 |  |  | null |  |
| 40 | fisfeeallocate | 已采购费用分摊 | bpchar | 1 |  | √ | '0' | 已采购费用分摊 |
| 41 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 42 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 45 | fissplitcreate | 是否拆单生成 | bpchar | 1 |  | √ | '0' | 是否拆单生成 |
| 46 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 47 | fwriteoffstatus | 勾稽状态 | varchar | 5 |  | √ | ' ' | 勾稽状态,枚举: A :已核销 B :未核销 |
| 48 | fprofitcenterorgid | 利润中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 49 | finnerbilltype | 内部交易单据类别 | varchar | 30 |  | √ | ' ' | 内部交易单据类别,枚举: in :对内 out :对外 |
| 50 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 51 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 52 | fcostupdatetime | 成本更新时间 | timestamp | 0 |  |  | null | 成本更新时间 |
| 53 | ftempvouchernum | 暂估凭证号 | varchar | 80 |  | √ | ' ' | 暂估凭证号 |
| 54 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 55 | fstorageorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 56 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 57 | ftempvoucherid | 暂估凭证id | int8 | 64 |  | √ | 0 | 暂估凭证id |
| 58 | fisdischargevoucher | 是否生成冲回凭证 | bpchar | 1 |  | √ | '0' | 是否生成冲回凭证 |
| 59 | fcalstatus | 核算处理状态 | bpchar | 1 |  | √ | 'A' | 核算处理状态,枚举: A :成功 B :失败 C :处理中 |
| 60 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 61 | ffeevouchernum | 费用凭证号 | varchar | 80 |  | √ | ' ' | 费用凭证号 |
| 62 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 63 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 64 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 65 | fissplit | 是否被拆单 | bpchar | 1 |  | √ | '0' | 是否被拆单 |
| 66 | fcalbillid | 核算单ID | int8 | 64 |  | √ | 0 | 核算单ID |
| 67 | fcalbilltype | 核算单类型 | varchar | 5 |  | √ | ' ' | 核算单类型,枚举: OUT :出库 IN :入库 |
| 68 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 69 | fdischargetype | 冲回方式 | varchar | 5 |  | √ | ' ' | 冲回方式,枚举: A :单到冲回 B :月初一次冲回 C :差额调整 |
| 70 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 71 | frevconfirmnode | 收入确认时点 | varchar | 30 |  | √ | ' ' | 收入确认时点,枚举: signIn :签收 saleOut :出库 |
| 72 | fadminorgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 73 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 74 | fisfeevoucher | 是否生成费用凭证 | bpchar | 1 |  | √ | '0' | 是否生成费用凭证 |
| 75 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 76 | fcurrencyid | 交易币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 77 | ffivouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_calcostrecord_pkey |  | fid |
| 2 | idx_cal_calrecord_billno |  | fbillno |
| 3 | idx_cal_calrecord_org |  | fcalorgid |
| 4 | idx_cal_calrecord_pc |  | fperiodid,fcostaccountid |
| 5 | idx_cal_costrecord_supplierid |  | fsupplierid |
| 6 | idx_cal_calrecord_bizet |  | fbizentityobjectid |
| 7 | idx_cal_costrecord_customerid |  | fcustomerid |
| 8 | idx_cal_calrecord_bizbillid |  | fbizbillid |
| 9 | idx_cal_calcostrecord_calbillid |  | fcalbillid |
| 10 | idx_cal_calrecord_cb |  | fcostaccountid,fbookdate,fcalorgid,fbizentityobjectid |
| 11 | idx_cal_calrecord_billnum |  | fbillnumber |
| 12 | idx_cal_calrecord_bizdate |  | fbizdate |
| 13 | idx_cal_calrecord_bkd |  | fbookdate |

---

## 费用分摊明细-子表 t_cal_sharedetailentry

- **表名称：** 费用分摊明细-子表
- **表名：** t_cal_sharedetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 2 | fsharercdid | 费用分摊记录id | int8 | 64 |  | √ | 0 | 费用分摊记录id |
| 3 | fasstactid | 往来户 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fasstacttype | 往来类型 | varchar | 30 |  | √ | 'bd_supplier' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 |
| 6 | fshareamount | 分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 分摊金额 |
| 7 | ffeeupdatetype | 费用更新成本类型 | varchar | 30 |  | √ | ' ' | 费用更新成本类型,枚举: A :核算成本记录 B :成本调整单 |
| 8 | fcostrecordid | fcostrecordid | int8 | 64 |  | √ | 0 |  |
| 9 | frealshareamount | frealshareamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | fcostaccountid | fcostaccountid | int8 | 64 |  | √ | 0 |  |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | fcurrencyid | 分摊明细币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_sharedetailentry_pkey |  | fdetailid |
| 2 | idx_cal_sharede_cre |  | fentryid |
