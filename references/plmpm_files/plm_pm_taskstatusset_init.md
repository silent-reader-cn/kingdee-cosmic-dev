# 任务状态设置初始化配置-plm_pm_taskstatusset_init

## 任务状态设置初始化配置-主表 t_plm_pm_taskset_init

- **表名称：** 任务状态设置初始化配置-主表
- **表名：** t_plm_pm_taskset_init

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | ffromstatus | 源状态 | int8 | 64 |  | √ | 0 | 任务状态 plm_pm_taskstatus |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fstatusseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fname | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 18 | fbindopt | 对应操作 | varchar | 50 |  | √ | ' ' | 对应操作 |
| 19 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | foptmodel | 操作方式 | bpchar | 1 |  | √ | '0' | 操作方式 |
| 21 | fismainline | 是否主线连接点 | bpchar | 1 |  | √ | '0' | 是否主线连接点 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | ftostatus | 目标状态 | int8 | 64 |  | √ | 0 | 任务状态 plm_pm_taskstatus |
| 24 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 25 | fisshow | 是否初始显示 | bpchar | 1 |  | √ | '0' | 是否初始显示 |
| 26 | fischeck | 是否勾选 | bpchar | 1 |  | √ | '0' | 是否勾选 |
| 27 | fhasopt | 是否有操作 | bpchar | 1 |  | √ | '0' | 是否有操作 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_taskset_init |  | fid |
| 2 | idx_t_plm_pm_taskset_init_master |  | fmasterid |
| 3 | idx_plm_pm_taskset_init_m0 |  | fmasterid |
| 4 | idx_t_plm_pm_taskset_init_createorg |  | fcreateorgid |

---

## 任务状态设置初始化配置-使用范围表 t_plm_pm_taskset_init_u

- **表名称：** 任务状态设置初始化配置-使用范围表
- **表名：** t_plm_pm_taskset_init_u

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
| 1 | pk_t_plm_pm_taskset_init_u |  | fdataid,fuseorgid |
| 2 | idx_t_plm_pm_taskset_init_u_uo |  | fuseorgid |

---

## 任务状态设置初始化配置-多语言表 t_plm_pm_taskset_init_l

- **表名称：** 任务状态设置初始化配置-多语言表
- **表名：** t_plm_pm_taskset_init_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_taskset_init_l |  | fpkid |
| 2 | idx_plm_pm_taskset_init_l_0 |  | fid,flocaleid |
