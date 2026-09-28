# 我的付款记录-occba_mymoneyincome_b2b

## 我的付款记录-主表 t_occba_moneyincome

- **表名称：** 我的付款记录-主表
- **表名：** t_occba_moneyincome

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsumrecamount | 付款总金额 | numeric | 23 | 10 | √ | 0 | 付款总金额 |
| 3 | freaccountname | 付款账户名称 | varchar | 255 |  | √ | ' ' | 付款账户名称 |
| 4 | fbilldate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 5 | freceivechannelid | 收款渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 6 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmoneytypeid | 资金类型 | int8 | 64 |  | √ | 0 | [资金类型 occba_moneytype_b2b](../occba_files/occba_moneytype_b2b.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fsalesyearid | 所属年份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 10 | fpooltype | 付款类别 | bpchar | 1 |  | √ | 'A' | 付款类别,枚举: A :品牌商 B :渠道商 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | frecaccountid | 收款银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 13 | fmoneyorgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fpayaccount | 付款账号 | varchar | 255 |  | √ | ' ' | 付款账号 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | frecbank | 收款银行 | varchar | 255 |  | √ | ' ' | 收款银行 |
| 17 | forderremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 18 | fpaycustomerid | 付款客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fpayaccountid | 付款银行账户Id | int8 | 64 |  | √ | 0 | 付款银行账户Id |
| 21 | fpayerbankid | 付款银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fmoneyaccountid | 资金账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fdatasources | 数据来源 | bpchar | 1 |  | √ | '2' | 数据来源,枚举: 0 :星瀚财务云 1 :EAS Cloud 2 :手工录入 3 :经销商提报 4 :星空旗舰版财务云 |
| 26 | fjoinsumrecamount | fjoinsumrecamount | numeric | 23 | 10 | √ | 0 |  |
| 27 | fpaytype | 支付方式 | bpchar | 1 |  | √ | '0' | 支付方式,枚举: 0 :银行转账 1 :现金 2 :微信 3 :支付宝 4 :其他 |
| 28 | fpaybank | 付款银行 | varchar | 255 |  | √ | ' ' | 付款银行 |
| 29 | fsalesmonthid | 所属月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 30 | fpaychannelid | 付款渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 31 | frecaccount | 收款账号 | varchar | 255 |  | √ | ' ' | 收款账号 |
| 32 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_moneyincome |  | fid |
| 2 | idx_occba_moneyincome_bno |  | fbillno |
| 3 | idx_occba_moneyincome_date |  | fbilldate |

---

## 我的付款记录-关联追踪表 t_occba_moneyincome_tc

- **表名称：** 我的付款记录-关联追踪表
- **表名：** t_occba_moneyincome_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_moneyincome_tc_tbill |  | ftbillid |
| 2 | pk_occba_moneyincome_tc |  | fid |
| 3 | idx_occba_moneyincome_tc_tid |  | ftid |

---

## 收款明细单据体-子表 t_occba_incomeentry

- **表名称：** 收款明细单据体-子表
- **表名：** t_occba_incomeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsettledintamt | 已结算利息 | numeric | 23 | 10 | √ | 0 | 已结算利息 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsalerid | 业务员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fjoinrecamount | 已生成付款单金额 | numeric | 23 | 10 | √ | 0 | 已生成付款单金额 |
| 6 | fpredictintamt | 预计利息 | numeric | 23 | 10 | √ | 0 | 预计利息 |
| 7 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 8 | finterest | 利息（%） | numeric | 23 | 10 | √ | 0 | 利息（%） |
| 9 | frecamount | 付款金额 | numeric | 23 | 10 | √ | 0 | 付款金额 |
| 10 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fusedamount | 已使用金额 | numeric | 23 | 10 | √ | 0 | 已使用金额 |
| 12 | funuseamount | 未使用金额 | numeric | 23 | 10 | √ | 0 | 未使用金额 |
| 13 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 14 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 15 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 16 | foutamount | 已调出金额 | numeric | 23 | 10 | √ | 0 | 已调出金额 |
| 17 | fintacctid | 利息账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 18 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 22 | fsettlechannelid | 收款渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 23 | fcalcintway | 计息方式 | bpchar | 1 |  | √ | 'A' | 计息方式,枚举: A :一次性计息 |
| 24 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fentryremark | 行备注 | varchar | 500 |  | √ | ' ' | 行备注 |
| 26 | freloutamount | 关联调出金额 | numeric | 23 | 10 | √ | 0 | 关联调出金额 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fwinterpolicyid | 冬储政策 | int8 | 64 |  | √ | 0 | [冬储款计息政策 occba_winterpolicy](../occba_files/occba_winterpolicy.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_incomeentry_fid |  | fid |
| 2 | pk_occba_incomeentry |  | fentryid |

---

## 我的付款记录-反写记录表 t_occba_moneyincome_wb

- **表名称：** 我的付款记录-反写记录表
- **表名：** t_occba_moneyincome_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_moneyincome_wb |  | fentryid |
| 2 | idx_occba_moneyincome_wb_fk |  | fid |

---

## 关联子实体-子表 t_occba_incomeentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occba_incomeentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_incomeentry_lk |  | fpkid |
| 2 | idx_occba_incomeentry_lk_fk |  | fentryid |
