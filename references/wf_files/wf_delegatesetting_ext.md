# 委托设置-wf_delegatesetting_ext

## 委托设置-主表 t_wf_delegatesetting

- **表名称：** 委托设置-主表
- **表名：** t_wf_delegatesetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fsendmsg | 委托任务处理后通知委托人 | bpchar | 1 |  | √ | '1' | 委托任务处理后通知委托人 |
| 4 | fprocdefid | 流程 | int8 | 64 |  | √ | 0 | 流程管理 wf_processdefinition |
| 5 | factivityid | 委托节点Id | varchar | 2000 |  | √ | ' ' | 委托节点Id |
| 6 | fdelegatetodo | 委托已有待办任务 | bpchar | 1 |  | √ | '0' | 委托已有待办任务 |
| 7 | fstarttime | 委托期间.开始 | timestamp | 0 |  |  | null | 委托期间.开始 |
| 8 | fstatus | 状态 | varchar | 30 |  | √ | '1' | 状态,枚举: 0 :禁用 1 :启用 |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fdeleruleshowtext | 委托条件(列表显示值) | varchar | 80 |  | √ | ' ' | 委托条件(列表显示值) |
| 12 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | factivityname | 委托节点名称 | varchar | 2000 |  | √ | ' ' | 委托节点名称 |
| 14 | fdelegateexpression | 委托条件表达式 | text | 0 |  |  | null | 委托条件表达式 |
| 15 | fassignorid | 委托人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fendtime | 委托期间.结束 | timestamp | 0 |  |  | null | 委托期间.结束 |
| 17 | freceivemsg | 委托期间我能接收任务 | bpchar | 1 |  | √ | '0' | 委托期间我能接收任务 |
| 18 | fdelegaterule | 委托条件 | text | 0 |  |  | null | 委托条件 |
| 19 | fentrabillid | 单据 | varchar | 36 |  | √ | ' ' | 实体元数据 bos_entitymeta |
| 20 | ftrusteeid | 受托人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fscope | 委托方式 | varchar | 30 |  | √ | ' ' | 委托方式,枚举: 1 :按流程委托 2 :按单据委托 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_delegateset_assignor |  | fassignorid |
| 2 | pk_t_wf_delegatesetting |  | fid |

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
