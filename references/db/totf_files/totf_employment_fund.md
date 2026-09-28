# 残疾人就业保障金台账-totf_employment_fund

## 残疾人就业保障金台账-主表 t_totf_employment_fund

- **表名称：** 残疾人就业保障金台账-主表
- **表名：** t_totf_employment_fund

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fstaffnumber | 上年在职职工人数 | int8 | 64 |  | √ | 0 | 上年在职职工人数 |
| 4 | fzspm | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 5 | fbqybtse | 本期应补（退）费额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）费额 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdeductionamount | 减免税（费）额 | numeric | 23 | 10 | √ | 0 | 减免税（费）额 |
| 8 | fenddate | 税（费）款所属期止 | timestamp | 0 |  |  | null | 税（费）款所属期止 |
| 9 | ftaxdeductiontype | ftaxdeductiontype | varchar | 50 |  | √ | ' ' |  |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | ftaxdeductionid | 减免性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 12 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fratio | 应安排残疾人就业比例 | numeric | 23 | 10 | √ | 0 | 应安排残疾人就业比例 |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | ftaxdeductionname | ftaxdeductionname | varchar | 50 |  | √ | ' ' |  |
| 19 | fsalary | 上年在职职工工资总额 | numeric | 23 | 10 | √ | 0 | 上年在职职工工资总额 |
| 20 | fstartdate | 税（费）款所属期起 | timestamp | 0 |  |  | null | 税（费）款所属期起 |
| 21 | fdisablednumber | 上年实际安排残疾人就业人数 | int8 | 64 |  | √ | 0 | 上年实际安排残疾人就业人数 |
| 22 | fpayperiod | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月 season :季 halfyear :半年 year :年 |
| 23 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 纳税申报基础资料 tpo_declare_base |
| 24 | faveragesalary | 上年在职职工年平均工资（或当地社会平均工资的2倍） | numeric | 23 | 10 | √ | 0 | 上年在职职工年平均工资（或当地社会平均工资的2倍） |
| 25 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 26 | fbqynse | 本期应纳费额 | numeric | 23 | 10 | √ | 0 | 本期应纳费额 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fbqyjse | 本期已缴费额 | numeric | 23 | 10 | √ | 0 | 本期已缴费额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_employment_fund |  | fid |
| 2 | idx_t_totf_employment_fund |  | forgid,fstartdate,fenddate |
