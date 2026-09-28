# 设备需求计划变更单-msplan_eqxneedplan

## 关联子实体-子表 t_msplan_eqxneedplanentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_msplan_eqxneedplanentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_eqxneedplanentry_lk |  | fpkid |
| 2 | idx_msplan_eqxneedplanentry_lk_fk |  | fentryid |

---

## 单据体-子表 t_msplan_eqxneedplanentry

- **表名称：** 单据体-子表
- **表名：** t_msplan_eqxneedplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstime | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fpgres | 评估结果 | varchar | 5 |  | √ | ' ' | 评估结果,枚举: A :待评估 B :满足 C :部分满足 D :短缺 |
| 5 | fstarttaskid | 开始任务ID | int8 | 64 |  | √ | 0 | 开始任务ID |
| 6 | fisdelive | 配送确认 | bpchar | 1 |  | √ | '0' | 配送确认 |
| 7 | fsourcetype | 需求来源类型 | varchar | 100 |  | √ | ' ' | 需求来源类型 |
| 8 | fkey | 关键 | bpchar | 1 |  | √ | '0' | 关键 |
| 9 | fend | 结束节点 | varchar | 100 |  | √ | ' ' | 结束节点 |
| 10 | fresource | 资源 | int8 | 64 |  | √ | 0 | 分组基础资料带组织模板 mpdm_equipment |
| 11 | fusetime | 使用时长(小时) | numeric | 23 | 10 | √ | 0 | 使用时长(小时) |
| 12 | fqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 13 | fsourcebilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 14 | fchoose | 可选 | bpchar | 1 |  | √ | '0' | 可选 |
| 15 | fstart | 开始节点 | varchar | 100 |  | √ | ' ' | 开始节点 |
| 16 | fsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 17 | fquittime | 撤离时间 | timestamp | 0 |  |  | null | 撤离时间 |
| 18 | fendtaskid | 结束任务ID | int8 | 64 |  | √ | 0 | 结束任务ID |
| 19 | fftime | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 20 | fisquit | 撤离确认 | bpchar | 1 |  | √ | '0' | 撤离确认 |
| 21 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 22 | fsourceentryseq | 来源单据行号 | int8 | 64 |  | √ | 0 | 来源单据行号 |
| 23 | fplantime | 计划工时(小时) | numeric | 23 | 10 | √ | 0 | 计划工时(小时) |
| 24 | fsourcebillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 25 | farea | 位置 | varchar | 100 |  | √ | ' ' | 位置 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fdelivetime | 配送时间 | timestamp | 0 |  |  | null | 配送时间 |
| 28 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_eqxneedplanentry |  | fentryid |
| 2 | idx_msplan_eqxneedplanentry_fk |  | fid |

---

## 设备需求计划变更单-主表 t_msplan_eqxneedplan

- **表名称：** 设备需求计划变更单-主表
- **表名：** t_msplan_eqxneedplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fmodel | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 4 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 5 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fecnremark | 变更原因 | varchar | 300 |  | √ | ' ' | 变更原因 |
| 8 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fclosedate | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fcloseor | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fworkcenter | 检修工作中心 | int8 | 64 |  | √ | 0 | 工作中心检修信息 mpdm_workcenter_info |
| 13 | fecnstatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :空 B :变更中 C :变更完成 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fchecktype | 检修类别 | int8 | 64 |  | √ | 0 | 检修类别 mpdm_checkcategory |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fworkstatus | 业务状态 | varchar | 5 |  | √ | ' ' | 业务状态,枚举: A :下达 B :关闭 C :空 |
| 18 | fdatasource | 数据来源 | varchar | 5 |  | √ | ' ' | 数据来源,枚举: A :手工新增 B :计算产生 |
| 19 | fproject | 项目号 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_eqxneedplan_fk |  | fbillstatus |
| 2 | pk_msplan_eqxneedplan |  | fid |

---

## 设备需求计划变更单-反写记录表 t_msplan_eqxneedplan_wb

- **表名称：** 设备需求计划变更单-反写记录表
- **表名：** t_msplan_eqxneedplan_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_eqxneedplan_wb |  | fentryid |
| 2 | idx_msplan_eqxneedplan_wb_fk |  | fid |

---

## 关联子实体-子表 t_msplan_eqxneedplan_lk

- **表名称：** 关联子实体-子表
- **表名：** t_msplan_eqxneedplan_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_eqxneedplan_lk_fk |  | fid |
| 2 | pk_msplan_eqxneedplan_lk |  | fpkid |

---

## 设备需求计划变更单-关联追踪表 t_msplan_eqxneedplan_tc

- **表名称：** 设备需求计划变更单-关联追踪表
- **表名：** t_msplan_eqxneedplan_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_eqxneedplan_tc_tbill |  | ftbillid |
| 2 | pk_msplan_eqxneedplan_tc |  | fid |
| 3 | idx_msplan_eqxneedplan_tc_tid |  | ftid |
