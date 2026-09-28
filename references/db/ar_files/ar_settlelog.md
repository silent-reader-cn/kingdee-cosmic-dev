# 应收核销日志-ar_settlelog

## 应收核销日志-主表 t_ar_settlelog

- **表名称：** 应收核销日志-主表
- **表名：** t_ar_settlelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsettletype | 核销方式 | varchar | 30 |  | √ | ' ' | 核销方式,枚举: auto :自动核销 manual :手工核销 match :方案匹配核销 |
| 4 | fschemeno | 方案编码 | varchar | 50 |  | √ | ' ' | 方案编码 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fschemepk | 方案pk | int8 | 64 |  | √ | 0 | 方案pk |
| 8 | fexecutestatus | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: 1 :执行成功 2 :执行中 3 :执行失败 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fbegintime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fschemename | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 13 | fcreatorid | 核销人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 15 | fisexception | 是否异常 | bpchar | 1 |  | √ | '0' | 是否异常 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_sl_begintime |  | fbegintime |
| 2 | t_ar_settlelog_pkey |  | fid |
| 3 | idx_ar_sl_schemepk |  | fschemepk |

---

## 分录-子表 t_ar_settlelogentry

- **表名称：** 分录-子表
- **表名：** t_ar_settlelogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsettlerelation | 核销关系 | varchar | 30 |  | √ | ' ' | 核销关系,枚举: appaysettle :应付付款核销 apself :应付红蓝对冲 payself :付款红蓝对冲 arapsettle :应收冲应付 arself :应收红蓝对冲 recself :收款红蓝对冲 recsettle :应收收款核销 recpaysettle :收款冲退款 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fasstentrycount | 辅方单据分录数量 | int8 | 64 |  | √ | 0 | 辅方单据分录数量 |
| 5 | fexceptioninfo | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 6 | fmainentrycount | 主方单据分录数量 | int8 | 64 |  | √ | 0 | 主方单据分录数量 |
| 7 | fasstcount | 辅方单据数量 | int8 | 64 |  | √ | 0 | 辅方单据数量 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fexceptioninfo_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |
| 10 | fsettlerecordcount | 生成核销记录数 | int8 | 64 |  | √ | 0 | 生成核销记录数 |
| 11 | fmaincount | 主方单据数量 | int8 | 64 |  | √ | 0 | 主方单据数量 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fisexception | 是否异常 | bpchar | 1 |  | √ | '0' | 是否异常 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_sle_fid |  | fid |
| 2 | t_ar_settlelogentry_pkey |  | fentryid |
