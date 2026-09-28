# IPO项目进度-ipm_project_progress_bill

## 任务参与人-多选基础资料表 t_ipm_project_participant

- **表名称：** 任务参与人-多选基础资料表
- **表名：** t_ipm_project_participant

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipo_project_participant_fk |  | fid |
| 2 | pk_t_ipm_project_participant |  | fpkid |

---

## IPO项目进度-主表 t_ipm_project_progress

- **表名称：** IPO项目进度-主表
- **表名：** t_ipm_project_progress

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 1 | id |
| 2 | forgfield | forgfield | int8 | 64 |  | √ | 0 |  |
| 3 | fdirectorid | 任务负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fbasetaskgroupname | 事项任务类型名称 | varchar | 255 |  | √ | ' ' | 事项任务类型名称 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fsortindex | 排序下标 | numeric | 10 | 2 |  | null | 排序下标 |
| 8 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | factualendtime | 实际日期.结束 | timestamp | 0 |  |  | null | 实际日期.结束 |
| 10 | ftaskstate | 任务状态 | bpchar | 1 |  | √ | ' ' | 任务状态,枚举: 0 :未开始 1 :进行中 2 :已延迟 3 :已完成 4 :已取消 |
| 11 | ftaskdesc | 任务描述 | varchar | 500 |  | √ | ' ' | 任务描述 |
| 12 | fexpenseaccountid | 费用科目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 13 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fbasetaskgroupsort | 基础任务库分组排序字段 | numeric | 22 | 2 |  | null | 基础任务库分组排序字段 |
| 15 | factualstarttime | 实际日期.开始 | timestamp | 0 |  |  | null | 实际日期.开始 |
| 16 | fipoorgid | IPO主体 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |
| 17 | fsortcode | 排序编码 | varchar | 50 |  | √ | ' ' | 排序编码 |
| 18 | fplandaynum | 计划天数 | int8 | 64 |  | √ | 0 | 计划天数 |
| 19 | ftaskname | 任务名称 | varchar | 200 |  | √ | ' ' | 任务名称 |
| 20 | furgencylevel | 紧急程度 | bpchar | 1 |  | √ | ' ' | 紧急程度,枚举: H :高 M :中 L :低 |
| 21 | fbasetaskid | 事项任务ID | int8 | 64 |  | √ | 0 | 事项任务ID |
| 22 | factualdaynum | 实际天数 | int8 | 64 |  | √ | 0 | 实际天数 |
| 23 | fbasetaskgroupid | 事项任务类型ID | int8 | 64 |  | √ | 0 | 事项任务类型ID |
| 24 | fplanendtime | 计划日期.结束 | timestamp | 0 |  |  | null | 计划日期.结束 |
| 25 | fspeedvalue | 任务进度 | numeric | 23 | 10 |  | null | 任务进度 |
| 26 | fplanstarttime | 计划日期.开始 | timestamp | 0 |  |  | null | 计划日期.开始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipm_project_progress |  | fid |
| 2 | idx_task_name |  | ftaskname |
