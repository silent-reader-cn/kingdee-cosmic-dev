# 电商售后服务单-pbd_eafservicebill

## 电商售后服务单-主表 t_mal_eafservice

- **表名称：** 电商售后服务单-主表
- **表名：** t_mal_eafservice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 4 | freturnphone | 退换联系电话 | varchar | 50 |  | √ | ' ' | 退换联系电话 |
| 5 | fapplydate | 申请时间 | timestamp | 0 |  |  | null | 申请时间 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forderid | 电商订单号 | varchar | 50 |  | √ | ' ' | 电商订单号 |
| 8 | freturnamount | 退货金额 | numeric | 23 | 10 | √ | 0.0000000000 | 退货金额 |
| 9 | fcancelstatus | 取消状态 | varchar | 10 |  | √ | ' ' | 取消状态,枚举: 0 :不可取消 1 :可取消 |
| 10 | fporderid | 电商父订单号 | varchar | 50 |  | √ | ' ' | 电商父订单号 |
| 11 | fpickwaretype | 取件方式 | varchar | 10 |  | √ | ' ' | 取件方式,枚举: 4 :上门取件 7 :客户送货 40 :客户发货 1 :客户自发 61 :晨光上门取件 62 :晨光第三方物流 10 :上门取货 20 :客户邮寄 |
| 12 | fafsservicestep | 服务单环节 | varchar | 255 |  | √ | ' ' | 服务单环节 |
| 13 | fafsservicestepdate | 服务单环节处理时间 | timestamp | 0 |  |  | null | 服务单环节处理时间 |
| 14 | fsource | 来源商城 | bpchar | 1 |  | √ | ' ' | 来源商城,枚举: 2 :京东商城 3 :苏宁商城 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛 |
| 15 | freturnaddress | 退换邮寄地址 | varchar | 255 |  | √ | ' ' | 退换邮寄地址 |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | freturntype | 售后类型 | varchar | 10 |  | √ | ' ' | 售后类型,枚举: 10 :退货 20 :换货 30 :维修 1 :退货 2 :换货 3 :维修 4 :退货 5 :换货 |
| 19 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 20 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fafsservicestepnum | 服务单环节编码 | varchar | 10 |  | √ | ' ' | 服务单环节编码 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 服务单号 | varchar | 50 |  | √ | ' ' | 服务单号 |
| 24 | freturncontact | 退换联系人 | varchar | 50 |  | √ | ' ' | 退换联系人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_eafservice |  | fnumber |
| 2 | t_mal_eafservice_pkey |  | fid |

---

## 电商售后服务单-多语言表 t_mal_eafservice_l

- **表名称：** 电商售后服务单-多语言表
- **表名：** t_mal_eafservice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_eafservice_l_pkey |  | fpkid |
| 2 | inx_mal_eafservice_l |  | fid |

---

## 单据体-子表 t_mal_eafserventry

- **表名称：** 单据体-子表
- **表名：** t_mal_eafserventry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgoodsid | 商品 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 3 | fsku | 商品编码 | varchar | 50 |  | √ | ' ' | 商品编码 |
| 4 | freturnqty | 退货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 退货数量 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_eafserventry_pkey |  | fentryid |
| 2 | inx_mal_eafserveny |  | fid |
