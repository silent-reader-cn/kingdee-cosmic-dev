# 保证金存入处理F7-fbd_suretybill_f7

## 保证金存入处理F7-主表 t_fbd_suretybill

- **表名称：** 保证金存入处理F7-主表
- **表名：** t_fbd_suretybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fterm | 期限（ymd） | varchar | 50 |  | √ | ' ' | 期限（ymd） |
| 3 | finteresttype | 利率类型 | varchar | 50 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 |
| 4 | forgid | 存款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ftotalamount | ftotalamount | numeric | 23 | 10 | √ | 0 |  |
| 6 | fdemandrate | 活期利率（%） | numeric | 23 | 10 | √ | 0 | 活期利率（%） |
| 7 | fbizstatus | 保证金业务状态 | varchar | 50 |  | √ | ' ' | 保证金业务状态,枚举: surety_ing :存入中 surety_done :已存入 surety_part :已部分存出 surety_end :已存出 |
| 8 | famount | 保证金金额 | numeric | 23 | 10 | √ | 0 | 保证金金额 |
| 9 | fendinstdate | 上次结息日 | timestamp | 0 |  |  | null | 上次结息日 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsurplusamount | fsurplusamount | numeric | 23 | 10 | √ | 0 |  |
| 12 | finvestvarietiesid | 保证金品种 | int8 | 64 |  | √ | 0 | 保证金品种 fbd_investvariety_surety |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fprefutureamt | fprefutureamt | numeric | 23 | 10 | √ | 0 |  |
| 16 | fapplyid | fapplyid | int8 | 64 |  | √ | 0 |  |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 19 | fratefloatpoint | 利率浮动基点 | numeric | 19 | 6 | √ | 0 | 利率浮动基点 |
| 20 | fintdate | 起息日 | timestamp | 0 |  |  | null | 起息日 |
| 21 | fbillno | 单据编码 | varchar | 30 |  | √ | ' ' | 单据编码 |
| 22 | freleaseamount | 已存出金额 | numeric | 23 | 10 | √ | 0 | 已存出金额 |
| 23 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 26 | fsourcebilltype | fsourcebilltype | varchar | 50 |  | √ | ' ' |  |
| 27 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fproductfactoryid | 保证金模型 | int8 | 64 |  | √ | 0 | 保证金模型 fbd_investmodel_surety |
| 30 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 31 | fsettleaccountid | 保证金账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 32 | flastreleasedate | 上次存出日期 | timestamp | 0 |  |  | null | 上次存出日期 |
| 33 | frevenueplanid | frevenueplanid | int8 | 64 |  | √ | 0 |  |
| 34 | frateadjuststyle | 利率重置方式 | varchar | 50 |  | √ | ' ' | 利率重置方式,枚举: deadline :即期调整 |
| 35 | frevenueway | 收益方式 | varchar | 50 |  | √ | ' ' | 收益方式,枚举: stage :固定频率收益 norevenue :无收益 |
| 36 | ffinaccountid | ffinaccountid | int8 | 64 |  | √ | 0 |  |
| 37 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 38 | freferencerateid | 参考利率 | int8 | 64 |  | √ | 0 | 参考利率 tbd_referrate |
| 39 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 40 | fbasis | 计息基准 | varchar | 50 |  | √ | ' ' | 计息基准,枚举: Actual/actual :Actual/actual SIA_30_360 :30/360(SIA) Actual_360 :Actual/360 Actual_365 :Acutal/365 BMA_30_360 :30/360(BMA) ISDA_30_360 :30/360(ISDA) European_30_360 :30/360(European) Japanese_Actual_365 :Acutal/365(Japanese) ICMA_Actual_actual :Actual/actual(ICMA) ICMA_Actual_360 :Actual/360(ICMA) ICMA_Actual_365 :Acutal/365(ICMA) ICMA_30_360 :30/360E(ICMA) |
| 41 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 42 | fendpreinstdate | fendpreinstdate | timestamp | 0 |  |  | null |  |
| 43 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 44 | finterestrate | 定期利率（%） | numeric | 23 | 10 | √ | 0 | 定期利率（%） |
| 45 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 46 | fratesign | 利率浮动基点（BP） | varchar | 50 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |
| 47 | ffinorginfoid | 存款机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |

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
