# 小规模本期缴税情况计提单据-tcvat_xgm_current_pay_jt

## 小规模本期缴税情况计提单据-主表 t_tcvat_xgm_cur_pay_jt

- **表名称：** 小规模本期缴税情况计提单据-主表
- **表名：** t_tcvat_xgm_cur_pay_jt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属月份 | varchar | 50 |  | √ | ' ' | 所属月份 |
| 3 | ftaxableamount | 应税销售额 | numeric | 23 | 10 | √ | 0 | 应税销售额 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1-3%货物和劳务类 2 :2-3%服务和无形资产类 3 :3-5%服务类和不动产类 4 :4-其中：不动产类 5 :5-减免税项目类 6 :6-销售已使用固定资产类 7 :7-出口免税类 8 :8-小计 9 :9-3%货物和劳务类 10 :10-3%服务和无形资产类 11 :11-5%服务类和不动产类 12 :12-其中：不动产类 13 :13-减免税项目类 14 :14-销售已使用固定资产类 15 :15-出口免税类 16 :16-小计 17 :17-3%货物和劳务类 18 :18-3%服务和无形资产类 19 :19-5%服务类和不动产类 20 :20-其中：不动产类 21 :21-减免税项目类 22 :22-销售已使用固定资产类 23 :23-出口免税类 24 :24-小计 25 :25-合计 |
| 5 | fincomeincludtax | 含税收入合计 | numeric | 23 | 10 | √ | 0 | 含税收入合计 |
| 6 | ftaxrate | 征收率 | numeric | 23 | 10 | √ | 0 | 征收率 |
| 7 | fsalesexcludtax | 不含税销售额 | numeric | 23 | 10 | √ | 0 | 不含税销售额 |
| 8 | fparentid | 父ID | int8 | 64 |  | √ | 0 | 父ID |
| 9 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 10 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fdiffammount | 差额扣除额 | numeric | 23 | 10 | √ | 0 | 差额扣除额 |
| 12 | ftaxfreeamount | 免税销售额 | numeric | 23 | 10 | √ | 0 | 免税销售额 |
| 13 | fdescription | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 14 | fsalesincludtax | 含税销售额 | numeric | 23 | 10 | √ | 0 | 含税销售额 |
| 15 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 16 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 17 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 18 | fspecialincludtax | 其中：开具专用发票不含税销售额 | numeric | 23 | 10 | √ | 0 | 其中：开具专用发票不含税销售额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_taxc_xgmcurpayjt_serialno |  | fserialno |
| 2 | idx_taxc_xgmcurpayjt_xh_sbb |  | fewblxh,fsbbid |
| 3 | idx_taxc_xgmcurpayjt_combine |  | ftaxperiod,forgid,fdeadline |
| 4 | pk_tcvat_xgm_cur_pay_jt |  | fid |
