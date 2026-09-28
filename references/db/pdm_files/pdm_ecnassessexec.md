# 工程变更评估运算-pdm_ecnassessexec

## 运算日志-子表 t_pdm_ecnassexecentry

- **表名称：** 运算日志-子表
- **表名：** t_pdm_ecnassexecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocessdata | 处理数据量 | int8 | 64 |  | √ | 0 | 处理数据量 |
| 3 | fdetailmsg | 详细信息 | varchar | 1000 |  | √ | ' ' | 详细信息 |
| 4 | foperatmin | 运行时间（秒） | numeric | 23 | 10 | √ | 0 | 运行时间（秒） |
| 5 | fstepseq | 步骤顺序 | varchar | 50 |  | √ | ' ' | 步骤顺序 |
| 6 | fstepname | 步骤名称 | varchar | 200 |  | √ | ' ' | 步骤名称 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fresult | 运行结果 | varchar | 200 |  | √ | ' ' | 运行结果 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_ecnassexecentry |  | fentryid |
| 2 | idx_pdm_ecnassexecentry_id |  | fid |

---

## 工程变更评估运算-使用范围表 t_pdm_ecnassessexec_u

- **表名称：** 工程变更评估运算-使用范围表
- **表名：** t_pdm_ecnassessexec_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pdm_ecnassessexec_u |  | fdataid,fuseorgid |
| 2 | idx_t_pdm_ecnassessexec_u_uo |  | fuseorgid |

---

## 工程变更评估运算-多语言表 t_pdm_ecnassessexec_l

- **表名称：** 工程变更评估运算-多语言表
- **表名：** t_pdm_ecnassessexec_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_ecnassessexec_l_fid |  | fid,flocaleid |
| 2 | pk_pdm_ecnassessexec_l |  | fpkid |

---

## 工程变更评估运算-使用范围位图表 t_pdm_ecnassessexec_m

- **表名称：** 工程变更评估运算-使用范围位图表
- **表名：** t_pdm_ecnassessexec_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pdm_ecnassessexec_m |  | forgid |

---

## 工程变更评估运算-主表 t_pdm_ecnassessexec

- **表名称：** 工程变更评估运算-主表
- **表名：** t_pdm_ecnassessexec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstime | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsourceid | fsourceid | int8 | 64 |  | √ | 0 |  |
| 5 | fcalculatepro | 计算进度 | numeric | 23 | 10 | √ | 0 | 计算进度 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fplanid | 供应单据类型 | varchar | 50 |  | √ | ' ' | 供应单据类型 |
| 9 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fsummin | 计算总时长（秒） | numeric | 23 | 10 | √ | 0 | 计算总时长（秒） |
| 11 | faccstatus | 任务状态 | varchar | 5 |  | √ | ' ' | 任务状态,枚举: A :暂存 B :计划 C :终止 D :关闭 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fmrplogid | MRP运算日志 | int8 | 64 |  | √ | 0 | [运算日志 mrp_caculate_log](../msplan_files/mrp_caculate_log.md) |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fetime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fjobid | 调整建议 | varchar | 50 |  | √ | ' ' | 调整建议 |
| 23 | fbussid | MRP业务方案 | int8 | 64 |  | √ | 0 | [业务方案配置 mrp_businessplan](../msplan_files/mrp_businessplan.md) |
| 24 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fexecstatus | 执行状态 | varchar | 5 |  | √ | ' ' | 执行状态,枚举: A :未开始 B :错误 C :终止 D :完成 E :执行中 |
| 26 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 28 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 29 | fprogramid | MRP计划方案 | int8 | 64 |  | √ | 0 | [计划方案定义(作废) mrp_planprogram](../msplan_files/mrp_planprogram.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_ecnassessexec_no |  | fnumber |
| 2 | idx_t_pdm_ecnassessexec_master |  | fmasterid |
| 3 | pk_pdm_ecnassessexec |  | fid |
| 4 | idx_t_pdm_ecnassessexec_createorg |  | fcreateorgid |
