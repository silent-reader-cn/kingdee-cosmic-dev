# 销户申请-am_acctclosebill

## 销户申请-主表 t_am_acctclosebill

- **表名称：** 销户申请-主表
- **表名：** t_am_acctclosebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 3 | fclosedate | 销户日期 | timestamp | 0 |  |  | null | 销户日期 |
| 4 | fauthorizeinfo | fauthorizeinfo | varchar | 255 |  | √ | ' ' |  |
| 5 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 6 | fapplytime | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | ffinancialchapter | 财务专用章名称 | varchar | 80 |  | √ | ' ' | 财务专用章名称 |
| 11 | fclosedatef | 预计销户日期 | timestamp | 0 |  |  | null | 预计销户日期 |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :销户审批中 C :完成 H :销户处理中 R :销户复核中 I :审核中 E :退单 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fbacktime | fbacktime | timestamp | 0 |  |  | null |  |
| 17 | ffcommonseal | 公章名称 | varchar | 80 |  | √ | ' ' | 公章名称 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 20 | fbackreason | 退单意见 | varchar | 500 |  | √ | ' ' | 退单意见 |
| 21 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fbasecurrencyid | fbasecurrencyid | int8 | 64 |  | √ | 0 |  |
| 23 | fclosereason | fclosereason | varchar | 255 |  | √ | ' ' |  |
| 24 | flegalperson | 账户法定代表人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 26 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 27 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | faccountbankid | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 30 | flocamt | 金额折本位币 | numeric | 19 | 6 | √ | 0.000000 | 金额折本位币 |
| 31 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_am_closebill_num |  | fbillno |
| 2 | t_am_acctclosebill_pkey |  | fid |

---

## 销户申请-多语言表 t_am_acctclosebill_l

- **表名称：** 销户申请-多语言表
- **表名：** t_am_acctclosebill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclosereason | 销户原因及其它销户要求 | varchar | 255 |  | √ | ' ' | 销户原因及其它销户要求 |
| 3 | fauthorizeinfo | 印鉴授权信息 | varchar | 255 |  | √ | ' ' | 印鉴授权信息 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_am_acctclosebill_l_pkey |  | fpkid |
| 2 | t_am_acctclosebill_l_fid |  | fid,flocaleid |
