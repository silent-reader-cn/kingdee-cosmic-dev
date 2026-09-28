# 堤围防护费台账-totf_embankment_account

## 堤围防护费台账-主表 t_totf_embankment_account

- **表名称：** 堤围防护费台账-主表
- **表名：** t_totf_embankment_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fzsxm | fzsxm | varchar | 50 |  | √ | ' ' |  |
| 3 | ftaxrate | 应税所得率 | numeric | 23 | 10 | √ | 0 | 应税所得率 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fzspm | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdeductionamount | 减免税（费）额 | numeric | 23 | 10 | √ | 0 | 减免税（费）额 |
| 8 | fenddate | 税（费）款所属期止 | timestamp | 0 |  |  | null | 税（费）款所属期止 |
| 9 | fjbrysfzjlx | fjbrysfzjlx | varchar | 50 |  | √ | ' ' |  |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fzzsdeductiontype | 增值税小规模纳税减免性质 | varchar | 50 |  | √ | ' ' | 增值税小规模纳税减免性质 |
| 12 | ftaxdeductionid | 减免性质代码和名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 13 | fjbrphone | fjbrphone | varchar | 50 |  | √ | ' ' |  |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ftaxableitem | 应税项 | numeric | 23 | 10 | √ | 0 | 应税项 |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | foperator | foperator | varchar | 50 |  | √ | ' ' |  |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fzzsdeductrate | 增值税小规模纳税人享受减征比例（%） | numeric | 23 | 10 | √ | 0 | 增值税小规模纳税人享受减征比例（%） |
| 21 | foperatorno | foperatorno | varchar | 50 |  | √ | ' ' |  |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fzspmname | fzspmname | varchar | 50 |  | √ | ' ' |  |
| 24 | fstartdate | 税（费）款所属期起 | timestamp | 0 |  |  | null | 税（费）款所属期起 |
| 25 | fquickdeduction | 速算扣除数 | numeric | 23 | 10 | √ | 0 | 速算扣除数 |
| 26 | fpayperiod | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月 season :季 halfyear :半年 year :年 |
| 27 | fsbbid | 申报表 | int8 | 64 |  | √ | 0 | [纳税申报表基础资料 bdtaxr_nsrxx](../bdtaxr_files/bdtaxr_nsrxx.md) |
| 28 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: dataimport :数据引入 handadd :手工新增 |
| 29 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 30 | fdeductitem | 减除项 | numeric | 23 | 10 | √ | 0 | 减除项 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fbqyjse | 本期已缴税（费）额 | numeric | 23 | 10 | √ | 0 | 本期已缴税（费）额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_totf_em_account_otse |  | forgid,ftaxoffice,fstartdate,fenddate |
| 2 | pk_totf_embankment_account |  | fid |
