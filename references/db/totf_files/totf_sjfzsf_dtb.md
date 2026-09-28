# 通用申报表动态行表-totf_sjfzsf_dtb

## 通用申报表动态行表-主表 t_totf_sjfzsf_dtb

- **表名称：** 通用申报表动态行表-主表
- **表名：** t_totf_sjfzsf_dtb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 申报表id | int8 | 64 |  | √ | 0 | 申报表id |
| 2 | fsybh | 税源编号 | varchar | 50 |  | √ | ' ' | 税源编号 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 4 | fzsxm | 征收项目 | varchar | 50 |  | √ | ' ' | 征收项目 |
| 5 | fxgmjze | 增值税小规模纳税人减征额 | numeric | 23 | 10 | √ | 0 | 增值税小规模纳税人减征额 |
| 6 | fzszm | 征收子目 | varchar | 50 |  | √ | ' ' | 征收子目 |
| 7 | fyjfjscke | 应缴费基数减除额 | numeric | 23 | 10 | √ | 0 | 应缴费基数减除额 |
| 8 | fflhdwse | （费) 率或单位税额 | numeric | 23 | 10 | √ | 0 | （费) 率或单位税额 |
| 9 | fysx | 应税项 | numeric | 23 | 10 | √ | 0 | 应税项 |
| 10 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 11 | fzspm | 征收品目 | varchar | 50 |  | √ | ' ' | 征收品目 |
| 12 | fxgmjzbl | 增值税小规模纳税人享受减征比例（%） | numeric | 23 | 10 | √ | 0 | 增值税小规模纳税人享受减征比例（%） |
| 13 | fsskcs | 速算扣除数 | numeric | 23 | 10 | √ | 0 | 速算扣除数 |
| 14 | fenddate | 税（费）款所属期止 | timestamp | 0 |  |  | null | 税（费）款所属期止 |
| 15 | fybse | 本期应 补（退）税（费）额 | numeric | 23 | 10 | √ | 0 | 本期应 补（退）税（费）额 |
| 16 | fjcx | 减除项 | numeric | 23 | 10 | √ | 0 | 减除项 |
| 17 | fyssdl | 应税所得率 | numeric | 23 | 10 | √ | 0 | 应税所得率 |
| 18 | fynse | 本期应纳税（费）额 | numeric | 23 | 10 | √ | 0 | 本期应纳税（费）额 |
| 19 | fyjse | 本期已缴税 （费）额 | numeric | 23 | 10 | √ | 0 | 本期已缴税 （费）额 |
| 20 | fjmxz | 减免性质 | varchar | 50 |  | √ | ' ' | 减免性质 |
| 21 | fxgmjmxz | 增值税小规模纳税减免性质 | varchar | 50 |  | √ | ' ' | 增值税小规模纳税减免性质 |
| 22 | fseqno | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 23 | fjsfyjs | 计税(费) 依据税 | numeric | 23 | 10 | √ | 0 | 计税(费) 依据税 |
| 24 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 25 | fsymc | 税源名称 | varchar | 50 |  | √ | ' ' | 税源名称 |
| 26 | fyjfjs | 应缴费基数 | numeric | 23 | 10 | √ | 0 | 应缴费基数 |
| 27 | fdeductioncode | 减免性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 28 | fjmse | 减免税（费）额 | numeric | 23 | 10 | √ | 0 | 减免税（费）额 |
| 29 | fstartdate | 税（费） 款所属期起 | timestamp | 0 |  |  | null | 税（费） 款所属期起 |
| 30 | fqmzgrs | 期末职工人数 | int8 | 64 |  | √ | 0 | 期末职工人数 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fzsbl | 征收比例 | numeric | 23 | 10 | √ | 0 | 征收比例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_totf_sjfzsf_1 |  | fid |
| 2 | pk_totf_sjfzsf_dtb |  | fentryid |
