# 运算日志-mrp_caculate_log

## 单据体-子表 t_mrp_caculatelogentry

- **表名称：** 单据体-子表
- **表名：** t_mrp_caculatelogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdetailmsg_tag | 详细信息_详情 | text | 0 |  |  | ' ' | 详细信息_详情 |
| 3 | fprocessdata | 处理数据量 | int8 | 64 |  | √ | 0 | 处理数据量 |
| 4 | fdetailmsg | 详细信息 | varchar | 255 |  | √ | ' ' | 详细信息 |
| 5 | foperatmin | 运行时间（分钟） | numeric | 23 | 10 | √ | 0.0000000000 | 运行时间（分钟） |
| 6 | fstepseq | 步骤顺序 | varchar | 50 |  | √ | ' ' | 步骤顺序 |
| 7 | fstepname | 步骤名称 | varchar | 200 |  | √ | ' ' | 步骤名称 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fresult | 运行结果 | varchar | 50 |  | √ | ' ' | 运行结果 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_caculatelogentry |  | fentryid |
| 2 | idx_mrp_caculatelogentry |  | fid,fseq |

---

## 运算日志-主表 t_mrp_caculatelog

- **表名称：** 运算日志-主表
- **表名：** t_mrp_caculatelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanprogamid | 计划方案ID | int8 | 64 |  | √ | 0 | 计划方案ID |
| 3 | fistoformal | 模拟计划转正式 | bpchar | 1 |  | √ | '0' | 模拟计划转正式 |
| 4 | fclearstatus | 清理状态 | varchar | 30 |  | √ | 'A' | 清理状态,枚举: A :未清理 B :已清理 |
| 5 | fplangramentity | 计划方案实体标识 | varchar | 60 |  | √ | ' ' | 计划方案实体标识 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmachineid | 运算机器ID | varchar | 50 |  | √ | ' ' | 运算机器ID |
| 8 | fcalculatepro | 计算进度 | numeric | 23 | 10 | √ | 0.0000000000 | 计算进度 |
| 9 | fprogramnumber | 计划方案编码 | varchar | 60 |  | √ | ' ' | 计划方案编码 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fisallowdateinpast | 允许计划订单开始日期在过去 | bpchar | 1 |  | √ | '0' | 允许计划订单开始日期在过去 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 15 | fsummin | 计算总时长（分钟） | numeric | 23 | 10 | √ | 0.0000000000 | 计算总时长（分钟） |
| 16 | fiscustomize | 定制 | bpchar | 1 |  | √ | '0' | 定制 |
| 17 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fplandate | 计划日期 | timestamp | 0 |  |  | null | 计划日期 |
| 20 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 21 | fisllc | 重算低位码 | bpchar | 1 |  | √ | '0' | 重算低位码 |
| 22 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 23 | fisnotsetup | 未设置 | bpchar | 1 |  | √ | '0' | 未设置 |
| 24 | fcreateorgid | 计划组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fbomcheckresult | BOM嵌套检查结果 | varchar | 255 |  | √ | ' ' | BOM嵌套检查结果 |
| 27 | fmrpid | MRP计算实例ID | varchar | 255 |  | √ | ' ' | MRP计算实例ID |
| 28 | fcalculatestatus | 计算状态 | varchar | 100 |  | √ | ' ' | 计算状态,枚举: A :正常结束 B :异常终止 C :手工终止 D :运行中 |
| 29 | frecaluteresult | 重算低位码结果 | varchar | 255 |  | √ | ' ' | 重算低位码结果 |
| 30 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 31 | fprogramname | 计划方案名称 | varchar | 60 |  | √ | ' ' | 计划方案名称 |
| 32 | fismpsonly | 只算MPS | bpchar | 1 |  | √ | '0' | 只算MPS |
| 33 | foperatmode | 运行方式 | varchar | 255 |  | √ | ' ' | 运行方式 |
| 34 | fplsschemeid | fplsschemeid | int8 | 64 |  | √ | 0 |  |
| 35 | fplantag | fplantag | varchar | 255 |  | √ | ' ' |  |
| 36 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 37 | fiscommon | 通用 | bpchar | 1 |  | √ | '0' | 通用 |
| 38 | fdataversion | 数据版本定义 | int8 | 64 |  | √ | 0 | 数据版本 msplan_ds_version |
| 39 | fstartdate | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 40 | fruntype | 运算类型 | varchar | 30 |  | √ | ' ' | 运算类型,枚举: A :MRP B :齐套计划 C :调拨计划 D :计划齐套 E :交货计划 F :库存计划 H :资源计划 I :资源评估 P :产线排程 |
| 41 | fisselection | 选配 | bpchar | 1 |  | √ | '0' | 选配 |
| 42 | foperatmodekey | 运行方式标识 | varchar | 255 |  | √ | ' ' | 运行方式标识 |
| 43 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 44 | fplantype | 计划类型 | varchar | 255 |  | √ | ' ' | 计划类型 |
| 45 | fnumber | 计划运算号 | varchar | 30 |  | √ | ' ' | 计划运算号 |
| 46 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 47 | fisbomcheck | BOM嵌套检查 | bpchar | 1 |  | √ | '0' | BOM嵌套检查 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_caculatelog |  | fid |
| 2 | idx_t_mrp_caculatelog_createorg |  | fcreateorgid |
| 3 | idx_t_mrp_caculatelog_master |  | fmasterid |
| 4 | idx_mrp_caculatelog_fnumber |  | fnumber,fcreateorgid |

---

## 运算日志-使用范围表 t_mrp_caculatelog_u

- **表名称：** 运算日志-使用范围表
- **表名：** t_mrp_caculatelog_u

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
| 1 | t_mrp_caculatelog_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_mrp_caculatelog_u_uo |  | fuseorgid |

---

## 计划标识-多选基础资料表 t_mrp_caculatelog_tag

- **表名称：** 计划标识-多选基础资料表
- **表名：** t_mrp_caculatelog_tag

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 计划标识 mpdm_plantag |
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

## 运算日志-使用范围位图表 t_mrp_caculatelog_m

- **表名称：** 运算日志-使用范围位图表
- **表名：** t_mrp_caculatelog_m

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
| 1 | pk_t_mrp_caculatelog_m |  | forgid |

---

## 运算日志-多语言表 t_mrp_caculatelog_l

- **表名称：** 运算日志-多语言表
- **表名：** t_mrp_caculatelog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_caculatelog_l |  | fpkid |
| 2 | idx_mrp_caculatelog_l |  | fid,flocaleid |
