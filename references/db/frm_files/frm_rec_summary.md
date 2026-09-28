# 对账汇总结果快照-frm_rec_summary

## 对账汇总结果快照-主表 t_frm_rec_summary

- **表名称：** 对账汇总结果快照-主表
- **表名：** t_frm_rec_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 3 | fexecplanid | 对账方案 | int8 | 64 |  | √ | 0 | [业财对账方案 frm_reconciliation_scheme](../frm_files/frm_reconciliation_scheme.md) |
| 4 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fdataruleid | 取数规则 | int8 | 64 |  | √ | 0 | [业务取数规则 frm_recdatarule](../frm_files/frm_recdatarule.md) |
| 9 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 10 | fbizappid | 业务系统 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_frm_rec_summary |  | fid |
| 2 | idx_frm_sumsnapshot |  | forgid,fperiodid,fbizappid,fbooktypeid |

---

## 科目-多选基础资料表 t_frm_rec_sumentry_acct

- **表名称：** 科目-多选基础资料表
- **表名：** t_frm_rec_sumentry_acct

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
| 1 | pk_t_frm_rec_sumentry_acct |  | fpkid |
| 2 | idx_frm_rec_sumssen_acct |  | fentryid |

---

## 单据体-子表 t_frm_rec_summaryentry

- **表名称：** 单据体-子表
- **表名：** t_frm_rec_summaryentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassist | 核算维度（隐藏） | varchar | 255 |  | √ | ' ' | 核算维度（隐藏） |
| 3 | fenddiff | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fassistgl | 核算维度 | varchar | 255 |  | √ | ' ' | 核算维度 |
| 6 | fendgl | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |
| 7 | fbizassist | 业务维度（隐藏） | varchar | 255 |  | √ | ' ' | 业务维度（隐藏） |
| 8 | fbegindiff | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |
| 9 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 1 :对平 0 :未对平 |
| 10 | fplandetailid | 对账方案分录id | int8 | 64 |  | √ | 0 | 对账方案分录id |
| 11 | fassisttype | 方案页签类型 | int4 | 32 |  | √ | 0 | 方案页签类型 |
| 12 | fcreditapp | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 13 | fruleid | 规则分录id | varchar | 2000 |  | √ | ' ' | 规则分录id |
| 14 | fdebitapp | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 15 | fignorediff | 忽略不平 | bpchar | 1 |  | √ | '0' | 忽略不平 |
| 16 | fendapp | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 17 | fbizassist_tag | 业务维度（隐藏）_详情 | text | 0 |  | √ | ' ' | 业务维度（隐藏）_详情 |
| 18 | fassitapp | 业务维度 | varchar | 255 |  | √ | ' ' | 业务维度 |
| 19 | fcreditdiff | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |
| 20 | fcreditgl | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |
| 21 | finitdiff | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |
| 22 | finitapp | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 23 | finitgl | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |
| 24 | fbeginapp | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 25 | fbegingl | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | fdebitgl | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |
| 29 | fdebitdiff | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_frm_rec_summaryentry |  | fentryid |
| 2 | idx_frm_rec_sumssentry |  | fid |
