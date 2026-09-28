# 通用台账-totf_general_account

## 通用台账-主表 t_totf_general_account

- **表名称：** 通用台账-主表
- **表名：** t_totf_general_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fzszm | 征收子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tysbsf_bizdef_entry |
| 3 | ftaxrate | 征收比例 | numeric | 23 | 10 | √ | 0 | 征收比例 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fzspm | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 6 | famount | 本期应纳费额 | numeric | 23 | 10 | √ | 0 | 本期应纳费额 |
| 7 | fsourcedata | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: hand :手工新增 import :数据导入 |
| 8 | fbqybtse | 本期应补退费额 | numeric | 23 | 10 | √ | 0 | 本期应补退费额 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fdeductionamount | 减免费额 | numeric | 23 | 10 | √ | 0 | 减免费额 |
| 11 | fenddate | 费款所属期止 | timestamp | 0 |  |  | null | 费款所属期止 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | frate | 征收标准（费率） | numeric | 23 | 10 | √ | 0 | 征收标准（费率） |
| 14 | ftaxdeductionid | 减免性质代码和名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 15 | ftaxtype | 征收项目 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 16 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | ftaxableitem | 应缴费基数 | numeric | 23 | 10 | √ | 0 | 应缴费基数 |
| 19 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fstartdate | 费款所属期起 | timestamp | 0 |  |  | null | 费款所属期起 |
| 23 | fpayperiod | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月 season :季 halfyear :半年 year :年 count :次 |
| 24 | ftaxbasis | 计费依据 | numeric | 23 | 10 | √ | 0 | 计费依据 |
| 25 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | [纳税申报表基础资料 bdtaxr_nsrxx](../bdtaxr_files/bdtaxr_nsrxx.md) |
| 26 | fquickdeduction | 扣除数 | numeric | 23 | 10 | √ | 0 | 扣除数 |
| 27 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 28 | fdeductitem | 应缴费基数减除额 | numeric | 23 | 10 | √ | 0 | 应缴费基数减除额 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fbqyjse | 本期已缴费额 | numeric | 23 | 10 | √ | 0 | 本期已缴费额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_totf_general_account |  | forgid,fstartdate,fenddate |
| 2 | pk_totf_general_account |  | fid |
