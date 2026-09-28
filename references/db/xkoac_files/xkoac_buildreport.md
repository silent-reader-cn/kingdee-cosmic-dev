# 经营流水账生成报告-xkoac_buildreport

## 经营流水账生成报告-主表 t_xkoac_buildreport

- **表名称：** 经营流水账生成报告-主表
- **表名：** t_xkoac_buildreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famoeabid | 经营单元 | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 3 | fvouchertype | 流水账类型 | bpchar | 1 |  | √ | '2' | 流水账类型,枚举: 2 :收入 1 :费用 3 :转账 |
| 4 | fsourcenum | 来源单据编号 | varchar | 100 |  | √ | ' ' | 来源单据编号 |
| 5 | fbatchnumber | 生成批号 | varchar | 80 |  | √ | ' ' | 生成批号 |
| 6 | fbuildtasktag | 任务标识 | varchar | 80 |  | √ | ' ' | 任务标识 |
| 7 | fsourcebilltype | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fbuildstate | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 0 :已生成 1 :未生成 |
| 10 | fsourcesys | 来源系统 | varchar | 36 |  | √ | ' ' | [业务应用列表 bos_devp_bizapplist](../devnew_files/bos_devp_bizapplist.md) |
| 11 | foacvchid | 经营流水账id | int8 | 64 |  | √ | 0 | 经营流水账id |
| 12 | fautoplanid | 定时生成经营流水账方案 | int8 | 64 |  | √ | 0 | [定时生成经营流水账方案 xkoac_autovchplan](../xkoac_files/xkoac_autovchplan.md) |
| 13 | faccountbookid | 经营账簿 | int8 | 64 |  | √ | 0 | [经营账簿 xkoac_operatingbook](../xkoac_files/xkoac_operatingbook.md) |
| 14 | fsourcebill | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 15 | foacvchno | 经营流水账编号 | varchar | 30 |  | √ | ' ' | 经营流水账编号 |
| 16 | fbuildtype | 生成方式 | bpchar | 1 |  | √ | ' ' | 生成方式,枚举: 1 :定时自动生成 2 :实时自动生成 3 :生成经营流水账向导操作 |
| 17 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fsourcebillid | 来源单据id | varchar | 36 |  | √ | ' ' | 来源单据id |
| 19 | fperiod | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 20 | fvchimptplan | 来源方案 | int8 | 64 |  | √ | 0 | [经营流水账来源方案 xkoac_voucherimptplan](../xkoac_files/xkoac_voucherimptplan.md) |
| 21 | fvchplanseq | 来源方案行编码ID | int4 | 32 |  | √ | 0 | 来源方案行编码ID |
| 22 | fdatetimefield | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 23 | fbilltypeid | 交易类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkoac_buildreport |  | fid |
| 2 | idx_xkoac_buildreport |  | faccountbookid,fperiod,famoeabid |

---

## 报告明细-子表 t_xkoac_buildreportentry

- **表名称：** 报告明细-子表
- **表名：** t_xkoac_buildreportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmessage | 提示信息 | varchar | 1000 |  | √ | ' ' | 提示信息 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcheckitem | 检查项 | varchar | 5 |  | √ | ' ' | 检查项,枚举: 0 :权限 1 :经营账簿 2 :来源方案 3 :经营单元 4 :日期 5 :网控 6 :其他 7 :数据来源 8 :经营科目 9 :经营核算维度 10 :金额 11 :币种 12 :汇率 13 :跨单据体字段 14 :来源字段标识 15 :来源字段 16 :经营流水账 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ferrlevel | 提示类型 | varchar | 5 |  | √ | ' ' | 提示类型,枚举: 0 :警告 1 :异常 2 :错误 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_buildreportentry |  | fid,fcheckitem,ferrlevel |
| 2 | pk_t_xkoac_buildreportentry |  | fentryid |
