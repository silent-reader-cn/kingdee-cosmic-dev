# 委托设置-wf_delegatesetting

## 委托设置-主表 t_wf_delegatesetting

- **表名称：** 委托设置-主表
- **表名：** t_wf_delegatesetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsendmsg | 委托任务处理后通知委托人 | bpchar | 1 |  | √ | '1' | 委托任务处理后通知委托人 |
| 4 | fprocdefid | 流程 | int8 | 64 |  | √ | 0 | [流程管理 wf_processdefinition](../wf_files/wf_processdefinition.md) |
| 5 | factivityid | 委托节点Id | varchar | 2000 |  | √ | ' ' | 委托节点Id |
| 6 | fdelegatetodo | 委托已有待办任务 | bpchar | 1 |  | √ | '0' | 委托已有待办任务 |
| 7 | fsource | 来源 | varchar | 50 |  | √ | ' ' | 来源 |
| 8 | fstarttime | 委托期间.开始 | timestamp | 0 |  |  | null | 委托期间.开始 |
| 9 | fstatus | 状态 | varchar | 30 |  | √ | '1' | 状态,枚举: 0 :禁用 1 :启用 |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fdeleruleshowtext | 委托条件(列表显示值) | varchar | 80 |  | √ | ' ' | 委托条件(列表显示值) |
| 13 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | factivityname | 委托节点名称 | varchar | 2000 |  | √ | ' ' | 委托节点名称 |
| 15 | fdelegateexpression | 委托条件表达式 | text | 0 |  |  | null | 委托条件表达式 |
| 16 | fassignorid | 委托人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fendtime | 委托期间.结束 | timestamp | 0 |  |  | null | 委托期间.结束 |
| 18 | freceivemsg | 委托期间委托人接收任务 | bpchar | 1 |  | √ | '0' | 委托期间委托人接收任务 |
| 19 | fdelegaterule | 委托条件 | text | 0 |  |  | null | 委托条件 |
| 20 | fentrabillid | 单据 | varchar | 36 |  | √ | ' ' | [实体元数据 bos_entitymeta](../mdl_files/bos_entitymeta.md) |
| 21 | fisappliesallversions | 是否应用于所有版本 | bpchar | 1 |  | √ | '0' | 是否应用于所有版本 |
| 22 | ftrusteeid | 受托人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fscope | 委托方式 | varchar | 30 |  | √ | ' ' | 委托方式,枚举: 1 :按流程委托 2 :按单据委托 3 :全部任务委托 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_delegateset_assignor |  | fassignorid,fstarttime,fendtime,fstatus |
| 2 | idx_wf_delegateset_procdefid |  | fprocdefid |
| 3 | pk_t_wf_delegatesetting |  | fid |
| 4 | idx_wf_delegateset_entrbillid |  | fentrabillid |

---

## 委托设置-多语言表 t_wf_delegatesetting_l

- **表名称：** 委托设置-多语言表
- **表名：** t_wf_delegatesetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeleruleshowtext | 委托条件(列表显示值) | varchar | 80 |  | √ | ' ' | 委托条件(列表显示值) |
| 3 | factivityname | 委托节点名称 | varchar | 2000 |  | √ | ' ' | 委托节点名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_wf_delegatesetting_l |  | fpkid |
| 2 | idx_wf_delegatesetting_l |  | fid,flocaleid |
