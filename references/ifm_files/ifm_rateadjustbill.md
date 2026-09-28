# 内部贷款利率调整-ifm_rateadjustbill

## 内部贷款利率调整-主表 t_cfm_rateadjustbill

- **表名称：** 内部贷款利率调整-主表
- **表名：** t_cfm_rateadjustbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 借款单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fnotrepayamount | 未收回本金 | numeric | 19 | 6 | √ | 0 | 未收回本金 |
| 4 | fafterratesign | 调整后利率浮动基点（BP） | varchar | 50 |  | √ | ' ' | 调整后利率浮动基点（BP）,枚举: add :加 subtract :减 |
| 5 | famount | 借款金额 | numeric | 19 | 6 | √ | 0 | 借款金额 |
| 6 | frefrateid | 参考利率 | int8 | 64 |  | √ | 0 | 参考利率 tbd_referrate |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fafterratefloatpoint | 调整利率浮动基点（BP） | numeric | 23 | 10 | √ | 0 | 调整利率浮动基点（BP） |
| 10 | fcreditorgid | 债权人(组织) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fdrawamount | 已放款金额 | numeric | 19 | 6 | √ | 0 | 已放款金额 |
| 12 | fratefloatpoint | 调整利率浮动基点（BP） | numeric | 23 | 10 | √ | 0 | 调整利率浮动基点（BP） |
| 13 | fbillno | 利率调整单编号 | varchar | 30 |  | √ | ' ' | 利率调整单编号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fafterrefrateid | 调整后参考利率 | int8 | 64 |  | √ | 0 | 参考利率 tbd_referrate |
| 16 | frateadjustkey | 利率重置周期 | varchar | 50 |  | √ | ' ' | 利率重置周期,枚举: D :按天 W :按周 M :按月 |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fadjustele | 调整选项 | varchar | 50 |  | √ | ' ' | 调整选项,枚举: adjustcontract :调整合同 adjustloan :调整提款 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fproductfactoryid | 融资模型 | int8 | 64 |  | √ | 0 | 融资模型 cfm_productfactory |
| 21 | floancontractbillid | 合同单据编号 | int8 | 64 |  | √ | 0 | 融资合同 cfm_loancontractbill_f7 |
| 22 | frateadjustval | 利率重置周期值 | int8 | 64 |  | √ | 0 | 利率重置周期值 |
| 23 | fafterrateadjustkey | 调整后利率重置周期 | varchar | 50 |  | √ | ' ' | 调整后利率重置周期,枚举: D :按天 W :按周 M :按月 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 26 | fafterrateadjustval | 调整利率重置周期值 | int8 | 64 |  | √ | 0 | 调整利率重置周期值 |
| 27 | fadjusteffectdate | 调整生效日期 | timestamp | 0 |  |  | null | 调整生效日期 |
| 28 | fcreditortype | 债权人类型 | varchar | 50 |  | √ | ' ' | 债权人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 settlecenter :结算中心 custom :客商 other :其他 |
| 29 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: cfm :融资管理 invest :投资管理 bond :债券 ifm :内部金融管理 |
| 30 | fafterinterestrate | 合同调整后利率（%） | numeric | 23 | 10 | √ | 0 | 合同调整后利率（%） |
| 31 | finterestrate | 合同利率(%) | numeric | 23 | 10 | √ | 0 | 合同利率(%) |
| 32 | fcurrencyid | 借款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fratesign | 利率浮动基点（BP） | varchar | 50 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_rateadjustbill |  | fid |
| 2 | idx_cfm_rateadjustbill |  | fproductfactoryid |

---

## 单据体-子表 t_cfm_rateadjustbill_e

- **表名称：** 单据体-子表
- **表名：** t_cfm_rateadjustbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fafterlratesign | 调整后(加,减) | varchar | 50 |  | √ | ' ' | 调整后(加,减),枚举: add :加 subtract :减 |
| 3 | flloanrate | 放款利率（%） | numeric | 23 | 10 | √ | 0 | 放款利率（%） |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | flnotrepayamount | 未收本金 | numeric | 19 | 6 | √ | 0 | 未收本金 |
| 6 | fldrawbillid | 放款单编号 | int8 | 64 |  | √ | 0 | 提款处理 cfm_loanbill_f7 |
| 7 | fafterlratefloatpoint | 调整后利率浮动基点（BP） | numeric | 19 | 6 | √ | 0 | 调整后利率浮动基点（BP） |
| 8 | flratesign | (加,减) | varchar | 50 |  | √ | ' ' | (加,减),枚举: add :加 subtract :减 |
| 9 | flratefloatpoint | 利率浮动基点（BP） | numeric | 19 | 6 | √ | 0 | 利率浮动基点（BP） |
| 10 | flisadjust | 利率调整 | bpchar | 1 |  | √ | '0' | 利率调整 |
| 11 | fldrawamount | 放款金额 | numeric | 19 | 6 | √ | 0 | 放款金额 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fafterloanrate | 调整后放款利率（%） | numeric | 23 | 10 | √ | 0 | 调整后放款利率（%） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_rateadjustbill_e |  | fentryid |
| 2 | idx_cfm_rateadjustbill_e |  | fid |
