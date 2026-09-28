# 工作中心检修信息-mpdm_workcenter_info

## 工作中心检修信息-主表 t_mpdm_resource

- **表名称：** 工作中心检修信息-主表
- **表名：** t_mpdm_resource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 3 | fprofitworkcenter | 是否盈利工作中心 | bpchar | 1 |  | √ | '0' | 是否盈利工作中心 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fresourcelevelid | 工作中心等级 | int8 | 64 |  | √ | 0 | 资源等级 mpdm_resource_level |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 工作中心编码 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 11 | fresourcetypeid | fresourcetypeid | int8 | 64 |  | √ | 0 |  |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fresponsiblepersonid | 责任人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fparentid | 上级 | int8 | 64 |  | √ | 0 | 工作中心检修信息 mpdm_workcenter_info |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fwarehouseid | 仓库id（弃用） | int8 | 64 |  | √ | 0 | 仓库id（弃用） |
| 22 | fresponsibleorgid | 责任部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 25 | fplanroomid | 计划室 | int8 | 64 |  | √ | 0 | 计划室 mpdm_planroom |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpdm_resource_fcro |  | fcreateorgid |
| 2 | idx_t_mpdm_resource_createorg |  | fcreateorgid |
| 3 | idx_t_mpdm_resource_master |  | fmasterid |
| 4 | pk_mpdm_resource |  | fid |
| 5 | idx_t_mpdm_mpdm_resource_fnum |  | fnumber |
| 6 | idx_t_mpdm_resource_fcrt |  | fcreatetime |

---

## 工作中心检修信息-使用范围表 t_mpdm_resource_u

- **表名称：** 工作中心检修信息-使用范围表
- **表名：** t_mpdm_resource_u

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
| 1 | pk_t_mpdm_resource_u |  | fdataid,fuseorgid |
| 2 | idx_t_mpdm_resource_u_uo |  | fuseorgid |

---

## 工作中心检修信息-多语言表 t_mpdm_resource_l

- **表名称：** 工作中心检修信息-多语言表
- **表名：** t_mpdm_resource_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | ffullname | 长名称 | varchar | 50 |  | √ | ' ' | 长名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_resource_l |  | fpkid |
| 2 | idx_mpdm_resource_l |  | fid,flocaleid |

---

## 工作中心检修信息-使用范围位图表 t_mpdm_resource_m

- **表名称：** 工作中心检修信息-使用范围位图表
- **表名：** t_mpdm_resource_m

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
| 1 | pk_t_mpdm_resource_m |  | forgid |

---

## 检修资源约束-子表 t_mpdm_resource_conf

- **表名称：** 检修资源约束-子表
- **表名：** t_mpdm_resource_conf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fabilityid | 资源约束配置 | int8 | 64 |  | √ | 0 | 资源约束配置 mpdm_resconstraint_config |
| 3 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 4 | fsupplyway | 容量供应方式 | varchar | 50 |  | √ | ' ' | 容量供应方式,枚举: A :独占 B :有限共享 C :无限共享 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fabilitymultiple | 容量供应倍数 | int4 | 32 |  | √ | 0 | 容量供应倍数 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_resource_conf |  | fentryid |
| 2 | idx_mpdm_resource_conf_fs |  | fid,fseq |
