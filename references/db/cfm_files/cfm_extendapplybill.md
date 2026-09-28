# 借款展期申请-cfm_extendapplybill

## 借款展期申请-主表 t_cfm_extendapplybill

- **表名称：** 借款展期申请-主表
- **表名：** t_cfm_extendapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freferrateid | 参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 3 | frateadjustcycle | 利率重置周期 | int8 | 64 |  | √ | 0 | 利率重置周期 |
| 4 | forgid | 借款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | frenewalinterestrate | 展期利率（%） | numeric | 23 | 10 | √ | 0 | 展期利率（%） |
| 6 | fnotrepayamount | 未还本金 | numeric | 23 | 10 | √ | 0 | 未还本金 |
| 7 | famount | 借款金额 | numeric | 23 | 10 | √ | 0 | 借款金额 |
| 8 | frateadjustcycletype | 利率重置周期 | varchar | 50 |  | √ | ' ' | 利率重置周期,枚举: D :按天 W :按周 M :按月 |
| 9 | frenewalexpiredate | 展期后合同到期日期 | timestamp | 0 |  |  | null | 展期后合同到期日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 13 | fdrawamount | 已提款金额 | numeric | 23 | 10 | √ | 0 | 已提款金额 |
| 14 | fbusinessstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: 1 :申请中 2 :办理中 3 :未办理 4 :已办理 5 :已退单 |
| 15 | fratefloatpoint | 利率浮动基点 | numeric | 16 | 6 | √ | 0 | 利率浮动基点 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fremark | 展期利率调整说明 | varchar | 255 |  | √ | ' ' | 展期利率调整说明 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fprevrenewalexpiredate | 展期前合同到期日期 | timestamp | 0 |  |  | null | 展期前合同到期日期 |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fproductfactoryid | 融资模型 | int8 | 64 |  | √ | 0 | [融资模型 cfm_productfactory](../cfm_files/cfm_productfactory.md) |
| 24 | floancontractbillid | 合同单据编号 | int8 | 64 |  | √ | 0 | [借款合同 cfm_loancontractbill_f7](../cfm_files/cfm_loancontractbill_f7.md) |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fdescription | 申请原因 | varchar | 255 |  | √ | ' ' | 申请原因 |
| 27 | fisadjustinterestrate | 调整利率 | bpchar | 1 |  | √ | '0' | 调整利率 |
| 28 | frateadjuststyle | 利率重置方式 | varchar | 50 |  | √ | ' ' | 利率重置方式,枚举: deadline :即期调整 cycle :周期性调整 hand :手工调整 noadjust :不调整 |
| 29 | floantype | 贷款类型 | varchar | 50 |  | √ | ' ' | 贷款类型,枚举: loan :普通贷款 sl :银团贷款 ec :企业往来 entrust :委托贷款 bond :债券发行 |
| 30 | fbizdate | 展期签订日期 | timestamp | 0 |  |  | null | 展期签订日期 |
| 31 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: cfm :融资管理 invest :投资管理 bond :债券 ifm :内部金融管理 |
| 32 | fcurrencyid | 借款币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fratesign | 利率浮动基点（BP） | varchar | 50 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |
| 35 | fprotocolno | 展期协议号 | varchar | 255 |  | √ | ' ' | 展期协议号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_extendapplybill |  | fbillno,fbillstatus |
| 2 | pk_cfm_extendapplybill |  | fid |

---

## 借款展期申请-多语言表 t_cfm_extendapplybill_l

- **表名称：** 借款展期申请-多语言表
- **表名：** t_cfm_extendapplybill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 展期利率调整说明 | varchar | 255 |  | √ | ' ' | 展期利率调整说明 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdescription | 申请原因 | varchar | 255 |  | √ | ' ' | 申请原因 |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_extendapplybill_l |  | fpkid |
| 2 | idx_cfm_extendapplybill_l |  | fid |

---

## 提款信息-子表 t_cfm_extendapplybill_e

- **表名称：** 提款信息-子表
- **表名：** t_cfm_extendapplybill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprevrenewalexpiredate | 展期前到期日期 | timestamp | 0 |  |  | null | 展期前到期日期 |
| 3 | floanbillid | 提款单编号 | int8 | 64 |  | √ | 0 | [提款处理单 cfm_loanbill_f7](../cfm_files/cfm_loanbill_f7.md) |
| 4 | fnotrepayamount | 未还本金 | numeric | 23 | 10 | √ | 0 | 未还本金 |
| 5 | fdrawamount | 提款金额 | numeric | 23 | 10 | √ | 0 | 提款金额 |
| 6 | fispayinst | 展期 | bpchar | 1 |  | √ | '0' | 展期 |
| 7 | fextendamount | 展期金额 | numeric | 23 | 10 | √ | 0 | 展期金额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fexrateadjustdate | 首次展期利率调整日 | timestamp | 0 |  |  | null | 首次展期利率调整日 |
| 11 | flrenewalexpiredate | 展期后到期日期 | timestamp | 0 |  |  | null | 展期后到期日期 |
| 12 | frepayamount | 已还本金 | numeric | 23 | 10 | √ | 0 | 已还本金 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_extendapplybill_e |  | fentryid |
| 2 | idx_cfm_extendapplybill_e |  | fid,floanbillid |
