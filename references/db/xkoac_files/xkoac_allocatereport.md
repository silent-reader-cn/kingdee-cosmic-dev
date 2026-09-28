# 经营费用分摊报告-xkoac_allocatereport

## 经营费用分摊报告-主表 t_xkoac_allocatereport

- **表名称：** 经营费用分摊报告-主表
- **表名：** t_xkoac_allocatereport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famoeabid | 经营单元 | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 3 | fsourcenum | 来源单据编号 | varchar | 100 |  | √ | ' ' | 来源单据编号 |
| 4 | fbuildtasktag | 生成批号 | varchar | 100 |  | √ | ' ' | 生成批号 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fresultbill | 结果单ID | int8 | 64 |  | √ | 0 | 结果单ID |
| 7 | fimptplan | 分摊方案编码 | int8 | 64 |  | √ | 0 | [经营费用分摊方案 xkoac_allocationplan](../xkoac_files/xkoac_allocationplan.md) |
| 8 | fallocatestatus | 分摊状态 | bpchar | 1 |  | √ | '0' | 分摊状态,枚举: 0 :分摊成功 1 :分摊失败 |
| 9 | faccountbookid | 经营账簿 | int8 | 64 |  | √ | 0 | [经营账簿 xkoac_operatingbook](../xkoac_files/xkoac_operatingbook.md) |
| 10 | fsourcebill | 来源单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsourcebillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 13 | fplanseq | 分摊方案行ID | int4 | 32 |  | √ | 0 | 分摊方案行ID |
| 14 | fperiod | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 15 | fresultbillno | 经营费用分摊结果单编号 | varchar | 100 |  | √ | ' ' | 经营费用分摊结果单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_allocatereport |  | fid |
| 2 | idx_xkoac_allocatereport |  | faccountbookid,fperiod |

---

## 报告明细-子表 t_xkoac_allctreportentry

- **表名称：** 报告明细-子表
- **表名：** t_xkoac_allctreportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmessage | 分摊结果提示信息 | varchar | 1000 |  | √ | ' ' | 分摊结果提示信息 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcheckitem | 检查项 | varchar | 5 |  | √ | ' ' | 检查项,枚举: 0 :权限 1 :经营账簿 2 :来源方案 3 :经营单元 4 :期间 5 :网控 6 :其他 7 :数据来源 8 :经营科目 9 :经营核算维度 10 :金额 11 :币种 12 :汇率 13 :跨单据体字段 14 :来源字段标识 15 :来源字段 16 :分摊规则 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ferrlevel | 提示类型 | varchar | 5 |  | √ | ' ' | 提示类型,枚举: 0 :警告 1 :异常 2 :错误 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_allctreportentry |  | fid |
| 2 | pk_xkoac_allctreportentry |  | fentryid |
