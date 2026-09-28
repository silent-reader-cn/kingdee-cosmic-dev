# 渠道类型-ocdbd_channel_type

## 渠道类型-多语言表 t_ocdbd_chl_type_l

- **表名称：** 渠道类型-多语言表
- **表名：** t_ocdbd_chl_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 类型名称 | varchar | 100 |  | √ | ' ' | 类型名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_chltypel_fidflid |  | fid,flocaleid |
| 2 | pk_ocdbd_chl_type_l |  | fpkid |

---

## 渠道类型-使用范围表 t_ocdbd_chl_type_u

- **表名称：** 渠道类型-使用范围表
- **表名：** t_ocdbd_chl_type_u

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
| 1 | pk_t_ocdbd_chl_type_u |  | fdataid,fuseorgid |
| 2 | idx_t_ocdbd_chl_type_u_uo |  | fuseorgid |

---

## 渠道类型-主表 t_ocdbd_chl_type

- **表名称：** 渠道类型-主表
- **表名：** t_ocdbd_chl_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fisinsideorg | 是否内部组织 | bpchar | 1 |  | √ | '0' | 是否内部组织 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | ftypeid | 类型标识 | bpchar | 1 |  | √ | 'Z' | 类型标识,枚举: A :经销商 B :经销门店 C :经销商兼门店 D :直营门店（独立核算） E :直营门店（非独立核算） F :加盟门店（独立核算） G :加盟门店（非独立核算） H :在线商城 I :内部组织 Z :其他 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 类型编码 | varchar | 80 |  | √ | ' ' | 类型编码 |
| 19 | fissyspreset | 是否系统预设 | bpchar | 1 |  | √ | '0' | 是否系统预设 |
| 20 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 21 | fisstore | 是否门店 | bpchar | 1 |  | √ | '0' | 是否门店 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ocdbd_chl_type_createorg |  | fcreateorgid |
| 2 | pk_ocdbd_chl_type |  | fid |
| 3 | idx_t_ocdbd_chl_type_master |  | fmasterid |
| 4 | idx_ocdbd_chltype_num |  | fnumber |
