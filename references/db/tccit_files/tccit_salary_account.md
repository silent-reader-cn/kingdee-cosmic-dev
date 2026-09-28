# 工资薪金台账-tccit_salary_account

## 工资薪金台账-主表 t_tccit_salary_account

- **表名称：** 工资薪金台账-主表
- **表名：** t_tccit_salary_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fprojectorpart | 项目/部门 | varchar | 50 |  | √ | ' ' | 项目/部门 |
| 4 | factualpaynotax | 实际发放的不可税前列支的其他工资 | numeric | 23 | 10 | √ | 0.0000000000 | 实际发放的不可税前列支的其他工资 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | forg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fmigration | 迁移状态 | varchar | 50 |  | √ | ' ' | 迁移状态 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | flastyearpay | 其中：发放上年金额 | numeric | 23 | 10 | √ | 0.0000000000 | 其中：发放上年金额 |
| 14 | faccountyear | 记账年度 | timestamp | 0 |  |  | null | 记账年度 |
| 15 | factualpay | 本年实际发放金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本年实际发放金额 |
| 16 | fgivemoney | 汇算清缴前发放金额 | numeric | 23 | 10 | √ | 0.0000000000 | 汇算清缴前发放金额 |
| 17 | fbillno | 业务编码 | varchar | 30 |  | √ | ' ' | 业务编码 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_salary_account |  | forg |
| 2 | pk_tccit_salary_account |  | fid |
