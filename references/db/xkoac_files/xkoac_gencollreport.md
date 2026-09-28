# 经营费用归集单生成报告-xkoac_gencollreport

## 报告明细-子表 t_xkoac_gencollrepentry

- **表名称：** 报告明细-子表
- **表名：** t_xkoac_gencollrepentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmessage | 提示信息 | varchar | 500 |  | √ | ' ' | 提示信息 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcheckitem | 检查项 | varchar | 2 |  | √ | ' ' | 检查项,枚举: 0 :权限 1 :经营账簿 2 :组织架构版本 3 :归集方案 4 :经营单元 5 :日期 6 :网控 7 :过滤条件 8 :费用项目 9 :经营科目 10 :经营核算维度 11 :金额 12 :币种 13 :汇率 14 :跨单据体字段 15 :来源字段标识 16 :来源字段值 17 :其他 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ferrlevel | 提示类型 | bpchar | 1 |  | √ | ' ' | 提示类型,枚举: 0 :警告 1 :异常 2 :错误 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_gencollrepentry |  | fentryid |
| 2 | idx_xkoac_gcrentry_fid |  | fid |

---

## 经营费用归集单生成报告-主表 t_xkoac_gencollreport

- **表名称：** 经营费用归集单生成报告-主表
- **表名：** t_xkoac_gencollreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famoeabid | 经营单元 | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 3 | fbatchnumber | 生成批号 | varchar | 50 |  | √ | ' ' | 生成批号 |
| 4 | fbuildtasktag | 任务标识 | varchar | 50 |  | √ | ' ' | 任务标识 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsrcbillid | 来源单据字符ID | varchar | 36 |  | √ | ' ' | 来源单据字符ID |
| 7 | fcollplanid | 归集方案编码 | int8 | 64 |  | √ | 0 | [经营费用归集方案 xkoac_collplan](../xkoac_files/xkoac_collplan.md) |
| 8 | fbuildstate | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 0 :已生成 1 :未生成 |
| 9 | fsourcesys | 来源系统 | varchar | 36 |  | √ | ' ' | [业务应用列表 bos_devp_bizapplist](../devnew_files/bos_devp_bizapplist.md) |
| 10 | faccountbookid | 经营账簿 | int8 | 64 |  | √ | 0 | [经营账簿 xkoac_operatingbook](../xkoac_files/xkoac_operatingbook.md) |
| 11 | fsourcebill | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | fsrctype | 来源类型 | bpchar | 1 |  | √ | ' ' | 来源类型,枚举: 1 :业务单据 2 :总账凭证 |
| 13 | fsrcbillintid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 14 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fplanseq | 归集方案行ID | int4 | 32 |  | √ | 0 | 归集方案行ID |
| 16 | fcollid | 经营费用归集单ID | int8 | 64 |  | √ | 0 | 经营费用归集单ID |
| 17 | fperiod | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 18 | fsrcbilltype | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 19 | fcollnum | 经营费用归集单编号 | varchar | 50 |  | √ | ' ' | 经营费用归集单编号 |
| 20 | fsrcbillnum | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_gcrrt_tag |  | fbuildtasktag |
| 2 | pk_xkoac_gencollreport |  | fid |
| 3 | idx_xkoac_gcrrt_bpps |  | faccountbookid,fperiod,fcollplanid,fplanseq |

---

## 报告明细-多语言表 t_xkoac_gencollrepentry_l

- **表名称：** 报告明细-多语言表
- **表名：** t_xkoac_gencollrepentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmessage | 提示信息 | varchar | 500 |  | √ | ' ' | 提示信息 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_gencollrepentry_l |  | fpkid |
| 2 | idx_xkoac_gcrepentry_l |  | fentryid,flocaleid |
