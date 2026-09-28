# 资产调出单-fa_dispatch

## 分录-子表 t_fa_disptbillentry

- **表名称：** 分录-子表
- **表名：** t_fa_disptbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foriginmethodid | 来源方式 | int8 | 64 |  | √ | 0 | 增减方式 fa_changemode |
| 3 | fdispatchqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 4 | fdetailcurrencyld | fdetailcurrencyld | int8 | 64 |  | √ | 0 |  |
| 5 | finusestatusid | 使用状态 | int8 | 64 |  | √ | 0 | 使用状态 fa_usestatus |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 8 | finusedeptid | 调入使用部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fevaluate | 评估价值 | numeric | 19 | 6 | √ | 0.000000 | 评估价值 |
| 10 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fdispatchfare | 调拨费用 | numeric | 19 | 6 | √ | 0.000000 | 调拨费用 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | finstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | 存放地点 fa_storeplace |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_disbilent_fseq |  | fseq |
| 2 | t_fa_disptbillentry_pkey |  | fentryid |

---

## 资产调出单-主表 t_fa_disptbill

- **表名称：** 资产调出单-主表
- **表名：** t_fa_disptbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finassetunitid | 调入资产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fdispatchtype | 调拨类型 | varchar | 50 |  | √ | 'A' | 调拨类型,枚举: A :平价调拨 B :非平价调拨 |
| 4 | forgid | 调出货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fhasvoucher | 凭证 | bpchar | 1 |  | √ | '0' | 凭证 |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | finuserid | 调入负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fchangemodeid | 减少方式 | int8 | 64 |  | √ | 0 | 增减方式 fa_changemode |
| 10 | fassetunitid | 调出资产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | foutuserid | 调出申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fdispatchdate | 调拨日期 | timestamp | 0 |  |  | null | 调拨日期 |
| 15 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbillstatus | 调拨单状态 | varchar | 50 |  | √ | 'TEMPSTORE' | 调拨单状态,枚举: A :暂存 B :已提交 C :已审核 D :已确认 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | freason | 调拨原因 | varchar | 255 |  |  | ' ' | 调拨原因 |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fappliantid | 调拨申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | finorgid | 调入货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fcurrencyrate | 结算汇率 | numeric | 19 | 6 | √ | 0.000000 | 结算汇率 |
| 24 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_disbil_fseq |  | fseq |
| 2 | t_fa_disptbill_pkey |  | fid |
