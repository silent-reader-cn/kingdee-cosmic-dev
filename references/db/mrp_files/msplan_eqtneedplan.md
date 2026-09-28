# 资源调整建议-msplan_eqtneedplan

## 单据体-子表 t_msplan_eqtneedplanentry

- **表名称：** 单据体-子表
- **表名：** t_msplan_eqtneedplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | 源分录ID | int8 | 64 |  | √ | 0 | 源分录ID |
| 3 | fstime | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fadvtype | 调整类型 | varchar | 50 |  | √ | ' ' | 调整类型,枚举: A :建议新增 B :建议取消 C :数量调整 D :时间调整 |
| 6 | fpgres | 评估结果 | varchar | 50 |  | √ | ' ' | 评估结果,枚举: A :待评估 B :满足 C :部分满足 D :短缺 |
| 7 | fstarttaskid | 开始任务ID | int8 | 64 |  | √ | 0 | 开始任务ID |
| 8 | fisdelive | 配送确认 | bpchar | 1 |  | √ | '0' | 配送确认 |
| 9 | fsourcetype | 需求来源类型 | varchar | 100 |  | √ | ' ' | 需求来源类型 |
| 10 | fkey | 关键 | bpchar | 1 |  | √ | '0' | 关键 |
| 11 | fend | 结束节点 | varchar | 100 |  | √ | ' ' | 结束节点 |
| 12 | fresource | 设备资源 | int8 | 64 |  | √ | 0 | [分组基础资料带组织模板 mpdm_equipment](../mpdm_files/mpdm_equipment.md) |
| 13 | fusetime | 使用时长(小时) | numeric | 23 | 10 | √ | 0 | 使用时长(小时) |
| 14 | fqty | 设备数量 | numeric | 23 | 10 | √ | 0 | 设备数量 |
| 15 | fchoose | 可选 | bpchar | 1 |  | √ | '0' | 可选 |
| 16 | fstart | 开始节点 | varchar | 100 |  | √ | ' ' | 开始节点 |
| 17 | fquittime | 撤离时间 | timestamp | 0 |  |  | null | 撤离时间 |
| 18 | fendtaskid | 结束任务ID | int8 | 64 |  | √ | 0 | 结束任务ID |
| 19 | fftime | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 20 | fisquit | 撤离确认 | bpchar | 1 |  | √ | '0' | 撤离确认 |
| 21 | fplantime | 计划工时(小时) | numeric | 23 | 10 | √ | 0 | 计划工时(小时) |
| 22 | fadvftime | 建议完成时间 | timestamp | 0 |  |  | null | 建议完成时间 |
| 23 | fadvqty | 建议数量 | numeric | 23 | 10 | √ | 0 | 建议数量 |
| 24 | farea | 位置 | varchar | 100 |  | √ | ' ' | 位置 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fdelivetime | 配送时间 | timestamp | 0 |  |  | null | 配送时间 |
| 27 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fadvstime | 建议开始时间 | timestamp | 0 |  |  | null | 建议开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_eqtneedplanentry_fk |  | fid |
| 2 | pk_msplan_eqtneedplanentry |  | fentryid |

---

## 资源调整建议-主表 t_msplan_eqtneedplan

- **表名称：** 资源调整建议-主表
- **表名：** t_msplan_eqtneedplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodel | 检修设备类型 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 3 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fclosedate | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 5 | flogid | 日志 | int8 | 64 |  | √ | 0 | [运算日志 mrp_caculate_log](../msplan_files/mrp_caculate_log.md) |
| 6 | fecnstatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :空 B :变更中 C :变更完成 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fchecktype | 检修类别 | int8 | 64 |  | √ | 0 | [检修类别 mpdm_checkcategory](../mpdm_files/mpdm_checkcategory.md) |
| 9 | fisdeal | 处理状态 | bpchar | 1 |  | √ | '0' | 处理状态 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fworkstatus | 业务状态 | varchar | 5 |  | √ | ' ' | 业务状态,枚举: A :下达 B :关闭 C :空 |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 15 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 18 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 19 | fcloseor | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fworkcenter | 检修工作中心 | int8 | 64 |  | √ | 0 | [工作中心检修信息 mpdm_workcenter_info](../mpdm_files/mpdm_workcenter_info.md) |
| 21 | fecnbillid | 管理变更单ID | int8 | 64 |  | √ | 0 | 管理变更单ID |
| 22 | fdatasource | 数据来源 | varchar | 5 |  | √ | ' ' | 数据来源,枚举: A :手工新增 B :计算产生 |
| 23 | fproject | 项目号 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_eqtneedplan |  | fid |
| 2 | idx_msplan_eqtneedplan_fk |  | fbillstatus |
