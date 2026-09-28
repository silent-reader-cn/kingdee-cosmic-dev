# 差异转出单-sco_costdifftranout

## 物料明细-子表 t_cal_stdcostdiffentry

- **表名称：** 物料明细-子表
- **表名：** t_cal_stdcostdiffentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproductlineid | fproductlineid | int8 | 64 |  | √ | 0 |  |
| 3 | fqueuetype | 序列类型 | varchar | 50 |  | √ | ' ' | 序列类型,枚举: 0 :入库 1 :出库 |
| 4 | finvbillid | 库存单据ID | int8 | 64 |  | √ | 0 | 库存单据ID |
| 5 | fcaldimensionid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 cal_bd_caldimension](../cal_files/cal_bd_caldimension.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 8 | fsubentryentity | subentryentity_json | text | 0 |  |  | null | subentryentity_json |
| 9 | fsrcentryseq | 对方单据行号 | int8 | 64 |  | √ | 0 | 对方单据行号 |
| 10 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 11 | finvbillnum | 库存单据编号 | varchar | 50 |  | √ | ' ' | 库存单据编号 |
| 12 | fcostestimatebillentryid | 被冲回的暂估调价单据分录ID | int8 | 64 |  | √ | 0 | 被冲回的暂估调价单据分录ID |
| 13 | fdevcost | 研发费用 | varchar | 10 |  | √ | '0' | 研发费用,枚举: 1 :是 0 :否 |
| 14 | ffeerecordentryid | 采购费用分摊记录分录ID | int8 | 64 |  | √ | 0 | 采购费用分摊记录分录ID |
| 15 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 16 | fsrcbizentityobject | 对方业务对象 | varchar | 50 |  | √ | ' ' | 对方业务对象 |
| 17 | fwarehsouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 18 | flot | 批号 | varchar | 255 |  | √ | ' ' | 批号 |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | ffeesharetotalamt | 费用分摊累计分摊字段 | numeric | 23 | 10 | √ | 0 | 费用分摊累计分摊字段 |
| 21 | finventryseq | 库存单据行号 | int8 | 64 |  | √ | 0 | 库存单据行号 |
| 22 | fadjustamt | 调整金额 | numeric | 23 | 10 | √ | 0 | 调整金额 |
| 23 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 24 | fstorageorgunitid | 库存组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | finvbizentityobject | 库存业务对象 | varchar | 50 |  | √ | ' ' | 库存业务对象 |
| 26 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 27 | fsrcbillid | 对方单据ID | int8 | 64 |  | √ | 0 | 对方单据ID |
| 28 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 29 | fstocktypename | fstocktypename | varchar | 100 |  | √ | ' ' |  |
| 30 | finvauditdate | 落库审核日期 | timestamp | 0 |  |  | null | 落库审核日期 |
| 31 | fcostestimatebillid | 被冲回的暂估重估单据ID | int8 | 64 |  | √ | 0 | 被冲回的暂估重估单据ID |
| 32 | finvbizdate | 落库记账日期 | timestamp | 0 |  |  | null | 落库记账日期 |
| 33 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fecalstatus | 核算处理状态 | varchar | 50 |  | √ | ' ' | 核算处理状态,枚举: A :成功 B :失败 C :处理中 |
| 35 | ffeerecordid | 采购费用分摊记录ID | int8 | 64 |  | √ | 0 | 采购费用分摊记录ID |
| 36 | fcostdomainkey | 成本域维度 | varchar | 50 |  | √ | ' ' | 成本域维度 |
| 37 | fsignnum | 数值方向 | int8 | 64 |  | √ | 0 | 数值方向 |
| 38 | ftranstype | 调拨类型 | varchar | 50 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 39 | fhooklogid | 入库勾稽日志ID | int8 | 64 |  | √ | 0 | 入库勾稽日志ID |
| 40 | faccounttype | 计价方法 | varchar | 50 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 G :先进先出法 C :即时移动平均法 E :即时先进先出法 D :标准成本法 |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | fsrcbillnum | 对方单据编号 | varchar | 50 |  | √ | ' ' | 对方单据编号 |
| 43 | fsrcbilltypeid | 对方单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 44 | fgroupdiffbillnum | 合并单编号 | varchar | 100 |  | √ | ' ' | 合并单编号 |
| 45 | fdiff_k | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 46 | fdiff_h | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 47 | finvbillentryid | 库存单据行ID | int8 | 64 |  | √ | 0 | 库存单据行ID |
| 48 | fdiff_g | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 49 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 50 | fhooklogentryid | 入库勾稽日志分录ID | int8 | 64 |  | √ | 0 | 入库勾稽日志分录ID |
| 51 | fentrystatus | 分录状态 | varchar | 50 |  | √ | ' ' | 分录状态,枚举: A :暂存 B :已提交 C :已审核 |
| 52 | finvbilltype | 库存单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 53 | fdiff_s | 成本更新差异 | numeric | 23 | 10 | √ | 0 | 成本更新差异 |
| 54 | fdiff_r | 未吸收费用 | numeric | 23 | 10 | √ | 0 | 未吸收费用 |
| 55 | fdiff_q | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 56 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 57 | fdiff_p | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 58 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | [核算范围 cal_bd_calrange](../cal_files/cal_bd_calrange.md) |
| 59 | ffeeprojectid | 费用项目编码 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 60 | fdiff_m | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 61 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 62 | fstocktypeid | 存货类别编码 | int8 | 64 |  | √ | 0 | [存货类别 bd_materialcategory](../basedata_files/bd_materialcategory.md) |
| 63 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 64 | fdiff_c | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 65 | fgroupdiffbillid | 合并单id | int8 | 64 |  | √ | 0 | 合并单id |
| 66 | fnoupdatecalfields | 不更新核算字段 | varchar | 255 |  | √ | ' ' | 不更新核算字段 |
| 67 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 68 | fsrcbillentryid | 对方单据行ID | int8 | 64 |  | √ | 0 | 对方单据行ID |
| 69 | fdiff_y | 预留3 | numeric | 23 | 10 | √ | 0 | 预留3 |
| 70 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 71 | fdiff_x | 预留1 | numeric | 23 | 10 | √ | 0 | 预留1 |
| 72 | fdiff_w | 预留2 | numeric | 23 | 10 | √ | 0 | 预留2 |
| 73 | fdiff_t | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 74 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 75 | finvbiztypeid | 库存业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_stdcostdiff_e |  | fentryid |
| 2 | idx_cal_costadjustentry_invbid |  | finvbillid,fid |
| 3 | idx_cal_stdcostdiffentry_inveid |  | finvbillentryid |
| 4 | idx_cal_stdcostdiffentry_costestbill |  | fcostestimatebillid,fcostestimatebillentryid |
| 5 | idx_cal_stdcostdiffentry_srcid |  | fsrcbillid |
| 6 | idx_cal_costadjustentry_mat2 |  | fmaterialid,fid |
| 7 | idx_cal_stdcostdiffentry_cdkey |  | fid,fcostdomainkey |
| 8 | idx_cal_stdcostdiffentry |  | fid |
| 9 | idx_cal_costadjustentry_invb |  | fid,finvbillid |

---

## 差异转出单-多语言表 t_cal_stdcostdiff_l

- **表名称：** 差异转出单-多语言表
- **表名：** t_cal_stdcostdiff_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_stdcostdiff_l |  | fpkid |
| 2 | idx_cal_stdcostdiff_l |  | fid |

---

## 差异转出单-主表 t_cal_stdcostdiff

- **表名称：** 差异转出单-主表
- **表名：** t_cal_stdcostdiff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 5 | fbiztype | 核算单类型 | varchar | 50 |  | √ | ' ' | 核算单类型,枚举: A :入库 B :出库 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcreatetype | 创建类型 | varchar | 50 |  | √ | ' ' | 创建类型,枚举: A :手工录入 B :采购勾稽 D :费用分摊 E :期末余额汇报表-出单 F :出库核算-成组单据成本调整 I :费用暂估 J :费用分摊-费用自动冲回 O :手工导入 N :出库核算-尾差调整 U :委外勾稽 V :出库核算-前期出库成本调整 W :差异分摊 X :单据同步 Y :完工产品结算 Z :期末成本计算 C1 :卷算成本更新 WW-A1 :委外加工费 WW-A2 :委外费用 WW-A3 :委外制造费用 WW-A4 :委外材料费 B-A1 :暂估调价 WW-A5 :出库核算 G :标准成本尾差调整 B-A2 :销售勾稽 LIMIT-Q :数量限制 LIMIT-A :金额限制 T :期末差异调整 DIFF-ADJUST :差异平衡 |
| 8 | fisupdatecost | 更新存货成本 | bpchar | 1 |  | √ | '1' | 更新存货成本 |
| 9 | ffeeshareflagid | 费用分摊反分摊标识 | int8 | 64 |  | √ | 0 | 费用分摊反分摊标识 |
| 10 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 11 | fcalstatus | 核算处理状态 | varchar | 50 |  | √ | ' ' | 核算处理状态,枚举: A :成功 B :失败 C :处理中 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fvoucherid | 凭证id | int8 | 64 |  | √ | 0 | 凭证id |
| 14 | fbillsrctype | 单据来源类型 | varchar | 50 |  | √ | ' ' | 单据来源类型,枚举: A :手工新增 B :单据同步 C :成本变更 D :差异分摊 |
| 15 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 16 | fsrcsys | 来源系统 | bpchar | 1 |  | √ | 'A' | 来源系统,枚举: A :存货核算 B :成本系统 |
| 17 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 18 | fgroupdiffbillid | fgroupdiffbillid | int8 | 64 |  | √ | 0 |  |
| 19 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fcustsupplierid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 22 | fcheckstrikeaccount | 已冲回 | bpchar | 1 |  | √ | '0' | 已冲回 |
| 23 | fvouchernum | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 24 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 26 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 27 | fcostaccount | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 28 | fadminorgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 30 | fisvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 31 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 32 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fsrcbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 35 | fcstypeid | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 |
| 36 | fgroupdiffbillnum | fgroupdiffbillnum | varchar | 80 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_stdcostdiff |  | fid |
| 2 | idx_cal_stdcostdiff_billn |  | fbillno |
| 3 | idx_cal_stdcostdiff_bookdate |  | fbookdate |
| 4 | idx_cal_stdcostdiff_fsid |  | ffeeshareflagid |
| 5 | idx_cal_stdcostdiff_org |  | fcostaccount,fbookdate |
| 6 | idx_cal_stdcostdiff_cb |  | fid,forgid |
