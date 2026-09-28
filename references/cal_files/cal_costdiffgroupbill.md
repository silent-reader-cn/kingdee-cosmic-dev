# 标准成本差异合并单-cal_costdiffgroupbill

## 标准成本差异合并单-主表 t_cal_diffgroupbill

- **表名称：** 标准成本差异合并单-主表
- **表名：** t_cal_diffgroupbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproductlineid | fproductlineid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fcaldimensionid | 核算维度 | int8 | 64 |  | √ | 0 | 核算维度 cal_bd_caldimension |
| 5 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本（作废） bd_materialversion |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 8 | fisupdatecost | 更新存货成本 | bpchar | 1 |  | √ | '1' | 更新存货成本 |
| 9 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 10 | fwarehsouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 11 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | flot | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 13 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 14 | fadjustamt | 调整金额 | numeric | 23 | 10 | √ | 0 | 调整金额 |
| 15 | fvoucherid | 凭证id | int8 | 64 |  | √ | 0 | 凭证id |
| 16 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 17 | fstorageorgunitid | 库存组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 19 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 20 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcustsupplierid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 22 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fcostaccount | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 25 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | ftranstype | 调拨类型 | varchar | 5 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 27 | faccounttype | 计价方法 | varchar | 5 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 F :个别计价法 B :移动加权平均法 C :实时移动加权平均法 D :标准成本法 E :先进先出法（实时） G :先进先出法（月末） |
| 28 | fisvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fsrcbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 31 | fcstypeid | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 |
| 32 | fdiff_k | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 33 | fdiff_h | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 34 | fdiff_g | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 35 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 36 | fremark_tag | fremark_tag | text | 0 |  |  | null |  |
| 37 | fdiff_s | 成本更新差异 | numeric | 23 | 10 | √ | 0 | 成本更新差异 |
| 38 | fdiff_r | 未吸收费用 | numeric | 23 | 10 | √ | 0 | 未吸收费用 |
| 39 | fdiff_q | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 40 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 41 | fdiff_p | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 42 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | 核算范围 cal_bd_calrange |
| 43 | fdiff_m | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 44 | ffeeprojectid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 45 | fbiztype | 核算单类型 | varchar | 5 |  | √ | ' ' | 核算单类型,枚举: A :入库 B :出库 |
| 46 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | fstocktypeid | 存货类别编码 | int8 | 64 |  | √ | 0 | 存货类别 bd_materialcategory |
| 48 | fcreatetype | 创建类型 | varchar | 5 |  | √ | ' ' | 创建类型,枚举: A :手工录入 B :采购核销 D :费用分摊 E :期末余额汇报表-出单 F :出库核算-成组单据成本调整 I :费用暂估 J :费用分摊-费用自动冲回 O :手工导入 N :出库核算-尾差调整 U :委外核销 V :出库核算-前期出库成本调整 W :差异分摊 X :单据同步 Y :完工产品结算 Z :期末成本计算 C1 :卷算成本更新 WW-A1 :委外加工费 WW-A2 :委外费用 WW-A3 :委外制造费用 WW-A4 :委外材料费 B-A1 :暂估调价 G :标准成本尾差调整 |
| 49 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 50 | fdiff_c | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 51 | fremark | fremark | varchar | 255 |  |  | null |  |
| 52 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 53 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 54 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 55 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 56 | fadminorgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 57 | fdiff_t | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 58 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 59 | finvbiztypeid | 库存业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 60 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_diffgroupbill_org |  | forgid |
| 2 | idx_cal_diffgroupbill_cpm |  | fperiodid,fcostaccount,fmaterialid |
| 3 | idx_cal_diffgroupbill_mat |  | fmaterialid |
| 4 | pk_cal_diffgroupbill |  | fid |

---

## 标准成本差异合并单-多语言表 t_cal_diffgroupbill_l

- **表名称：** 标准成本差异合并单-多语言表
- **表名：** t_cal_diffgroupbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 100 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_diffgroupbill_l |  | fpkid |
| 2 | idx_diffgroupbill_l |  | fid,flocaleid |
