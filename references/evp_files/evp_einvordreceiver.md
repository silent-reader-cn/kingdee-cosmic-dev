# 数电票普通发票-evp_einvordreceiver

## 数电票普通发票-主表 t_evp_einvordreceiver

- **表名称：** 数电票普通发票-主表
- **表名：** t_evp_einvordreceiver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisintopool | 电子凭证入池 | bpchar | 1 |  | √ | '0' | 电子凭证入池 |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbeginperiod | 权责发生制下支出所属期起 | varchar | 50 |  | √ | ' ' | 权责发生制下支出所属期起 |
| 5 | fhasbeenpaid | 已付款 | bpchar | 1 |  | √ | '0' | 已付款 |
| 6 | ffileurl | 原文件地址 | varchar | 500 |  | √ | ' ' | 原文件地址 |
| 7 | fendyear | 所得税税前扣除年度止 | varchar | 50 |  | √ | ' ' | 所得税税前扣除年度止 |
| 8 | farchivebatchcode | 归档批次号 | varchar | 255 |  | √ | ' ' | 归档批次号 |
| 9 | fcostcompany | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | ffilename | 原文件名 | varchar | 2000 |  | √ | ' ' | 原文件名 |
| 11 | finvoicenumber | 发票号 | varchar | 50 |  | √ | ' ' | 发票号 |
| 12 | fcontractnumber | 合同编码 | varchar | 50 |  | √ | ' ' | 合同编码 |
| 13 | foriginsysid | 集成系统 | int8 | 64 |  | √ | 0 | 集成系统配置 evp_originsys |
| 14 | ftotalamountexcludingtax | 不含税金额合计 | numeric | 23 | 10 | √ | 0 | 不含税金额合计 |
| 15 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 16 | fdirectbillno | 关联单据编号 | varchar | 50 |  | √ | ' ' | 关联单据编号 |
| 17 | fvoucherid | 关联凭证id | varchar | 50 |  | √ | ' ' | 关联凭证id |
| 18 | fbeginyear | 所得税税前扣除年度起 | varchar | 50 |  | √ | ' ' | 所得税税前扣除年度起 |
| 19 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 20 | fseqno | 票据流水号（唯一标识） | varchar | 255 |  | √ | ' ' | 票据流水号（唯一标识） |
| 21 | famortizationmethod | 固定资产无形资产摊销方法 | varchar | 50 |  | √ | ' ' | 固定资产无形资产摊销方法 |
| 22 | fdirectbilltype | 关联单据类型 | varchar | 50 |  | √ | ' ' | 关联单据类型 |
| 23 | fbasetext_tag | 原文件base64_详情 | text | 0 |  |  | null | 原文件base64_详情 |
| 24 | ffileurl_tag | 原文件地址_详情 | text | 0 |  |  | null | 原文件地址_详情 |
| 25 | fhasbeencompleted | 已所得税税前扣除 | bpchar | 1 |  | √ | '0' | 已所得税税前扣除 |
| 26 | fishandle | 数据来源 | bpchar | 1 |  | √ | '0' | 数据来源,枚举: 0 :API导入 1 :手工新增 2 :系统抽取 |
| 27 | fbillid | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 28 | fbookdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 29 | fintopooldate | 入池时间 | timestamp | 0 |  |  | null | 入池时间 |
| 30 | ftotaltaxamount | 税额合计 | numeric | 23 | 10 | √ | 0 | 税额合计 |
| 31 | fisredinvoice | 红字发票 | bpchar | 1 |  | √ | '0' | 红字发票 |
| 32 | foperatorid | 入池操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fdirectbillid | 关联单据ID | int8 | 64 |  | √ | 0 | 关联单据ID |
| 34 | fisdelete | 已删除 | bpchar | 1 |  | √ | '0' | 已删除 |
| 35 | fvoucherno | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 36 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 37 | fbasetext | 原文件base64 | varchar | 500 |  | √ | ' ' | 原文件base64 |
| 38 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | fnameofseller | 销售方名称 | varchar | 255 |  | √ | ' ' | 销售方名称 |
| 40 | fisarchive | 归档 | bpchar | 1 |  | √ | '0' | 归档 |
| 41 | felectronicnumber | 银行回单编号 | varchar | 50 |  | √ | ' ' | 银行回单编号 |
| 42 | fendperiod | 权责发生制下支出所属期止 | varchar | 50 |  | √ | ' ' | 权责发生制下支出所属期止 |
| 43 | fdateofissue | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 44 | ftaxsocialcreditcode | 销售方纳税人识别号（统一社会信用代码） | varchar | 50 |  | √ | ' ' | 销售方纳税人识别号（统一社会信用代码） |
| 45 | fmatchingstate | 业务单据和发票匹配状态 | varchar | 50 |  | √ | ' ' | 业务单据和发票匹配状态 |
| 46 | fxbrlurl | xbrl文件地址 | varchar | 255 |  | √ | ' ' | xbrl文件地址 |
| 47 | fbatchcode | 批次号 | varchar | 255 |  | √ | ' ' | 批次号 |
| 48 | fhasbeenfsos | 已做保理、出售、 资产证券化 | bpchar | 1 |  | √ | '0' | 已做保理、出售、 资产证券化 |
| 49 | fhasbeenchecked | 已验真 | bpchar | 1 |  | √ | '0' | 已验真 |
| 50 | fhasbeenbooked | 已入账 | bpchar | 1 |  | √ | '0' | 已入账 |
| 51 | ftaxincludedamountinfigur | 价税合计（小写） | numeric | 23 | 10 | √ | 0 | 价税合计（小写） |
| 52 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_evp_einvordreceiver |  | fid |
| 2 | idx_evp_einvordreceiver |  | forgid,fbillid |
