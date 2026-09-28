# 商旅付款申请单-er_checkingpaybill

## 发票明细-子表 t_er_invoiceitemcp

- **表名称：** 发票明细-子表
- **表名：** t_er_invoiceitemcp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | fexcludeamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 5 | finvoiceitemoffset | 是否抵扣 | bpchar | 1 |  | √ | '0' | 是否抵扣 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fitementryid | 费用项目分录id | int8 | 64 |  | √ | 0 | 费用项目分录id |
| 8 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 9 | finvoiceheadentryid | 发票头分录id | int8 | 64 |  | √ | 0 | 发票头分录id |
| 10 | funitprice | 不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税单价 |
| 11 | fgoodscode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 12 | fspecmodel | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 13 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 14 | finvoicecloudoffset | 发票抵扣 | bpchar | 1 |  | √ | '1' | 发票抵扣 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 17 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_invoiceitemcp_itementry |  | fitementryid |
| 2 | idx_er_invoiceitemcp_invhead |  | finvoiceheadentryid |
| 3 | t_er_invoiceitemcp_pkey |  | fentryid |
| 4 | idx_er_invoiceitemcp_fid |  | fid |

---

## 发票云附件-子表 t_er_invoiceattachinfo

- **表名称：** 发票云附件-子表
- **表名：** t_er_invoiceattachinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattachname | 附件名称 | varchar | 255 |  |  | null | 附件名称 |
| 3 | fattachurl | 附件 url | varchar | 512 |  |  | null | 附件 url |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fattachremark | 备注 | varchar | 1024 |  |  | null | 备注 |
| 6 | fattachno | 附件序列号 | varchar | 80 |  | √ | ' ' | 附件序列号 |
| 7 | frotationangle | 旋转角度 | varchar | 30 |  |  | null | 旋转角度 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | foriginalname | 源文件名称 | varchar | 255 |  |  | null | 源文件名称 |
| 10 | fgathertime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 11 | fsnapshoturl | 快照 url | varchar | 512 |  |  | null | 快照 url |
| 12 | fattachtype | 文件类型 | varchar | 30 |  |  | null | 文件类型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_invoiceattachinfo |  | fentryid |
| 2 | idx_er_invoiceattachinfo_fid |  | fid |

---

## 商旅付款申请单-主表 t_er_checkingpay

- **表名称：** 商旅付款申请单-主表
- **表名：** t_er_checkingpay

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvokeinvoicecloud | 是否与发票云交互 | bpchar | 1 |  | √ | '0' | 是否与发票云交互 |
| 3 | fappliercompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ftotalamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 6 | fpayertype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 |
| 7 | fcompany | 付款公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbankaccount | 银行账号(废弃) | varchar | 80 |  | √ | ' ' | 银行账号(废弃) |
| 9 | fpayamount | 实付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 实付金额 |
| 10 | fpaybillnum | 付款单号 | varchar | 100 |  | √ | ' ' | 付款单号 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fdifferenttax | 专票税额差异 | numeric | 23 | 10 | √ | 0 | 专票税额差异 |
| 13 | fenddate | 结束期间 | varchar | 50 |  | √ | ' ' | 结束期间 |
| 14 | foperationtype | 服务类型 | bpchar | 1 |  | √ | ' ' | 服务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 7 :用餐预订 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fserver | 服务商 | varchar | 100 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 MEITUAN :美团 |
| 17 | fapplyexplain | 申请说明 | varchar | 600 |  | √ | ' ' | 申请说明 |
| 18 | fannexnum | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 19 | fapplierdeptid | 申请人部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | forderformid | 订单表单ID | varchar | 30 |  | √ | ' ' | 订单表单ID |
| 21 | fpayerid | 收款人 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 22 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fpayerbankid | 收款银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 25 | fpaymodeid | 支付方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 26 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待付款 G :已付款 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 29 | fpaybillid | 付款单id | int8 | 64 |  | √ | 0 | 付款单id |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | fautomapinvoice | 智能发票报销 | bpchar | 1 |  | √ | '0' | 智能发票报销 |
| 32 | fbankname | 银行名称(废弃) | varchar | 100 |  | √ | ' ' | 银行名称(废弃) |
| 33 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fimagenumber | 影像编号 | varchar | 50 |  | √ | ' ' | 影像编号 |
| 35 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 36 | fperiod | 期间 | varchar | 50 |  | √ | ' ' | 期间 |
| 37 | fhappenddate | 费用发生时间 | timestamp | 0 |  |  | null | 费用发生时间 |
| 38 | fpayeraccount | 银行账号 | varchar | 80 |  | √ | ' ' | 银行账号 |
| 39 | fpaybillwriteback | 付款单反写金额 | numeric | 23 | 10 | √ | 0.0000000000 | 付款单反写金额 |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_checkingpay_fcompany |  | fcompany |
| 2 | t_er_checkingpay_pkey |  | fid |
| 3 | idx_er_checkingpay_fbillno |  | fbillno |
| 4 | idx_er_checkingpay_fbillstatus |  | fbillstatus |

