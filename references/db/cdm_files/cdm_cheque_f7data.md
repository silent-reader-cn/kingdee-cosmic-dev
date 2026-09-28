# 支票F7数据-cdm_cheque_f7data

## 支票F7数据-主表 t_cdm_cheque

- **表名称：** 支票F7数据-主表
- **表名：** t_cdm_cheque

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpurchdate | 购入日期 | timestamp | 0 |  |  | null | 购入日期 |
| 3 | ffilldate | ffilldate | timestamp | 0 |  |  | null |  |
| 4 | finvaliddate | finvaliddate | timestamp | 0 |  |  | null |  |
| 5 | frelatebillnumber | frelatebillnumber | varchar | 100 |  | √ | ' ' |  |
| 6 | fpurchase | fpurchase | int8 | 64 |  | √ | 0 |  |
| 7 | famount | famount | int8 | 64 |  | √ | 0 |  |
| 8 | fmodifytime | 最后更新日期 | timestamp | 0 |  |  | null | 最后更新日期 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | freplacechar | freplacechar | varchar | 10 |  | √ | ' ' |  |
| 11 | frelatebilltype | frelatebilltype | varchar | 100 |  | √ | ' ' |  |
| 12 | fcoderule | fcoderule | varchar | 128 |  | √ | ' ' |  |
| 13 | finvaliduser | finvaliduser | int8 | 64 |  | √ | 0 |  |
| 14 | frelateamount | frelateamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 15 | finvalidmark | finvalidmark | varchar | 510 |  | √ | ' ' |  |
| 16 | fbillno | 票据号码 | varchar | 100 |  | √ | ' ' | 票据号码 |
| 17 | fstartno | fstartno | int8 | 64 |  | √ | 0 |  |
| 18 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fbatchno | fbatchno | varchar | 100 |  | √ | ' ' |  |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | frelatebillid | 关联单据ID | int8 | 64 |  | √ | 0 | 关联单据ID |
| 22 | fcurrency | fcurrency | int8 | 64 |  | √ | 0 |  |
| 23 | fbank | 开户银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 24 | ffilluser | ffilluser | int8 | 64 |  | √ | 0 |  |
| 25 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 26 | faccountbank | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 27 | cfbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: |
| 28 | fchequestatus | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :空白 1 :已领用 2 :已填开 3 :已作废 |
| 29 | fpurchorg | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 31 | fbilltype | fbilltype | varchar | 60 |  | √ | ' ' |  |
| 32 | fbilltypeid | 票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cdm_cheque_purchorg |  | fpurchorg |
| 2 | idx_t_cdm_cheque_billno |  | fbillno |
| 3 | t_cdm_cheque_pkey |  | fid |
| 4 | idx_t_cdm_cheque_accountbank |  | faccountbank |
