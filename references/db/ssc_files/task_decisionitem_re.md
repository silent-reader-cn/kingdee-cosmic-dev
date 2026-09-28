# 决策项分配查询-task_decisionitem_re

## 决策项分配查询-多语言表 t_tk_decisionitemre_l

- **表名称：** 决策项分配查询-多语言表
- **表名：** t_tk_decisionitemre_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_decisionitemre_l_pkey |  | fpkid |
| 2 | tk_decirela_l_idx |  | fid,flocaleid |

---

## 决策项分配查询-主表 t_tk_decisionitemre

- **表名称：** 决策项分配查询-主表
- **表名：** t_tk_decisionitemre

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | ftasktypeid | 任务类型 | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fssccenter | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 12 | fapprovaltype | 审批类型 | varchar | 30 |  | √ | ' ' | 审批类型,枚举: 0 :审批不通过 1 :审批通过 2 :审批打回 |
| 13 | fbilltypeid | 业务单据 | int8 | 64 |  | √ | 0 | [业务单据 task_taskbill](../ssc_files/task_taskbill.md) |
| 14 | fdecisionitem | 决策项 | int8 | 64 |  | √ | 0 | [决策项 task_decisionitem](../ssc_files/task_decisionitem.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | tk_decirela_itemid_idx |  | fdecisionitem |
| 2 | tk_decirela_billtype_idx |  | fbilltypeid,ftasktypeid |
| 3 | t_tk_decisionitemre_pkey |  | fid |
