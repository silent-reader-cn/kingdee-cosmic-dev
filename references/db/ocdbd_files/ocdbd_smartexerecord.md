# 智能审单记录-ocdbd_smartexerecord

## 智能审单记录-主表 t_ocdbd_smartexerecord

- **表名称：** 智能审单记录-主表
- **表名：** t_ocdbd_smartexerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbatchnumber | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 3 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 4 | fuser | 通知人员 | varchar | 2000 |  | √ | ' ' | 通知人员 |
| 5 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fresulttext | 审单检查项结果 | text | 0 |  |  | ' ' | 审单检查项结果 |
| 8 | fcontroltype | 单据控制方式 | varchar | 50 |  | √ | ' ' | 单据控制方式,枚举: nocontrol :不控制 confirm :提醒确认 force :严格控制 |
| 9 | fschemaid | 智能审单方案 | int8 | 64 |  | √ | 0 | [智能审单方案 ocdbd_scheme](../ocdbd_files/ocdbd_scheme.md) |
| 10 | fhandletype | 不通过处理方式 | varchar | 10 |  | √ | ' ' | 不通过处理方式,枚举: A :转人工复审 B :自动循环 C :不通过打回 |
| 11 | fitemid | fitemid | varchar | 50 |  | √ | ' ' |  |
| 12 | fsuccess | 审单成功 | bpchar | 1 |  | √ | ' ' | 审单成功 |
| 13 | fschemaresultid | fschemaresultid | int8 | 64 |  | √ | 0 |  |
| 14 | fcreatedate | 智能审单时间 | timestamp | 0 |  |  | null | 智能审单时间 |
| 15 | fbillpkid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 16 | forderstatus | 订单状态(待更新) | varchar | 10 |  | √ | ' ' | 订单状态(待更新),枚举: A :暂存 B :已提交 |
| 17 | fitem | fitem | varchar | 50 |  | √ | ' ' |  |
| 18 | fsmartauditstatus | 智能审单状态 | varchar | 10 |  | √ | ' ' | 智能审单状态,枚举: A :未提交智审 B :待人工审核 C :人工审核成功 D :待智能审核 E :智能审核中 F :自动循环审单 G :转人工复核 S :智能审核成功 |
| 19 | fitemresultid | fitemresultid | int8 | 64 |  | √ | 0 |  |
| 20 | fbillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 21 | fbilltypeid | 单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_smartexerecord_c |  | fcreatedate |
| 2 | idx_ocdbd_smartexerecord_b |  | fbillpkid |
| 3 | pk_ocdbd_smartexerecord |  | fid |

---

## 单据体-子表 t_ocdbd_smartrecord_ent

- **表名称：** 单据体-子表
- **表名：** t_ocdbd_smartrecord_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispass | 通过 | bpchar | 1 |  | √ | ' ' | 通过 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fresult | 检查结果 | text | 0 |  |  | ' ' | 检查结果 |
| 5 | fitemname | 检查项名 | varchar | 200 |  | √ | ' ' | 检查项名 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fitemid | 检查项id | int8 | 64 |  | √ | 0 | 检查项id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_smartrecord_ent |  | fentryid |
| 2 | idx_ocdbd_recordent |  | fid |
