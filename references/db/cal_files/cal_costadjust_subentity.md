# 成本调整单-cal_costadjust_subentity

## 成本要素明细-子表 t_cal_costadjust_detail

- **表名称：** 成本要素明细-子表
- **表名：** t_cal_costadjust_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 2 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | 成本调整单分录id | int8 | 64 |  | √ | 0 | 成本调整单分录id |
| 6 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 8 | fadjustamt | 调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costadjust_detail_pkey |  | fdetailid |
| 2 | idx_cal_costadjust_detail_sub |  | fentryid,fcostsubelementid |
| 3 | idx_cal_cadetail_entryid |  | fentryid |

---

## 物料明细-子表 t_cal_costadjustbillentry

- **表名称：** 物料明细-子表
- **表名：** t_cal_costadjustbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgfield | forgfield | int8 | 64 |  | √ | 0 |  |
| 3 | fqueuetype | 序列类型 | bpchar | 1 |  | √ | '0' | 序列类型,枚举: 0 :入库 1 :出库 |
| 4 | finvbillid | 库存单据ID | int8 | 64 |  | √ | 0 | 库存单据ID |
| 5 | fcaldimensionid | 核算维度 | int8 | 64 |  | √ | 0 | 核算维度 cal_bd_caldimension |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 8 | fsrcentryseq | 对方单据行号 | int8 | 64 |  | √ | 0 | 对方单据行号 |
| 9 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 10 | finvbillnum | 库存单据编号 | varchar | 80 |  | √ | ' ' | 库存单据编号 |
| 11 | fcostestimatebillentryid | 被冲回的暂估调价单据分录ID | int8 | 64 |  | √ | 0 | 被冲回的暂估调价单据分录ID |
| 12 | ffeerecordentryid | 采购费用分摊记录分录ID | int8 | 64 |  | √ | 0 | 采购费用分摊记录分录ID |
| 13 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 14 | fsrcbizentityobject | 对方业务对象 | varchar | 80 |  | √ | ' ' | 对方业务对象 |
| 15 | fwarehsouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 16 | flot | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | ffeesharetotalamt | 费用分摊累计分摊字段 | numeric | 23 | 10 | √ | 0.0000000000 | 费用分摊累计分摊字段 |
| 19 | finventryseq | 库存单据行号 | int8 | 64 |  | √ | 0 | 库存单据行号 |
| 20 | fadjustamt | 调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整金额 |
| 21 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 22 | fstorageorgunitid | 库存组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | finvbizentityobject | 库存业务对象 | varchar | 80 |  | √ | ' ' | 库存业务对象 |
| 24 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 25 | fsrcbillid | 对方单据ID | int8 | 64 |  | √ | 0 | 对方单据ID |
| 26 | finvauditdate | 落库审核日期 | timestamp | 0 |  |  | null | 落库审核日期 |
| 27 | fcostestimatebillid | 被冲回的暂估重估单据ID | int8 | 64 |  | √ | 0 | 被冲回的暂估重估单据ID |
| 28 | finvbizdate | 落库记账日期 | timestamp | 0 |  |  | null | 落库记账日期 |
| 29 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fecalstatus | 核算处理状态 | bpchar | 1 |  | √ | 'A' | 核算处理状态,枚举: A :成功 B :失败 C :处理中 |
| 31 | ffeerecordid | 采购费用分摊记录ID | int8 | 64 |  | √ | 0 | 采购费用分摊记录ID |
| 32 | fcostdomainkey | 成本域维度 | varchar | 50 |  | √ | ' ' | 成本域维度 |
| 33 | fsignnum | 数值方向 | int8 | 64 |  | √ | 1 | 数值方向 |
| 34 | ftranstype | 调拨类型 | bpchar | 1 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 35 | fhooklogid | 入库勾稽日志ID | int8 | 64 |  | √ | 0 | 入库勾稽日志ID |
| 36 | faccounttype | 计价方法 | varchar | 5 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 G :先进先出法 C :即时移动平均法 E :即时先进先出法 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | fsrcbillnum | 对方单据编号 | varchar | 80 |  | √ | ' ' | 对方单据编号 |
| 39 | fsrcbilltypeid | 对方单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 40 | finvbillentryid | 库存单据行ID | int8 | 64 |  | √ | 0 | 库存单据行ID |
| 41 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 42 | fhooklogentryid | 入库勾稽日志分录ID | int8 | 64 |  | √ | 0 | 入库勾稽日志分录ID |
| 43 | fentrystatus | 分录状态 | bpchar | 1 |  | √ | 'C' | 分录状态,枚举: A :暂存 B :已提交 C :已审核 |
| 44 | finvbilltype | 库存单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 45 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 46 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | 核算范围 cal_bd_calrange |
| 47 | ffeeprojectid | 费用项目编码 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 48 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 49 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 50 | fsrcbillentryid | 对方单据行ID | int8 | 64 |  | √ | 0 | 对方单据行ID |
| 51 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 52 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 53 | finvbiztypeid | 库存业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costadjustbillentry_pkey |  | fentryid |
| 2 | idx_cal_costadjustentry_costestimatebill |  | fcostestimatebillid,fcostestimatebillentryid |
| 3 | idx_cal_costadjustbillentry |  | fid |
| 4 | idx_cal_costadjustentry_cdkey |  | fcostdomainkey,fid |
| 5 | idx_cal_costadjustentry_srcid |  | fsrcbillid |
| 6 | idx_cal_costadjustentry_invid |  | finvbillid |

