# 已确认单据(废弃)-sim_confirm_bill

## 已确认单据(废弃)-关联追踪表 t_sim_confirm_bill_tc

- **表名称：** 已确认单据(废弃)-关联追踪表
- **表名：** t_sim_confirm_bill_tc

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
| 1 | pk_sim_confirm_bill_tc |  | fid |
| 2 | idx_sim_confirm_bill_tc_tbill |  | ftbillid |
| 3 | idx_sim_confirm_bill_tc_tid |  | ftid |

---

## 关联子实体-子表 t_sim_confirm_bill_item_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sim_confirm_bill_item_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftaxamount | 含税金额_确认携带值 | numeric | 23 | 10 |  | null | 含税金额_确认携带值 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | famount | 不含税金额_确认携带值 | numeric | 23 | 10 |  | null | 不含税金额_确认携带值 |
| 5 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 6 | fnum | 数量_确认携带值 | numeric | 23 | 10 |  | null | 数量_确认携带值 |
| 7 | famount_old | 不含税金额_原始携带值 | numeric | 23 | 10 |  | null | 不含税金额_原始携带值 |
| 8 | fnum_old | 数量_原始携带值 | numeric | 23 | 10 |  | null | 数量_原始携带值 |
| 9 | ftaxamount_old | 含税金额_原始携带值 | numeric | 23 | 10 |  | null | 含税金额_原始携带值 |
| 10 | ftax_old | 税额_原始携带值 | numeric | 23 | 10 |  | null | 税额_原始携带值 |
| 11 | ftax | 税额_确认携带值 | numeric | 23 | 10 |  | null | 税额_确认携带值 |
| 12 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 13 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_confirm_bill_item_lk |  | fpkid |
| 2 | idx_sim_confirm_bill_item_lk_fk |  | fentryid |

---

## 已确认单据(废弃)-反写记录表 t_sim_confirm_bill_wb

- **表名称：** 已确认单据(废弃)-反写记录表
- **表名：** t_sim_confirm_bill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_confirm_bill_wb_fk |  | fid |
| 2 | pk_sim_confirm_bill_wb |  | fentryid |

---

## 已确认单据(废弃)-主表 t_sim_confirm_bill

- **表名称：** 已确认单据(废弃)-主表
- **表名：** t_sim_confirm_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuyeraddr | 购方地址、电话 | varchar | 100 |  | √ | ' ' | 购方地址、电话 |
| 3 | fdifference | 税额误差 | numeric | 23 | 10 | √ | 0.0000000000 | 税额误差 |
| 4 | fsuppliercontact | 供应商联系人 | varchar | 100 |  | √ | ' ' | 供应商联系人 |
| 5 | fcontractdate | 合同日期 | timestamp | 0 |  |  | null | 合同日期 |
| 6 | fdrawer | 开票人 | varchar | 50 |  | √ | ' ' | 开票人 |
| 7 | fbilltaxrate | 单据税率 | varchar | 30 |  | √ | ' ' | 单据税率 |
| 8 | fbillextrafield2 | 已确认单据扩展字段2 | varchar | 200 |  | √ | ' ' | 已确认单据扩展字段2 |
| 9 | fbillextrafield1 | 已确认单据扩展字段1 | varchar | 200 |  | √ | ' ' | 已确认单据扩展字段1 |
| 10 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 11 | fpurchasername | 采购商名称 | varchar | 100 |  | √ | ' ' | 采购商名称 |
| 12 | fconfirmbillno | 编号 | varchar | 100 |  | √ | ' ' | 编号 |
| 13 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fsaleraddr | 销方地址电话 | varchar | 100 |  | √ | ' ' | 销方地址电话 |
| 15 | fsplitrule | 拆合规则 | varchar | 50 |  | √ | ' ' | 拆合规则,枚举: |
| 16 | fbuyername | 购方名称 | varchar | 100 |  | √ | ' ' | 购方名称 |
| 17 | fsalertaxno | 销方纳税人识别号 | varchar | 50 |  | √ | ' ' | 销方纳税人识别号 |
| 18 | foriginalinvoiceno | 待冲蓝票号码 | varchar | 15 |  | √ | ' ' | 待冲蓝票号码 |
| 19 | fconfirmbillstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :未处理 2 :已处理 3 :已作废 |
| 20 | fbuyerphone | 收票人电话 | varchar | 100 |  | √ | ' ' | 收票人电话 |
| 21 | fdeduction | 扣除额(差额) | numeric | 23 | 10 | √ | 0.0000000000 | 扣除额(差额) |
| 22 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 026 :增值税电子普通发票 028 :增值税电子专用发票 007 :增值税纸质普通发票 004 :增值税纸质专用发票 |
| 23 | foriginalinvoicecode | 待冲蓝票代码 | varchar | 20 |  | √ | ' ' | 待冲蓝票代码 |
| 24 | fbuyerbank | 购方开户行及账号 | varchar | 100 |  | √ | ' ' | 购方开户行及账号 |
| 25 | fsalername | 销方名称 | varchar | 50 |  | √ | ' ' | 销方名称 |
| 26 | fbuyeremail | 收票人邮箱 | varchar | 100 |  | √ | ' ' | 收票人邮箱 |
| 27 | fpayee | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 28 | fhsbz | 是否含税 | varchar | 50 |  | √ | ' ' | 是否含税,枚举: 0 :不含税 1 :含税 |
| 29 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 30 | foldinvoiceamount | 原始合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 原始合计金额 |
| 31 | fpurchasercontact | 采购商联系人 | varchar | 100 |  | √ | ' ' | 采购商联系人 |
| 32 | ftotaltax | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 33 | freviewer | 复核人 | varchar | 50 |  | √ | ' ' | 复核人 |
| 34 | fbuyertaxno | 购方纳税人识别号 | varchar | 100 |  | √ | ' ' | 购方纳税人识别号 |
| 35 | fsalerbank | 销方开户行及账号 | varchar | 100 |  | √ | ' ' | 销方开户行及账号 |
| 36 | fissuestrategy | 是否使用开票人策略 | varchar | 10 |  | √ | ' ' | 是否使用开票人策略,枚举: 0 :是 1 :否 |
| 37 | fpurchaserphone | 采购商电话 | varchar | 100 |  | √ | ' ' | 采购商电话 |
| 38 | fbillnature | 单据性质 | varchar | 30 |  | √ | ' ' | 单据性质,枚举: 1 :正数 2 :负数 |
| 39 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 40 | fsuppliername | 供应商名称 | varchar | 100 |  | √ | ' ' | 供应商名称 |
| 41 | fcontractamount | 合同金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合同金额 |
| 42 | fcontractno | 合同编号 | varchar | 100 |  | √ | ' ' | 合同编号 |
| 43 | fsupplierphone | 供应商电话 | varchar | 100 |  | √ | ' ' | 供应商电话 |
| 44 | fbuyerproperty | 购方类型 | varchar | 30 |  | √ | ' ' | 购方类型,枚举: 0 :企业 1 :个人 |
| 45 | foldbillnos | 原始单据编号 | varchar | 2000 |  | √ | ' ' | 原始单据编号 |
| 46 | finvoiceamount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 47 | fwxid | 微信ID | varchar | 50 |  | √ | ' ' | 微信ID |
| 48 | fbuyerpersonname | 收票人名称 | varchar | 100 |  | √ | ' ' | 收票人名称 |
| 49 | fsystemsource | 数据来源系统 | varchar | 50 |  | √ | ' ' | 数据来源系统 |
| 50 | fjqbh | 开票设备 | varchar | 50 |  | √ | ' ' | 开票设备,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_confirm_bill |  | fconfirmbillno |
| 2 | pk_sim_confirm_bill |  | fid |

