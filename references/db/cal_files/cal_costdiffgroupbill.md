# 标准成本差异合并单-cal_costdiffgroupbill

## 标准成本差异合并单-主表 t_cal_diffgroupbill

- **表名称：** 标准成本差异合并单-主表
- **表名：** t_cal_diffgroupbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproductlineid | fproductlineid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcaldimensionid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 cal_bd_caldimension](../cal_files/cal_bd_caldimension.md) |
| 5 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本（作废） bd_materialversion](../basedata_files/bd_materialversion.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 8 | fdevcost | 研发费用 | varchar | 10 |  | √ | '0' | 研发费用,枚举: 1 :是 0 :否 |
| 9 | fisupdatecost | 更新存货成本 | bpchar | 1 |  | √ | '1' | 更新存货成本 |
| 10 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 11 | fwarehsouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | flot | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 14 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 15 | fadjustamt | 调整金额 | numeric | 23 | 10 | √ | 0 | 调整金额 |
| 16 | fvoucherid | 凭证id | int8 | 64 |  | √ | 0 | 凭证id |
| 17 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 18 | fstorageorgunitid | 库存组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 20 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcustsupplierid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 23 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 24 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fcostaccount | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 27 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | ftranstype | 调拨类型 | varchar | 5 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 29 | faccounttype | 计价方法 | varchar | 5 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 F :个别计价法 B :移动加权平均法 C :实时移动加权平均法 D :标准成本法 E :先进先出法（实时） G :先进先出法（月末） |
| 30 | fisvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fsrcbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 33 | fcstypeid | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 |
| 34 | fdiff_k | 费用价差 | numeric | 23 | 10 | √ | 0 | 费用价差 |
| 35 | fdiff_h | 发票价差 | numeric | 23 | 10 | √ | 0 | 发票价差 |
| 36 | fdiff_g | 订单价差 | numeric | 23 | 10 | √ | 0 | 订单价差 |
| 37 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 38 | fremark_tag | fremark_tag | text | 0 |  |  | null |  |
| 39 | fdiff_s | 成本更新差异 | numeric | 23 | 10 | √ | 0 | 成本更新差异 |
| 40 | fdiff_r | 未吸收费用 | numeric | 23 | 10 | √ | 0 | 未吸收费用 |
| 41 | fdiff_q | 制造费用差异 | numeric | 23 | 10 | √ | 0 | 制造费用差异 |
| 42 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 43 | fdiff_p | 材料耗用差异 | numeric | 23 | 10 | √ | 0 | 材料耗用差异 |
| 44 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | [核算范围 cal_bd_calrange](../cal_files/cal_bd_calrange.md) |
| 45 | fdiff_m | 标准成本变更差异 | numeric | 23 | 10 | √ | 0 | 标准成本变更差异 |
| 46 | ffeeprojectid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 47 | fbiztype | 核算单类型 | varchar | 5 |  | √ | ' ' | 核算单类型,枚举: A :入库 B :出库 |
| 48 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 49 | fstocktypeid | 存货类别编码 | int8 | 64 |  | √ | 0 | [存货类别 bd_materialcategory](../basedata_files/bd_materialcategory.md) |
| 50 | fcreatetype | 创建类型 | varchar | 5 |  | √ | ' ' | 创建类型,枚举: A :手工录入 B :采购核销 D :费用分摊 E :期末余额汇报表-出单 F :出库核算-成组单据成本调整 I :费用暂估 J :费用分摊-费用自动冲回 O :手工导入 N :出库核算-尾差调整 U :委外核销 V :出库核算-前期出库成本调整 W :差异分摊 X :单据同步 Y :完工产品结算 Z :期末成本计算 C1 :卷算成本更新 WW-A1 :委外加工费 WW-A2 :委外费用 WW-A3 :委外制造费用 WW-A4 :委外材料费 B-A1 :暂估调价 G :标准成本尾差调整 |
| 51 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 52 | fdiff_c | 跌价差异 | numeric | 23 | 10 | √ | 0 | 跌价差异 |
| 53 | fremark | fremark | varchar | 255 |  |  | null |  |
| 54 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 56 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 57 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 58 | fadminorgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 59 | fdiff_t | 其他价差 | numeric | 23 | 10 | √ | 0 | 其他价差 |
| 60 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 61 | finvbiztypeid | 库存业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 62 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

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
