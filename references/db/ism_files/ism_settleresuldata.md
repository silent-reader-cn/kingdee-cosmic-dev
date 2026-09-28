# 结算生成日志-ism_settleresuldata

## 生成结果-子表 t_ism_settleresult_s

- **表名称：** 生成结果-子表
- **表名：** t_ism_settleresult_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsettleentitykey | 结算单据名称 | varchar | 50 |  | √ | ' ' | 业务对象 bos_objecttype |
| 3 | fsettlebillno | 结算单据编号 | varchar | 100 |  | √ | ' ' | 结算单据编号 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsettlebillid | 结算单据ID | int8 | 64 |  | √ | 0 | 结算单据ID |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ism_settleresult_s |  | fid |
| 2 | pk_ism_settleresult_s |  | fentryid |

---

## 下级组织-多选基础资料表 t_ism_settleresult_suborg

- **表名称：** 下级组织-多选基础资料表
- **表名：** t_ism_settleresult_suborg

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
| 1 | idx_ism_settleresult_suborg |  | fid |
| 2 | pk_ism_settleresult_suborg |  | fpkid |

---

## 异常信息-子表 t_ism_settleresult_sume

- **表名称：** 异常信息-子表
- **表名：** t_ism_settleresult_sume

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ferrcount | 异常记录数量 | int4 | 32 |  | √ | 0 | 异常记录数量 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fmsgcode | 异常描述 | varchar | 30 |  | √ | ' ' | 异常描述,枚举: E01 :跨组织业务单据没有找到匹配的结算路线 E02 :结算路径中的业务组织不在会计核算体系的下级组织中，请检查 E03 :跨组织业务单据没有生成内部交易单据，请检查 E04 :跨组织业务单据的需求方组织没有对应客户，请检查 E05 :跨组织业务单据的供应方组织没有对应供应商，请检查 E06 :跨组织业务单据根据取价规则未取到结算币别，请检查 E07 :跨组织业务单据根据取价规则未取到供应方汇率，请检查 E11 :跨组织业务单据未生成内部交易单据，不能生成结算清单。可用“批量生成内部交易单据”功能生成 E12 :分步调入单关联的分步调出单还未生成应收结算清单，请先创建对应分步调出单的应收结算清单 E13 :价格等于0且赠品不为“是” E14 :单据还未生成应收结算清单，不能生成应付结算清单 E15 :跨组织业务单据根据取价规则未取到需求方汇率，请检查 E16 :业务单据已生成了应收结算清单 E17 :业务单据已生成了应付结算清单 E18 :价格小于0，价格不允许为负数 E19 :退货的分步调出单关联的退货分步调入单还未生成应付结算清单，请先创建对应分步调入单的应付结算清单 E20 :退货单据还未生成应付结算清单，不能生成应收结算清单 E21 :收入确认时点为“签收”时，分步调入退回单须先生成分步调出退回单且已审核，才能生成结算清单 E91 :没有要生成结算清单的数据 E99 :创建结算清单失败 E22 :没有匹配的结算路径 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_settleresult_sume |  | fentryid |
| 2 | idx_ism_settleresult_sume |  | fid |

---

## 结算生成日志-主表 t_ism_settleresult

- **表名称：** 结算生成日志-主表
- **表名：** t_ism_settleresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferrrecordcount | 异常记录数 | int4 | 32 |  | √ | 0 | 异常记录数 |
| 3 | facctsysid | 会计核算体系 | int8 | 64 |  | √ | 0 | 核算体系 xkbd_accountingsys |
| 4 | fsettletype | 结算类型 | varchar | 30 |  | √ | ' ' | 结算类型,枚举: Manual :手工结算 ManualBatch :手工后台分批结算 AutoSchedule :自动结算 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 7 | fsettleendtime | 结算执行结束时间 | timestamp | 0 |  |  | null | 结算执行结束时间 |
| 8 | fresultmessage | 结算失败信息 | varchar | 1024 |  | √ | ' ' | 结算失败信息 |
| 9 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fdescription | 说明 | varchar | 1024 |  | √ | ' ' | 说明 |
| 11 | fsettlestatus | 结算状态 | varchar | 30 |  | √ | ' ' | 结算状态,枚举: 0 :结算中 1 :结算完成 9 :结算失败 |
| 12 | frollsettle | 滚动结算 | varchar | 30 |  | √ | ' ' | 滚动结算,枚举: 0 :否 1 :是 |
| 13 | fenddate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 14 | farsettlebillcount | 生成应收结算清单数量 | int4 | 32 |  | √ | 0 | 生成应收结算清单数量 |
| 15 | facctorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fautosettlescheme | 自动结算方案 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 17 | fsessionid | 线程ID | varchar | 100 |  | √ | ' ' | 线程ID |
| 18 | fsettlestarttime | 结算执行开始时间 | timestamp | 0 |  |  | null | 结算执行开始时间 |
| 19 | fresultstatus | 创建结果 | varchar | 30 |  | √ | ' ' | 创建结果,枚举: success :成功 fail :失败 |
| 20 | fapsettlebillcount | 生成应付结算清单数量 | int4 | 32 |  | √ | 0 | 生成应付结算清单数量 |
| 21 | fnaturalmonth | 按自然月结算 | varchar | 30 |  | √ | ' ' | 按自然月结算,枚举: 0 :否 1 :是 |
| 22 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | fsettledate | 结算日期 | timestamp | 0 |  |  | null | 结算日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_settleresult |  | fid |
| 2 | idx_ism_settleresult |  | fsessionid |
