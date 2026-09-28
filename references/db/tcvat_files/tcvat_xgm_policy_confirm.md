# 小规模政策确认-tcvat_xgm_policy_confirm

## 小规模政策确认-主表 t_tcvat_policyconfirm

- **表名称：** 小规模政策确认-主表
- **表名：** t_tcvat_policyconfirm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fruledata | 规则数据 | varchar | 255 |  | √ | ' ' | 规则数据 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | flevytype | 征收方式: | varchar | 50 |  | √ | ' ' | 征收方式:,枚举: czzs :查账征收 aqhz :按期汇总 hdzs :核定征收 |
| 5 | fbqsfsyjzzc | fbqsfsyjzzc | varchar | 50 |  | √ | ' ' |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | freportperiod | 申报属期： | timestamp | 0 |  |  | null | 申报属期： |
| 8 | ftaxplayeraptitude | 纳税人类型: | varchar | 100 |  | √ | ' ' | 纳税人类型:,枚举: zzsybnsr :一般纳税人 zzsxgmnsr :小规模纳税人 |
| 9 | fstatus | 状态 | varchar | 100 |  | √ | ' ' | 状态 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbillno | 底稿编号 | varchar | 60 |  | √ | ' ' | 底稿编号 |
| 12 | fruledata_tag | 规则数据_详情 | text | 0 |  |  | null | 规则数据_详情 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fcodeandname | 所属行业: | int8 | 64 |  | √ | 0 | 行业代码及名称 tpo_tcvat_industrycode |
| 17 | fdeclaretype | 申报方式: | varchar | 50 |  | √ | ' ' | 申报方式:,枚举: 1 :独立申报 2 :汇总申报 3 :被汇总申报 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 20 | fapplicablediffer | fapplicablediffer | bpchar | 1 |  | √ | ' ' |  |
| 21 | fisapplicableplus | fisapplicableplus | bpchar | 1 |  | √ | ' ' |  |
| 22 | fdeadline | 缴纳期限: | varchar | 30 |  | √ | ' ' | 缴纳期限:,枚举: acsb :按次申报 aysb :按月申报 ajsb :按季申报 |
| 23 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 24 | fregistertype | 登记注册类型: | int8 | 64 |  | √ | 0 | [注册登记类型 tax_info_registertype](../tctb_files/tax_info_registertype.md) |
| 25 | fdeductionrate | fdeductionrate | varchar | 30 |  | √ | ' ' |  |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_policyconfirm |  | freportperiod,forgid |
| 2 | t_tcvat_policyconfirm_pkey |  | fid |