---

## 单据体-子表 t_sim_confirm_bill_item

- **表名称：** 单据体-子表
- **表名：** t_sim_confirm_bill_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 含税金额 |
| 3 | fremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 4 | fextrafield | 扩展字段 | varchar | 200 |  | √ | ' ' | 扩展字段 |
| 5 | frowdifference | 税额误差 | numeric | 23 | 10 | √ | 0.0000000000 | 税额误差 |
| 6 | ftaxrate | 税率 | varchar | 30 |  | √ | ' ' | 税率,枚举: 0 :0% 0.01 :1% 0.015 :1.5% 0.03 :3% 0.04 :4% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.16 :16% 0.17 :17% |
| 7 | frowtype | 明细行类型 | varchar | 30 |  | √ | ' ' | 明细行类型,枚举: 0 :整单折扣 1 :单行折扣 2 :商品行 3 :负数行 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 10 | fdeduction | fdeduction | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | ftaxpremark | 是否享受优惠 | varchar | 50 |  | √ | ' ' | 是否享受优惠,枚举: 1 :享受 0 :不享受 |
| 12 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 13 | ftaxunitprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 14 | funitprice | 不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税单价 |
| 15 | fgoodscode | 税收分类编码 | varchar | 50 |  | √ | ' ' | 税收分类编码 |
| 16 | fgoodsname | 商品名称 | varchar | 100 |  | √ | ' ' | 商品名称 |
| 17 | fspecification | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 18 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 19 | fgoodssimplename | 商品简称 | varchar | 100 |  | √ | ' ' | 商品简称 |
| 20 | fbillsourceid | 单据来源id | varchar | 50 |  | √ | ' ' | 单据来源id |
| 21 | fzzstsgl | 优惠政策内容 | varchar | 200 |  | √ | ' ' | 优惠政策内容 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 23 | fspbm | 商品编码 | varchar | 50 |  | √ | ' ' | 商品编码 |
| 24 | funit | 计量单位 | varchar | 50 |  | √ | ' ' | 计量单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_confirm_bill_item_fk |  | fid |
| 2 | pk_sim_confirm_bill_item |  | fentryid |

---

## 已确认单据(废弃)-分表 t_sim_confirm_bill_e

- **表名称：** 已确认单据(废弃)-分表
- **表名：** t_sim_confirm_bill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foriginalissuetime | 待冲蓝票开票日期 | timestamp | 0 |  |  | null | 待冲蓝票开票日期 |
| 3 | finfocode | 信息表编号 | varchar | 200 |  | √ | ' ' | 信息表编号 |
| 4 | fspecialtype | 特殊票种 | varchar | 50 |  | √ | ' ' | 特殊票种,枚举: 00 :非特殊票种 02 :收购 06 :抵扣通行费 07 :不抵扣通行费 08 :成品油 |
| 5 | fapplicant | 申请方 | varchar | 50 |  | √ | ' ' | 申请方,枚举: 2 :销方申请 1 :购方申请-未抵扣 0 :购方申请-已抵扣 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_confirm_bill_e |  | fspecialtype |
| 2 | pk_sim_confirm_bill_e |  | fid |
