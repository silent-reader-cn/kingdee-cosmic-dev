# 处理意见-task_dealopinionsopen

## 左边单据体-子表 t_tk_opinionsopentype

- **表名称：** 左边单据体-子表
- **表名：** t_tk_opinionsopentype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftasktype | 任务类型 | int8 | 64 |  | √ | 0 | 任务类型 task_tasktype |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fbilltype | 业务单据 | int8 | 64 |  | √ | 0 | 业务单据 task_taskbill |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_opinionsopentype |  | fid |
| 2 | t_tk_opinionsopentype_pkey |  | fentryid |

---

## 处理意见-多语言表 t_tk_opinionsopen_l

- **表名称：** 处理意见-多语言表
- **表名：** t_tk_opinionsopen_l

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
| 1 | t_tk_opinionsopen_l_pkey |  | fpkid |
| 2 | index_ssc_opinionsopen_l |  | fid,flocaleid |

---

## 处理意见-使用范围位图表 t_tk_opinionsopen_m

- **表名称：** 处理意见-使用范围位图表
- **表名：** t_tk_opinionsopen_m

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
| 1 | pk_t_tk_opinionsopen_m |  | forgid |

---

## 处理意见-使用范围表 t_tk_opinionsopen_u

- **表名称：** 处理意见-使用范围表
- **表名：** t_tk_opinionsopen_u

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
| 1 | idx_t_tk_opinionsopen_u_uo |  | fuseorgid |
| 2 | pk_t_tk_opinionsopen_u |  | fdataid,fuseorgid |

---

## 处理意见-主表 t_tk_opinionsopen

- **表名称：** 处理意见-主表
- **表名：** t_tk_opinionsopen

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fbasetype | 业务单据隐藏 | int8 | 64 |  | √ | 0 | 业务单据 task_taskbill |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | ferp | 属于的系统 | varchar | 100 |  | √ | ' ' | 属于的系统 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fbindbillnum | 绑定单据编码 | varchar | 100 |  | √ | ' ' | 绑定单据编码 |
| 13 | fcreateorgid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fsscid | 共享中心-废弃 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fbindbillname | 绑定单据编码 | varchar | 100 |  | √ | ' ' | 绑定单据编码 |
| 19 | fdistemsionskey | 维度字段key | varchar | 100 |  | √ | ' ' | 维度字段key |
| 20 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 21 | fdistemsions | 自定义维度 | varchar | 100 |  | √ | ' ' | 自定义维度 |
| 22 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 24 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 25 | funiversalopinion | 通用处理意见 | varchar | 255 |  | √ | ' ' | 通用处理意见 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_opinionsopen_pkey |  | fid |
| 2 | idx_t_tk_opinionsopen_createorg |  | fcreateorgid |
| 3 | idx_t_tk_opinionsopen_master |  | fmasterid |
| 4 | index_ssc_opinionsopen |  | fnumber |

---

## 子单据体-子表 t_tk_opinionsopendis

- **表名称：** 子单据体-子表
- **表名：** t_tk_opinionsopendis

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | expenseitem | expenseitem | int8 | 64 |  | √ | 0 |  |
| 2 | ftriptype | 出差类型 | int8 | 64 |  | √ | 0 | 出差类型 er_triptype |
| 3 | fexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fopinion | 处理意见 | varchar | 510 |  | √ | ' ' | 处理意见 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fexpensetype | 费用类型 | int8 | 64 |  | √ | 0 | 费用类型 task_expensetype |
| 8 | fcoverids | 文本 | varchar | 100 |  | √ | ' ' | 文本 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fsubdistemsions | 自定义维度 | varchar | 100 |  | √ | ' ' | 自定义维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_opinionsopendis_pkey |  | fdetailid |
| 2 | index_ssc_opinionsopendis |  | fcoverids |
