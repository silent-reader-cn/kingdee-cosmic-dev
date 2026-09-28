# 水土保持补偿费台账-totf_stbcbcf_account

## 水土保持补偿费台账-主表 t_totf_stbcbcf_account

- **表名称：** 水土保持补偿费台账-主表
- **表名：** t_totf_stbcbcf_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fzsxm | fzsxm | varchar | 50 |  | √ | ' ' |  |
| 3 | fzszm | 征收子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tysbsf_bizdef_entry |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fzspm | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 6 | fyjfjsjme | 应缴费基数减除额 | numeric | 23 | 10 |  | null | 应缴费基数减除额 |
| 7 | fsourcedata | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :手工新增 1 :系统采集 2 :数据引入 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fdeductionamount | 减免税（费）额 | numeric | 23 | 10 | √ | 0 | 减免税（费）额 |
| 10 | fenddate | 税（费）款所属期止 | timestamp | 0 |  |  | null | 税（费）款所属期止 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | frate | 费率 | numeric | 23 | 10 | √ | 0 | 费率 |
| 13 | ftaxdeductionid | 减免性质代码和名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 16 | ftaxperiod | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: season :季 halfyear :半年 year :年 count :次 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbqynsfe | 本期应纳税（费）额 | numeric | 23 | 10 | √ | 0 | 本期应纳税（费）额 |
| 19 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fbqybtfe | 本期应补（退）费额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）费额 |
| 23 | fisrulecollection | 应缴费基数是否通过规则取数 | varchar | 1 |  | √ | '0' | 应缴费基数是否通过规则取数 |
| 24 | fyjfjs | 应缴费基数 | numeric | 23 | 10 | √ | 0 | 应缴费基数 |
| 25 | fstartdate | 税（费）款所属期起 | timestamp | 0 |  |  | null | 税（费）款所属期起 |
| 26 | fquickdeduction | 扣除数 | numeric | 23 | 10 | √ | 0 | 扣除数 |
| 27 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | [纳税申报表基础资料 bdtaxr_nsrxx](../bdtaxr_files/bdtaxr_nsrxx.md) |
| 28 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fbqyjse | 本期已缴税（费）额 | numeric | 23 | 10 | √ | 0 | 本期已缴税（费）额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_stbcbcf_account |  | fid |
| 2 | idx_stbcbcf_account_forgid |  | forgid,fstartdate,fenddate,fzspm,fzszm |
