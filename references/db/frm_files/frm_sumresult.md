# 对账汇总结果-frm_sumresult

## 单据体-子表 t_frm_sumresultentry

- **表名称：** 单据体-子表
- **表名：** t_frm_sumresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbegindifflocal | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |
| 3 | fassist | 核算维度（隐藏） | varchar | 1000 |  | √ | ' ' | 核算维度（隐藏） |
| 4 | fendapplocal | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 5 | fenddiff | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fassistgl | 核算维度 | varchar | 255 |  | √ | ' ' | 核算维度 |
| 8 | fendgl | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |
| 9 | fbizassist | 业务维度（隐藏） | varchar | 255 |  | √ | ' ' | 业务维度（隐藏） |
| 10 | fbegindiff | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |
| 11 | fstatus | 对账结果 | bpchar | 1 |  | √ | ' ' | 对账结果,枚举: 1 :平衡 0 :不平衡 |
| 12 | fdebitapplocal | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 13 | fplandetailid | 对账方案分录id | int8 | 64 |  | √ | 0 | 对账方案分录id |
| 14 | fcreditapp | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 15 | fbeginapplocal | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 16 | fendgllocal | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |
| 17 | fcreditgllocal | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |
| 18 | fdebitapp | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 19 | fdebitdifflocal | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |
| 20 | fendapp | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 21 | fbegingllocal | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |
| 22 | fcreditapplocal | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 23 | fbizdataruleld | 业务取数规则 | int8 | 64 |  | √ | 0 | [业务取数规则 frm_recdatarule](../frm_files/frm_recdatarule.md) |
| 24 | fbizassist_tag | 业务维度（隐藏）_详情 | text | 0 |  |  | null | 业务维度（隐藏）_详情 |
| 25 | fassitapp | 业务维度 | varchar | 255 |  | √ | ' ' | 业务维度 |
| 26 | fcreditdiff | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |
| 27 | fcreditdifflocal | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |
| 28 | fruleentryids | 规则分录ID | varchar | 2000 |  | √ | ' ' | 规则分录ID |
| 29 | fcreditgl | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |
| 30 | fentryamounttype | 对账取值类型 | bpchar | 1 |  | √ | '3' | 对账取值类型,枚举: 3 :本期增加+本期减少+余额 2 :本期增加+本期减少 0 :本期增加 1 :本期减少 |
| 31 | fbeginapp | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 32 | fenddifflocal | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |
| 33 | fbegingl | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 36 | fdebitgl | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |
| 37 | fdebitdiff | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |
| 38 | fdebitgllocal | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_frm_sumresultentry |  | fid |
| 2 | pk_t_frm_sumresultentry |  | fentryid |

---

## 科目-多选基础资料表 t_frm_sumentry_acct

- **表名称：** 科目-多选基础资料表
- **表名：** t_frm_sumentry_acct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_frm_sumentry_acct |  | fpkid |
| 2 | idx_frm_sumresultentry_acct |  | fentryid |

---

## 对账汇总结果-主表 t_frm_sumresult

- **表名称：** 对账汇总结果-主表
- **表名：** t_frm_sumresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexecplanid | 业财对账方案 | int8 | 64 |  | √ | 0 | [业财对账方案 frm_reconciliation_scheme](../frm_files/frm_reconciliation_scheme.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | faccountbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 8 | fbizappid | 业务系统 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_frm_sumresult |  | fid |
| 2 | idx_frm_sumresult |  | faccountbookid,fperiodid,fexecplanid,fbizappid |

---

## 单据体-子表 t_frm_sumresultentry_plan

- **表名称：** 单据体-子表
- **表名：** t_frm_sumresultentry_plan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplandetailid | 对账方案分录id | int8 | 64 |  | √ | 0 | 对账方案分录id |
| 3 | fplanglsetting | 对账方案分录总账信息（存储） | varchar | 255 |  | √ | ' ' | 对账方案分录总账信息（存储） |
| 4 | fplanglsetting_tag | 对账方案分录总账信息（存储）_详情 | text | 0 |  |  | null | 对账方案分录总账信息（存储）_详情 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_frm_sumresultentry_plan |  | fentryid |
| 2 | idx_frm_sumresultentry_plan |  | fid |
