# 初始化数据录入-cal_initbill

## 成本要素明细-子表 t_cal_initbill_detail

- **表名称：** 成本要素明细-子表
- **表名：** t_cal_initbill_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubyearissuecost | 本年累计发出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出金额 |
| 2 | fcostdiff | 差异 | numeric | 23 | 10 | √ | 0.0000000000 | 差异 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fsubyearincost | 本年累计收入金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入金额 |
| 5 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 8 | fsubyearincostdiff | 本年累计收入差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入差异 |
| 9 | fsubyearissueqty | 本年累计发出数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出数量 |
| 10 | fsubyearinqty | 本年累计收入数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入数量 |
| 11 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 12 | funitprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 14 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 15 | fbaseunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fsubyearissuecostdiff | 本年累计发出差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出差异 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_initbill_detail_pkey |  | fdetailid |
| 2 | idx_cal_initdetail_fentryid |  | fentryid |
| 3 | idx_cal_initbill_detail_sub |  | fentryid,fcostsubelementid |

---

## 初始化数据录入-多语言表 t_cal_initbill_l

- **表名称：** 初始化数据录入-多语言表
- **表名：** t_cal_initbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_initbill_l_pkey |  | fpkid |
| 2 | idx_cal_initbill_l |  | fid,flocaleid |

---

## 单据体-多语言表 t_cal_initbillentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_cal_initbillentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_initbillentry_l_pkey |  | fpkid |
| 2 | idx_cal_initbillentry_l |  | fentryid,flocaleid |

---

## 单据体-子表 t_cal_initbillentry

- **表名称：** 单据体-子表
- **表名：** t_cal_initbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fyearissuecostdiff | 本年累计发出差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出差异 |
| 3 | fcaldimensionid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 cal_bd_caldimension](../cal_files/cal_bd_caldimension.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 6 | fyearincostdiff | 本年累计收入差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入差异 |
| 7 | fsrcentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 8 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 9 | fdevcost | 研发费用 | varchar | 10 |  | √ | '0' | 研发费用,枚举: 1 :是 0 :否 |
| 10 | funitprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 11 | fsrcbizentityobject | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 12 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 |
| 13 | fwarehsouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 14 | flot | 批号 | varchar | 255 |  | √ | ' ' | 批号 |
| 15 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fyearinqty | 本年累计收入数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入数量 |
| 17 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 18 | fstorageorgunitid | 库存组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 20 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 21 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 22 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 23 | fyearissuecost | 本年累计发出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出金额 |
| 24 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fecalstatus | 核算处理状态 | bpchar | 1 |  | √ | 'A' | 核算处理状态,枚举: A :成功 B :失败 C :处理中 |
| 26 | fcostdomainkey | 成本域维度 | varchar | 50 |  | √ | ' ' | 成本域维度 |
| 27 | fsignnum | 数值方向 | int8 | 64 |  | √ | 0 | 数值方向 |
| 28 | faccounttype | 计价方法 | bpchar | 1 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 G :先进先出法 C :即时移动平均法 E :即时先进先出法 D :标准成本法 |
| 29 | fyearissueqty | 本年累计发出数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出数量 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fsrcbillnum | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 32 | fsrcbilltypeid | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 33 | fyearincost | 本年累计收入金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入金额 |
| 34 | fcostdiff | 差异 | numeric | 23 | 10 | √ | 0.0000000000 | 差异 |
| 35 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 36 | fentrystatus | 分录状态 | bpchar | 1 |  | √ | 'C' | 分录状态,枚举: A :暂存 B :已提交 C :已审核 |
| 37 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 38 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 39 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | [核算范围 cal_bd_calrange](../cal_files/cal_bd_calrange.md) |
| 40 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 41 | fcreatetype | 差异类型 | bpchar | 1 |  | √ | ' ' | 差异类型,枚举: G :订单价差 H :发票价差 K :费用价差 M :标准成本变更差异 P :材料耗用差异 Q :制造费用差异 R :未吸收费用 S :成本更新差异 T :其他价差 |
| 42 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 43 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 44 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 45 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 46 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 47 | fstockindate | 入库日期 | timestamp | 0 |  |  | null | 入库日期 |
| 48 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 49 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 50 | fbizbillentryid | 业务单据分录ID | int8 | 64 |  | √ | 0 | 业务单据分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_initbillentry_cdkey |  | fcostdomainkey,fid |
| 2 | idx_cal_initbillentry_fid |  | fid |
| 3 | idx_cal_initentry_fmatid |  | fmaterialid |
| 4 | t_cal_initbillentry_pkey |  | fentryid |

---

## 初始化数据录入-主表 t_cal_initbill

- **表名称：** 初始化数据录入-主表
- **表名：** t_cal_initbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fcalstatus | 核算处理状态 | bpchar | 1 |  | √ | 'A' | 核算处理状态,枚举: A :成功 B :失败 C :处理中 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | flocalcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 17 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 18 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 19 | fbizentityobject | 业务对象 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_initbill_acc |  | fcostaccountid,fbizdate |
| 2 | idx_cal_initbill_calorg |  | fcalorgid |
| 3 | t_cal_initbill_pkey |  | fid |
| 4 | idx_cal_initbill_fbizdate |  | fbizdate |
