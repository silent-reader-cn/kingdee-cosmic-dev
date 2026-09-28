# 资产调出单-fa_dispatch

## 调出资产详情-子表 t_fa_disptbillentry

- **表名称：** 调出资产详情-子表
- **表名：** t_fa_disptbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foriginmethodid | 来源方式 | int8 | 64 |  | √ | 0 | [增减方式 fa_changemode](../fa_files/fa_changemode.md) |
| 3 | foutoriginalval | 调出资产原值 | numeric | 19 | 6 | √ | 0 | 调出资产原值 |
| 4 | fdispatchqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 5 | fdetailcurrencyld | fdetailcurrencyld | int8 | 64 |  | √ | 0 |  |
| 6 | finusestatusid | 使用状态 | int8 | 64 |  | √ | 0 | [使用状态 fa_usestatus](../fa_files/fa_usestatus.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | foutcurrency | 调出本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | foutdecval | 调出减值准备 | numeric | 19 | 6 | √ | 0 | 调出减值准备 |
| 10 | ffincard | 财务卡片 | int8 | 64 |  | √ | 0 | [财务卡片基础资料 fa_card_fin_base](../fa_files/fa_card_fin_base.md) |
| 11 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 12 | fpolicy | 调出组织会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 13 | fpreresidualval | 调出预计净残值 | numeric | 19 | 6 | √ | 0 | 调出预计净残值 |
| 14 | finusedeptid | 调入使用部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fevaluate | 评估价值 | numeric | 19 | 6 | √ | 0.000000 | 评估价值 |
| 16 | foutnetworth | 调出净值 | numeric | 19 | 6 | √ | 0 | 调出净值 |
| 17 | foutaccumdepre | 调出累计折旧 | numeric | 19 | 6 | √ | 0 | 调出累计折旧 |
| 18 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fdispatchfare | 调拨费用 | numeric | 19 | 6 | √ | 0.000000 | 调拨费用 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | finstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 22 | foutnetamount | 调出净额 | numeric | 19 | 6 | √ | 0 | 调出净额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_disptbillentry_pkey |  | fentryid |
| 2 | idx_fa_disbilent_fseq |  | fseq |

---

## 资产调出单-主表 t_fa_disptbill

- **表名称：** 资产调出单-主表
- **表名：** t_fa_disptbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finassetunitid | 调入资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdispatchtype | 调拨类型 | varchar | 50 |  | √ | 'A' | 调拨类型,枚举: A :平价调拨 B :非平价调拨 |
| 4 | forgid | 调出货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fhasvoucher | 凭证 | bpchar | 1 |  | √ | '0' | 凭证 |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | finuserid | 调入负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fchangemodeid | 减少方式 | int8 | 64 |  | √ | 0 | [增减方式 fa_changemode](../fa_files/fa_changemode.md) |
| 10 | fassetunitid | 调出资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | foutuserid | 调出申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fdispatchdate | 调拨日期 | timestamp | 0 |  |  | null | 调拨日期 |
| 15 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbillstatus | 调拨单状态 | varchar | 50 |  | √ | 'TEMPSTORE' | 调拨单状态,枚举: A :暂存 B :已提交 C :已审核 D :已确认 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | freason | 调拨原因 | varchar | 255 |  |  | ' ' | 调拨原因 |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fmigsrc | 是否迁移 | int4 | 32 |  | √ | 0 | 是否迁移 |
| 22 | fappliantid | 调拨申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | finorgid | 调入货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fcurrencyrate | 结算汇率 | numeric | 19 | 6 | √ | 0.000000 | 结算汇率 |
| 25 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_disbil_fseq |  | fseq |
| 2 | t_fa_disptbill_pkey |  | fid |

---

## 调入资产详情-子表 t_fa_dispatchbillentry_in

- **表名称：** 调入资产详情-子表
- **表名：** t_fa_dispatchbillentry_in

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutpolicy | 调出组织会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 3 | fistaxincluded | 含税 | bpchar | 1 |  | √ | '0' | 含税 |
| 4 | findecval | 调入减值准备 | numeric | 19 | 6 | √ | 0 | 调入减值准备 |
| 5 | fdispatchqty | 数量 | numeric | 19 | 6 | √ | 0 | 数量 |
| 6 | finpolicy | 调入组织会计政策 | int8 | 64 |  | √ | 0 | [会计政策 xkbd_policy](../fibd_files/xkbd_policy.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | foutdecval | 调出减值准备 | numeric | 19 | 6 | √ | 0 | 调出减值准备 |
| 9 | finaccumdepre | 调入累计折旧 | numeric | 19 | 6 | √ | 0 | 调入累计折旧 |
| 10 | fismainpolicy | 主会计政策 | bpchar | 1 |  | √ | '0' | 主会计政策 |
| 11 | finpreresidualval | 调入预计净残值 | numeric | 19 | 6 | √ | 0 | 调入预计净残值 |
| 12 | fiscrosslegal | 是否跨法人 | bpchar | 1 |  | √ | '0' | 是否跨法人,枚举: 1 :是 0 :否 |
| 13 | ffincardid | 财务卡片 | int8 | 64 |  | √ | 0 | [财务卡片基础资料 fa_card_fin_base](../fa_files/fa_card_fin_base.md) |
| 14 | foutnetamount | 调出净额 | numeric | 19 | 6 | √ | 0 | 调出净额 |
| 15 | finoriginalval | 调入资产原值 | numeric | 19 | 6 | √ | 0 | 调入资产原值 |
| 16 | foriginmethodid | 增减方式 | int8 | 64 |  | √ | 0 | [增减方式 fa_changemode](../fa_files/fa_changemode.md) |
| 17 | foutoriginalval | 调出资产原值 | numeric | 19 | 6 | √ | 0 | 调出资产原值 |
| 18 | finnetamount | 调入净额 | numeric | 19 | 6 | √ | 0 | 调入净额 |
| 19 | finusestatusid | 使用状态 | int8 | 64 |  | √ | 0 | [使用状态 fa_usestatus](../fa_files/fa_usestatus.md) |
| 20 | foutcurrency | 调出组织本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | finnetworth | 调入净值 | numeric | 19 | 6 | √ | 0 | 调入净值 |
| 22 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 23 | fdispatchamount | 调拨结算金额 | numeric | 19 | 6 | √ | 0 | 调拨结算金额 |
| 24 | fdepredperiodnum | 调出已折旧期间数 | int4 | 32 |  | √ | 0 | 调出已折旧期间数 |
| 25 | fincurrency | 调入本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | finusedeptid | 调入使用部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | foutnetworth | 调出净值 | numeric | 19 | 6 | √ | 0 | 调出净值 |
| 28 | fmeasurementid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | foutaccumdepre | 调出累计折旧 | numeric | 19 | 6 | √ | 0 | 调出累计折旧 |
| 30 | fiscross | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | finstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 33 | foutpreresidualval | 调出预计净残值 | numeric | 19 | 6 | √ | 0 | 调出预计净残值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_dispatch_fincard |  | ffincardid |
| 2 | idx_fa_dispatch_realcard |  | frealcardid |
| 3 | pk_fa_dispatchbillentry_in |  | fentryid |
