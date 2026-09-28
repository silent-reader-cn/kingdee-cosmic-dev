# 方案执行队列-xkcr_smartmerge_exe_queue

## 合并组织-多选基础资料表 t_xkcr_sm_queue_org

- **表名称：** 合并组织-多选基础资料表
- **表名：** t_xkcr_sm_queue_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_sm_queue_org |  | fpkid |
| 2 | idx_xkcr_sm_queue_org_fid |  | fid |

---

## 合并范围-多选基础资料表 t_xkcr_sm_queue_scope

- **表名称：** 合并范围-多选基础资料表
- **表名：** t_xkcr_sm_queue_scope

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_sm_queue_scope_fid |  | fid |
| 2 | pk_xkcr_sm_queue_scope |  | fpkid |

---

## 方案执行队列-主表 t_xkcr_sm_execute_queue

- **表名称：** 方案执行队列-主表
- **表名：** t_xkcr_sm_execute_queue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 异常信息 | varchar | 1000 |  |  | ' ' | 异常信息 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fremark_tag | 异常信息_详情 | text | 0 |  |  | ' ' | 异常信息_详情 |
| 7 | fsubmittime | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 8 | fretrycount | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fautolock | 执行锁 | bpchar | 1 |  | √ | '0' | 执行锁 |
| 11 | fstatus | 执行状态 | varchar | 50 |  | √ | '0' | 执行状态,枚举: 0 :待执行 1 :执行中 2 :完成 3 :执行异常 |
| 12 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fsmartmergeplan | 自动合并方案 | int8 | 64 |  | √ | 0 | [自动合并方案 xkcr_smart_merge_plan](../xkcr_files/xkcr_smart_merge_plan.md) |
| 14 | fyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 15 | fcreatetype | 执行方式 | bpchar | 1 |  | √ | '0' | 执行方式,枚举: 0 :自动 1 :手动 |
| 16 | fperiod | 期间 | int4 | 32 |  | √ | 0 | 期间 |
| 17 | fopkeys | 操作编码 | varchar | 500 |  | √ | ' ' | 操作编码 |
| 18 | fbillno | 执行记录 | varchar | 30 |  | √ | ' ' | 执行记录 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_sm_execute_queue_sch |  | fsmartmergeplan,fbillno |
| 2 | pk_xkcr_sm_execute_queue |  | fid |
