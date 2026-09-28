# 巡检计划-cal_datacheck_plan

## 物料版本-多选基础资料表 t_cal_cplan_mversion

- **表名称：** 物料版本-多选基础资料表
- **表名：** t_cal_cplan_mversion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_cplan_mversion_pkey |  | fpkid |
| 2 | idx_cal_cplan_mversion_fid |  | fid |

---

## 仓位-多选基础资料表 t_cal_cplan_location

- **表名称：** 仓位-多选基础资料表
- **表名：** t_cal_cplan_location

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_cplan_location_pkey |  | fpkid |
| 2 | idx_cal_cplan_location_fid |  | fid |

---

## 成本主体-多选基础资料表 t_cal_cplan_costaccount

- **表名称：** 成本主体-多选基础资料表
- **表名：** t_cal_cplan_costaccount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_cplan_costaccount_pkey |  | fpkid |
| 2 | idx_cal_cplan_cact_fid |  | fid |

---

## 库存组织-多选基础资料表 t_cal_cplan_storageorg

- **表名称：** 库存组织-多选基础资料表
- **表名：** t_cal_cplan_storageorg

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
| 1 | t_cal_cplan_storageorg_pkey |  | fpkid |
| 2 | idx_cal_cplan_sorg_fid |  | fid |

---

## 库存状态-多选基础资料表 t_cal_cplan_invstatus

- **表名称：** 库存状态-多选基础资料表
- **表名：** t_cal_cplan_invstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_cplan_invstatus_pkey |  | fpkid |
| 2 | idx_cal_cplan_invstatus_fid |  | fid |

---

## 物料-多选基础资料表 t_cal_cplan_material

- **表名称：** 物料-多选基础资料表
- **表名：** t_cal_cplan_material

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_cplan_material_pkey |  | fpkid |
| 2 | idx_cal_cplan_material_fid |  | fid |

---

## 库存类型-多选基础资料表 t_cal_cplan_invtype

- **表名称：** 库存类型-多选基础资料表
- **表名：** t_cal_cplan_invtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_cplan_invtype_fid |  | fid |
| 2 | t_cal_cplan_invtype_pkey |  | fpkid |

---

## 核算组织-多选基础资料表 t_cal_cplan_calorg

- **表名称：** 核算组织-多选基础资料表
- **表名：** t_cal_cplan_calorg

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
| 1 | t_cal_cplan_calorg_pkey |  | fpkid |
| 2 | idx_cal_cplan_calorg_fid |  | fid |

---

## 项目号-多选基础资料表 t_cal_cplan_project

- **表名称：** 项目号-多选基础资料表
- **表名：** t_cal_cplan_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_cplan_project_fid |  | fid |
| 2 | t_cal_cplan_project_pkey |  | fpkid |

---

## 巡检计划-主表 t_cal_datacheck_plan

- **表名称：** 巡检计划-主表
- **表名：** t_cal_datacheck_plan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fscheduleid | 调度计划 | varchar | 36 |  | √ | ' ' | [调度计划 sch_schedule](../sys_files/sch_schedule.md) |
| 4 | fjobid | 调度作业 | varchar | 36 |  | √ | ' ' | [调度作业 sch_job](../sys_files/sch_job.md) |
| 5 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 1 :启用 0 :禁用 |
| 6 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 7 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 8 | fchecktaskid | 检查任务 | int8 | 64 |  | √ | 0 | [检查任务 cal_datacheck_task](../cal_files/cal_datacheck_task.md) |
| 9 | fstarttime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 10 | fplan | cron表达式 | varchar | 300 |  | √ | ' ' | cron表达式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_chplan_no |  | fnumber |
| 2 | t_cal_datacheck_plan_pkey |  | fid |

---

## 仓库-多选基础资料表 t_cal_cplan_warehouse

- **表名称：** 仓库-多选基础资料表
- **表名：** t_cal_cplan_warehouse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_cplan_warehouse_pkey |  | fpkid |
| 2 | idx_cal_cplan_whouse_fid |  | fid |

---

## 巡检计划-多语言表 t_cal_datacheck_plan_l

- **表名称：** 巡检计划-多语言表
- **表名：** t_cal_datacheck_plan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_chplan_l_fid |  | fid |
| 2 | t_cal_datacheck_plan_l_pkey |  | fpkid |

---

## 巡检计划-使用范围位图表 t_cal_datacheck_plan_m

