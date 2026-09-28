# 红字增值税专用发票信息表-tdm_invoice_input_red

## 红字专用发票明细-子表 t_tdm_speinvoice_item_red

- **表名称：** 红字专用发票明细-子表
- **表名：** t_tdm_speinvoice_item_red

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdetailamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 3 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 4 | funitprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 5 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 6 | fgoodsname | 货物（劳务服务）名称 | varchar | 120 |  | √ | ' ' | 货物（劳务服务）名称 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fcount | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_speinvoice_item_red_fk |  | fid |
| 2 | pk_tdm_speinvoice_item_red |  | fentryid |

---

## 红字增值税专用发票信息表-主表 t_tdm_invoice_input_red

- **表名称：** 红字增值税专用发票信息表-主表
- **表名：** t_tdm_invoice_input_red

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 7 | finvoicecode | 对应蓝字发票代码 | varchar | 32 |  | √ | ' ' | 对应蓝字发票代码 |
| 8 | finvoicedata | 填开日期 | timestamp | 0 |  |  | null | 填开日期 |
| 9 | fbuyername | 购方名称 | varchar | 100 |  | √ | ' ' | 购方名称 |
| 10 | finvoiceno | 对应蓝字发票号码 | varchar | 32 |  | √ | ' ' | 对应蓝字发票号码 |
| 11 | fdeductedstatus | 购买方抵扣状态 | varchar | 30 |  | √ | ' ' | 购买方抵扣状态,枚举: 0 :未抵扣 1 :已抵扣 |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fsalertaxno | 销方税号 | varchar | 20 |  | √ | ' ' | 销方税号 |
| 14 | fbuyertaxno | 购方税号 | varchar | 20 |  | √ | ' ' | 购方税号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fserialno | 红字专用发票信息表编号 | varchar | 50 |  | √ | ' ' | 红字专用发票信息表编号 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 21 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 2 :电子专票 4 :纸质专票 |
| 22 | finvoiceamount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 23 | fsalername | 销方名称 | varchar | 100 |  | √ | ' ' | 销方名称 |
| 24 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源 |
| 25 | ftotaltaxamount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_invoice_input_red |  | fid |
| 2 | idx_tdm_invoice_input_red |  | forgid |
