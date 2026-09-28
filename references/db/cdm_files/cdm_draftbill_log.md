# 票据日志-cdm_draftbill_log

## 票据日志-主表 t_cdm_draftbill_log

- **表名称：** 票据日志-主表
- **表名：** t_cdm_draftbill_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdraftbillno | 票据号码 | varchar | 255 |  | √ | ' ' | 票据号码 |
| 3 | fsplitedsubbillid | 拆分后的子票id | int8 | 64 |  | √ | 0 | 拆分后的子票id |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdraftbillnumber | 票据单据编号 | varchar | 50 |  | √ | ' ' | 票据单据编号 |
| 6 | fbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: process :处理中 fail :交易失败 success :交易成功 |
| 7 | fbizbillno | 业务单据编号 | varchar | 50 |  | √ | ' ' | 业务单据编号 |
| 8 | famount | 当前子票包金额 | numeric | 23 | 10 | √ | 0 | 当前子票包金额 |
| 9 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 10 | fbiztype | 业务处理 | varchar | 50 |  | √ | ' ' | 业务处理,枚举: endorse :票据背书 pledge :票据质押 discount :票据贴现 payinterest :买方付息 refund :票据退票 rlspledge :质押解除 trusteeship :票据托管 retrieve :托管取回 collect :票据托收 billsplit :票据拆分 receivebill :票据收款 intopool :票据入池 outpool :票据出池 draftallocation :票据调度（归集/下拨/调拨） payoff :票据解付 relatedpay :关联付款 allocate :票据调拨 allocateup :票据归集 allocatedown :票据下拨 redeem :票据兑付 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fdealamount | 业务发生金额 | numeric | 23 | 10 | √ | 0 | 业务发生金额 |
| 13 | fusedamount | 已用金额 | numeric | 23 | 10 | √ | 0 | 已用金额 |
| 14 | flockedamount | 已锁定金额 | numeric | 23 | 10 | √ | 0 | 已锁定金额 |
| 15 | fdraftid | 票据id | int8 | 64 |  | √ | 0 | 票据id |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fsourcebilltype | 业务单据类型 | varchar | 50 |  | √ | ' ' | 业务单据类型 |
| 18 | fupdatebizbillid | 更新时操作的业务id | int8 | 64 |  | √ | 0 | 更新时操作的业务id |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fissplit | 业务拆分 | bpchar | 1 |  | √ | '0' | 业务拆分 |
| 21 | fbillidentitycode | 票据识别码 | varchar | 255 |  | √ | ' ' | 票据识别码 |
| 22 | fdeleteflag | 业务删除 | bpchar | 1 |  | √ | '0' | 业务删除 |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | foldlogid | 旧日志id | int8 | 64 |  | √ | 0 | 旧日志id |
| 25 | fsubbillrange | 当前子票包区间 | varchar | 50 |  | √ | ' ' | 当前子票包区间 |
| 26 | fspecialflag | 日志特殊标识 | varchar | 255 |  | √ | ' ' | 日志特殊标识,枚举: A :出纳调度预锁生成 B :确认失败 |
| 27 | favailableamount | 可用金额 | numeric | 23 | 10 | √ | 0 | 可用金额 |
| 28 | fnewchildlogid | 对应的预占子日志id | int8 | 64 |  | √ | 0 | 对应的预占子日志id |
| 29 | fsourcebillid | 业务单据id | int8 | 64 |  | √ | 0 | 业务单据id |
| 30 | foriginalsubbillamount | 原始子票包金额 | numeric | 23 | 10 | √ | 0 | 原始子票包金额 |
| 31 | frptype | 收付类型 | varchar | 50 |  | √ | ' ' | 收付类型,枚举: paybill :开票 receivebill :收票 |
| 32 | foriginalsubbillrang | 原始子票包区间 | varchar | 255 |  | √ | ' ' | 原始子票包区间 |
| 33 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_draftbill_log |  | fid |
| 2 | idx_cdm_draftbill_log |  | fdeleteflag,fsourcebillid,fdraftid |
