# 余额查询-bei_bankbalance

## 余额查询-多语言表 t_bei_bankbalance_l

- **表名称：** 余额查询-多语言表
- **表名：** t_bei_bankbalance_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | flocaleid | flocaleid | varchar | 100 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_bankbalance_l_pkey |  | fpkid |
| 2 | idx_bei_bankbalance_l |  | fid,flocaleid,fdescription |

---

## 余额查询-主表 t_bei_bankbalance

- **表名称：** 余额查询-主表
- **表名：** t_bei_bankbalance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flogo | 银行LOGO | varchar | 100 |  | √ | ' ' | 银行LOGO |
| 3 | fvalibalance | 可用余额 | numeric | 23 | 10 |  | null | 可用余额 |
| 4 | famount | 当前余额 | numeric | 23 | 10 |  | null | 当前余额 |
| 5 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fisupdate | 是否更新过 | bpchar | 1 |  | √ | '0' | 是否更新过 |
| 9 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 10 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 14 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 15 | fcreditamount | fcreditamount | numeric | 19 | 6 |  | null |  |
| 16 | fscorgid | fscorgid | int8 | 64 |  | √ | 0 |  |
| 17 | fdebitamount | fdebitamount | numeric | 19 | 6 |  | null |  |
| 18 | fbasecurrencyid | fbasecurrencyid | int8 | 64 |  | √ | 0 |  |
| 19 | fbizdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 20 | fupdatetime | fupdatetime | timestamp | 0 |  |  | null |  |
| 21 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 22 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: frombank :银企接口 import :模板引入 modify :系统修复 cbs :招行CBS |
| 23 | fbankid | 开户行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 24 | flstbalance | 昨日余额 | numeric | 23 | 10 |  | null | 昨日余额 |
| 25 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | faccountbankid | 账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 28 | fkeycol | fkeycol | varchar | 255 |  | √ | ' ' |  |
| 29 | flocamt | 金额折本位币 | numeric | 23 | 10 |  | null | 金额折本位币 |
| 30 | fcompanyid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_balance |  | faccountbankid,fcurrencyid,fbizdate |
| 2 | idx_balance_cacb |  | fcompanyid,faccountbankid,fcurrencyid,fbizdate |
| 3 | t_bei_bankbalance_pkey |  | fid |
