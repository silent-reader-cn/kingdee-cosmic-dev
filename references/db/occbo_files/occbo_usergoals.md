# 人员目标单-occbo_usergoals

## 目标详情-分表 t_occbo_usgoals_entry_a

- **表名称：** 目标详情-分表
- **表名：** t_occbo_usgoals_entry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompleterate13 | 完成率13 | varchar | 50 |  | √ | ' ' | 完成率13 |
| 3 | fcompleterate12 | 完成率12 | varchar | 50 |  | √ | ' ' | 完成率12 |
| 4 | fcompleterate15 | 完成率15 | varchar | 50 |  | √ | ' ' | 完成率15 |
| 5 | fcompleterate14 | 完成率14 | varchar | 50 |  | √ | ' ' | 完成率14 |
| 6 | fcompleterate16 | 完成率16 | varchar | 50 |  | √ | ' ' | 完成率16 |
| 7 | fcompleterate7 | 完成率7 | varchar | 50 |  | √ | ' ' | 完成率7 |
| 8 | fcompleterate8 | 完成率8 | varchar | 50 |  | √ | ' ' | 完成率8 |
| 9 | fcompleterate9 | 完成率9 | varchar | 50 |  | √ | ' ' | 完成率9 |
| 10 | fcompleterate1 | 完成率1 | varchar | 50 |  | √ | ' ' | 完成率1 |
| 11 | fcompleterate2 | 完成率2 | varchar | 50 |  | √ | ' ' | 完成率2 |
| 12 | fcompleterate3 | 完成率3 | varchar | 50 |  | √ | ' ' | 完成率3 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 14 | fcompleterate4 | 完成率4 | varchar | 50 |  | √ | ' ' | 完成率4 |
| 15 | fcompleterate5 | 完成率5 | varchar | 50 |  | √ | ' ' | 完成率5 |
| 16 | fcompleterate11 | 完成率11 | varchar | 50 |  | √ | ' ' | 完成率11 |
| 17 | fcompleterate6 | 完成率6 | varchar | 50 |  | √ | ' ' | 完成率6 |
| 18 | fcompleterate10 | 完成率10 | varchar | 50 |  | √ | ' ' | 完成率10 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_usgoals_entry_a |  | fid |
| 2 | pk_occbo_usgoals_entry_a |  | fentryid |

---

## 目标详情-子表 t_occbo_usgoals_entry

