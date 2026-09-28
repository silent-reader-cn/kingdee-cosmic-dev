# ssc发票-task_invoice

## 单据体-子表 t_tk_invoiceentry

- **表名称：** 单据体-子表
- **表名：** t_tk_invoiceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxexcluded | 不含税单价 | numeric | 19 | 6 | √ | 0.000000 | 不含税单价 |
| 3 | ftaxrate | 税率 | numeric | 19 | 6 | √ | 0.000000 | 税率 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fspecs | 规格型号 | varchar | 255 |  |  | null | 规格型号 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ftaxprice | 含税单价 | numeric | 19 | 6 | √ | 0.000000 | 含税单价 |
| 8 | fmoney | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 9 | ftaxtotal | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 10 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fquantity | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 13 | fproductname | 商品名称 | varchar | 255 |  |  | null | 商品名称 |
| 14 | ftaxamt | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_invoiceentry_pkey |  | fentryid |
| 2 | index_ssc_invoiceentry |  | fid,fmaterialid |

---

## ssc发票-主表 t_tk_invoice

- **表名称：** ssc发票-主表
- **表名：** t_tk_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fauthenticatedate | 认证日期 | timestamp | 0 |  |  | null | 认证日期 |
| 3 | fcontactsale | 销方地址/电话 | varchar | 255 |  |  | null | 销方地址/电话 |
| 4 | fcheckcode | 校验码 | varchar | 255 |  |  | null | 校验码 |
| 5 | famount | 金额合计 | numeric | 19 | 6 | √ | 0.000000 | 金额合计 |
| 6 | fauthenticatestatus | 认证状态 | varchar | 100 |  | √ | ' ' | 认证状态 |
| 7 | fpassword | 密码区 | varchar | 255 |  |  | null | 密码区 |
| 8 | fiscreditnote | 红字发票 | bpchar | 1 |  | √ | '0' | 红字发票 |
| 9 | fhasstamp | 是否有印章 | bpchar | 1 |  | √ | '0' | 是否有印章 |
| 10 | ftemplatetype | 模板类型 | varchar | 100 |  | √ | ' ' | 模板类型 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | ftransferout | 进项转出 | numeric | 19 | 6 | √ | 0.000000 | 进项转出 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcompanysale | 销方公司 | varchar | 255 |  |  | null | 销方公司 |
| 15 | fbankinformationbuy | 购方银行名称/账号 | varchar | 255 |  |  | null | 购方银行名称/账号 |
| 16 | finvoicenumber | 发票号码 | varchar | 100 |  | √ | ' ' | 发票号码 |
| 17 | fcompanybuy | 购方公司 | varchar | 255 |  |  | null | 购方公司 |
| 18 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 19 | ftaxnumberbuy | 购方公司税号 | varchar | 30 |  | √ | ' ' | 购方公司税号 |
| 20 | finvoicecode | 发票代码 | varchar | 100 |  | √ | ' ' | 发票代码 |
| 21 | fbillstatu | fbillstatu | varchar | 30 |  | √ | ' ' |  |
| 22 | fauthenticatorid | 认证人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 24 | fremark | 备注 | varchar | 255 |  |  | null | 备注 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fvoucherid | 凭证 | int8 | 64 |  | √ | 0 | 凭证 |
| 27 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | fauthenticateway | 认证方式 | varchar | 100 |  | √ | ' ' | 认证方式 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fbillstatue | fbillstatue | bpchar | 1 |  | √ | ' ' |  |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fistrue | 发票真伪 | bpchar | 1 |  | √ | '0' | 发票真伪 |
| 33 | fduedate | 认证到期日 | timestamp | 0 |  |  | null | 认证到期日 |
| 34 | fimagenumber | 影像编码 | varchar | 100 |  | √ | ' ' | 影像编码 |
| 35 | fimagepage | 影像页码 | int8 | 64 |  | √ | 0 | 影像页码 |
| 36 | finvoicetype | 发票类型 | varchar | 100 |  | √ | ' ' | 发票类型 |
| 37 | ftax | 税额合计 | numeric | 19 | 6 | √ | 0.000000 | 税额合计 |
| 38 | fbankinformationsale | 销方银行名称/账号 | varchar | 255 |  |  | null | 销方银行名称/账号 |
| 39 | fbillid | 业务单据ID | varchar | 50 |  | √ | ' ' | 业务单据ID |
| 40 | fcontactbuy | 购方地址/电话 | varchar | 255 |  |  | null | 购方地址/电话 |
| 41 | fdeductible | 可抵税额 | numeric | 19 | 6 | √ | 0.000000 | 可抵税额 |
| 42 | ftaxnumbersale | 销方公司税号 | varchar | 30 |  | √ | ' ' | 销方公司税号 |
| 43 | famounttax | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fbilltypeid | 业务单据 | int8 | 64 |  | √ | 0 | 业务单据 task_taskbill |
| 46 | ftemplatetpye | ftemplatetpye | varchar | 255 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_invoice |  | fbillid |
| 2 | t_tk_invoice_pkey |  | fid |
| 3 | idx_ssc_invoice_invonum |  | finvoicenumber |
