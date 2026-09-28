# 其他设备需求计划-msplan_otherneedplan

## 单据体-子表 t_msplan_orneedplanentry

- **表名称：** 单据体-子表
- **表名：** t_msplan_orneedplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 设备数量 | numeric | 23 | 10 | √ | 0 | 设备数量 |
| 3 | fstime | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 4 | fchoose | 可选 | bpchar | 1 |  | √ | '0' | 可选 |
| 5 | fstart | 开始节点 | varchar | 100 |  | √ | ' ' | 开始节点 |
| 6 | fendtaskid | 结束任务ID | int8 | 64 |  | √ | 0 | 结束任务ID |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fftime | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 9 | fstarttaskid | 开始任务ID | int8 | 64 |  | √ | 0 | 开始任务ID |
| 10 | fkey | 关键 | bpchar | 1 |  | √ | '0' | 关键 |
| 11 | fend | 结束节点 | varchar | 100 |  | √ | ' ' | 结束节点 |
| 12 | fresource | 资源 | int8 | 64 |  | √ | 0 | [分组基础资料带组织模板 mpdm_equipment](../mpdm_files/mpdm_equipment.md) |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_orneedplanentry |  | fentryid |
| 2 | idx_msplan_orneedplanentry_fk |  | fid |

---

## 其他设备需求计划-主表 t_msplan_orneedplan

- **表名称：** 其他设备需求计划-主表
- **表名：** t_msplan_orneedplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodel | 检修设备类型 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 4 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 5 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fclosedate | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fcloseor | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fworkcenter | 检修工作中心 | int8 | 64 |  | √ | 0 | [工作中心检修信息 mpdm_workcenter_info](../mpdm_files/mpdm_workcenter_info.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fchecktype | 检修类别 | int8 | 64 |  | √ | 0 | [检修类别 mpdm_checkcategory](../mpdm_files/mpdm_checkcategory.md) |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fworkstatus | 业务状态 | varchar | 5 |  | √ | ' ' | 业务状态,枚举: A :下达 B :关闭 C :空 |
| 16 | fdatasource | 数据来源 | varchar | 5 |  | √ | ' ' | 数据来源,枚举: A :手工新增 B :计算产生 |
| 17 | fisspec | 特殊 | bpchar | 1 |  | √ | '0' | 特殊 |
| 18 | fproject | 项目号 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_orneedplan_fk |  | fbillstatus |
| 2 | pk_msplan_orneedplan |  | fid |
