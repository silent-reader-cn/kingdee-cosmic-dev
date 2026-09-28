# 存货跌价冲回单-cal_price_revbill

## 关联子实体-子表 t_cal_price_revbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cal_price_revbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_price_revbill_lk_pkey |  | fpkid |
| 2 | idx_cal_price_revbill_lk_fk |  | fid |

---

## 存货跌价冲回单-主表 t_cal_price_revbill

- **表名称：** 存货跌价冲回单-主表
- **表名：** t_cal_price_revbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccsettingid | 方案编码 | int8 | 64 |  | √ | 0 | [存货跌价准备设置 cal_fallprice_setting](../cal_files/cal_fallprice_setting.md) |
| 3 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fvouchernum | 凭证号 | varchar | 60 |  | √ | ' ' | 凭证号 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 16 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 17 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 18 | fperiod | 会计期间编码 | int8 | 64 |  | √ | 0 | 会计期间编码 |
| 19 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 20 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 21 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_price_revbill_acct |  | fcostaccountid |
| 2 | idx_cal_price_revbill_bd |  | fbookdate |
| 3 | idx_cal_price_revbill_sid |  | fsourcebillid |
| 4 | idx_cal_price_revbill_opa |  | forgid,fperiodid,faccsettingid |
| 5 | idx_cal_price_revbill_pd |  | fperiod |
| 6 | t_cal_price_revbill_pkey |  | fid |

---

## 存货跌价冲回单-多语言表 t_cal_price_revbill_l

- **表名称：** 存货跌价冲回单-多语言表
- **表名：** t_cal_price_revbill_l

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
| 1 | idx_cal_price_revbill_l_lo |  | flocaleid |
| 2 | t_cal_price_revbill_l_pkey |  | fpkid |

---

## 关联子实体-子表 t_cal_pricerevbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cal_pricerevbillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_pricerevbillentry_lk_fk |  | fentryid |
| 2 | t_cal_pricerevbillentry_lk_pkey |  | fpkid |

---

## 物料明细-子表 t_cal_pricerevbillentry

- **表名称：** 物料明细-子表
- **表名：** t_cal_pricerevbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fmaterialgroupid | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 4 | fsourceentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcurperiodoutqty | 本期出库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期出库数量 |
| 7 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 8 | famount | 存货余额 | numeric | 23 | 10 | √ | 0.0000000000 | 存货余额 |
| 9 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 10 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 11 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 12 | finvagefrom | 库龄从（天） | int8 | 64 |  | √ | 0 | 库龄从（天） |
| 13 | fwarehousegroupid | 仓库分组 | int8 | 64 |  | √ | 0 | [仓库分组 bd_warehousegroup](../sbd_files/bd_warehousegroup.md) |
| 14 | frushbaseqty | 跌价冲回数量 | numeric | 23 | 10 | √ | 0.0000000000 | 跌价冲回数量 |
| 15 | fdevcost | 研发费用 | varchar | 10 |  | √ | '0' | 研发费用,枚举: 1 :是 0 :否 |
| 16 | frealizableamount | 可变现净值 | numeric | 23 | 10 | √ | 0.0000000000 | 可变现净值 |
| 17 | frushamount | 跌价冲回金额 | numeric | 23 | 10 | √ | 0.0000000000 | 跌价冲回金额 |
| 18 | fassistid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 19 | fownertype | 货主类型 | varchar | 30 |  | √ | 'bos_org' | 货主类型,枚举: bos_org :核算组织 |
| 20 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 21 | funitrealizableamount | 单位可变现净值 | numeric | 23 | 10 | √ | 0.0000000000 | 单位可变现净值 |
| 22 | flot | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 23 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fcurperiodrushamount | 本期冲回金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期冲回金额 |
| 25 | fbaseprice | 存货平均价 | numeric | 23 | 10 | √ | 0.0000000000 | 存货平均价 |
| 26 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 28 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 29 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 30 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 31 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 33 | fcurperiodrushqty | 本期冲回数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期冲回数量 |
| 34 | fexpirydateto | 剩余有效期至（天） | int4 | 32 |  | √ | 999999 | 剩余有效期至（天） |
| 35 | fbaseqty | 存货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 存货数量 |
| 36 | fexpirydatefrom | 剩余有效期从（天） | int4 | 32 |  | √ | '-999999' | 剩余有效期从（天） |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | finvageto | 库龄至（天） | int8 | 64 |  | √ | 0 | 库龄至（天） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_pricerevbille_mat |  | fmaterialid |
| 2 | idx_cal_pricerevbille_sto |  | fstorageorgunitid |
| 3 | idx_cal_pricerevbillentry_ei |  | fid |
| 4 | t_cal_pricerevbillentry_pkey |  | fentryid |

---

## 存货跌价冲回单-关联追踪表 t_cal_price_revbill_tc

- **表名称：** 存货跌价冲回单-关联追踪表
- **表名：** t_cal_price_revbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_price_revbill_tc_pkey |  | fid |
| 2 | idx_cal_price_revbill_tc_tid |  | ftid |
| 3 | idx_cal_price_revbill_tc_tbill |  | ftbillid |

---

## 存货跌价冲回单-反写记录表 t_cal_price_revbill_wb

- **表名称：** 存货跌价冲回单-反写记录表
- **表名：** t_cal_price_revbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_price_revbill_wb_pkey |  | fentryid |
| 2 | idx_cal_price_revbill_wb_fk |  | fid |
