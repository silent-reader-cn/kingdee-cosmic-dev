# 银行电子回单-evp_bkerreceiver

## 银行电子回单-主表 t_evp_bkerreceiver

- **表名称：** 银行电子回单-主表
- **表名：** t_evp_bkerreceiver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpayandrevamount | 应收/付款项金额 | numeric | 23 | 10 | √ | 0 | 应收/付款项金额 |
| 3 | foperatorid | 入池操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fisintopool | 电子凭证入池 | bpchar | 1 |  | √ | '0' | 电子凭证入池 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fdirectbillid | 关联单据ID | int8 | 64 |  | √ | 0 | 关联单据ID |
| 7 | fisdelete | 已删除 | bpchar | 1 |  | √ | '0' | 已删除 |
| 8 | fvoucherno | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 9 | ffileurl | 原文件地址 | varchar | 500 |  |  | ' ' | 原文件地址 |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | fbasetext | 原文件base64 | varchar | 500 |  |  | null | 原文件base64 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | farchivebatchcode | 归档批次号 | varchar | 255 |  | √ | ' ' | 归档批次号 |
| 14 | fsourcexbrl | 原始xbrl | varchar | 1000 |  | √ | ' ' | 原始xbrl |
| 15 | ffilename | 原文件名 | varchar | 2000 |  |  | ' ' | 原文件名 |
| 16 | fisarchive | 归档 | bpchar | 1 |  | √ | '0' | 归档 |
| 17 | fhasbeenreconciled | 已对账 | bpchar | 1 |  | √ | '0' | 已对账 |
| 18 | fhasbeentransfer | 已流转 | bpchar | 1 |  | √ | '0' | 已流转 |
| 19 | fcontractnumber | 合同编号 | varchar | 200 |  |  | ' ' | 合同编号 |
| 20 | fsourcexbrldata_tag | 原始xbrlbase64_详情 | text | 0 |  |  | null | 原始xbrlbase64_详情 |
| 21 | funiquecode | 票据唯一标识 | varchar | 200 |  |  | ' ' | 票据唯一标识 |
| 22 | foriginsysid | 集成系统 | int8 | 64 |  | √ | 0 | [集成系统配置 evp_originsys](../evp_files/evp_originsys.md) |
| 23 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 24 | ftypeofinvoice | 票据类型 | varchar | 50 |  | √ | ' ' | 票据类型 |
| 25 | fdirectbillno | 关联单据号 | varchar | 50 |  | √ | ' ' | 关联单据号 |
| 26 | fvoucherid | 关联凭证id | varchar | 50 |  | √ | ' ' | 关联凭证id |
| 27 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 28 | fdateofissue | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 29 | fhasbeenclaimed | 已认领 | bpchar | 1 |  | √ | '0' | 已认领 |
| 30 | fseqno | 票据流水号（唯一标识） | varchar | 200 |  | √ | ' ' | 票据流水号（唯一标识） |
| 31 | fsourcexbrldata | 原始xbrlbase64 | varchar | 255 |  | √ | ' ' | 原始xbrlbase64 |
| 32 | fidentifyingcode | 回单校验码 | varchar | 200 |  |  | ' ' | 回单校验码 |
| 33 | ftransactionamountinfigur | 小写金额 | numeric | 23 | 10 | √ | 0 | 小写金额 |
| 34 | fdirectbilltype | 关联单据类型 | varchar | 50 |  | √ | ' ' | 关联单据类型 |
| 35 | fbasetext_tag | 原文件base64_详情 | text | 0 |  |  | null | 原文件base64_详情 |
| 36 | fxbrlurl | xbrl文件地址 | varchar | 500 |  |  | ' ' | xbrl文件地址 |
| 37 | fbatchcode | 批次号 | varchar | 128 |  | √ | ' ' | 批次号 |
| 38 | ffileurl_tag | 原文件地址_详情 | text | 0 |  |  | null | 原文件地址_详情 |
| 39 | fishandle | 数据来源 | bpchar | 1 |  | √ | '0' | 数据来源,枚举: 0 :API导入 1 :手工新增 2 :系统抽取 |
| 40 | fbillid | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 41 | fhasbeenbooked | 已入账 | bpchar | 1 |  | √ | '1' | 已入账 |
| 42 | fbookdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 43 | fintopooldate | 入池时间 | timestamp | 0 |  |  | null | 入池时间 |
| 44 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_evp_bkerreceiver |  | fid |
| 2 | idx_evp_bkerreceiver |  | forgid,fbillid |
