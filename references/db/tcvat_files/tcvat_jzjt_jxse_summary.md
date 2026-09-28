# 即征即退进项税额底稿-tcvat_jzjt_jxse_summary

## 即征即退进项税额底稿-主表 t_tcvat_jzjt_jxse_summary

- **表名称：** 即征即退进项税额底稿-主表
- **表名：** t_tcvat_jzjt_jxse_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 3 | fjzjtjxtax | 即征即退进项税额 | numeric | 23 | 10 | √ | 0 | 即征即退进项税额 |
| 4 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fewblxh | ewblxh | varchar | 30 |  | √ | ' ' | ewblxh,枚举: 1 :行号 count :合计行 |
| 7 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 8 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fbizdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 12 | fjzjtlx | 即征即退类型 | varchar | 50 |  | √ | ' ' | 即征即退类型,枚举: jzjt :即征即退 wfhf :无法划分 |
| 13 | fewblname | ewblname | varchar | 50 |  | √ | ' ' | ewblname |
| 14 | ftaxplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 15 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 16 | finputtax | 进项税额 | numeric | 23 | 10 | √ | 0 | 进项税额 |
| 17 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 18 | fjzjtamount | 即征即退销售额 | numeric | 23 | 10 | √ | 0 | 即征即退销售额 |
| 19 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 20 | fsbbid | sbbid | varchar | 50 |  | √ | ' ' | sbbid |
| 21 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 22 | famountsum | 销售额合计 | numeric | 23 | 10 | √ | 0 | 销售额合计 |
| 23 | fsplitrate | 划分比例 | numeric | 23 | 10 | √ | 0 | 划分比例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_jzjt_jxse_sum_1 |  | forgid,ftaxperiod |
| 2 | pk_tcvat_jzjt_jxse_summary |  | fid |
