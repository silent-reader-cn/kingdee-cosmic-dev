# 部门额度表-er_dept_reimctl

## 部门额度表-主表 t_er_dept_reimctl

- **表名称：** 部门额度表-主表
- **表名：** t_er_dept_reimctl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fwbsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 4 | fnovemberamount | 11月 | numeric | 23 | 10 | √ | 0.0000000000 | 11月 |
| 5 | ftotalamount | 年总额度 | numeric | 23 | 10 | √ | 0.0000000000 | 年总额度 |
| 6 | ffebruaryamount | 2月 | numeric | 23 | 10 | √ | 0.0000000000 | 2月 |
| 7 | fcompany | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fseptemberamount | 9月 | numeric | 23 | 10 | √ | 0.0000000000 | 9月 |
| 9 | fquarter2 | 2季度 | numeric | 23 | 10 | √ | 0.0000000000 | 2季度 |
| 10 | fquarter3 | 3季度 | numeric | 23 | 10 | √ | 0.0000000000 | 3季度 |
| 11 | fquarter4 | 4季度 | numeric | 23 | 10 | √ | 0.0000000000 | 4季度 |
| 12 | fisyearforward | 已年度结转 | bpchar | 1 |  | √ | '0' | 已年度结转 |
| 13 | fjulyamount | 7月 | numeric | 23 | 10 | √ | 0.0000000000 | 7月 |
| 14 | famountchangeflag | 同步修改后面月份 | bpchar | 1 |  | √ | '0' | 同步修改后面月份 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fquarter1 | 1季度 | numeric | 23 | 10 | √ | 0.0000000000 | 1季度 |
| 17 | faugustamount | 8月 | numeric | 23 | 10 | √ | 0.0000000000 | 8月 |
| 18 | fauditstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :未审 1 :已审 3 :冻结 2 :关闭 |
| 19 | fwbsrcbilltype | 数据来源 | varchar | 25 |  | √ | 'er_reimctl_new' | 数据来源,枚举: er_reimctl_new :手工新增 er_reimctl_modify :手工调整 er_reimctlapplybill :额度申请单 |
| 20 | fmayamount | 5月 | numeric | 23 | 10 | √ | 0.0000000000 | 5月 |
| 21 | fcostcompany | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fjanuaryamount | 1月 | numeric | 23 | 10 | √ | 0.0000000000 | 1月 |
| 24 | fdecemberamount | 12月 | numeric | 23 | 10 | √ | 0.0000000000 | 12月 |
| 25 | fjuneamount | 6月 | numeric | 23 | 10 | √ | 0.0000000000 | 6月 |
| 26 | fdateyear | 年度 | varchar | 4 |  | √ | ' ' | 年度,枚举: 2018 :2018年 2019 :2019年 2020 :2020年 2021 :2021年 2022 :2022年 2023 :2023年 2024 :2024年 2025 :2025年 2026 :2026年 2027 :2027年 2028 :2028年 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fdept | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 30 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 33 | femployee | 职员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | foctoberamount | 10月 | numeric | 23 | 10 | √ | 0.0000000000 | 10月 |
| 35 | famounttype | 额度类型 | bpchar | 1 |  | √ | '2' | 额度类型,枚举: 1 :个人额度 2 :部门额度 |
| 36 | fmarchamount | 3月 | numeric | 23 | 10 | √ | 0.0000000000 | 3月 |
| 37 | faprilamount | 4月 | numeric | 23 | 10 | √ | 0.0000000000 | 4月 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_dept_reimctlt_emp |  | femployee,fexpenseitem,fdateyear |
| 2 | t_er_dept_reimctl_pkey |  | fid |
