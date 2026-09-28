# 质检方案-task_qualitycheckscheme

## 抽选组织-多选基础资料表 t_tk_checkschemeorg

- **表名称：** 抽选组织-多选基础资料表
- **表名：** t_tk_checkschemeorg

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
| 1 | index_ssc_chkschorg_id |  | fid |
| 2 | t_tk_checkschemeorg_pkey |  | fpkid |

---

## 质检方案-主表 t_tk_qualitycheckscheme

- **表名称：** 质检方案-主表
- **表名：** t_tk_qualitycheckscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fisautoprocess | 审批类型 | bpchar | 1 |  | √ | ' ' | 审批类型,枚举: 0 :人工审批 1 :自动审批 2 :所有任务 |
| 4 | ftasktype | 任务类型 | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |
| 5 | fdismethod | 任务分配方式 | bpchar | 1 |  | √ | ' ' | 任务分配方式,枚举: 0 :手工分配 1 :自动分配 |
| 6 | ftaskduration | 任务期限（小时） | int8 | 64 |  | √ | 0 | 任务期限（小时） |
| 7 | ftimeframe | 时间范围类型 | varchar | 2 |  | √ | ' ' | 时间范围类型,枚举: 0 :昨日 1 :前2天 2 :前3天 3 :本周 4 :上周 5 :本月 6 :上月 7 :本年 8 :去年 9 :介于 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fenddate | 任务完成结束日期 | timestamp | 0 |  |  | null | 任务完成结束日期 |
| 11 | fsamplesize | 样本数（单）-弃用 | int8 | 64 |  | √ | 0 | 样本数（单）-弃用 |
| 12 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | ftaskbillcondiontion |  | text | 0 |  |  | null |  |
| 14 | fssccenterid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fwarningtime | 预警时间（小时） | int8 | 64 |  | √ | 0 | 预警时间（小时） |
| 17 | ftaskbill | 业务单据-弃用 | int8 | 64 |  | √ | 0 | [业务单据 task_taskbill](../ssc_files/task_taskbill.md) |
| 18 | fdescription | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 19 | fpercentage | 比例（%）-弃用 | int8 | 64 |  | √ | 0 | 比例（%）-弃用 |
| 20 | foperate | 操作 | varchar | 50 |  | √ | ' ' | 操作 |
| 21 | ftaskbillcondiontionjson |  | text | 0 |  |  | null |  |
| 22 | fsamplingmethod | 抽检方式 | bpchar | 1 |  | √ | ' ' | 抽检方式,枚举: 0 :按比例抽检 1 :按样本数抽检 |
| 23 | fstartdate | 任务完成起始日期 | timestamp | 0 |  |  | null | 任务完成起始日期 |
| 24 | fisrepeatsample | 重复抽取 | bpchar | 1 |  | √ | '1' | 重复抽取 |
| 25 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fdisrule | 任务分配规则 | bpchar | 1 |  | √ | '0' | 任务分配规则,枚举: 0 :按质检任务类型分配 1 :按原审单任务类型分配 |
| 27 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 28 | fqualitychecktasktype | 质检任务类型 | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_qltchktkbill_index |  | ftaskbill |
| 2 | t_tk_qualitycheckscheme_pkey |  | fid |

---

## 业务单据单据体-子表 t_tk_taskbillentry

- **表名称：** 业务单据单据体-子表
- **表名：** t_tk_taskbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsamplesize | 样本数（单） | int4 | 32 |  | √ | 0 | 样本数（单） |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcondition | 单据条件 | text | 0 |  |  | null | 单据条件 |
| 5 | ftaskbill | 业务单据 | int8 | 64 |  | √ | 0 | [业务单据 task_taskbill](../ssc_files/task_taskbill.md) |
| 6 | fconditionjson | 单据条件 | text | 0 |  |  | null | 单据条件 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fpercentage | 比例（%） | int4 | 32 |  | √ | 0 | 比例（%） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_taskbillentry |  | fentryid |
| 2 | idx_ssc_qctaskbillentry_fid |  | fid |

---

## 检查点单据体-子表 t_tk_cpentry

- **表名称：** 检查点单据体-子表
- **表名：** t_tk_cpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcpname | 名称 | int8 | 64 |  | √ | 0 | [质检点 task_checkingpoint](../som_files/task_checkingpoint.md) |
| 3 | fcpnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcpdescription | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_qualitycheckentry |  | fcpnumber |
| 2 | t_tk_cpentry_pkey |  | fentryid |

---

## 质检方案-多语言表 t_tk_qualitycheckscheme_l

- **表名称：** 质检方案-多语言表
- **表名：** t_tk_qualitycheckscheme_l

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
| 1 | index_ssc_qualitychecklang |  | fid,flocaleid |
| 2 | t_tk_qualitycheckscheme_l_pkey |  | fpkid |