- **表名称：** 目标详情-子表
- **表名：** t_occbo_usgoals_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgoalsnum12 | 目标值12 | numeric | 23 | 10 | √ | 0 | 目标值12 |
| 3 | fgoalsnum11 | 目标值11 | numeric | 23 | 10 | √ | 0 | 目标值11 |
| 4 | fgoalsnum14 | 目标值14 | numeric | 23 | 10 | √ | 0 | 目标值14 |
| 5 | fgoalsnum13 | 目标值13 | numeric | 23 | 10 | √ | 0 | 目标值13 |
| 6 | fgoalsnum10 | 目标值10 | numeric | 23 | 10 | √ | 0 | 目标值10 |
| 7 | factualnum1 | 完成值1 | numeric | 23 | 10 | √ | 0 | 完成值1 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fyearcompleterate | 年度完成率 | varchar | 50 |  | √ | ' ' | 年度完成率 |
| 10 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fgoalsnum16 | 目标值16 | numeric | 23 | 10 | √ | 0 | 目标值16 |
| 12 | fgoalsnum15 | 目标值15 | numeric | 23 | 10 | √ | 0 | 目标值15 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fentryuseid | 目标人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fyeargoalsnum | 年度目标值 | numeric | 23 | 10 | √ | 0 | 年度目标值 |
| 16 | fentrylevelgoalsid | 销售级别目标id | int8 | 64 |  | √ | 0 | 销售级别目标id |
| 17 | factualnum9 | 完成值9 | numeric | 23 | 10 | √ | 0 | 完成值9 |
| 18 | factualnum8 | 完成值8 | numeric | 23 | 10 | √ | 0 | 完成值8 |
| 19 | fgoalsnum8 | 目标值8 | numeric | 23 | 10 | √ | 0 | 目标值8 |
| 20 | factualnum7 | 完成值7 | numeric | 23 | 10 | √ | 0 | 完成值7 |
| 21 | fgoalsnum9 | 目标值9 | numeric | 23 | 10 | √ | 0 | 目标值9 |
| 22 | factualnum6 | 完成值6 | numeric | 23 | 10 | √ | 0 | 完成值6 |
| 23 | fgoalsnum6 | 目标值6 | numeric | 23 | 10 | √ | 0 | 目标值6 |
| 24 | factualnum5 | 完成值5 | numeric | 23 | 10 | √ | 0 | 完成值5 |
| 25 | fgoalsnum7 | 目标值7 | numeric | 23 | 10 | √ | 0 | 目标值7 |
| 26 | factualnum4 | 完成值4 | numeric | 23 | 10 | √ | 0 | 完成值4 |
| 27 | fgoalsnum4 | 目标值4 | numeric | 23 | 10 | √ | 0 | 目标值4 |
| 28 | factualnum3 | 完成值3 | numeric | 23 | 10 | √ | 0 | 完成值3 |
| 29 | fgoalsnum5 | 目标值5 | numeric | 23 | 10 | √ | 0 | 目标值5 |
| 30 | factualnum2 | 完成值2 | numeric | 23 | 10 | √ | 0 | 完成值2 |
| 31 | fyearcompletenum | 年度完成值 | numeric | 23 | 10 | √ | 0 | 年度完成值 |
| 32 | fgoalsnum2 | 目标值2 | numeric | 23 | 10 | √ | 0 | 目标值2 |
| 33 | factualnum15 | 完成值15 | numeric | 23 | 10 | √ | 0 | 完成值15 |
| 34 | fgoalsnum3 | 目标值3 | numeric | 23 | 10 | √ | 0 | 目标值3 |
| 35 | factualnum16 | 完成值16 | numeric | 23 | 10 | √ | 0 | 完成值16 |
| 36 | factualnum13 | 完成值13 | numeric | 23 | 10 | √ | 0 | 完成值13 |
| 37 | fgoalsnum1 | 目标值1 | numeric | 23 | 10 | √ | 0 | 目标值1 |
| 38 | factualnum14 | 完成值14 | numeric | 23 | 10 | √ | 0 | 完成值14 |
| 39 | factualnum11 | 完成值11 | numeric | 23 | 10 | √ | 0 | 完成值11 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | factualnum12 | 完成值12 | numeric | 23 | 10 | √ | 0 | 完成值12 |
| 42 | fkpiid | KPI名称 | int8 | 64 |  | √ | 0 | [KPI occbo_kpi_base](../occbo_files/occbo_kpi_base.md) |
| 43 | fentrydeptid | 所属部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | factualnum10 | 完成值10 | numeric | 23 | 10 | √ | 0 | 完成值10 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_usgoals_entry |  | fentryid |
| 2 | idx_occbo_usgoals_entry |  | fkpiid,fentryuseid |

---

## 人员目标单-主表 t_occbo_usergoals

- **表名称：** 人员目标单-主表
- **表名：** t_occbo_usergoals

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 目标名称 | varchar | 80 |  | √ | ' ' | 目标名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fgoalsyearid | 目标年度 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 8 | fuserid | 目标人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fsaleslevelid | 销售级别 | int8 | 64 |  | √ | 0 | [销售级别 occbo_saleslevel](../occbo_files/occbo_saleslevel.md) |
| 13 | fdepartmentid | 所属部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | flevelgoalsid | 销售级别目标 | int8 | 64 |  | √ | 0 | 销售级别目标 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fgoalsmap | 月份对应分录关系 | varchar | 2000 |  | √ | ' ' | 月份对应分录关系 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_usergoals |  | fid |
| 2 | idx_occbo_usergoals |  | fsaleslevelid,fuserid |
