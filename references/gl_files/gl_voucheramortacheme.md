# 凭证摊销-gl_voucheramortacheme

## 凭证摊销-主表 t_gl_voucheramortscheme

- **表名称：** 凭证摊销-主表
- **表名：** t_gl_voucheramortscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famortamount | 已摊销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已摊销金额 |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ftotalamount | 总摊销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 总摊销金额 |
| 5 | faccountbooksid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 6 | fismultiplebook | 是否多账簿 | bpchar | 1 |  | √ | '0' | 是否多账簿 |
| 7 | famortstyle | 摊销方式 | bpchar | 1 |  | √ | '1' | 摊销方式,枚举: 1 :按平均比例 2 :按固定额 3 :按日期摊销 4 :自定义 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | famortabstract | 凭证摘要 | varchar | 255 |  | √ | ' ' | 凭证摘要 |
| 10 | fenddate | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 11 | fplanperiod | 待摊销期间数 | numeric | 23 | 10 | √ | 0.0000000000 | 待摊销期间数 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fborrowingdirection | 借贷方向 | varchar | 30 |  | √ | ' ' | 借贷方向,枚举: 1 :待摊科目在贷，转入科目在借 0 :待摊科目在借，转入科目在贷 |
| 14 | famortstatus | 摊销状态 | bpchar | 1 |  | √ | '4' | 摊销状态,枚举: 1 :已启用 2 :进行中 3 :已完成 4 :已禁用 |
| 15 | fperiodamortamount | 每期摊销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 每期摊销金额 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: A :创建 B :已提交 C :已审核 D :作废 Z :暂存 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fbegindate | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 21 | fdptnames | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fstartperiodid | 开始期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 25 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 26 | fvouchertypeid | 生成凭证字 | int8 | 64 |  | √ | 0 | 凭证字 gl_vouchertype |
| 27 | fattachments | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 1 :启用 0 :禁用 |
| 29 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 30 | fcurrencyid | 本位币币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 31 | famortperiod | 已摊销期间数 | numeric | 23 | 10 | √ | 0.0000000000 | 已摊销期间数 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_voucheramortscheme |  | fid |
| 2 | idx_gl_voucheramortscheme |  | forgid,faccountbooksid |

---

## 凭证摊销-多语言表 t_gl_voucheramortscheme_l

- **表名称：** 凭证摊销-多语言表
- **表名：** t_gl_voucheramortscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_voucheramortscheme_l |  | fid,flocaleid |
| 2 | t_gl_voucheramortscheme_l_pkey |  | fpkid |

---

## 待摊科目-子表 t_gl_targetaccount

- **表名称：** 待摊科目-子表
- **表名：** t_gl_targetaccount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassgrpid | 核算维度（废弃） | int8 | 64 |  | √ | 0 | 核算维度 bd_asstacttype |
| 3 | fassgrp | 核算维度 | varchar | 2000 |  | √ | ' ' | 核算维度 |
| 4 | ftargetlocal | 本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 本位币金额 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fplandirection | 生成方向 | varchar | 2 |  | √ | '-1' | 生成方向,枚举: 1 :借 -1 :贷 |
| 7 | ftargetcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 8 | ftargetrowid | 行ID | varchar | 50 |  | √ | ' ' | 行ID |
| 9 | frate | 汇率 | numeric | 23 | 4 | √ | 0.0000 | 汇率 |
| 10 | fplantype | 取值来源 | bpchar | 1 |  | √ | '0' | 取值来源,枚举: 0 :固定值 1 :期末余额 2 :按凭证号 |
| 11 | ftargetassgrpcombo | ftargetassgrpcombo | bpchar | 1 |  | √ | '1' |  |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 14 | fplanamount | 待摊金额 | numeric | 19 | 6 | √ | 0.000000 | 待摊金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_targetaccount |  | fid |
| 2 | t_gl_targetaccount_pkey |  | fentryid |

---

## 自定义摊销-子表 t_gl_custompolicies

- **表名称：** 自定义摊销-子表
- **表名：** t_gl_custompolicies

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fcperiod | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fcamount | 摊销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 摊销金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_custompolicies |  | fentryid |
| 2 | idx_gl_custompolicies_fid |  | fid |

---

## 单据体-子表 t_gl_amortdetail

- **表名称：** 单据体-子表
- **表名：** t_gl_amortdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdetailaccountid | 科目 | int8 | 64 |  | √ | 0 | 科目 |
| 3 | fdetailassgrpid | 维度 | int8 | 64 |  | √ | 0 | 维度 |
| 4 | fdetailloctotal | 该维度本位币 | numeric | 21 | 6 | √ | 0 | 该维度本位币 |
| 5 | fdetailoritotal | 该维度原币 | numeric | 21 | 6 | √ | 0 | 该维度原币 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fdetailrowid | rowid | varchar | 50 |  | √ | ' ' | rowid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_amortdetail_fid |  | fid |
| 2 | pk_t_gl_amortdetail |  | fentryid |

---

## 摊销期间-子表 t_gl_policy

- **表名称：** 摊销期间-子表
- **表名：** t_gl_policy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fperioddetail | 本次摊销信息 | text | 0 |  |  | null | 本次摊销信息 |
| 3 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | fratio | 比例(%) | numeric | 19 | 6 | √ | 0.000000 | 比例(%) |
| 5 | fcuramortperiod | 本期摊销期间数 | numeric | 23 | 10 | √ | 0.0000000000 | 本期摊销期间数 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | famount | 摊销金额 | numeric | 19 | 6 | √ | 0.000000 | 摊销金额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fisvouchered | 是否已生成凭证 | bpchar | 1 |  | √ | '0' | 是否已生成凭证 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_policy_pkey |  | fentryid |
| 2 | idx_gl_policy |  | fid |

---

## 转入科目-子表 t_gl_destaccount

- **表名称：** 转入科目-子表
- **表名：** t_gl_destaccount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdestamount | 摊销金额 | numeric | 19 | 6 | √ | 0.000000 | 摊销金额 |
| 3 | fdestrowid | 行ID | varchar | 50 |  | √ | ' ' | 行ID |
| 4 | fassgrpid | 核算维度（废弃） | int8 | 64 |  | √ | 0 | 核算维度 bd_asstacttype |
| 5 | fratio | 比例(%) | numeric | 19 | 6 | √ | 0.000000 | 比例(%) |
| 6 | fdesttype | 取值方式 | bpchar | 1 |  | √ | '1' | 取值方式,枚举: 1 :按比例 2 :按金额 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fdestcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 9 | fdestdirection | 生成方向 | varchar | 2 |  | √ | '1' | 生成方向,枚举: 1 :借 -1 :贷 |
| 10 | fdestassgrp | 核算维度 | varchar | 2000 |  | √ | ' ' | 核算维度 |
| 11 | fdestassgrpcombo | fdestassgrpcombo | bpchar | 1 |  | √ | '1' |  |
| 12 | fdestlocal | 本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 本位币金额 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | faccountid | 科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_destaccount_pkey |  | fentryid |
| 2 | idx_gl_destaccount |  | fid |
