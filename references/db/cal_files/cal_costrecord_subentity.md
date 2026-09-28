# 核算成本记录-cal_costrecord_subentity

## 成本要素明细-子表 t_cal_costrecord_detail

- **表名称：** 成本要素明细-子表
- **表名：** t_cal_costrecord_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位实际成本 |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fstepamt | fstepamt | numeric | 23 | 10 | √ | 0 |  |
| 6 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 7 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 8 | fstandardcost | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fbaseunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 13 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | funitstandardcost | 单位标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位标准成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costrecord_detail_pkey |  | fdetailid |
| 2 | idx_cal_crddetail_elementid |  | fcostelementid |
| 3 | idx_cal_costrecord_detail_sub |  | fentryid,fcostsubelementid |
| 4 | idx_cal_crddetail_entryid |  | fentryid,fdetailid,fstandardcost,factualcost |
| 5 | idx_cal_crddetail_subelementid |  | fcostsubelementid |

---

## 核算成本记录-多语言表 t_cal_calcostrecord_l

- **表名称：** 核算成本记录-多语言表
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
| 10 | fsharedetailexitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |

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
| 3 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位实际成本 |
| 4 | fcaldimensionid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 cal_bd_caldimension](../cal_files/cal_bd_caldimension.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fancestorid | 原单单据id | int8 | 64 |  | √ | 0 | 原单单据id |
| 7 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 8 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 9 | fbalancesupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 10 | fsrcsysbillno | 来源系统单据编号 | varchar | 100 |  | √ | ' ' | 来源系统单据编号 |
| 11 | flot | 批号 | varchar | 255 |  | √ | ' ' | 批号 |
| 12 | ftaxamt | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 13 | fassistpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fsrcbillnumber | 业务单来源单据编号 | varchar | 80 |  | √ | ' ' | 业务单来源单据编号 |
| 15 | fwriteoffid | 勾稽记录ID | int8 | 64 |  | √ | 0 | 勾稽记录ID |
| 16 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 17 | fsrcbillid | 业务单来源单据ID | int8 | 64 |  | √ | 0 | 业务单来源单据ID |
| 18 | fmainbillnumber | 业务单核心单据编号 | varchar | 80 |  | √ | ' ' | 业务单核心单据编号 |
| 19 | ftotalsharefee | 累计分摊费用 | numeric | 23 | 10 | √ | 0.0000000000 | 累计分摊费用 |
| 20 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 21 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 22 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 24 | fstepamtww | 本阶金额（委外） | numeric | 23 | 10 | √ | 0 | 本阶金额（委外） |
| 25 | fcostsource | 成本来源 | varchar | 30 |  | √ | ' ' | 成本来源,枚举: 2 :出库核算 31 :入库成本汇总维护 32 :出库成本汇总维护 33 :入库成本维护 34 :出库成本维护 35 :其他存货核算 351 :其他存货核算（权重和费用） 36 :委外入库成本维护 37 :零成本批量维护 4 :勾稽与费用分摊 7 :返工取价 8 :实际成本核算 A :成本记录创建 B :应付结算清单 352 :其他存货核算（成本计算） |
| 26 | fproductid | 产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 27 | fisintransit | 启用在途 | bpchar | 1 |  | √ | '0' | 启用在途 |
| 28 | fstandardcost | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 29 | fsuitesettletype | 套件结算方式 | varchar | 50 |  | √ | ' ' | 套件结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fiscalculated | 是否已参与出库核算 | bpchar | 1 |  | √ | '0' | 是否已参与出库核算 |
| 32 | freceiveprojectid | 需求项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 33 | fmainbillentryseq | 业务单核心单据分录序号 | int8 | 64 |  | √ | 0 | 业务单核心单据分录序号 |
| 34 | fisallocate | 是否分摊 | bpchar | 1 |  | √ | '0' | 是否分摊 |
| 35 | ffatherentryid | 父分录id | int8 | 64 |  | √ | 0 | 父分录id |
| 36 | fgroupnumber | 成组号 | varchar | 100 |  | √ | ' ' | 成组号 |
| 37 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 38 | faudittime | 审核时间（废弃） | timestamp | 0 |  |  | null | 审核时间（废弃） |
| 39 | ffee | 采购成本 | numeric | 23 | 10 | √ | 0.0000000000 | 采购成本 |
| 40 | flocaltax | 税额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 税额本位币 |
| 41 | funitmanufacturecost | 单位制造费用 | numeric | 23 | 10 | √ | 0 | 单位制造费用 |
| 42 | fprojecttaskid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 43 | fdividebasisvalue | 划分依据值 | varchar | 500 |  | √ | ' ' | 划分依据值 |
| 44 | fsrcbillentity | 业务单来源单据实体 | varchar | 80 |  | √ | ' ' | 业务单来源单据实体 |
| 45 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 46 | fcostsrc | fcostsrc | bpchar | 1 |  |  | ' ' |  |
| 47 | fislastentry | 是否全部结转 | bpchar | 1 |  | √ | '0' | 是否全部结转 |
| 48 | fproducttype | 产品类别 | varchar | 50 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 49 | fsrcbillentryid | 业务单来源单据行ID | int8 | 64 |  | √ | 0 | 业务单来源单据行ID |
| 50 | ffatherbillid | 父单据id | int8 | 64 |  | √ | 0 | 父单据id |
| 51 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 52 | fprocesscost | 委外费用 | numeric | 23 | 10 | √ | 0.0000000000 | 委外费用 |
| 53 | fbizbillentryid | 业务单据分录ID | int8 | 64 |  | √ | 0 | 业务单据分录ID |
| 54 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |
| 55 | fproductnum | 生产编号 | varchar | 255 |  | √ | ' ' | 生产编号 |
| 56 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 57 | fdevtrial | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 58 | fqueuetype | 序列类型 | bpchar | 1 |  | √ | '0' | 序列类型,枚举: 0 :入库 1 :出库 |
| 59 | fmainbillentity | 业务单核心单据实体 | varchar | 80 |  | √ | ' ' | 业务单核心单据实体 |
| 60 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 61 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 62 | fsrcbillentryseq | 业务单来源单据分录序号 | int8 | 64 |  | √ | 0 | 业务单来源单据分录序号 |
| 63 | funitresource | 单位人工费用 | numeric | 23 | 10 | √ | 0 | 单位人工费用 |
| 64 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 65 | fkitsettleway | 套件内部结算方式 | varchar | 50 |  | √ | ' ' | 套件内部结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 66 | fmainbillid | 业务单核心单据ID | int8 | 64 |  | √ | 0 | 业务单核心单据ID |
| 67 | fdevcost | 研发费用 | varchar | 10 |  | √ | '0' | 研发费用,枚举: 1 :是 0 :否 |
| 68 | fgroupseq | 成组行号 | varchar | 100 |  | √ | ' ' | 成组行号 |
| 69 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 70 | floctaxamt | 价税合计本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计本位币 |
| 71 | funitprocesscost | 单位委外费用 | numeric | 23 | 10 | √ | 0.0000000000 | 单位委外费用 |
| 72 | fresource | 人工费用 | numeric | 23 | 10 | √ | 0 | 人工费用 |
| 73 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 74 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 75 | froaddamageqty | 途损数量 | numeric | 23 | 10 | √ | 0 | 途损数量 |
| 76 | fbalancecustomerid | 结算客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 77 | fadjustamount | 调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整金额 |
| 78 | fecalstatus | 分录核算处理状态 | bpchar | 1 |  | √ | 'A' | 分录核算处理状态,枚举: A :成功 B :失败 C :处理中 |
| 79 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 80 | fcaldimensionvalue | 核算维度值 | varchar | 100 |  | √ | ' ' | 核算维度值 |
| 81 | fcostdomainkey | 成本域维度 | varchar | 50 |  | √ | ' ' | 成本域维度 |
| 82 | fsignnum | 数值方向 | int4 | 32 |  | √ | 1 | 数值方向 |
| 83 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 84 | fsuitegroupid | 套件分组号 | int8 | 64 |  | √ | 0 | 套件分组号 |
| 85 | faccounttype | 计价方法 | varchar | 5 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 G :先进先出法 C :即时移动平均法 E :即时先进先出法 D :标准成本法 |
| 86 | fcostupdatedate | 成本更新时间 | timestamp | 0 |  |  | null | 成本更新时间 |
| 87 | funitmaterialcost | 单位材料成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位材料成本 |
| 88 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 89 | fentrystatus | 分录状态 | bpchar | 1 |  | √ | 'C' | 分录状态,枚举: A :暂存 B :已提交 C :已审核 |
| 90 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | [核算范围 cal_bd_calrange](../cal_files/cal_bd_calrange.md) |
| 91 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 92 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 93 | fisspanorg | 是否跨核算组织 | bpchar | 1 |  | √ | '0' | 是否跨核算组织 |
| 94 | fancestorentryid | 原单分录id | int8 | 64 |  | √ | 0 | 原单分录id |
| 95 | fmanufacturecost | 制造费用 | numeric | 23 | 10 | √ | 0 | 制造费用 |
| 96 | fcalentryid | 核算单分录ID | int8 | 64 |  | √ | 0 | 核算单分录ID |
| 97 | fmainbillentryid | 业务单核心单据行ID | int8 | 64 |  | √ | 0 | 业务单核心单据行ID |
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

---

## 核算成本记录-主表 t_cal_calcostrecord

- **表名称：** 核算成本记录-主表
- **表名：** t_cal_calcostrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouchertype | 凭证类型 | varchar | 5 |  | √ | ' ' | 凭证类型,枚举: A :正式凭证 B :暂估凭证 C :冲回凭证 |
| 3 | fwriteoffdate | 勾稽日期 | timestamp | 0 |  |  | null | 勾稽日期 |
| 4 | fbizentityobjectid | 业务对象 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fcarryovervouchernum | 结转凭证号 | varchar | 80 |  | √ | ' ' | 结转凭证号 |
| 6 | ffivoucherid | 正式凭证id | int8 | 64 |  | √ | 0 | 正式凭证id |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 10 | flocalcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 11 | fbizdirection | 业务方向 | varchar | 5 |  | √ | ' ' | 业务方向,枚举: A :正向 B :反向 |
| 12 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 13 | fistempvoucher | 是否生成暂估凭证 | bpchar | 1 |  | √ | '0' | 是否生成暂估凭证 |
| 14 | ffeevoucherid | 费用凭证id | int8 | 64 |  | √ | 0 | 费用凭证id |
| 15 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 16 | fiscostcarryover | 是否生成成本结转凭证 | bpchar | 1 |  | √ | '0' | 是否生成成本结转凭证 |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fwriteoffperiodid | 勾稽期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 19 | fwriteofftype | 勾稽类型 | varchar | 5 |  | √ | ' ' | 勾稽类型,枚举: A :红蓝核销 B :发票钩稽 C :费用分摊 |
| 20 | fisfivoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 21 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 22 | fwriteoffendperiodid | 勾稽完成期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 23 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 24 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fissubbillinvoiceverify | 子单已发票勾稽 | bpchar | 1 |  | √ | '0' | 子单已发票勾稽 |
| 26 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 27 | froaddamageowner | 途损归属 | varchar | 50 |  | √ | ' ' | 途损归属,枚举: OutOwner :调出货主 InOwner :调入货主 |
| 28 | fdischargevoucherid | 冲回凭证id | int8 | 64 |  | √ | 0 | 冲回凭证id |
| 29 | fcarryovervoucherid | 结转凭证id | int8 | 64 |  | √ | 0 | 结转凭证id |
| 30 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 31 | fisinnervirtualbill | fisinnervirtualbill | bpchar | 1 |  | √ | '0' |  |
| 32 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 33 | finvorgid | 对方公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fbillnumber | 业务单据编号 | varchar | 50 |  | √ | ' ' | 业务单据编号 |
| 35 | fcostcenterorgid | 成本中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | fdischargevouchernum | 冲回凭证号 | varchar | 80 |  | √ | ' ' | 冲回凭证号 |
| 37 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 38 | fcostsource | fcostsource | varchar | 30 |  | √ | ' ' |  |
| 39 | ftranstype | 调拨类型 | varchar | 5 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 40 | fcostupdatedate | fcostupdatedate | timestamp | 0 |  |  | null |  |
| 41 | fisfeeallocate | 已采购费用分摊 | bpchar | 1 |  | √ | '0' | 已采购费用分摊 |
| 42 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 43 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 46 | fissplitcreate | 是否拆单生成 | bpchar | 1 |  | √ | '0' | 是否拆单生成 |
| 47 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 48 | fsettleroutedetailid | 结算路径明细ID | int8 | 64 |  | √ | 0 | 结算路径明细ID |
| 49 | fwriteoffstatus | 勾稽状态 | varchar | 5 |  | √ | ' ' | 勾稽状态,枚举: A :已钩稽 B :未钩稽 |
| 50 | fprofitcenterorgid | 利润中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 51 | finnerbilltype | 内部交易单据类别 | varchar | 30 |  | √ | ' ' | 内部交易单据类别,枚举: in :对内 out :对外 |
| 52 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 53 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 54 | fcostupdatetime | 成本更新时间 | timestamp | 0 |  |  | null | 成本更新时间 |
| 55 | ftempvouchernum | 暂估凭证号 | varchar | 80 |  | √ | ' ' | 暂估凭证号 |
| 56 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 57 | fstorageorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 58 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 59 | ftempvoucherid | 暂估凭证id | int8 | 64 |  | √ | 0 | 暂估凭证id |
| 60 | fisdischargevoucher | 是否生成冲回凭证 | bpchar | 1 |  | √ | '0' | 是否生成冲回凭证 |
| 61 | fcalstatus | 核算处理状态 | bpchar | 1 |  | √ | 'A' | 核算处理状态,枚举: A :成功 B :失败 C :处理中 |
| 62 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 63 | ffeevouchernum | 费用凭证号 | varchar | 80 |  | √ | ' ' | 费用凭证号 |
| 64 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 65 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 66 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 67 | fissplit | 是否被拆单 | bpchar | 1 |  | √ | '0' | 是否被拆单 |
| 68 | fcalbillid | 核算单ID | int8 | 64 |  | √ | 0 | 核算单ID |
| 69 | fcalbilltype | 核算单类型 | varchar | 5 |  | √ | ' ' | 核算单类型,枚举: OUT :出库 IN :入库 |
| 70 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 71 | fdischargetype | 冲回方式 | varchar | 5 |  | √ | ' ' | 冲回方式,枚举: C :差额调整 |
| 72 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 73 | frevconfirmnode | 收入确认时点 | varchar | 30 |  | √ | ' ' | 收入确认时点,枚举: signIn :签收 saleOut :出库 |
| 74 | fadminorgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 75 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 76 | fisfeevoucher | 是否生成费用凭证 | bpchar | 1 |  | √ | '0' | 是否生成费用凭证 |
| 77 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 78 | fcurrencyid | 交易币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 79 | ffivouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |

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
| 1 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
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
| 12 | fcurrencyid | 分摊明细币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
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
