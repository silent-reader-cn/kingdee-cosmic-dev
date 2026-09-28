# 保证金存入处理F7-fbd_suretybill_f7

## 保证金存入处理F7-主表 t_fbd_suretybill

- **表名称：** 保证金存入处理F7-主表
- **表名：** t_fbd_suretybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fterm | 期限（ymd） | varchar | 50 |  | √ | ' ' | 期限（ymd） |
| 3 | forgid | 存款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftotalamount | ftotalamount | numeric | 23 | 10 | √ | 0 |  |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | finvestvarietiesid | 保证金品种 | int8 | 64 |  | √ | 0 | [保证金品种 fbd_investvariety_surety](../fbd_files/fbd_investvariety_surety.md) |
| 7 | fprefutureamt | fprefutureamt | numeric | 23 | 10 | √ | 0 |  |
| 8 | fapplyid | fapplyid | int8 | 64 |  | √ | 0 |  |
| 9 | fratefloatpoint | 利率浮动基点 | numeric | 19 | 6 | √ | 0 | 利率浮动基点 |
| 10 | fintdate | 起息日 | timestamp | 0 |  |  | null | 起息日 |
| 11 | fbillno | 单据编码 | varchar | 30 |  | √ | ' ' | 单据编码 |
| 12 | freleaseamount | 已存出金额 | numeric | 23 | 10 | √ | 0 | 已存出金额 |
| 13 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 14 | fsourcebilltype | fsourcebilltype | varchar | 50 |  | √ | ' ' |  |
| 15 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fproductfactoryid | 保证金模型 | int8 | 64 |  | √ | 0 | [保证金模型 fbd_investmodel_surety](../fbd_files/fbd_investmodel_surety.md) |
| 17 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 18 | frateadjuststyle | 利率重置方式 | varchar | 50 |  | √ | ' ' | 利率重置方式,枚举: deadline :即期调整 |
| 19 | ffinaccountid | 活期账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 20 | freferencerateid | 参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 21 | fbasis | 计息基准 | varchar | 50 |  | √ | ' ' | 计息基准,枚举: Actual/actual :Actual/actual SIA_30_360 :30/360(SIA) Actual_360 :Actual/360 Actual_365 :Actual/365 BMA_30_360 :30/360(BMA) ISDA_30_360 :30/360(ISDA) European_30_360 :30/360(European) Japanese_Actual_365 :Actual/365(Japanese) ICMA_Actual_actual :Actual/actual(ICMA) ICMA_Actual_360 :Actual/360(ICMA) ICMA_Actual_365 :Actual/365(ICMA) ICMA_30_360 :30/360E(ICMA) |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fendpreinstdate | fendpreinstdate | timestamp | 0 |  |  | null |  |
| 24 | fisvoucher | fisvoucher | bpchar | 1 |  | √ | '0' |  |
| 25 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 26 | ffinorginfoid | 存款机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 27 | finteresttype | 利率类型 | varchar | 50 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 |
| 28 | fdemandrate | 活期利率（%） | numeric | 23 | 10 | √ | 0 | 活期利率（%） |
| 29 | fbizstatus | 保证金业务状态 | varchar | 50 |  | √ | ' ' | 保证金业务状态,枚举: surety_ing :存入中 surety_done :已存入 surety_part :已部分存出 surety_end :已存出 |
| 30 | famount | 保证金金额 | numeric | 23 | 10 | √ | 0 | 保证金金额 |
| 31 | fendinstdate | 上次结息日 | timestamp | 0 |  |  | null | 上次结息日 |
| 32 | fsurplusamount | 剩余金额 | numeric | 23 | 10 | √ | 0 | 剩余金额 |
| 33 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 34 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 36 | fexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 37 | fsettledate | fsettledate | timestamp | 0 |  |  | null |  |
| 38 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 39 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fappendedamt | fappendedamt | numeric | 23 | 10 | √ | 0 |  |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | fpaybillid | fpaybillid | int8 | 64 |  | √ | 0 |  |
| 43 | fsettleaccountid | 保证金账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 44 | flastreleasedate | 上次存出日期 | timestamp | 0 |  |  | null | 上次存出日期 |
| 45 | frevenueplanid | frevenueplanid | int8 | 64 |  | √ | 0 |  |
| 46 | fsuretyrate | 保证金比例（%） | numeric | 23 | 10 | √ | 0 | 保证金比例（%） |
| 47 | frevenueway | 收益方式 | varchar | 50 |  | √ | ' ' | 收益方式,枚举: stage :固定频率收益 norevenue :无收益 |
| 48 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 49 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 50 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 51 | finterestrate | 定期利率（%） | numeric | 23 | 10 | √ | 0 | 定期利率（%） |
| 52 | fratesign | 利率浮动基点（BP） | varchar | 50 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fbd_suretybill_bn |  | fbillno |
| 2 | pk_fbd_suretybill |  | fid |

---

## 保证金存入处理F7-多语言表 t_fbd_suretybill_l

- **表名称：** 保证金存入处理F7-多语言表
- **表名：** t_fbd_suretybill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fbd_suretybill_l |  | fpkid |
| 2 | idx_fbd_suretybill_l_0 |  | fid,flocaleid |

---

## 保证金存入处理F7-分表 t_fbd_suretybill_f

- **表名称：** 保证金存入处理F7-分表
- **表名：** t_fbd_suretybill_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpayeeacctno | 收款账号 | varchar | 100 |  | √ | ' ' | 收款账号 |
| 3 | feassrcid | feassrcid | varchar | 50 |  | √ | ' ' |  |
| 4 | finitamount | finitamount | numeric | 23 | 10 | √ | 0 |  |
| 5 | fisfinaccountfrozen | 活期账户冻结 | bpchar | 1 |  | √ | '0' | 活期账户冻结 |
| 6 | flockpayamt | flockpayamt | numeric | 23 | 10 | √ | 0 |  |
| 7 | fpayeebankname | 收款银行 | varchar | 100 |  | √ | ' ' | 收款银行 |
| 8 | finvestorgtype | 存款机构类型 | varchar | 50 |  | √ | ' ' | 存款机构类型,枚举: bd_finorginfo :金融机构 bd_customer :客户 bd_supplier :供应商 fbd_other :其他 |
| 9 | ffinorgother | 存款机构 | varchar | 255 |  | √ | ' ' | 存款机构 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fbd_suretybill_f |  | fid |
| 2 | idx_suretybill_f_feassrcid |  | feassrcid |
| 3 | idx_suretybill_f_fdepositorgid |  | fpayeeacctno |
