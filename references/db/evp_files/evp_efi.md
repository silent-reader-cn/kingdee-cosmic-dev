# 财政电子票据-evp_efi

## 财政电子票据-主表 t_evp_efi

- **表名称：** 财政电子票据-主表
- **表名：** t_evp_efi

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisredinvoice | 红字发票 | bpchar | 1 |  | √ | '0' | 红字发票 |
| 3 | feinvoiceid | 财政电子票据标识 | varchar | 50 |  | √ | ' ' | 财政电子票据标识 |
| 4 | foperatorid | 入池操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fisintopool | 电子凭证入池 | bpchar | 1 |  | √ | '0' | 电子凭证入池 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fdirectbillid | 关联单据ID | int8 | 64 |  | √ | 0 | 关联单据ID |
| 8 | fisdelete | 已删除 | bpchar | 1 |  | √ | '0' | 已删除 |
| 9 | fbilldate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 10 | fvoucherno | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 11 | ffileurl | 原文件地址 | varchar | 500 |  |  | ' ' | 原文件地址 |
| 12 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fbasetext | 原文件base64 | varchar | 500 |  | √ | ' ' | 原文件base64 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | farchivebatchcode | 归档批次号 | varchar | 255 |  | √ | ' ' | 归档批次号 |
| 16 | fcostcompany | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fsourcexbrl | 原始xbrl | varchar | 1000 |  | √ | ' ' | 原始xbrl |
| 18 | ffilename | 原文件名 | varchar | 2000 |  |  | ' ' | 原文件名 |
| 19 | fisarchive | 归档 | bpchar | 1 |  | √ | '0' | 归档 |
| 20 | finvoicenumber | 发票号 | varchar | 50 |  | √ | ' ' | 发票号 |
| 21 | fsourcexbrldata_tag | 原始xbrlbase64_详情 | text | 0 |  |  | null | 原始xbrlbase64_详情 |
| 22 | foriginsysid | 集成系统 | int8 | 64 |  | √ | 0 | [集成系统配置 evp_originsys](../evp_files/evp_originsys.md) |
| 23 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 24 | fdirectbillno | 关联单据号 | varchar | 50 |  | √ | ' ' | 关联单据号 |
| 25 | fvoucherid | 关联凭证id | varchar | 50 |  | √ | ' ' | 关联凭证id |
| 26 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 27 | fseqno | 票据流水号（唯一标识） | varchar | 255 |  | √ | ' ' | 票据流水号（唯一标识） |
| 28 | fsourcexbrldata | 原始xbrlbase64 | varchar | 255 |  | √ | ' ' | 原始xbrlbase64 |
| 29 | fdirectbilltype | 关联单据类型 | varchar | 50 |  | √ | ' ' | 关联单据类型 |
| 30 | fbasetext_tag | 原文件base64_详情 | text | 0 |  |  | null | 原文件base64_详情 |
| 31 | fxbrlurl | xbrl文件地址 | varchar | 500 |  |  | ' ' | xbrl文件地址 |
| 32 | fbatchcode | 批次号 | varchar | 255 |  | √ | ' ' | 批次号 |
| 33 | ffileurl_tag | 原文件地址_详情 | text | 0 |  |  | null | 原文件地址_详情 |
| 34 | fishandle | 数据来源 | bpchar | 1 |  | √ | '0' | 数据来源,枚举: 0 :API导入 1 :手工新增 2 :系统抽取 |
| 35 | fbillid | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 36 | fpaidamt | 总金额 | numeric | 23 | 10 | √ | 0 | 总金额 |
| 37 | fhasbeenchecked | 已验真 | bpchar | 1 |  | √ | '0' | 已验真 |
| 38 | fhasbeenbooked | 已入账 | bpchar | 1 |  | √ | '0' | 已入账 |
| 39 | fbookdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 40 | fintopooldate | 入池时间 | timestamp | 0 |  |  | null | 入池时间 |
| 41 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_evp_efi |  | fid |
| 2 | idx_evp_efi |  | forgid,fbillid |
