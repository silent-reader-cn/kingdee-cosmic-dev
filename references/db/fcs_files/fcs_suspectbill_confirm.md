# 疑似重复确认单-fcs_suspectbill_confirm

## 签署人单据体-子表 t_fcs_suspectconfirmuser

- **表名称：** 签署人单据体-子表
- **表名：** t_fcs_suspectconfirmuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdisclaimercontent | 风险告知内容 | varchar | 255 |  | √ | ' ' | 风险告知内容 |
| 3 | fdisclaimername | 风险告知 | varchar | 255 |  | √ | ' ' | 风险告知 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdisclaimercontent_tag | 风险告知内容_详情 | text | 0 |  |  | null | 风险告知内容_详情 |
| 6 | fconfirmtime | 签署时间 | timestamp | 0 |  |  | null | 签署时间 |
| 7 | fconfirmuser | 签署人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fconfirmusetype | 签署人类型 | varchar | 30 |  | √ | ' ' | 签署人类型,枚举: A :签署人 B :知悉人 |
| 10 | fdisclaimerid | fdisclaimerid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fcs_suspectconfirmuser |  | fid |
| 2 | pk_fcs_suspectconfirmuser |  | fentryid |

---

## 疑似重复确认单-主表 t_fcs_suspectconfirm

- **表名称：** 疑似重复确认单-主表
- **表名：** t_fcs_suspectconfirm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsourcetype | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统,枚举: cas :出纳 |
| 10 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 11 | fbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 12 | fisexpire | 是否过期 | bpchar | 1 |  | √ | ' ' | 是否过期 |
| 13 | fbillentity | 来源单据类型 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 14 | fsourcebillno | 来源单据编号 | varchar | 100 |  | √ | ' ' | 来源单据编号 |
| 15 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcs_suspectconfirm |  | fid |

---

## 单据体-子表 t_fcs_suspectconfirmentry

- **表名称：** 单据体-子表
- **表名：** t_fcs_suspectconfirmentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuspectbillid | 疑似重复单据id | int8 | 64 |  | √ | 0 | 疑似重复单据id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fcs_suspectconfirmentry |  | fentryid |
| 2 | idx_fcs_suspectconfirmentry |  | fid |
