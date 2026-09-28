# 自动生成调度任务执行记录-cas_recpayruletaskrecord

## 单据体-子表 t_cas_ruleentryrecord

- **表名称：** 单据体-子表
- **表名：** t_cas_ruleentryrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperatebillno | 操作单据编号 | varchar | 2000 |  | √ | ' ' | 操作单据编号 |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | ftargetbillno | 下游单据编号 | varchar | 128 |  | √ | ' ' | 下游单据编号 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_ruleentryrecord |  | ftargetbillno |
| 2 | pk_t_cas_ruleentryrecord |  | fentryid |

---

## 适用组织-多选基础资料表 t_cas_ruletask_useorg

- **表名称：** 适用组织-多选基础资料表
- **表名：** t_cas_ruletask_useorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cas_ruletask_useorg |  | fpkid |
| 2 | idx_cas_ruletask_useorg |  | fid |

---

## 自动生成调度任务执行记录-主表 t_cas_ruletaskrecord

- **表名称：** 自动生成调度任务执行记录-主表
- **表名：** t_cas_ruletaskrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpayerbasetype | 付款单位类型 | varchar | 64 |  | √ | ' ' | 付款单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 cas_othercontactunit :其他往来单位 bos_user :人员 other :其他 |
| 3 | fdatafilterdesc | 适用条件 | varchar | 1024 |  | √ | ' ' | 适用条件 |
| 4 | fhandlebill | 入账单据 | varchar | 64 |  | √ | ' ' | 入账单据,枚举: recvbill :收款单 paybill :付款单 |
| 5 | fschemaid | 方案id | int8 | 64 |  | √ | 0 | 方案id |
| 6 | frecbilltype | 收款单单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fbiztype | 业务类型 | varchar | 64 |  | √ | ' ' | 业务类型,枚举: rec :收款 pay :付款 recticket :票据 |
| 9 | ftouchtype | 触发方式 | varchar | 64 |  | √ | ' ' | 触发方式,枚举: 1 :自动执行 2 :手工触发 |
| 10 | foperatecount | 当前规则匹配成功的单据数量 | int8 | 64 |  | √ | 0 | 当前规则匹配成功的单据数量 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fpaybilltype | 付款单单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 13 | fschemabillno | 规则编码 | varchar | 128 |  | √ | ' ' | 规则编码 |
| 14 | fruleid | 规则项Id | int8 | 64 |  | √ | 0 | 规则项Id |
| 15 | fschema | 方案名称 | varchar | 256 |  | √ | ' ' | 方案名称 |
| 16 | fruntime | 执行时间（秒） | int8 | 64 |  | √ | 0 | 执行时间（秒） |
| 17 | fpayeebase | 收款单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fmatchallcount | 当前方案匹配成功总数量 | int8 | 64 |  | √ | 0 | 当前方案匹配成功总数量 |
| 20 | fremark | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 21 | ffundflowitem | 资金用途 | int8 | 64 |  | √ | 0 | 资金用途 cas_fundflowitem |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fsettletype | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 24 | frunresult | 执行结果 | varchar | 64 |  | √ | ' ' | 执行结果,枚举: 1 :成功 2 :失败 3 :部分成功 |
| 25 | fbillstatus | 单据状态 | varchar | 8 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcontactunittype | 往来单位类型 | varchar | 64 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 other :其他 |
| 27 | frectype | 收款用途 | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 28 | fpayerbase | 付款单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fbillcount | 查询单据数量 | int8 | 64 |  | √ | 0 | 查询单据数量 |
| 31 | fpayeebasetype | 收款单位类型 | varchar | 64 |  | √ | ' ' | 收款单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 bos_org :公司 other :其他 |
| 32 | fpaytype | 付款用途 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 33 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 34 | fsettleorg | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 36 | fpayertext | 付款单位 | varchar | 256 |  | √ | ' ' | 付款单位 |
| 37 | fhandlescheme | 处理方案 | varchar | 64 |  | √ | ' ' | 处理方案,枚举: rule :按规则生成 recv :收款认领 ticket :票据认领 |
| 38 | fcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 39 | fpayeetext | 收款单位 | varchar | 256 |  | √ | ' ' | 收款单位 |
| 40 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 41 | frulename | 规则项名称 | varchar | 256 |  | √ | ' ' | 规则项名称 |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_ruletaskrecord |  | fschemaid |
| 2 | pk_t_cas_ruletaskrecord |  | fid |
