# 铁路客票行程单-evp_raireceiver

## 铁路客票行程单-主表 t_evp_raireceiver

- **表名称：** 铁路客票行程单-主表
- **表名：** t_evp_raireceiver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisredinvoice | 红字发票 | bpchar | 1 |  | √ | '0' | 红字发票 |
| 3 | foperatorid | 入池操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fisintopool | 电子凭证入池 | bpchar | 1 |  | √ | '0' | 电子凭证入池 |
| 5 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fdirectbillid | 关联单据ID | int8 | 64 |  | √ | 0 | 关联单据ID |
| 8 | fisdelete | 已删除 | bpchar | 1 |  | √ | '0' | 已删除 |
| 9 | fvoucherno | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 10 | ffileurl | 原文件地址 | varchar | 500 |  | √ | ' ' | 原文件地址 |
| 11 | fdeductiontaxperiod | 抵扣税期 | varchar | 50 |  | √ | ' ' | 抵扣税期 |
| 12 | fhasbeendeducted | 已抵扣 | bpchar | 1 |  | √ | ' ' | 已抵扣 |
| 13 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fbasetext | 原文件base64 | varchar | 500 |  | √ | ' ' | 原文件base64 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | farchivebatchcode | 归档批次号 | varchar | 255 |  | √ | ' ' | 归档批次号 |
| 17 | fcostcompany | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | ffilename | 原文件名 | varchar | 2000 |  | √ | ' ' | 原文件名 |
| 19 | fisarchive | 归档 | bpchar | 1 |  | √ | '0' | 归档 |
| 20 | finvoicenumber | 发票号 | varchar | 50 |  | √ | ' ' | 发票号 |
| 21 | foriginsysid | 集成系统 | int8 | 64 |  | √ | 0 | 集成系统配置 evp_originsys |
| 22 | ftotalamountexcludingtax | 金额（不含税） | numeric | 23 | 10 | √ | 0 | 金额（不含税） |
| 23 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 24 | fdirectbillno | 关联单据编号 | varchar | 50 |  | √ | ' ' | 关联单据编号 |
| 25 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 26 | fvoucherid | 关联凭证id | varchar | 50 |  | √ | ' ' | 关联凭证id |
| 27 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 28 | fdateofissue | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 29 | fseqno | 票据流水号（唯一标识） | varchar | 255 |  | √ | ' ' | 票据流水号（唯一标识） |
| 30 | fdirectbilltype | 关联单据类型 | varchar | 50 |  | √ | ' ' | 关联单据类型 |
| 31 | fbasetext_tag | 原文件base64_详情 | text | 0 |  |  | null | 原文件base64_详情 |
| 32 | fxbrlurl | xbrl文件地址 | varchar | 255 |  | √ | ' ' | xbrl文件地址 |
| 33 | fbatchcode | 批次号 | varchar | 255 |  | √ | ' ' | 批次号 |
| 34 | ffileurl_tag | 原文件地址_详情 | text | 0 |  |  | null | 原文件地址_详情 |
| 35 | fishandle | 数据来源 | bpchar | 1 |  | √ | '0' | 数据来源,枚举: 0 :API导入 1 :手工新增 2 :系统抽取 |
| 36 | fbillid | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 37 | fhasbeenbooked | 已入账 | bpchar | 1 |  | √ | '0' | 已入账 |
| 38 | fbookdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 39 | fintopooldate | 入池时间 | timestamp | 0 |  |  | null | 入池时间 |
| 40 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evp_raireceiver |  | forgid,fbillid |
| 2 | pk_t_evp_raireceiver |  | fid |
