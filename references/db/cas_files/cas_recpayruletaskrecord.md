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
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
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
| 2 | frecpayerrorsize | 确认收付款失败数量 | int8 | 64 |  | √ | 0 | 确认收付款失败数量 |
| 3 | fsubmiterror | 提交异常信息 | varchar | 2000 |  | √ | ' ' | 提交异常信息 |
| 4 | fhandlebill | 入账单据 | varchar | 64 |  | √ | ' ' | 入账单据,枚举: recvbill :收款单 paybill :付款单 |
| 5 | frecbilltype | 收款单单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | foperatecount | 当前规则匹配成功的单据数量 | int8 | 64 |  | √ | 0 | 当前规则匹配成功的单据数量 |
| 8 | fsaveerror | 下推保存异常信息 | varchar | 2000 |  | √ | ' ' | 下推保存异常信息 |
| 9 | fruleid | 规则项Id | int8 | 64 |  | √ | 0 | 规则项Id |
| 10 | fschema | 方案名称 | varchar | 256 |  | √ | ' ' | 方案名称 |
| 11 | fruntime | 执行时间（秒） | int8 | 64 |  | √ | 0 | 执行时间（秒） |
| 12 | fpayeebase | 收款单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fmatchallcount | 当前规则操作成功总数量 | int8 | 64 |  | √ | 0 | 当前规则操作成功总数量 |
| 15 | ffundflowitem | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 16 | frunresult | 执行结果 | varchar | 64 |  | √ | ' ' | 执行结果,枚举: 1 :成功 2 :失败 3 :部分成功 |
| 17 | fbillstatus | 单据状态 | varchar | 8 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcontactunittype | 往来单位类型 | varchar | 64 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 other :其他 |
| 19 | fpayerbase | 付款单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 20 | fbizbillstatu | 下游单据状态 | bpchar | 1 |  | √ | '0' | 下游单据状态,枚举: 0 :暂存 1 :提交 2 :审核 3 :已收款/已付款 |
| 21 | fbillcount | 查询单据数量 | int8 | 64 |  | √ | 0 | 查询单据数量 |
| 22 | fsaveerrorsize | 下推保存失败数量 | int8 | 64 |  | √ | 0 | 下推保存失败数量 |
| 23 | fauditerror | 审核异常信息 | varchar | 2000 |  | √ | ' ' | 审核异常信息 |
| 24 | fpayeebasetype | 收款单位类型 | varchar | 64 |  | √ | ' ' | 收款单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 bos_org :公司 other :其他 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fsettleorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fhandlescheme | 处理方案 | varchar | 64 |  | √ | ' ' | 处理方案,枚举: rule :按规则生成 recv :收款认领 ticket :票据认领 |
| 28 | fcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 29 | fpayeetext | 收款单位 | varchar | 256 |  | √ | ' ' | 收款单位 |
| 30 | frulename | 规则项名称 | varchar | 256 |  | √ | ' ' | 规则项名称 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fpayerbasetype | 付款单位类型 | varchar | 64 |  | √ | ' ' | 付款单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 cas_othercontactunit :其他往来单位 bos_user :人员 other :其他 |
| 33 | frecpayerror | 确认收付款异常信息 | varchar | 2000 |  | √ | ' ' | 确认收付款异常信息 |
| 34 | fdatafilterdesc | 适用条件 | varchar | 1024 |  | √ | ' ' | 适用条件 |
| 35 | fschemaid | 方案id | int8 | 64 |  | √ | 0 | 方案id |
| 36 | fbiztype | 业务类型 | varchar | 64 |  | √ | ' ' | 业务类型,枚举: rec :收款 pay :付款 recticket :票据 |
| 37 | ftouchtype | 触发方式 | varchar | 64 |  | √ | ' ' | 触发方式,枚举: 1 :自动执行 2 :手工触发 |
| 38 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fpaybilltype | 付款单单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 40 | fsubmiterrorsize | 提交失败数量 | int8 | 64 |  | √ | 0 | 提交失败数量 |
| 41 | fschemabillno | 规则编码 | varchar | 128 |  | √ | ' ' | 规则编码 |
| 42 | fremark | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fsettletype | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 45 | frectype | 收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 46 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 47 | fpaytype | 付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 48 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 49 | fpayertext | 付款单位 | varchar | 256 |  | √ | ' ' | 付款单位 |
| 50 | fauditerrorsize | 审核失败数量 | int8 | 64 |  | √ | 0 | 审核失败数量 |
| 51 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_ruletaskrecord |  | fschemaid |
| 2 | pk_t_cas_ruletaskrecord |  | fid |
