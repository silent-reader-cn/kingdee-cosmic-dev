# 计划模拟运算日志-mrp_simcaculate_log

## 计划模拟运算日志-多语言表 t_mrp_simcaculatelog_l

- **表名称：** 计划模拟运算日志-多语言表
- **表名：** t_mrp_simcaculatelog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_simcaculatelog_l_lid |  | fid,flocaleid |
| 2 | pk_mrp_simcaculatelog_l |  | fpkid |

---

## 计划模拟运算日志-使用范围表 t_mrp_simcaculatelog_u

- **表名称：** 计划模拟运算日志-使用范围表
- **表名：** t_mrp_simcaculatelog_u

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
| 1 | idx_t_mrp_simcaculatelog_u_uo |  | fuseorgid |
| 2 | pk_t_mrp_simcaculatelog_u |  | fdataid,fuseorgid |

---

## 计划模拟运算日志-主表 t_mrp_simcaculatelog

- **表名称：** 计划模拟运算日志-主表
- **表名：** t_mrp_simcaculatelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanprogamid | 计划方案ID | int8 | 64 |  | √ | 0 | 计划方案ID |
| 3 | fistoformal | 模拟计划转正式 | bpchar | 1 |  | √ | '0' | 模拟计划转正式 |
| 4 | fclearstatus | 清理状态 | varchar | 30 |  | √ | ' ' | 清理状态,枚举: A :未清理 B :已清理 |
| 5 | fplangramentity | 计划方案实体标识 | varchar | 50 |  | √ | ' ' | 计划方案实体标识 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmachineid | 运算机器ID | varchar | 50 |  | √ | ' ' | 运算机器ID |
| 8 | fcalculatepro | 计算进度 | numeric | 23 | 10 | √ | 0 | 计算进度 |
| 9 | fprogramnumber | 计划方案编码 | varchar | 50 |  |  | null | 计划方案编码 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fisallowdateinpast | 允许计划订单开始日期在过去 | bpchar | 1 |  | √ | '0' | 允许计划订单开始日期在过去 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 15 | fsummin | 计算总时长（分钟） | numeric | 23 | 10 | √ | 0 | 计算总时长（分钟） |
| 16 | fiscustomize | 定制 | bpchar | 1 |  | √ | '0' | 定制 |
| 17 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 20 | fplandate | 计划日期 | timestamp | 0 |  |  | null | 计划日期 |
| 21 | fheartbeattime | 心跳时间(30秒更新一次) | timestamp | 0 |  |  | null | 心跳时间(30秒更新一次) |
| 22 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 23 | fisllc | 重算低位码 | bpchar | 1 |  | √ | '0' | 重算低位码 |
| 24 | fisnotsetup | 未设置 | bpchar | 1 |  | √ | '0' | 未设置 |
| 25 | fcreateorgid | 计划组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 27 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fbomcheckresult | BOM嵌套检查结果 | varchar | 255 |  | √ | ' ' | BOM嵌套检查结果 |
| 29 | fmrpid | MRP计算实例ID | varchar | 50 |  | √ | ' ' | MRP计算实例ID |
| 30 | fcalculatestatus | 计算状态 | varchar | 100 |  | √ | ' ' | 计算状态,枚举: A :正常结束 B :异常终止 C :手工终止 D :运行中 |
| 31 | frecaluteresult | 重算低位码结果 | varchar | 255 |  | √ | ' ' | 重算低位码结果 |
| 32 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | fprogramname | 计划方案名称 | varchar | 50 |  |  | null | 计划方案名称 |
| 34 | fismpsonly | 只算MPS | bpchar | 1 |  | √ | '0' | 只算MPS |
| 35 | foperatmode | 运行方式 | varchar | 50 |  | √ | ' ' | 运行方式 |
| 36 | fheartbeat | 心跳检测 | varchar | 4 |  | √ | ' ' | 心跳检测,枚举: 0 :检测未开始 1 :心跳正常 2 :心跳异常终止 3 :已完成 |
| 37 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 38 | fiscommon | 通用 | bpchar | 1 |  | √ | '0' | 通用 |
| 39 | fdataversion | 数据版本定义 | int8 | 64 |  | √ | 0 | [数据版本 msplan_ds_version](../msplan_files/msplan_ds_version.md) |
| 40 | fstartdate | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 41 | fruntype | 运算类型 | varchar | 30 |  | √ | ' ' | 运算类型,枚举: A :标准MRP B :预算MRP P :项目MRP S :模拟MRP |
| 42 | fisselection | 选配 | bpchar | 1 |  | √ | '0' | 选配 |
| 43 | foperatmodekey | 运行方式标识 | varchar | 50 |  | √ | ' ' | 运行方式标识 |
| 44 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 45 | fplantype | 计划类型 | varchar | 255 |  | √ | ' ' | 计划类型 |
| 46 | fnumber | 计划运算号 | varchar | 30 |  | √ | ' ' | 计划运算号 |
| 47 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 48 | fisbomcheck | BOM嵌套检查 | bpchar | 1 |  | √ | '0' | BOM嵌套检查 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mrp_simcaculatelog_master |  | fmasterid |
| 2 | idx_t_mrp_simcaculatelog_createorg |  | fcreateorgid |
| 3 | idx_mrp_simcaculatelog_fnumber |  | fnumber |
| 4 | pk_mrp_simcaculatelog |  | fid |

---

## 计划标识-多选基础资料表 t_mrp_caculatelog_tag

- **表名称：** 计划标识-多选基础资料表
- **表名：** t_mrp_caculatelog_tag

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [计划标识 mpdm_plantag](../mpdm_files/mpdm_plantag.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_caculatelog_tag |  | fpkid |
| 2 | idx_mrp_cac_tag_fid |  | fid |

---

## 单据体-子表 t_mrp_simcaculatelogentry

- **表名称：** 单据体-子表
- **表名：** t_mrp_simcaculatelogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdetailmsg_tag | 详细信息_详情 | text | 0 |  |  | null | 详细信息_详情 |
| 3 | fprocessdata | 处理数据量 | int8 | 64 |  | √ | 0 | 处理数据量 |
| 4 | fdetailmsg | 详细信息 | varchar | 255 |  | √ | ' ' | 详细信息 |
| 5 | foperatmin | 运行时间（分钟） | numeric | 23 | 10 | √ | 0 | 运行时间（分钟） |
| 6 | fstepseq | 步骤顺序 | varchar | 50 |  | √ | ' ' | 步骤顺序 |
| 7 | fstepname | 步骤名称 | varchar | 500 |  | √ | ' ' | 步骤名称 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fresult | 运行结果 | varchar | 50 |  | √ | ' ' | 运行结果 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_simcaculateloge_fid |  | fid |
| 2 | pk_mrp_simcaculatelogentry |  | fentryid |
