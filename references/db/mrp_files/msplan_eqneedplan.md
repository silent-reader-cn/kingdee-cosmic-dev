# 设备需求计划-msplan_eqneedplan

## 设备需求计划-主表 t_msplan_eqneedplan

- **表名称：** 设备需求计划-主表
- **表名：** t_msplan_eqneedplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fmodel | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 4 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 5 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fclosedate | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fcloseor | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fworkcenter | 检修工作中心 | int8 | 64 |  | √ | 0 | 工作中心检修信息 mpdm_workcenter_info |
| 12 | fecnstatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :空 B :变更中 C :变更完成 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fchecktype | 检修类别 | int8 | 64 |  | √ | 0 | 检修类别 mpdm_checkcategory |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fworkstatus | 业务状态 | varchar | 5 |  | √ | ' ' | 业务状态,枚举: A :下达 B :关闭 C :空 |
| 17 | fdatasource | 数据来源 | varchar | 5 |  | √ | ' ' | 数据来源,枚举: A :手工新增 B :计算产生 |
| 18 | fproject | 项目号 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_eqneedplan |  | fid |
| 2 | idx_msplan_eqneedplan_fk |  | fbillstatus |

---

## 单据体-子表 t_msplan_eqneedplanentry

- **表名称：** 单据体-子表
- **表名：** t_msplan_eqneedplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 设备数量 | numeric | 23 | 10 | √ | 0 | 设备数量 |
| 3 | fstime | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 4 | fchoose | 可选 | bpchar | 1 |  | √ | '0' | 可选 |
| 5 | fstart | 开始节点 | varchar | 100 |  | √ | ' ' | 开始节点 |
| 6 | fquittime | 撤离时间 | timestamp | 0 |  |  | null | 撤离时间 |
| 7 | fendtaskid | 结束任务ID | int8 | 64 |  | √ | 0 | 结束任务ID |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fpgres | 评估结果 | varchar | 5 |  | √ | ' ' | 评估结果,枚举: A :待评估 B :满足 C :部分满足 D :短缺 |
| 10 | fftime | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 11 | fstarttaskid | 开始任务ID | int8 | 64 |  | √ | 0 | 开始任务ID |
| 12 | fisquit | 撤离确认 | bpchar | 1 |  | √ | '0' | 撤离确认 |
| 13 | fplantime | 计划工时(小时) | numeric | 23 | 10 | √ | 0 | 计划工时(小时) |
| 14 | fisdelive | 配送确认 | bpchar | 1 |  | √ | '0' | 配送确认 |
| 15 | fsourcetype | 需求来源类型 | varchar | 100 |  | √ | ' ' | 需求来源类型 |
| 16 | fkey | 关键 | bpchar | 1 |  | √ | '0' | 关键 |
| 17 | farea | 位置 | varchar | 100 |  | √ | ' ' | 位置 |
| 18 | fend | 结束节点 | varchar | 100 |  | √ | ' ' | 结束节点 |
| 19 | fresource | 设备资源 | int8 | 64 |  | √ | 0 | 分组基础资料带组织模板 mpdm_equipment |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fusetime | 使用时长(小时) | numeric | 23 | 10 | √ | 0 | 使用时长(小时) |
| 22 | fdelivetime | 配送时间 | timestamp | 0 |  |  | null | 配送时间 |
| 23 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_eqneedplanentry_fk |  | fid |
| 2 | pk_msplan_eqneedplanentry |  | fentryid |
