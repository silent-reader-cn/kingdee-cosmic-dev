# 对账汇总结果-frm_sumresult

## 单据体-子表 t_frm_sumresultentry

- **表名称：** 单据体-子表
- **表名：** t_frm_sumresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassist | 核算维度（隐藏） | varchar | 1000 |  | √ | ' ' | 核算维度（隐藏） |
| 3 | fenddiff | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fassistgl | 核算维度 | varchar | 255 |  | √ | ' ' | 核算维度 |
| 6 | fendgl | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |
| 7 | fbizassist | 业务维度（隐藏） | varchar | 255 |  | √ | ' ' | 业务维度（隐藏） |
| 8 | fbegindiff | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |
| 9 | fstatus | 对账结果 | bpchar | 1 |  | √ | ' ' | 对账结果,枚举: 1 :平衡 0 :不平衡 |
| 10 | fplandetailid | 对账方案分录id | int8 | 64 |  | √ | 0 | 对账方案分录id |
| 11 | fcreditapp | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 12 | fdebitapp | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 13 | fendapp | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 14 | fbizdataruleld | 业务取数规则 | int8 | 64 |  | √ | 0 | 业务取数规则 frm_recdatarule |
| 15 | fbizassist_tag | 业务维度（隐藏）_详情 | text | 0 |  |  | null | 业务维度（隐藏）_详情 |
| 16 | fassitapp | 业务维度 | varchar | 255 |  | √ | ' ' | 业务维度 |
| 17 | fcreditdiff | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |
| 18 | fruleentryids | 规则分录ID | varchar | 2000 |  | √ | ' ' | 规则分录ID |
| 19 | fcreditgl | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |
| 20 | fentryamounttype | 对账取值类型 | bpchar | 1 |  | √ | '3' | 对账取值类型,枚举: 3 :本期增加+本期减少+余额 2 :本期增加+本期减少 0 :本期增加 1 :本期减少 |
| 21 | fbeginapp | 业务系统 | numeric | 23 | 10 | √ | 0 | 业务系统 |
| 22 | fbegingl | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | fdebitgl | 总账 | numeric | 23 | 10 | √ | 0 | 总账 |
| 26 | fdebitdiff | 差异 | numeric | 23 | 10 | √ | 0 | 差异 |

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
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
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
| 2 | fexecplanid | 业财对账方案 | int8 | 64 |  | √ | 0 | 业财对账方案 frm_reconciliation_scheme |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | faccountbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 8 | fbizappid | 业务系统 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
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
