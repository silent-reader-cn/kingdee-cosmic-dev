# 任务量系数-task_taskquantcoefficient

## 任务量系数-主表 t_tk_taskquantcoefficient

- **表名称：** 任务量系数-主表
- **表名：** t_tk_taskquantcoefficient

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fbasetype | 业务单据隐藏 | int8 | 64 |  | √ | 0 | [业务单据 task_taskbill](../ssc_files/task_taskbill.md) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | ferp | 属于的系统 | varchar | 100 |  | √ | ' ' | 属于的系统 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fbindbillnum | 绑定单据编码 | varchar | 100 |  | √ | ' ' | 绑定单据编码 |
| 13 | fcoefficientshead | 标准系数 | numeric | 23 | 10 | √ | 0.0000000000 | 标准系数 |
| 14 | fcreateorgid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fssccenterid | 共享中心-废弃 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fbindbillname | 绑定单据名称 | varchar | 100 |  | √ | ' ' | 绑定单据名称 |
| 20 | fdistemsionskey | 维度字段key | varchar | 100 |  | √ | ' ' | 维度字段key |
| 21 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | '1' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fdistemsions | 自定义维度 | varchar | 100 |  | √ | ' ' | 自定义维度 |
| 23 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 25 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tk_taskquantcoefficient_createorg |  | fcreateorgid |
| 2 | index_ssc_taskquantcoeffcient |  | fcoefficientshead |
| 3 | t_tk_taskquantcoefficient_pkey |  | fid |
| 4 | idx_t_tk_taskquantcoefficient_master |  | fmasterid |

---

## 任务量系数-使用范围位图表 t_tk_taskquantcoefficient_m

- **表名称：** 任务量系数-使用范围位图表
- **表名：** t_tk_taskquantcoefficient_m

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
| 1 | pk_t_tk_taskquantcoefficient_m |  | forgid |

---

## 任务量系数-多语言表 t_tk_taskquantcoefficient_l

- **表名称：** 任务量系数-多语言表
- **表名：** t_tk_taskquantcoefficient_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_taskquantcoefficient |  | fid,flocaleid |
| 2 | t_tk_taskquantcoefficient_l_pkey |  | fpkid |

---

## 任务量系数-使用范围表 t_tk_taskquantcoefficient_u

- **表名称：** 任务量系数-使用范围表
- **表名：** t_tk_taskquantcoefficient_u

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
| 1 | pk_t_tk_taskquantcoefficient_u |  | fdataid,fuseorgid |
| 2 | idx_t_tk_taskquantcoefficient_u_uo |  | fuseorgid |

---

## 子单据体-子表 t_tk_taskquantitydetail

- **表名称：** 子单据体-子表
- **表名：** t_tk_taskquantitydetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftriptype | ftriptype | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitem | fexpenseitem | int8 | 64 |  | √ | 0 |  |
| 3 | fratioid | 因子id | varchar | 50 |  | √ | ' ' | 因子id |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fexpensetype | fexpensetype | int8 | 64 |  | √ | 0 |  |
| 7 | fcoverids | fcoverids | varchar | 100 |  | √ | ' ' |  |
| 8 | fcoefficientssub | 任务量系数 | numeric | 23 | 10 | √ | 0.0000000000 | 任务量系数 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | ftaskratio | 任务量系数决定因子 | varchar | 50 |  | √ | ' ' | 任务量系数决定因子 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_taskquantitydetail_pkey |  | fdetailid |
| 2 | index_ssc_taskquantitydetail |  | fcoverids |

---

## 单据体-子表 t_tk_taskquantitytype

- **表名称：** 单据体-子表
- **表名：** t_tk_taskquantitytype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftasktype | 任务类型 | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fbilltype | 业务单据 | int8 | 64 |  | √ | 0 | [业务单据 task_taskbill](../ssc_files/task_taskbill.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_taskquantitytype_pkey |  | fentryid |
| 2 | index_ssc_taskqualitytype |  | fid |
