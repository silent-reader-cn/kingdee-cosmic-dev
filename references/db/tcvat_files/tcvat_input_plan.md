# 进项智能测算-tcvat_input_plan

## 进项智能测算-主表 t_tcvat_input_plan

- **表名称：** 进项智能测算-主表
- **表名：** t_tcvat_input_plan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsqsfl | 上期税负率 | numeric | 23 | 10 | √ | 0.0000000000 | 上期税负率 |
| 3 | fbqhdsre | 本期核定收入额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期核定收入额 |
| 4 | fbqjxzce | 本期进项转出额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期进项转出额 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fskssq | 税款所属期 | varchar | 100 |  | √ | ' ' | 税款所属期 |
| 8 | fbqmdtse | 本期免抵退税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期免抵退税额 |
| 9 | fbqsyyrzjxse | 本期剩余应认证进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期剩余应认证进项税额 |
| 10 | fbqyjsre | 本期预计收入额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期预计收入额 |
| 11 | fbqjhdkjxse | 本期计划抵扣进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期计划抵扣进项税额 |
| 12 | fbqyjrzjxse | 本期已认证进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期已认证进项税额 |
| 13 | fbqyjynse | 本期预计应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期预计应纳税额 |
| 14 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fbqyrzjxse | 本期应认证进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应认证进项税额 |
| 16 | fbqynsjze | 本期应纳税减征额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应纳税减征额 |
| 17 | fbqyjsfl | 本期预计税负率 | numeric | 23 | 10 | √ | 0.0000000000 | 本期预计税负率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_input_plan_org |  | forg,fskssq |
| 2 | t_tcvat_input_plan_pkey |  | fid |
