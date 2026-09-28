# 分支机构税款分摊因素台账单据-tccit_branch_share_bill

## 分支机构税款分摊因素台账单据-主表 t_tccit_branch_share

- **表名称：** 分支机构税款分摊因素台账单据-主表
- **表名：** t_tccit_branch_share

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxorg | 税务组织信息 | int8 | 64 |  | √ | 0 | [税务组织信息 bastax_taxorg](../bastax_files/bastax_taxorg.md) |
| 3 | fparticipation | 总机构参与三因素分配 | bpchar | 1 |  | √ | '0' | 总机构参与三因素分配 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdeclaration | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 1 :独立 2 :汇总 3 :被汇总 |
| 6 | fhbfnszt | 是否是纳税主体 | varchar | 50 |  | √ | ' ' | 是否是纳税主体,枚举: 1 :是 0 :不是 |
| 7 | finitsharerate | 初始分配比例 | varchar | 50 |  | √ | ' ' | 初始分配比例 |
| 8 | funifiedsocialcode | 社会统一信用代码 | varchar | 50 |  | √ | ' ' | 社会统一信用代码 |
| 9 | fasset | 资产总额 | numeric | 23 | 10 | √ | 0 | 资产总额 |
| 10 | fdatastatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: 1 :已采集 2 :未采集 |
| 11 | fsumscheme | 汇总方案 | int8 | 64 |  | √ | 0 | [汇总方案 tctb_org_group_latest](../tctb_files/tctb_org_group_latest.md) |
| 12 | fnewinitsharerate | 初始分配比例（新字段） | numeric | 23 | 10 | √ | 0 | 初始分配比例（新字段） |
| 13 | fsharerate | 分配比例 | varchar | 50 |  | √ | ' ' | 分配比例 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | foperator | 操作人 | varchar | 50 |  | √ | ' ' | 操作人 |
| 17 | foperatetime | 操作时间 | varchar | 50 |  | √ | ' ' | 操作时间 |
| 18 | frefreshtime | 最新刷新时间 | timestamp | 0 |  |  | null | 最新刷新时间 |
| 19 | fincome | 营业收入 | numeric | 23 | 10 | √ | 0 | 营业收入 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fnewsharerate | 分配比例(新字段) | numeric | 23 | 10 | √ | 0 | 分配比例(新字段) |
| 22 | fnsrmc | 税务组织名称 | varchar | 50 |  | √ | ' ' | 税务组织名称 |
| 23 | fsalary | 职工薪酬 | numeric | 23 | 10 | √ | 0 | 职工薪酬 |
| 24 | fperiod | 所属税期 | timestamp | 0 |  |  | null | 所属税期 |
| 25 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统采集 2 :手工登记 3 :数据引入 |
| 26 | fusable | 数据是否可用 | varchar | 50 |  | √ | ' ' | 数据是否可用,枚举: 0 :不可用 1 :可用 |
| 27 | ftaxoffice | 主管税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 28 | forgname | 组织名称 | varchar | 250 |  | √ | ' ' | 组织名称 |
| 29 | fshareid | 是否分摊税款 | varchar | 50 |  | √ | ' ' | 是否分摊税款,枚举: true :是 false :否 |
| 30 | forgseq | 组织序号 | int4 | 32 |  | √ | 0 | 组织序号 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_branch_share |  | fid |
| 2 | idx_tccit_branch_share |  | forgid,fperiod |
