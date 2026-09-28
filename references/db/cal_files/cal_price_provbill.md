# 存货跌价计提单-cal_price_provbill

## 存货跌价计提单-主表 t_cal_price_provbill

- **表名称：** 存货跌价计提单-主表
- **表名：** t_cal_price_provbill

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
| 8 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 9 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmigrate | 迁移数据 | bpchar | 1 |  | √ | '0' | 迁移数据 |
| 11 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fvouchernum | 凭证号 | varchar | 60 |  | √ | ' ' | 凭证号 |
| 13 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 14 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 18 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 19 | fperiod | 会计期间编码 | int8 | 64 |  | √ | 0 | 会计期间编码 |
| 20 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 21 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 22 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 23 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_price_provbill_pkey |  | fid |
| 2 | idx_cal_price_provbill_cop |  | fcostaccountid,forgid,fperiodid |
| 3 | idx_cal_price_provbill_bd |  | fbookdate |
| 4 | idx_cal_price_provbill_pd |  | fperiod |

---

## 物料明细-子表 t_cal_price_proventry

- **表名称：** 物料明细-子表
- **表名：** t_cal_price_proventry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpreentryid | 上期分录id | int8 | 64 |  | √ | 0 | 上期分录id |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fhasamount | 已提跌价准备 | numeric | 23 | 10 | √ | 0.0000000000 | 已提跌价准备 |
| 5 | freplenishamount | 本期补提准备 | numeric | 23 | 10 | √ | 0.0000000000 | 本期补提准备 |
| 6 | fmaterialgroupid | 物料分类编码 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 9 | famount | 存货余额 | numeric | 23 | 10 | √ | 0.0000000000 | 存货余额 |
| 10 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 11 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 12 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 13 | finvagefrom | 库龄从（天） | int8 | 64 |  | √ | 0 | 库龄从（天） |
| 14 | fwarehousegroupid | 仓库分组编码 | int8 | 64 |  | √ | 0 | [仓库分组 bd_warehousegroup](../sbd_files/bd_warehousegroup.md) |
| 15 | frushbaseqty | 跌价冲回数量 | numeric | 23 | 10 | √ | 0.0000000000 | 跌价冲回数量 |
| 16 | fdevcost | 研发费用 | varchar | 10 |  | √ | '0' | 研发费用,枚举: 1 :是 0 :否 |
| 17 | frealizableamount | 可变现净值 | numeric | 23 | 10 | √ | 0.0000000000 | 可变现净值 |
| 18 | frushamount | 跌价冲回金额 | numeric | 23 | 10 | √ | 0.0000000000 | 跌价冲回金额 |
| 19 | fassistid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 20 | fownertype | 货主类型 | varchar | 30 |  | √ | 'bos_org' | 货主类型,枚举: bos_org :核算组织 |
| 21 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 22 | funitrealizableamount | 单位可变现净值 | numeric | 23 | 10 | √ | 0.0000000000 | 单位可变现净值 |
| 23 | flot | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 24 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fbaseprice | 存货平均价 | numeric | 23 | 10 | √ | 0.0000000000 | 存货平均价 |
| 26 | fendperiod | 结束期间编码 | int8 | 64 |  | √ | 999999 | 结束期间编码 |
| 27 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 29 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 30 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 31 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 32 | frequireamount | 应提跌价准备 | numeric | 23 | 10 | √ | 0.0000000000 | 应提跌价准备 |
| 33 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 35 | fexpirydateto | 剩余有效期至（天） | int4 | 32 |  | √ | 999999 | 剩余有效期至（天） |
| 36 | fbaseqty | 存货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 存货数量 |
| 37 | ffallpricescale | 存货跌价比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 存货跌价比例(%) |
| 38 | fexpirydatefrom | 剩余有效期从（天） | int4 | 32 |  | √ | '-999999' | 剩余有效期从（天） |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | finvageto | 库龄至（天） | int8 | 64 |  | √ | 0 | 库龄至（天） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_price_provbille_sto |  | fstorageorgunitid |
| 2 | idx_cal_price_provbille_fid |  | fid |
| 3 | t_cal_price_proventry_pkey |  | fentryid |
| 4 | idx_cal_price_proventry_ep |  | fendperiod |
| 5 | idx_cal_price_provbille_mat |  | fmaterialid |

---

## 存货跌价计提单-多语言表 t_cal_price_provbill_l

- **表名称：** 存货跌价计提单-多语言表
- **表名：** t_cal_price_provbill_l

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
| 1 | idx_cal_price_provbill_l_loc |  | flocaleid |
| 2 | t_cal_price_provbill_l_pkey |  | fpkid |
