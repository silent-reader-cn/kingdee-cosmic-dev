# 土地增值税税源明细表-tcret_tdzzssy_mx

## 土地增值税税源明细表-主表 t_tcret_tdzzssy_mx

- **表名称：** 土地增值税税源明细表-主表
- **表名：** t_tcret_tdzzssy_mx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuildingtype | fbuildingtype | varchar | 50 |  | √ | ' ' |  |
| 3 | fswjqtsr | 实物收入及其他收入 | numeric | 23 | 10 | √ | 0 | 实物收入及其他收入 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 sum :合计 |
| 5 | fyssr | 应税收入 | numeric | 23 | 10 | √ | 0 | 应税收入 |
| 6 | fbqybtse | 本期应缴税额 | numeric | 23 | 10 | √ | 0 | 本期应缴税额 |
| 7 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 8 | fbuildingtypeid | 房产类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tdzzs_bizdef_entry |
| 9 | fsubbuildingtypeid | 房产类型子目 | int8 | 64 |  | √ | 0 | 房产类型子目 tcret_tdzzs_fclxzm |
| 10 | fhbsr | 货币收入 | numeric | 23 | 10 | √ | 0 | 货币收入 |
| 11 | fstxssr | 视同销售收入 | numeric | 23 | 10 | √ | 0 | 视同销售收入 |
| 12 | fyzl | 预征率（%） | numeric | 23 | 10 | √ | 0 | 预征率（%） |
| 13 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 14 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0 | 应纳税额 |
| 15 | fsubbuildingtype | fsubbuildingtype | varchar | 50 |  | √ | ' ' |  |
| 16 | fbqyjse | 本期已缴税额 | numeric | 23 | 10 | √ | 0 | 本期已缴税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcret_tdzzssy_mx1 |  | fsbbid,fewblxh |
| 2 | pk_tcret_tdzzssy_mx |  | fid |
