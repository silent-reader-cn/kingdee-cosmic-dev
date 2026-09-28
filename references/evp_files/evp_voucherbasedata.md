# 凭证-evp_voucherbasedata

## 凭证-主表 t_evp_voucher

- **表名称：** 凭证-主表
- **表名：** t_evp_voucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatorid | foperatorid | int8 | 64 |  | √ | 0 |  |
| 3 | fisintopool | fisintopool | bpchar | 1 |  | √ | '0' |  |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fdirectbillid | fdirectbillid | int8 | 64 |  | √ | 0 |  |
| 6 | fisdelete | 已删除 | bpchar | 1 |  | √ | '0' | 已删除 |
| 7 | fvoucherno | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 8 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 10 | farchivebatchcode | farchivebatchcode | varchar | 255 |  | √ | ' ' |  |
| 11 | fisarchive | fisarchive | bpchar | 1 |  | √ | '0' |  |
| 12 | foriginsysid | 集成系统 | int8 | 64 |  | √ | 0 | 集成系统配置 evp_originsys |
| 13 | fbillno | fbillno | varchar | 50 |  | √ | ' ' |  |
| 14 | fdirectbillno | fdirectbillno | varchar | 50 |  | √ | ' ' |  |
| 15 | fvdescription | 摘要 | varchar | 200 |  | √ | ' ' | 摘要 |
| 16 | fvoucherid | fvoucherid | varchar | 50 |  | √ | ' ' |  |
| 17 | fxhvoucherid | fxhvoucherid | int8 | 64 |  | √ | 0 |  |
| 18 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 19 | fseqno | fseqno | varchar | 200 |  | √ | ' ' |  |
| 20 | fhaspullbill | fhaspullbill | bpchar | 1 |  | √ | '0' |  |
| 21 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 22 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 23 | fdirectbilltype | fdirectbilltype | varchar | 50 |  | √ | ' ' |  |
| 24 | fperiodtypeid | fperiodtypeid | int8 | 64 |  | √ | 0 |  |
| 25 | fbatchcode | fbatchcode | varchar | 128 |  | √ | ' ' |  |
| 26 | fishandle | fishandle | bpchar | 1 |  | √ | '0' |  |
| 27 | fbillid | 原始单据ID | varchar | 50 |  | √ | ' ' | 原始单据ID |
| 28 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 29 | fintopooldate | fintopooldate | timestamp | 0 |  |  | null |  |
| 30 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_evp_voucher |  | fid |
| 2 | idx_evp_voucher |  | fbillid,forgid |
