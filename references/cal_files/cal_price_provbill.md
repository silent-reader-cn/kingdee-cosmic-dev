# 存货跌价计提单-cal_price_provbill

## 存货跌价计提单-主表 t_cal_price_provbill

- **表名称：** 存货跌价计提单-主表
- **表名：** t_cal_price_provbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccsettingid | 方案编码 | int8 | 64 |  | √ | 0 | 存货跌价准备设置 cal_fallprice_setting |
| 3 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 9 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fvouchernum | 凭证号 | varchar | 60 |  | √ | ' ' | 凭证号 |
| 12 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 13 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 17 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 18 | fperiod | 会计期间编码 | int8 | 64 |  | √ | 0 | 会计期间编码 |
| 19 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 20 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 21 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 22 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

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
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fhasamount | 已提跌价准备 | numeric | 23 | 10 | √ | 0.0000000000 | 已提跌价准备 |
| 5 | freplenishamount | 本期补提准备 | numeric | 23 | 10 | √ | 0.0000000000 | 本期补提准备 |
| 6 | fmaterialgroupid | 物料分类编码 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 9 | famount | 存货余额 | numeric | 23 | 10 | √ | 0.0000000000 | 存货余额 |
| 10 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 11 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 12 | finvagefrom | 库龄从（天） | int8 | 64 |  | √ | 0 | 库龄从（天） |
| 13 | fwarehousegroupid | 仓库分组编码 | int8 | 64 |  | √ | 0 | 仓库分组 bd_warehousegroup |
| 14 | frushbaseqty | 跌价冲回数量 | numeric | 23 | 10 | √ | 0.0000000000 | 跌价冲回数量 |
| 15 | frealizableamount | 可变现净值 | numeric | 23 | 10 | √ | 0.0000000000 | 可变现净值 |
| 16 | frushamount | 跌价冲回金额 | numeric | 23 | 10 | √ | 0.0000000000 | 跌价冲回金额 |
| 17 | fassistid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 18 | fownertype | 货主类型 | varchar | 30 |  | √ | 'bos_org' | 货主类型,枚举: bos_org :核算组织 |
| 19 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 20 | funitrealizableamount | 单位可变现净值 | numeric | 23 | 10 | √ | 0.0000000000 | 单位可变现净值 |
| 21 | flot | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 22 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | fbaseprice | 存货平均价 | numeric | 23 | 10 | √ | 0.0000000000 | 存货平均价 |
| 24 | fendperiod | 结束期间编码 | int8 | 64 |  | √ | 999999 | 结束期间编码 |
| 25 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 27 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 28 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 29 | frequireamount | 应提跌价准备 | numeric | 23 | 10 | √ | 0.0000000000 | 应提跌价准备 |
| 30 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 32 | fexpirydateto | 剩余有效期至（天） | int4 | 32 |  | √ | 999999 | 剩余有效期至（天） |
| 33 | fbaseqty | 存货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 存货数量 |
| 34 | ffallpricescale | 存货跌价比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 存货跌价比例(%) |
| 35 | fexpirydatefrom | 剩余有效期从（天） | int4 | 32 |  | √ | '-999999' | 剩余有效期从（天） |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 37 | finvageto | 库龄至（天） | int8 | 64 |  | √ | 0 | 库龄至（天） |

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
