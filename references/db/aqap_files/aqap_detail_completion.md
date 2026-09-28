# 银企交易明细完整性检查报表-aqap_detail_completion

## 银企交易明细完整性检查报表-主表 t_aqap_detail_completion

- **表名称：** 银企交易明细完整性检查报表-主表
- **表名：** t_aqap_detail_completion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcompensation_detail | 补偿详情 | varchar | 256 |  |  | null | 补偿详情 |
| 6 | facc_no | 账号 | varchar | 50 |  | √ | ' ' | 账号 |
| 7 | fcurrency | 币别 | varchar | 50 |  | √ | ' ' | 币别 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fcompensation_count | 补偿次数 | int8 | 64 |  | √ | 0 | 补偿次数 |
| 10 | fdetail_count | 交易明细数量 | int8 | 64 |  | √ | 0 | 交易明细数量 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbank_version | 银行版本 | int8 | 64 |  | √ | 0 | [银行启用管理 aqap_bank](../aqap_files/aqap_bank.md) |
| 13 | fbank_name | 银行名称 | varchar | 50 |  | √ | ' ' | 银行名称 |
| 14 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 15 | fsync_count | 联机查询次数 | int8 | 64 |  | √ | 0 | 联机查询次数 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fis_completed | 是否完整 | varchar | 50 |  | √ | ' ' | 是否完整,枚举: 1 :不完整 2 :补偿完整 |
| 18 | fbank_acnt | 账号 | int8 | 64 |  | √ | 0 | [银企账户 aqap_bank_acnt](../aqap_files/aqap_bank_acnt.md) |
| 19 | fenable | 使用状态 | int8 | 64 |  | √ | 0 | 使用状态 |
| 20 | fsync_date | 交易日期 | timestamp | 0 |  |  | null | 交易日期 |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_detail_completion |  | fbillno |
| 2 | pk_t_aqap_detail_completion |  | fid |
