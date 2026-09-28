# IPO财务问题自查整改清单-ipm_reform_bill

## IPO财务问题自查整改清单-主表 t_ipm_reform

- **表名称：** IPO财务问题自查整改清单-主表
- **表名：** t_ipm_reform

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | forgfield | forgfield | int8 | 64 |  | √ | 0 |  |
| 4 | factualendtime | 实际日期.结束 | timestamp | 0 |  |  | null | 实际日期.结束 |
| 5 | ftaskstate | 任务状态 | bpchar | 1 |  | √ | ' ' | 任务状态,枚举: 0 :未开始 1 :进行中 2 :已延迟 3 :已完成 4 :已取消 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | factualstarttime | 实际日期.开始 | timestamp | 0 |  |  | null | 实际日期.开始 |
| 8 | fthemetype | 主题分析类别 | int8 | 64 |  | √ | 0 | IPO主题分析菜单类型 theme_menu_type |
| 9 | fipoorgid | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |
| 10 | fplandaynum | 计划天数 | int8 | 64 |  | √ | 0 | 计划天数 |
| 11 | furgencylevel | 紧急程度 | bpchar | 1 |  | √ | ' ' | 紧急程度,枚举: H :高 M :中 L :低 |
| 12 | fdirectorid | 任务负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | factualdaynum | 实际天数 | int8 | 64 |  | √ | 0 | 实际天数 |
| 16 | freformdesc | 整改内容 | varchar | 500 |  | √ | ' ' | 整改内容 |
| 17 | fsortindex | 排序下标 | numeric | 10 | 2 |  | null | 排序下标 |
| 18 | ftakename | 任务名称 | varchar | 255 |  | √ | ' ' | 任务名称 |
| 19 | fplanendtime | 计划日期.结束 | timestamp | 0 |  |  | null | 计划日期.结束 |
| 20 | fspeedvalue | 进度值 | numeric | 23 | 10 |  | null | 进度值 |
| 21 | fplanstarttime | 计划日期.开始 | timestamp | 0 |  |  | null | 计划日期.开始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_task_name_uq |  | fthemetype,ftakename |
| 2 | pk_t_ipm_reform |  | fid |

---

## 任务参与人-多选基础资料表 t_ipm_reform_participant

- **表名称：** 任务参与人-多选基础资料表
- **表名：** t_ipm_reform_participant

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipm_reform_participant |  | fpkid |
| 2 | idx_ipo_reform_participant_fk |  | fid |