---

## 关联子实体-子表 t_er_checkingpay_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_checkingpay_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | stableid | stableid | int8 | 64 |  | √ | 0 |  |
| 3 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 4 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 5 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_checkingpay_lk_pkey |  | fpkid |
| 2 | idx_er_checkingpay_lk_fid |  | fid |

---

## 发票与费用明细-子表 t_er_tripinvoiceanditem

- **表名称：** 发票与费用明细-子表
- **表名：** t_er_tripinvoiceanditem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | finvoiceentryid | 发票头分录id | int8 | 64 |  | √ | 0 | 发票头分录id |
| 4 | fexpenseentryid | 费用明细分录id | int8 | 64 |  | √ | 0 | 费用明细分录id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tripinvoiceanditem_id |  | fid |
| 2 | idx_tripcheck_finvoiceentryid |  | finvoiceentryid |
| 3 | pk_t_er_tripinvoiceanditem |  | fentryid |
| 4 | idx_tripcheck_fexpenseentryid |  | fexpenseentryid |

---

## 关联子实体-子表 t_er_checkingpayentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_checkingpayentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_checkingpayentry_lk_pkey |  | fpkid |
| 2 | idx_er_checkingpayentry_lk_fk |  | fentryid |

---

## 商旅付款申请单-关联追踪表 t_er_checkingpay_tc

- **表名称：** 商旅付款申请单-关联追踪表
- **表名：** t_er_checkingpay_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_checkingpay_tc_pkey |  | fid |
| 2 | idx_er_checkingpay_tc_sbillid |  | fsbillid |
| 3 | idx_er_checkingpay_tc_tbillid |  | ftbillid |
| 4 | idx_er_checkingpay_tc_tbill |  | ftbillid |
| 5 | idx_er_checkingpay_tc_tid |  | ftid |

---

## 商旅付款申请单-反写记录表 t_er_checkingpay_wb

- **表名称：** 商旅付款申请单-反写记录表
- **表名：** t_er_checkingpay_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_checkingpay_wb_fid |  | fid |
| 2 | t_er_checkingpay_wb_pkey |  | fentryid |

---

## 发票信息-子表 t_er_invoiceinfocp

