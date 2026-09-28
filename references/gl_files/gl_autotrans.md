# 自动转账-gl_autotrans

## 分录信息-子表 t_gl_autotransentry

- **表名称：** 分录信息-子表
- **表名：** t_gl_autotransentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | foriginalamount | 原币金额 | numeric | 19 | 6 | √ | 0.000000 | 原币金额 |
| 4 | fprice | 单价 | numeric | 23 | 4 | √ | 0.0000 | 单价 |
| 5 | fdatasourcetype | 数据来源 | varchar | 5 |  | √ | '0' | 数据来源,枚举: 1 :转入 2 :按比例转出余额 3 :按比例转出本期借方发生额 4 :按比例转出本期贷方发生额 12 :按公式转出 13 :按公式转入 5 :按指定科目转出 6 :按指定科目转入 7 :按差额转入 8 :按报表设置转出 9 :按报表设置转入 10 :按Excel设置转出 11 :按Excel设置转入 |
| 6 | fqtyformula | 数量取数公式 | varchar | 2000 |  |  | ' ' | 数量取数公式 |
| 7 | fautorowid | 行ID | varchar | 50 |  | √ | ' ' | 行ID |
| 8 | fhaspostvoucher | fhaspostvoucher | bpchar | 1 |  | √ | '0' |  |
| 9 | fassisttranstype | 核算维度方式 | bpchar | 1 |  | √ | ' ' | 核算维度方式,枚举: 2 :自定义 1 :自动生成 |
| 10 | fpercenttype | 转账比例方式 | bpchar | 1 |  | √ | '0' | 转账比例方式,枚举: 0 :固定值 1 :自定义 |
| 11 | fqtyfrom | 数量来源 | varchar | 2 |  | √ | ' ' | 数量来源,枚举: 0 :固定值 1 :公式 2 :科目 3 :excel 4 :报表 |
| 12 | fpercent | 转账比例 | varchar | 30 |  | √ | ' ' | 转账比例 |
| 13 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 14 | fdc | 转账方向 | varchar | 2 |  | √ | '0' | 转账方向,枚举: 0 :自动平衡 1 :借 -1 :贷 |
| 15 | fassgrp | 核算维度 | varchar | 2000 |  | √ | ' ' | 核算维度 |
| 16 | fautotransdctype | fautotransdctype | bpchar | 1 |  | √ | '1' |  |
| 17 | fbcmformulajson | 金额取数公式（ACCT） | varchar | 2000 |  |  | ' ' | 金额取数公式（ACCT） |
| 18 | frptexp | 取数表达式 | varchar | 300 |  | √ | ' ' | 取数表达式 |
| 19 | fpercentexp | 比例公式id | int8 | 64 |  | √ | 0 | 比例公式id |
| 20 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 23 | fautopercent | 转账比例 | numeric | 19 | 6 | √ | 0.000000 | 转账比例 |
| 24 | fautodescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 25 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_autotransentry_pkey |  | fentryid |
| 2 | idx_gl_autotransentry_fid |  | fid |

---

## 自动转账-主表 t_gl_autotrans

- **表名称：** 自动转账-主表
- **表名：** t_gl_autotrans

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fcreatorid | 编制人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | faccountbook | faccountbook | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 8 | fvoucherentrysort | 凭证分录顺序 | bpchar | 1 |  | √ | '0' | 凭证分录顺序,枚举: 1 :模板顺序 2 :先转出后转入 3 :先借后贷 |
| 9 | fincurredamount | 应该发生金额 | numeric | 19 | 6 | √ | 0.000000 | 应该发生金额 |
| 10 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fdptnames | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fvouchernumber | fvouchernumber | varchar | 255 |  | √ | ' ' |  |
| 14 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 15 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 16 | fbookid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 17 | fvouchertypeid | 凭证字 | int8 | 64 |  | √ | 0 | 凭证字 gl_vouchertype |
| 18 | faccountbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 19 | fattachments | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 20 | ftransfertype | 转账类型 | bpchar | 1 |  | √ | '0' | 转账类型,枚举: 1 :普通转账 2 :结转损益 |
| 21 | fgeneratedamount | 已发生金额 | numeric | 19 | 6 | √ | 0.000000 | 已发生金额 |
| 22 | fvoucherdatetype | 凭证日期 | bpchar | 1 |  | √ | '1' | 凭证日期,枚举: 1 :期末最后一天 2 :系统日期 |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 24 | fleafintype | 转入非明细科目 | bpchar | 1 |  | √ | '0' | 转入非明细科目,枚举: 0 :平均结转 1 :按编码结转 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_autotrans_fid |  | forgid,fbookid |
| 2 | t_gl_autotrans_pkey |  | fid |

---

## 自动转账-多语言表 t_gl_autotrans_l

- **表名称：** 自动转账-多语言表
- **表名：** t_gl_autotrans_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_autotrans_l_pkey |  | fpkid |
| 2 | idx_gl_autotrans_l |  | fid,flocaleid |
