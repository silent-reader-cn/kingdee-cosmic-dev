# 银行电子回单-evp_bkerreceiver

## 银行电子回单-主表 t_evp_bkerreceiver

- **表名称：** 银行电子回单-主表
- **表名：** t_evp_bkerreceiver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpayandrevamount | 应收/付款项金额 | numeric | 23 | 10 | √ | 0 | 应收/付款项金额 |
| 3 | foperatorid | 入池操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fisintopool | 电子凭证入池 | bpchar | 1 |  | √ | '0' | 电子凭证入池 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdirectbillid | 关联单据ID | int8 | 64 |  | √ | 0 | 关联单据ID |
| 7 | fisdelete | 已删除 | bpchar | 1 |  | √ | '0' | 已删除 |
| 8 | fvoucherno | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 9 | ffileurl | 原文件地址 | varchar | 500 |  | √ | ' ' | 原文件地址 |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | fbasetext | 原文件base64 | varchar | 500 |  |  | null | 原文件base64 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | farchivebatchcode | 归档批次号 | varchar | 255 |  | √ | ' ' | 归档批次号 |
| 14 | ffilename | 原文件名 | varchar | 2000 |  | √ | ' ' | 原文件名 |
| 15 | fisarchive | 归档 | bpchar | 1 |  | √ | '0' | 归档 |
| 16 | fhasbeenreconciled | 已对账 | bpchar | 1 |  | √ | '0' | 已对账 |
| 17 | fhasbeentransfer | 已流转 | bpchar | 1 |  | √ | '0' | 已流转 |
| 18 | fcontractnumber | 合同编号 | varchar | 200 |  | √ | ' ' | 合同编号 |
| 19 | funiquecode | 票据唯一标识 | varchar | 200 |  | √ | ' ' | 票据唯一标识 |
| 20 | foriginsysid | 集成系统 | int8 | 64 |  | √ | 0 | 集成系统配置 evp_originsys |
| 21 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 22 | ftypeofinvoice | 票据类型 | varchar | 50 |  | √ | ' ' | 票据类型 |
| 23 | fdirectbillno | 关联单据编号 | varchar | 50 |  | √ | ' ' | 关联单据编号 |
| 24 | fvoucherid | 关联凭证id | varchar | 50 |  | √ | ' ' | 关联凭证id |
| 25 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 26 | fdateofissue | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 27 | fhasbeenclaimed | 已认领 | bpchar | 1 |  | √ | '0' | 已认领 |
| 28 | fseqno | 票据流水号（唯一标识） | varchar | 200 |  | √ | ' ' | 票据流水号（唯一标识） |
| 29 | fidentifyingcode | 回单校验码 | varchar | 200 |  | √ | ' ' | 回单校验码 |
| 30 | ftransactionamountinfigur | 小写金额 | numeric | 23 | 10 | √ | 0 | 小写金额 |
| 31 | fdirectbilltype | 关联单据类型 | varchar | 50 |  | √ | ' ' | 关联单据类型 |
| 32 | fbasetext_tag | 原文件base64_详情 | text | 0 |  |  | null | 原文件base64_详情 |
| 33 | fxbrlurl | xbrl文件地址 | varchar | 200 |  | √ | ' ' | xbrl文件地址 |
| 34 | fbatchcode | 批次号 | varchar | 128 |  | √ | ' ' | 批次号 |
| 35 | ffileurl_tag | 原文件地址_详情 | text | 0 |  |  | null | 原文件地址_详情 |
| 36 | fishandle | 数据来源 | bpchar | 1 |  | √ | '0' | 数据来源,枚举: 0 :API导入 1 :手工新增 2 :系统抽取 |
| 37 | fbillid | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 38 | fhasbeenbooked | 已入账 | bpchar | 1 |  | √ | '1' | 已入账 |
| 39 | fbookdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 40 | fintopooldate | 入池时间 | timestamp | 0 |  |  | null | 入池时间 |
| 41 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_evp_bkerreceiver |  | fid |
| 2 | idx_evp_bkerreceiver |  | forgid,fbillid |
