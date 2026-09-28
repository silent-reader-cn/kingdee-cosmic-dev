# 智能质检方案-task_smartcheckscheme

## 质检点单据体-子表 t_tk_smartschemecpentry

- **表名称：** 质检点单据体-子表
- **表名：** t_tk_smartschemecpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcpnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 3 | fcpname | 名称 | int8 | 64 |  | √ | 0 | [质检点 task_checkingpoint](../som_files/task_checkingpoint.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcpdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_smartqualmsgentry |  | fid |
| 2 | pk_t_tk_smartschemecpentry |  | fentryid |

---

## 智能质检方案-主表 t_tk_smartcheckscheme

- **表名称：** 智能质检方案-主表
- **表名：** t_tk_smartcheckscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexecutemode | 自动执行方式 | bpchar | 1 |  | √ | 'n' | 自动执行方式,枚举: w :每周 m :每月 y :每年 n :不自动执行 |
| 3 | fisautoprocess | 审批类型 | bpchar | 1 |  | √ | '0' | 审批类型,枚举: 0 :人工审批 1 :自动审批 2 :所有任务 |
| 4 | fdismethod | 任务分配方式 | bpchar | 1 |  | √ | ' ' | 任务分配方式,枚举: 0 :手工分配 1 :自动分配 |
| 5 | ftaskduration | 任务期限（小时） | int8 | 64 |  | √ | 0 | 任务期限（小时） |
| 6 | ftimeframe | 时间范围类型 | varchar | 2 |  | √ | ' ' | 时间范围类型,枚举: 0 :昨日 1 :前2天 2 :前3天 3 :本周 4 :上周 5 :本月 6 :上月 7 :本年 8 :去年 9 :介于 |
| 7 | fweek | 周 | varchar | 100 |  | √ | ' ' | 周,枚举: 2 :周一 3 :周二 4 :周三 5 :周四 6 :周五 7 :周六 1 :周日 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fmonth | 月 | varchar | 100 |  | √ | ' ' | 月,枚举: 1 :一月 2 :二月 3 :三月 4 :四月 5 :五月 6 :六月 7 :七月 8 :八月 9 :九月 10 :十月 11 :十一月 12 :十二月 |
| 14 | fdate | 日 | varchar | 100 |  | √ | ' ' | 日,枚举: 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 13 :13 14 :14 15 :15 16 :16 17 :17 18 :18 19 :19 20 :20 21 :21 22 :22 23 :23 24 :24 25 :25 26 :26 27 :27 28 :28 29 :29 30 :30 31 :31 |
| 15 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | freformrate | 整改率预警比例（%） | int8 | 64 |  | √ | 0 | 整改率预警比例（%） |
| 18 | fsamplesize | 样本数（单） | int8 | 64 |  | √ | 0 | 样本数（单） |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fwarningtime | 预警时间（小时） | int8 | 64 |  | √ | 0 | 预警时间（小时） |
| 21 | fdescription | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 22 | fpercentage | 比例（%） | int8 | 64 |  | √ | 0 | 比例（%） |
| 23 | fsamplingmethod | 抽检方式 | bpchar | 1 |  | √ | ' ' | 抽检方式,枚举: 0 :按比例抽检 1 :按样本数抽检 |
| 24 | fstartdate | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 25 | fisrepeatsample | 重复抽取 | bpchar | 1 |  | √ | '0' | 重复抽取 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fdisrule | 任务分配规则 | bpchar | 1 |  | √ | ' ' | 任务分配规则,枚举: 0 :按质检任务类型分配 1 :按原审单任务类型分配 |
| 28 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 29 | fqualitychecktasktype | 质检任务类型 | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_smartchecksch_fsscid |  | fsscid |
| 2 | pk_t_tk_smartcheckscheme |  | fid |

---

## 抽选组织-多选基础资料表 t_tk_smartschemeorg

- **表名称：** 抽选组织-多选基础资料表
- **表名：** t_tk_smartschemeorg

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
| 1 | pk_t_tk_smartschemeorg |  | fpkid |
| 2 | index_ssc_smartselectedorg |  | fbasedataid |

---

## 智能质检方案-多语言表 t_tk_smartcheckscheme_l

- **表名称：** 智能质检方案-多语言表
- **表名：** t_tk_smartcheckscheme_l

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
| 1 | pk_t_tk_smartcheckscheme_l |  | fpkid |
| 2 | index_ssc_smartchecksch_l_fid |  | fid,flocaleid |

---

## 业务单据-多选基础资料表 t_tk_smartschemetaskbill

- **表名称：** 业务单据-多选基础资料表
- **表名：** t_tk_smartschemetaskbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单据 task_taskbill](../ssc_files/task_taskbill.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_smartbilltype |  | fbasedataid |
| 2 | pk_t_tk_smartschemetaskbill |  | fpkid |

---

## 任务类型-多选基础资料表 t_tk_smartschemetasktype

- **表名称：** 任务类型-多选基础资料表
- **表名：** t_tk_smartschemetasktype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_smarttasktype |  | fbasedataid |
| 2 | pk_t_tk_smartschemetasktype |  | fpkid |