- **表名称：** 发票信息-子表
- **表名：** t_er_invoiceinfocp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 平均税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 平均税率（%） |
| 3 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 4 | fuploadseq | 采集顺序 | int8 | 64 |  | √ | 0 | 采集顺序 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '0' | 是否抵扣 |
| 7 | fisred | 红字发票 | bpchar | 1 |  | √ | '0' | 红字发票,枚举: 0 :否 1 :是 |
| 8 | fbuyeraddressphone | 地址电话 | varchar | 255 |  | √ | ' ' | 地址电话 |
| 9 | fpassengername | 旅客 | varchar | 255 |  |  | null | 旅客 |
| 10 | fenddate | 通行日期止 | timestamp | 0 |  |  | null | 通行日期止 |
| 11 | funitprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 12 | ffuelsurcharge | 燃油附加费 | numeric | 23 | 10 | √ | 0 | 燃油附加费 |
| 13 | finvoicecode | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 14 | fcity | 发票所在地 | varchar | 50 |  | √ | ' ' | 发票所在地 |
| 15 | fbuyername | 收票公司 | varchar | 250 |  | √ | ' ' | 收票公司 |
| 16 | fpassverifybuyername | 发票抬头一致 | varchar | 30 |  | √ | ' ' | 发票抬头一致,枚举: 1 :是 0 :否 |
| 17 | fpassverifybuyertaxno | 发票税号一致 | varchar | 30 |  | √ | ' ' | 发票税号一致,枚举: 1 :是 0 :否 |
| 18 | finvoiceno | 发票号码 | varchar | 129 |  | √ | ' ' | 发票号码 |
| 19 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |
| 20 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 21 | freasonfortransferout | 转出原因 | varchar | 30 |  | √ | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 22 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 23 | foffsetamount | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 24 | finvoicecurrencyid | 发票币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | fbuyerorgid | 收票公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :海关缴款书 23 :通用机打电子发票 24 :火车退票 25 :财政电子票据 |
| 27 | fairportconstructionfee | 机场建设费及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 机场建设费及其他 |
| 28 | ftocity | 目的地 | varchar | 50 |  | √ | ' ' | 目的地 |
| 29 | fcustomeridnumber | 身份证 | varchar | 50 |  | √ | ' ' | 身份证 |
| 30 | fstartdate | 通行日期起 | timestamp | 0 |  |  | null | 通行日期起 |
| 31 | ffairtime | 飞机乘机时间 | varchar | 20 |  | √ | ' ' | 飞机乘机时间 |
| 32 | ftransportnote | 运输票据 | varchar | 30 |  | √ | ' ' | 运输票据,枚举: 1 :是 0 :否 |
| 33 | fsequencenum | 是否连号 | varchar | 30 |  | √ | ' ' | 是否连号,枚举: 1 :是 2 :否 |
| 34 | ffrominvoicecloud | 发票云导入 | bpchar | 1 |  | √ | '0' | 发票云导入 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | finoutamount | 转出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出金额 |
| 37 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 38 | fsequencenuminfo | 连号信息 | varchar | 255 |  | √ | ' ' | 连号信息 |
| 39 | fticketchanges | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 1 :正常 2 :改签 3 :售票 4 :退票 |
| 40 | finvoiceischange | 是否修改 | varchar | 30 |  | √ | ' ' | 是否修改,枚举: 1 :否 2 :是 |
| 41 | falltaxrate | 税率(%) | varchar | 100 |  | √ | ' ' | 税率(%) |
| 42 | fothertotaltaxamount | 其他税费 | numeric | 23 | 10 | √ | 0 | 其他税费 |
| 43 | fnum | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 44 | finsurancepremium | 保险费 | numeric | 23 | 10 | √ | 0 | 保险费 |
| 45 | fspecmodel | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 46 | finvoicematch | 是否匹配 | bpchar | 1 |  | √ | '0' | 是否匹配 |
| 47 | fvalidatemessage | 发票校验结果 | varchar | 255 |  | √ | ' ' | 发票校验结果 |
| 48 | fairconstfee | 机场建设费 | numeric | 23 | 10 | √ | 0 | 机场建设费 |
| 49 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 50 | finvoicealltaxcode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 51 | fregion | 地域 | bpchar | 1 |  |  | null | 地域,枚举: 1 :国内 2 :国际 |
| 52 | fcount | 发票张数 | int8 | 64 |  | √ | 0 | 发票张数 |
| 53 | finvoicenotaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 54 | finvoicefrom | 发票来源 | varchar | 30 |  | √ | '1' | 发票来源,枚举: 1 :发票云 2 :OCR识别 3 :商旅月结 |
| 55 | fbillcreatetime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 56 | ffromcity | 出发地 | varchar | 50 |  | √ | ' ' | 出发地 |
| 57 | fbuyertaxno | 收票方税号 | varchar | 50 |  | √ | ' ' | 收票方税号 |
| 58 | fremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 59 | fmakeoutcompname | 开票公司 | varchar | 250 |  | √ | ' ' | 开票公司 |
| 60 | fismapexpense | 关联费用明细 | bpchar | 1 |  | √ | '1' | 关联费用明细,枚举: 1 :是 0 :否 |
| 61 | fpersonalinvoice | 个人发票 | varchar | 30 |  | √ | ' ' | 个人发票,枚举: 1 :是 0 :否 |
| 62 | fendorsement | 签注 | varchar | 255 |  | √ | ' ' | 签注 |
| 63 | finvoicegoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_invoiceinfocp_fseq |  | fid |
| 2 | idx_er_invoicecp_query |  | fserialno |
| 3 | t_er_invoiceinfocp_pkey |  | fentryid |

---

## 结算单关联信息-子表 t_er_checkingpayentry

- **表名称：** 结算单关联信息-子表
- **表名：** t_er_checkingpayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | flargeinvoicenum_tag | 发票号码_详情 | text | 0 |  | √ | ' ' | 发票号码_详情 |
| 4 | fserviceitem | 服务项目 | varchar | 10 |  | √ | ' ' | 服务项目,枚举: TICKET :票价 SERVICE :服务费 |
| 5 | factentryamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 6 | fmatch | 是否匹配 | bpchar | 1 |  | √ | '0' | 是否匹配 |
| 7 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 8 | fdept | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fcheckingbillno | 月结账单编码 | varchar | 255 |  | √ | ' ' | 月结账单编码 |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | fuserid | 人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | finvoicenum | finvoicenum | varchar | 255 |  | √ | ' ' |  |
| 13 | fcheckingbillid | 结算单id | int8 | 64 |  | √ | 0 | 结算单id |
| 14 | fnotaxoriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 15 | ftravelbill | 是否行程单/火车票 | bpchar | 1 |  | √ | '0' | 是否行程单/火车票 |
| 16 | fticketnum | 电子客票号/火车票 | varchar | 50 |  | √ | ' ' | 电子客票号/火车票 |
| 17 | foperationtype | 服务类型 | bpchar | 1 |  | √ | ' ' | 服务类型,枚举: 1 :酒店预订 2 :机票预订 3 :用车预订 4 :火车预订 5 :用餐预定 |
| 18 | fisuploadinvoicecloud | 是否上传发票云 | bpchar | 1 |  | √ | '0' | 是否上传发票云 |
| 19 | flargeinvoicenum | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fcheckingbillnum | 结算单号 | varchar | 100 |  | √ | ' ' | 结算单号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_checkingpayentry_pkey |  | fentryid |
| 2 | idx_er_checkingpayentry_id |  | fid |
