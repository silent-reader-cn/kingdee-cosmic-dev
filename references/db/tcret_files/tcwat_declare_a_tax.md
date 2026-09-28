# 申报表A税款信息-tcwat_declare_a_tax

## 申报表A税款信息-主表 t_tcwat_declare_a_tax

- **表名称：** 申报表A税款信息-主表
- **表名：** t_tcwat_declare_a_tax

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fljqsfdl | 累计取水量/累计发电量 | numeric | 23 | 10 | √ | 0 | 累计取水量/累计发电量 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: resourcetax :水资源税 sum :合计 1 :水资源B |
| 4 | fljcjhqsl | 累计超计划取水量 | numeric | 23 | 10 | √ | 0 | 累计超计划取水量 |
| 5 | fzszm | 征收子目 | varchar | 50 |  | √ | ' ' | 征收子目 |
| 6 | fbqljqsl | 本期累计取水量 | numeric | 23 | 10 | √ | 0 | 本期累计取水量 |
| 7 | fbqsybzse | 本期适用标准税额 | numeric | 23 | 10 | √ | 0 | 本期适用标准税额 |
| 8 | fzspm | 征收品目 | varchar | 50 |  | √ | ' ' | 征收品目 |
| 9 | fbqjmse | 本期减免税额 | numeric | 23 | 10 | √ | 0 | 本期减免税额 |
| 10 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 11 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税额 |
| 12 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 13 | fsqljqsl | 上期累计取水量 | numeric | 23 | 10 | √ | 0 | 上期累计取水量 |
| 14 | fbqjsqsfdl | 本期计税取水量/本期发电量 | numeric | 23 | 10 | √ | 0 | 本期计税取水量/本期发电量 |
| 15 | fhlshl | 合理损耗率 | numeric | 23 | 10 | √ | 0 | 合理损耗率 |
| 16 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 17 | fbqynse | 本期应纳税额 | numeric | 23 | 10 | √ | 0 | 本期应纳税额 |
| 18 | fbqqsl | 本期取水量 | numeric | 23 | 10 | √ | 0 | 本期取水量 |
| 19 | fljcjhqsbl | 累计超计划取水比例 | numeric | 23 | 10 | √ | 0 | 累计超计划取水比例 |
| 20 | fbqyjse | 本期已缴税额 | numeric | 23 | 10 | √ | 0 | 本期已缴税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcwat_declare_a_tax |  | fid |
| 2 | idx_tcwat_declare_a_tax |  | fsbbid,fewblxh |
