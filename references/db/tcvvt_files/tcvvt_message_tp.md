# 信息确认暂存表-tcvvt_message_tp

## 单据体-子表 t_tcvvt_xxqr_temp

- **表名称：** 单据体-子表
- **表名：** t_tcvvt_xxqr_temp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fselectid | 选择的id | int8 | 64 |  | √ | 0 | 选择的id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_xxqr_temp_fk |  | fid |
| 2 | pk_tcvvt_xxqr_temp |  | fentryid |

---

## 信息确认暂存表-主表 t_tcvvt_message_tp

- **表名称：** 信息确认暂存表-主表
- **表名：** t_tcvvt_message_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 3 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :未开始 1 :第一步 2 :第二步 |
| 4 | fstartdate | 开始时间： | timestamp | 0 |  |  | null | 开始时间： |
| 5 | forgid | 组织名称： | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fnewrule | 执行新准则： | varchar | 50 |  | √ | ' ' | 执行新准则：,枚举: yes :已执行 no :未执行 |
| 7 | freporttype | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型,枚举: aysb :月度 ajsb :季度 ansb :年度 |
| 8 | fdeclaretype | 申报企业类型： | varchar | 50 |  | √ | ' ' | 申报企业类型：,枚举: 100 :非跨地区经营企业 210 :总机构（跨省）——适用《跨地区经营汇总纳税企业所得税征收管理办法》 220 :总机构（跨省）——不适用《跨地区经营汇总纳税企业所得税征收管理办法》 230 :总机构（省内） 311 :分支机构（须进行完整年度申报并按比例纳税） 312 :分支机构（须进行完整年度申报但不就地缴纳） |
| 9 | fdeclaretype1criterion | 会计准则或会计制度： | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_message_tp |  | fenddate,forgid,fstartdate,fdeclaretype |
| 2 | pk_tcvvt_message_tp |  | fid |
