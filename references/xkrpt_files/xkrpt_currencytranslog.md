# 外币折算日志-xkrpt_currencytranslog

## 项目明细-子表 t_xkrpt_cts_log_itementry

- **表名称：** 项目明细-子表
- **表名：** t_xkrpt_cts_log_itementry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | ftransrate | 折算汇率 | varchar | 50 |  | √ | ' ' | 折算汇率 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fhisitemamount | 历史项目金额 | numeric | 23 | 10 | √ | 0 | 历史项目金额 |
| 6 | fitemcode | 报表项目编码 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 7 | ftransmethod | 折算方法 | int8 | 64 |  | √ | 0 | 外币折算方法 xkrpt_translation_method |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fitemdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_cts_log_item_eid |  | fentryid |
| 2 | pk_xkrpt_cts_log_itementry |  | fdetailid |

---

## 报表明细-子表 t_xkrpt_cts_log_rptentry

- **表名称：** 报表明细-子表
- **表名：** t_xkrpt_cts_log_rptentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetcurrency | 折算后币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | frptcode | 报表id标识 | varchar | 36 |  | √ | ' ' | 报表id标识 |
| 4 | ftransstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 0 :失败 1 :成功 2 :部分成功 |
| 5 | fsrccurrency | 折算前币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fyear | 年 | int4 | 32 |  | √ | 0 | 年 |
| 7 | fcompany | 公司名称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fperiod | 期 | int4 | 32 |  | √ | 0 | 期 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fmsg | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fscope | 合并范围 | int8 | 64 |  | √ | 0 | 合并范围 xkcr_scope |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_cts_log_rptentry |  | fentryid |
| 2 | idx_xkrpt_cts_log_rptentry_fid |  | fid |

---

## 外币折算日志-主表 t_xkrpt_currencytranslog

- **表名称：** 外币折算日志-主表
- **表名：** t_xkrpt_currencytranslog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcurrencytransscheme | 外币折算方案 | int8 | 64 |  | √ | 0 | 折算方案 xkrpt_currencyscheme |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | frptcount | 参加折算报表数 | int4 | 32 |  | √ | 0 | 参加折算报表数 |
| 5 | fexecstatus | 执行状态 | bpchar | 1 |  | √ | ' ' | 执行状态,枚举: 0 :失败 1 :成功 2 :部分成功 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fexecdatetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 9 | fsuccessrptcount | 成功折算报表 | int4 | 32 |  | √ | 0 | 成功折算报表 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_currencytranslog_sid |  | fcurrencytransscheme |
| 2 | pk_xkrpt_currencytranslog |  | fid |
