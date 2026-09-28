# 还款申请-cfm_repayapplybill_f7

## 还款申请-多语言表 t_cfm_repayapplybill_l

- **表名称：** 还款申请-多语言表
- **表名：** t_cfm_repayapplybill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 3 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
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

## 还款申请-主表 t_cfm_repayapplybill

- **表名称：** 还款申请-主表
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
| 7 | fcontractdrawamt | fcontractdrawamt | numeric | 19 | 6 | √ | 0 |  |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fbusinessstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: 1 :申请中 2 :办理中 3 :未办理 4 :已办理 5 :已退单 |
| 10 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | floancontractbillid | 合同单据编号 | int8 | 64 |  | √ | 0 | [借款合同 cfm_loancontractbill_f7](../cfm_files/cfm_loancontractbill_f7.md) |
| 15 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 16 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 17 | fisratio | fisratio | bpchar | 1 |  | √ | '0' |  |
| 18 | frepayway | 还款选择方式 | varchar | 50 |  | √ | ' ' | 还款选择方式,枚举: contractrepay :按借款合同还款 loanrepay :按提款单还款 |
| 19 | fnotrepayamt | fnotrepayamt | numeric | 19 | 6 | √ | 0 |  |
| 20 | ftotalamt | ftotalamt | numeric | 19 | 6 | √ | 0 |  |
| 21 | floantype | floantype | varchar | 50 |  | √ | ' ' |  |
| 22 | fbizdate | fbizdate | timestamp | 0 |  |  | null |  |
| 23 | fdatasource | fdatasource | varchar | 50 |  | √ | ' ' |  |
| 24 | finstamt | finstamt | numeric | 19 | 6 | √ | 0 |  |
| 25 | fcurrencyid | 借款币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cfm_repayapplybill |  | fbillno,fbillstatus |
| 2 | pk_cfm_repayapplybill |  | fid |
