# 通行费发票-tdm_input_transit_inv

## 通行费发票-主表 t_tdm_input_transit_inv

- **表名称：** 通行费发票-主表
- **表名：** t_tdm_input_transit_inv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvaliddate | 作废时间 | timestamp | 0 |  |  | null | 作废时间 |
| 3 | fdrawer | 开票人 | varchar | 60 |  | √ | ' ' | 开票人 |
| 4 | fcheckcode | 校验码 | varchar | 100 |  | √ | ' ' | 校验码 |
| 5 | fpayee | 收款人 | varchar | 60 |  | √ | ' ' | 收款人 |
| 6 | ftaxperioddate | 税期所属日期 | timestamp | 0 |  |  | null | 税期所属日期 |
| 7 | finvoicestatus | 发票状态 | varchar | 30 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 4 :异常 |
| 8 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 10 | fbuyeraccount | 购方银行帐号 | varchar | 300 |  | √ | ' ' | 购方银行帐号 |
| 11 | fbuyeraddressphone | 购方地址电话 | varchar | 200 |  | √ | ' ' | 购方地址电话 |
| 12 | feffectivetaxamount | 有效税额 | numeric | 23 | 10 | √ | 0.0000000000 | 有效税额 |
| 13 | fauthenticateflag | 认证标志 | varchar | 30 |  | √ | ' ' | 认证标志,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 4 :未认证 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fopentype | 开票类型 | varchar | 30 |  | √ | ' ' | 开票类型,枚举: 0 :蓝字发票 1 :红字发票 |
| 17 | fscanauthenticatetime | 扫描认证时间 | timestamp | 0 |  |  | null | 扫描认证时间 |
| 18 | fsaleraddressphone | 销方地址电话 | varchar | 200 |  | √ | ' ' | 销方地址电话 |
| 19 | fsaleraccount | 销方银行帐号 | varchar | 300 |  | √ | ' ' | 销方银行帐号 |
| 20 | fmachineno | 机器编号 | varchar | 60 |  | √ | ' ' | 机器编号 |
| 21 | fselecttime | 勾选时间 | timestamp | 0 |  |  | null | 勾选时间 |
| 22 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 23 | fselectauthenticatetime | 勾选认证时间 | timestamp | 0 |  |  | null | 勾选认证时间 |
| 24 | finvoicecode | 发票代码 | varchar | 64 |  | √ | ' ' | 发票代码 |
| 25 | freviewer | 复核人 | varchar | 60 |  | √ | ' ' | 复核人 |
| 26 | finvoicedata | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 27 | fbuyername | 购方名称 | varchar | 200 |  | √ | ' ' | 购方名称 |
| 28 | finvoiceno | 发票号码 | varchar | 64 |  | √ | ' ' | 发票号码 |
| 29 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 30 | fsalertaxno | 销方税号 | varchar | 40 |  | √ | ' ' | 销方税号 |
| 31 | fbuyertaxno | 购方税号 | varchar | 40 |  | √ | ' ' | 购方税号 |
| 32 | ftaxamount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 33 | fremark | 备注 | varchar | 480 |  | √ | ' ' | 备注 |
| 34 | ftaxperiod | 所属税期 | varchar | 20 |  | √ | ' ' | 所属税期 |
| 35 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 37 | ftaxperioddate2 | ftaxperioddate2 | timestamp | 0 |  |  | null |  |
| 38 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 39 | foriginalinvoiceno | 原发票号码 | varchar | 64 |  | √ | ' ' | 原发票号码 |
| 40 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 41 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 42 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 15 :通行费电子发票 |
| 43 | foriginalinvoicecode | 原发票代码 | varchar | 64 |  | √ | ' ' | 原发票代码 |
| 44 | finvoiceamount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 45 | fsalername | 销方名称 | varchar | 200 |  | √ | ' ' | 销方名称 |
| 46 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源 |
| 47 | fproxymark | 代开标识 | varchar | 30 |  | √ | ' ' | 代开标识,枚举: 0 :默认 1 :代开 |
| 48 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_input_transit_inv2 |  | fbaseinvoicetype |
| 2 | idx_tdm_input_transit_inv |  | forgid,ftaxperiod |
| 3 | t_tdm_input_transit_inv_pkey |  | fid |

---

## 通行费发票-分表 t_tdm_input_transit_inv_a

- **表名称：** 通行费发票-分表
- **表名：** t_tdm_input_transit_inv_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcertstatus | 认证状态 | varchar | 50 |  | √ | ' ' | 认证状态,枚举: 0 :未认证 1 :勾选认证 2 :扫描认证 |
| 3 | fisgeneratevoucher | 生成凭证 | varchar | 50 |  | √ | ' ' | 生成凭证,枚举: 1 :是 0 :否 |
| 4 | fselectresult | 勾选结果 | varchar | 50 |  | √ | ' ' | 勾选结果,枚举: 0 :- 1 :抵扣 2 :不抵扣 |
| 5 | fauthdate | 认证日期 | timestamp | 0 |  |  | null | 认证日期 |
| 6 | fsignstatus | 签收状态 | varchar | 50 |  | √ | ' ' | 签收状态,枚举: 1 :已签收 0 :未签收 |
| 7 | fselectstatus | 勾选状态 | varchar | 50 |  | √ | ' ' | 勾选状态,枚举: 1 :已勾选 0 :未勾选 |
| 8 | fsenddate | 发送时间 | timestamp | 0 |  |  | null | 发送时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_input_transit_inv_a |  | fselectstatus |
| 2 | pk_tdm_input_transit_inv_a |  | fid |

---

## 通行费发票明细-子表 t_tdm_tollinvoice_item

- **表名称：** 通行费发票明细-子表
- **表名：** t_tdm_tollinvoice_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fzerotaxrateflag | 零税率标识 | varchar | 30 |  | √ | ' ' | 零税率标识,枚举: 0 :非零税率 1 :免税 2 :不征税 3 :普通零税率 |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 5 | fdiscounttype | 折扣类型 | varchar | 30 |  | √ | ' ' | 折扣类型,枚举: 0 :正常行 1 :折扣行 2 :被折扣行 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdetailamount | 明细金额(不含税) | numeric | 23 | 10 | √ | 0.0000000000 | 明细金额(不含税) |
| 8 | fpreferentialpolicy | 优惠政策标识 | varchar | 30 |  | √ | ' ' | 优惠政策标识,枚举: 0 :不使用 1 :使用 |
| 9 | fenddate | 通行结束日期 | timestamp | 0 |  |  | null | 通行结束日期 |
| 10 | fgoodscode | 商品编码 | varchar | 100 |  | √ | ' ' | 商品编码 |
| 11 | fgoodsname | 货物名称 | varchar | 200 |  | √ | ' ' | 货物名称 |
| 12 | fspecmodel | 规格型号 | varchar | 100 |  | √ | ' ' | 规格型号 |
| 13 | fstartdate | 通行起始日期 | timestamp | 0 |  |  | null | 通行起始日期 |
| 14 | fversionno | 商品编码版本号 | varchar | 100 |  | √ | ' ' | 商品编码版本号 |
| 15 | fvatexception | 增值税特殊管理 | varchar | 100 |  | √ | ' ' | 增值税特殊管理 |
| 16 | fvehplate | 车牌号码 | varchar | 100 |  | √ | ' ' | 车牌号码 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_tollinvoice_item_pkey |  | fentryid |
| 2 | idx_t_tdm_tollinvoice_item |  | fid |