---

## 成本调整单-多语言表 t_cal_costadjustbill_l

- **表名称：** 成本调整单-多语言表
- **表名：** t_cal_costadjustbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 100 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costadjustbill_l_pkey |  | fpkid |
| 2 | idx_cal_costadjustbilll_id |  | fid,flocaleid |

---

## 成本调整单-主表 t_cal_costadjustbill

- **表名称：** 成本调整单-主表
- **表名：** t_cal_costadjustbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 5 | fbiztype | 核算单类型 | varchar | 5 |  | √ | ' ' | 核算单类型,枚举: A :入库 B :出库 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fcreatetype | 创建类型 | varchar | 5 |  | √ | ' ' | 创建类型,枚举: A :手工录入 B :采购勾稽 D :费用分摊 E :期末余额汇报表-出单 F :出库核算-成组单据成本调整 I :费用暂估 J :费用分摊-费用自动冲回 O :手工导入 N :出库核算-尾差调整 U :委外勾稽 V :出库核算-前期出库成本调整 W :差异分摊 X :单据同步 Y :完工产品结算 Z :期末成本计算 C1 :卷算成本更新 WW-A1 :委外加工费 WW-A2 :委外费用 WW-A3 :委外制造费用 WW-A4 :委外材料费 B-A1 :暂估调价 NP :出库核算-结存负单价调整 D1 :实际成本调整 |
| 8 | ffeeshareflagid | 费用分摊反分摊标识 | int8 | 64 |  | √ | 0 | 费用分摊反分摊标识 |
| 9 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 10 | fremark | fremark | varchar | 50 |  | √ | ' ' |  |
| 11 | fcalstatus | 核算处理状态 | bpchar | 1 |  | √ | 'A' | 核算处理状态,枚举: A :成功 B :失败 C :处理中 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fvoucherid | 凭证id | int8 | 64 |  | √ | 0 | 凭证id |
| 14 | fbillsrctype | 单据来源类型 | varchar | 30 |  | √ | 'A' | 单据来源类型,枚举: A :手工新增 B :单据同步 C :成本变更 D :差异分摊 |
| 15 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 16 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 17 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fcustsupplierid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 20 | fcheckstrikeaccount | 已冲回 | bpchar | 1 |  | √ | '0' | 已冲回 |
| 21 | fvouchernum | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 22 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 25 | fdifftype | 差异类型 | bpchar | 1 |  | √ | 'B' | 差异类型,枚举: B :实际成本 G :订单价差 H :发票价差 K :费用价差 P :材料耗用差异 Q :制造费用差异 R :未吸收费用 M :标准成本变更差异 S :成本更新差异 T :其他价差 |
| 26 | fcostaccount | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 27 | fadminorgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 29 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 30 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 31 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fcstypeid | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 |
| 34 | fsrcbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costadjustbill_pkey |  | fid |
| 2 | idx_cal_costadjust_date |  | fbizdate |
| 3 | idx_cal_costadjust_cb |  | fcostaccount,fbizdate |
| 4 | idx_cal_costadjustbill_org |  | forgid |
