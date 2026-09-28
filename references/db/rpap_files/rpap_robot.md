# 机器人-rpap_robot

## 机器人-多语言表 t_rpap_robot_l

- **表名称：** 机器人-多语言表
- **表名：** t_rpap_robot_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 机器人别名 | varchar | 255 |  |  | ' ' | 机器人别名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_rpap_robot_l_fid |  | fid |
| 2 | pk_t_rpap_robot_l |  | fpkid |

---

## 机器人-使用范围位图表 t_rpap_robot_m

- **表名称：** 机器人-使用范围位图表
- **表名：** t_rpap_robot_m

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
| 1 | pk_t_rpap_robot_m |  | forgid |

---

## 机器人-使用范围表 t_rpap_robot_u

- **表名称：** 机器人-使用范围表
- **表名：** t_rpap_robot_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | 0 |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_rpap_robot_u_uo |  | fuseorgid |
| 2 | pk_t_rpap_robot_u |  | fdataid,fuseorgid |

---

## 机器人-主表 t_rpap_robot

- **表名称：** 机器人-主表
- **表名：** t_rpap_robot

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexternalid | 外部id | varchar | 255 |  |  | ' ' | 外部id |
| 3 | fthirdtypeid | 第三方类型 | int8 | 64 |  | √ | 0 | 第三方类型 rpap_thirdtype |
| 4 | forgid | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fisdelete | 是否已经删除 | varchar | 10 |  | √ | '0' | 是否已经删除,枚举: 1 :已删除 0 :未删除 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fip | IP地址 | varchar | 60 |  | √ | ' ' | IP地址 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fcomputername | 计算机名 | varchar | 50 |  | √ | ' ' | 计算机名 |
| 15 | fonlinestatus | 在线状态 | varchar | 10 |  | √ | ' ' | 在线状态,枚举: 1 :在线 0 :离线 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fname | fname | varchar | 255 |  |  | ' ' |  |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fidentificationcode | 识别码 | varchar | 50 |  | √ | ' ' | 识别码 |
| 22 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 255 |  |  | ' ' | 编码 |
| 25 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_rpap_robot_orgid |  | forgid |
| 2 | pk_t_rpap_robot |  | fid |
| 3 | idx_rpap_robot_externalid |  | fexternalid,fthirdtypeid |
| 4 | idx_t_rpap_robot_createorg |  | fcreateorgid |
| 5 | idx_t_rpap_robot_master |  | fmasterid |
