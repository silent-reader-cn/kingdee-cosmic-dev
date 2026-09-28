# 资产处置单-fa_disposal

## 付款发票信息分录-子表 t_fa_disposal_invoice

- **表名称：** 付款发票信息分录-子表
- **表名：** t_fa_disposal_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftaxamount | 税额 | numeric | 19 | 4 | √ | 0.0000 | 税额 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | finvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 4 | fpayee | fpayee | int8 | 64 |  | √ | 0 |  |
| 5 | ftotalamount | 价税合计 | numeric | 19 | 4 | √ | 0.0000 | 价税合计 |
| 6 | finvoicenumber | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 7 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fpayeetype | fpayeetype | varchar | 50 |  | √ | ' ' |  |
| 10 | falltaxrate | 税率（%） | numeric | 19 | 4 | √ | 0.0000 | 税率 bd_taxrate |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | finvoiceno | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_disposal_invoice_fid |  | fid |
| 2 | pk_fa_disposal_invoice |  | fentryid |

---

## 资产处置单-反写记录表 t_fa_disposal_wb

- **表名称：** 资产处置单-反写记录表
- **表名：** t_fa_disposal_wb

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
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_disposal_wb |  | fentryid |
| 2 | idx_fa_disposal_wb_fid |  | fid |

---

## 资产处置详情分录-子表 t_fa_disposal_detail

- **表名称：** 资产处置详情分录-子表
- **表名：** t_fa_disposal_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdetailremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fclearbillid | 清理单号 | int8 | 64 |  | √ | 0 | 清理单详情基础资料 fa_cleardetail_base |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | frealcardid | 实物卡片 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_disposal_detail_fclrid |  | fclearbillid |
| 2 | idx_fa_disposal_detail_fid |  | fid |
| 3 | pk_fa_disposal_detail |  | fentryid |

---

## 资产处置单-关联追踪表 t_fa_disposal_tc

- **表名称：** 资产处置单-关联追踪表
- **表名：** t_fa_disposal_tc

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
| 1 | idx_fa_disposal_tc_tbill |  | ftbillid |
| 2 | pk_t_fa_disposal_tc |  | fid |
| 3 | idx_fa_disposal_tc_tid |  | ftid |
| 4 | idx_fa_disposal_tc_fsbillid |  | fsbillid |
| 5 | idx_fa_disposal_tc_ftbillid |  | ftbillid |

---

## 资产处置单-主表 t_fa_disposal

- **表名称：** 资产处置单-主表
- **表名：** t_fa_disposal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fpayee | 收款人名称 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbuyertypeid | 购买方类型 | varchar | 50 |  | √ | ' ' | 购买方类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 |
| 9 | fpayeetype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fdisposalfare | 处置费用 | numeric | 23 | 10 | √ | 0.0000000000 | 处置费用 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fpayqtycreate | 可生成付款单数量 | int4 | 32 |  | √ | 1 | 可生成付款单数量 |
| 14 | fbuyerid | 购买方名称 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 15 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 18 | fdisposalincome | 处置收入 | numeric | 23 | 10 | √ | 0.0000000000 | 处置收入 |
| 19 | finvoiceqtycreate | 可生成开票申请单数量 | int4 | 32 |  | √ | 1 | 可生成开票申请单数量 |
| 20 | fbillno | 处置单号 | varchar | 30 |  | √ | ' ' | 处置单号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_disposal |  | fid |
| 2 | idx_fa_disposal_fbillno |  | fbillno |

---

## 关联子实体-子表 t_fa_disposal_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fa_disposal_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_disposal_lk |  | fpkid |
| 2 | idx_fa_disposal_lk_fid |  | fid |
