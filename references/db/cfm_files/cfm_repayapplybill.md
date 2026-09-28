# 借款还款申请-cfm_repayapplybill

## 提款信息-子表 t_cfm_repayapplybill_e

- **表名称：** 提款信息-子表
- **表名：** t_cfm_repayapplybill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floanbillid | 提款单编号 | int8 | 64 |  | √ | 0 | [提款处理单 cfm_loanbill_f7](../cfm_files/cfm_loanbill_f7.md) |
| 3 | fpreintamt | 预计利息金额 | numeric | 19 | 6 | √ | 0 | 预计利息金额 |
| 4 | fnotrepayamount | 未还本金 | numeric | 19 | 6 | √ | 0 | 未还本金 |
| 5 | fdrawamount | 提款金额 | numeric | 19 | 6 | √ | 0 | 提款金额 |
| 6 | fispayinst | 付息 | bpchar | 1 |  | √ | '0' | 付息 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | frepayamount | 预计还款金额 | numeric | 19 | 6 | √ | 0 | 预计还款金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_repayapplybill_e |  | fentryid |
| 2 | idx_cfm_repayapplybill_e |  | fid |

---

## 借款还款申请-多语言表 t_cfm_repayapplybill_l

- **表名称：** 借款还款申请-多语言表
- **表名：** t_cfm_repayapplybill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 3 | fdescription | 申请说明 | varchar | 255 |  | √ | ' ' | 申请说明 |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | '0' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_repayapplybill_l |  | fpkid |
| 2 | idx_cfm_repayapplybill_l |  | fid |

---

## 借款还款申请-主表 t_cfm_repayapplybill

- **表名称：** 借款还款申请-主表
- **表名：** t_cfm_repayapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprerepaydate | 预计还款日期 | timestamp | 0 |  |  | null | 预计还款日期 |
| 3 | forgid | 借款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | famount | 申请还款金额 | numeric | 19 | 6 | √ | 0 | 申请还款金额 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcontractdrawamt | 合同提款金额 | numeric | 19 | 6 | √ | 0 | 合同提款金额 |
| 8 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 9 | fbusinessstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: 1 :申请中 2 :办理中 3 :未办理 4 :已办理 5 :已退单 |
| 10 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | floancontractbillid | 合同单据编号 | int8 | 64 |  | √ | 0 | [借款合同 cfm_loancontractbill_f7](../cfm_files/cfm_loancontractbill_f7.md) |
| 15 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 16 | fdescription | 申请说明 | varchar | 255 |  | √ | ' ' | 申请说明 |
| 17 | fisratio | 按比例还款 | bpchar | 1 |  | √ | '0' | 按比例还款 |
| 18 | frepayway | 还款选择方式 | varchar | 50 |  | √ | ' ' | 还款选择方式,枚举: contractrepay :按借款合同还款 loanrepay :按提款单还款 |
| 19 | fnotrepayamt | 合同剩余未还金额 | numeric | 19 | 6 | √ | 0 | 合同剩余未还金额 |
| 20 | ftotalamt | 申请还本付息总金额 | numeric | 19 | 6 | √ | 0 | 申请还本付息总金额 |
| 21 | floantype | 贷款类型 | varchar | 50 |  | √ | ' ' | 贷款类型,枚举: loan :普通贷款 sl :银团贷款 ec :企业往来 entrust :委托贷款 bond :债券发行 |
| 22 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 23 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: cfm :融资管理 invest :投资管理 bond :债券 ifm :内部金融管理 |
| 24 | finstamt | 申请付息金额 | numeric | 19 | 6 | √ | 0 | 申请付息金额 |
| 25 | fcurrencyid | 借款币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cfm_repayapplybill |  | fbillno,fbillstatus |
| 2 | pk_cfm_repayapplybill |  | fid |