- **表名称：** 巡检计划-使用范围位图表
- **表名：** t_cal_datacheck_plan_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwed | 星期三 | bpchar | 1 |  | √ | ' ' | 星期三 |
| 3 | fbydayorweek | 按日期或星期 | bpchar | 1 |  | √ | ' ' | 按日期或星期,枚举: d :日期 w :星期 |
| 4 | ftues | 星期二 | bpchar | 1 |  | √ | ' ' | 星期二 |
| 5 | fmar | 三月 | bpchar | 1 |  | √ | ' ' | 三月 |
| 6 | fsep | 九月 | bpchar | 1 |  | √ | ' ' | 九月 |
| 7 | foct | 十月 | bpchar | 1 |  | √ | ' ' | 十月 |
| 8 | fmay | 五月 | bpchar | 1 |  | √ | ' ' | 五月 |
| 9 | fapr | 四月 | bpchar | 1 |  | √ | ' ' | 四月 |
| 10 | fsun | 星期日 | bpchar | 1 |  | √ | ' ' | 星期日 |
| 11 | fmon | 星期一 | bpchar | 1 |  | √ | ' ' | 星期一 |
| 12 | ffri | 星期五 | bpchar | 1 |  | √ | ' ' | 星期五 |
| 13 | fjan | 一月 | bpchar | 1 |  | √ | ' ' | 一月 |
| 14 | fnov | 十一月 | bpchar | 1 |  | √ | ' ' | 十一月 |
| 15 | fnoweek | 星期几 | bpchar | 2 |  | √ | ' ' | 星期几,枚举: 1 :星期日 2 :星期一 3 :星期二 4 :星期三 5 :星期四 6 :星期五 7 :星期六 8 :自然日 9 :工作日 |
| 16 | faug | 八月 | bpchar | 1 |  | √ | ' ' | 八月 |
| 17 | fthur | 星期四 | bpchar | 1 |  | √ | ' ' | 星期四 |
| 18 | fbyweek | 星期 | bpchar | 1 |  | √ | ' ' | 星期 |
| 19 | fno | 第几个 | bpchar | 2 |  | √ | ' ' | 第几个,枚举: 1 :第一个 2 :第二个 3 :第三个 4 :第四个 5 :第五个 L :最后一个 |
| 20 | frepeatmode | 重复周期 | varchar | 10 |  | √ | ' ' | 重复周期,枚举: n :不重复 mi :每分钟 h :每小时 d :日期 w :星期 m :每月 y :每年 |
| 21 | fsat | 星期六 | bpchar | 1 |  | √ | ' ' | 星期六 |
| 22 | ffeb | 二月 | bpchar | 1 |  | √ | ' ' | 二月 |
| 23 | fjun | 六月 | bpchar | 1 |  | √ | ' ' | 六月 |
| 24 | fdec | 十二月 | bpchar | 1 |  | √ | ' ' | 十二月 |
| 25 | fjul | 七月 | bpchar | 1 |  | √ | ' ' | 七月 |
| 26 | fdesc | 调度计划示例 | varchar | 225 |  | √ | ' ' | 调度计划示例 |
| 27 | fcyclenum | 重复频率 | int8 | 64 |  | √ | 0 | 重复频率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_datacheck_plan_m_pkey |  | fid |

---

## 巡检计划-分表 t_cal_datacheck_plan_d

- **表名称：** 巡检计划-分表
- **表名：** t_cal_datacheck_plan_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftwentynine | 29 | bpchar | 1 |  | √ | ' ' | 29 |
| 3 | ffour | 04 | bpchar | 1 |  | √ | ' ' | 04 |
| 4 | ftwentytwo | 22 | bpchar | 1 |  | √ | ' ' | 22 |
| 5 | ftwentyeight | 28 | bpchar | 1 |  | √ | ' ' | 28 |
| 6 | ffifteen | 15 | bpchar | 1 |  | √ | ' ' | 15 |
| 7 | ften | 10 | bpchar | 1 |  | √ | ' ' | 10 |
| 8 | fnine | 09 | bpchar | 1 |  | √ | ' ' | 09 |
| 9 | ftwentythree | 23 | bpchar | 1 |  | √ | ' ' | 23 |
| 10 | ftwentyseven | 27 | bpchar | 1 |  | √ | ' ' | 27 |
| 11 | fsix | 06 | bpchar | 1 |  | √ | ' ' | 06 |
| 12 | ftwentyfive | 25 | bpchar | 1 |  | √ | ' ' | 25 |
| 13 | fthirtyone | 31 | bpchar | 1 |  | √ | ' ' | 31 |
| 14 | fthirty | 30 | bpchar | 1 |  | √ | ' ' | 30 |
| 15 | feleven | 11 | bpchar | 1 |  | √ | ' ' | 11 |
| 16 | fenddate | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 17 | ffive | 05 | bpchar | 1 |  | √ | ' ' | 05 |
| 18 | ftwelve | 12 | bpchar | 1 |  | √ | ' ' | 12 |
| 19 | ffourteen | 14 | bpchar | 1 |  | √ | ' ' | 14 |
| 20 | fseventeen | 17 | bpchar | 1 |  | √ | ' ' | 17 |
| 21 | ftwo | 02 | bpchar | 1 |  | √ | ' ' | 02 |
| 22 | fthree | 03 | bpchar | 1 |  | √ | ' ' | 03 |
| 23 | fnineteen | 19 | bpchar | 1 |  | √ | ' ' | 19 |
| 24 | fthirteen | 13 | bpchar | 1 |  | √ | ' ' | 13 |
| 25 | feight | 08 | bpchar | 1 |  | √ | ' ' | 08 |
| 26 | fone | 01 | bpchar | 1 |  | √ | ' ' | 01 |
| 27 | fsixteen | 16 | bpchar | 1 |  | √ | ' ' | 16 |
| 28 | fseven | 07 | bpchar | 1 |  | √ | ' ' | 07 |
| 29 | fstartdate | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 30 | ftwentyone | 21 | bpchar | 1 |  | √ | ' ' | 21 |
| 31 | ftwentyfour | 24 | bpchar | 1 |  | √ | ' ' | 24 |
| 32 | feighteen | 18 | bpchar | 1 |  | √ | ' ' | 18 |
| 33 | ftwentysix | 26 | bpchar | 1 |  | √ | ' ' | 26 |
| 34 | ftwenty | 20 | bpchar | 1 |  | √ | ' ' | 20 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_datacheck_plan_d_pkey |  | fid |
