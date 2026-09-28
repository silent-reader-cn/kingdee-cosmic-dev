# 电商流水入账调度任务执行记录-cas_ecommertaskrecord

## 单据体-子表 t_cas_ecommerentry

- **表名称：** 单据体-子表
- **表名：** t_cas_ecommerentry

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
| 1 | pk_t_cas_ecommerentry |  | fentryid |
| 2 | idx_cas_ecommerentry |  | ftargetbillno |

---

## 电商流水入账调度任务执行记录-主表 t_cas_ecommertaskrecord

- **表名称：** 电商流水入账调度任务执行记录-主表
- **表名：** t_cas_ecommertaskrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frecentday | 匹配最近X天流水 | int8 | 64 |  | √ | 0 | 匹配最近X天流水 |
| 3 | fpayerbasetype | 付款单位类型 | varchar | 64 |  | √ | ' ' | 付款单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 cas_othercontactunit :其他往来单位 bos_user :人员 other :其他 |
| 4 | fdatafilterdesc | 适用条件 | varchar | 1024 |  | √ | ' ' | 适用条件 |
| 5 | fschemaid | 方案id | int8 | 64 |  | √ | 0 | 方案id |
| 6 | fbillstate | 下游单据状态 | varchar | 8 |  | √ | ' ' | 下游单据状态,枚举: 1 :暂存 2 :已提交 3 :已审核 4 :已收款/已付款 |
| 7 | forg | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftouchtype | 触发方式 | varchar | 8 |  | √ | ' ' | 触发方式,枚举: 1 :自动执行 2 :手工触发 |
| 10 | foperatecount | 操作单据数量 | int8 | 64 |  | √ | 0 | 操作单据数量 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fschemabillno | 方案编号 | varchar | 128 |  | √ | ' ' | 方案编号 |
| 13 | ftargetbill | 目标单据 | varchar | 64 |  | √ | ' ' | 目标单据,枚举: cas_recbill :收款单 cas_paybill :付款单 |
| 14 | fruleid | 规则项Id | int8 | 64 |  | √ | 0 | 规则项Id |
| 15 | fschema | 方案名称 | varchar | 256 |  | √ | ' ' | 方案名称 |
| 16 | fruntime | 执行时间（秒） | int8 | 64 |  | √ | 0 | 执行时间（秒） |
| 17 | fpayeebase | 收款单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fremark | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fsettletype | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 22 | frunresult | 执行结果 | varchar | 64 |  | √ | ' ' | 执行结果,枚举: 1 :成功 2 :失败 3 :部分成功 |
| 23 | fbillstatus | 单据状态 | varchar | 8 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcontactunittype | 往来单位类型 | varchar | 64 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :人员 cas_othercontactunit :其他往来单位 other :其他 |
| 25 | ferrormsg | 异常信息 | varchar | 2000 |  | √ | ' ' | 异常信息 |
| 26 | frectype | 收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 27 | fpayerbase | 付款单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fpayeebasetype | 收款单位类型 | varchar | 64 |  | √ | ' ' | 收款单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 bos_org :公司 other :其他 |
| 30 | fpaytype | 付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | frecpayorg | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | faccountbank | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 34 | fsettleorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 36 | fgroupfield | 分组字段 | varchar | 256 |  | √ | ' ' | 分组字段,枚举: |
| 37 | fpayertext | 付款单位 | varchar | 256 |  | √ | ' ' | 付款单位 |
| 38 | fcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 39 | fpayeetext | 收款单位 | varchar | 256 |  | √ | ' ' | 收款单位 |
| 40 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 41 | frulename | 规则项名称 | varchar | 256 |  | √ | ' ' | 规则项名称 |
| 42 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_ecommertaskrecord |  | fschemaid |
| 2 | pk_t_cas_ecommertaskrecord |  | fid |
