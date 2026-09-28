# 车间设置-mpdm_workshopsetup

## 仓库-子表 t_mpdm_workshopentryb

- **表名称：** 仓库-子表
- **表名：** t_mpdm_workshopentryb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fisbackflush | 默认倒冲 | bpchar | 1 |  | √ | '0' | 默认倒冲 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fwarehouse | 编码 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_workshopentryb_fk |  | fid,fseq |
| 2 | t_mpdm_workshopentryb_pkey |  | fentryid |

---

## 退料类型-子表 t_mpdm_workshopentrya

- **表名称：** 退料类型-子表
- **表名：** t_mpdm_workshopentrya

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrynumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 3 | fdescribe | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_workshopentrya_pkey |  | fentryid |
| 2 | idx_mpdm_workshopentrya_fk |  | fid,fseq |

---

## 车间设置-主表 t_mpdm_workshopsetup

- **表名称：** 车间设置-主表
- **表名：** t_mpdm_workshopsetup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fworkprincipal | 车间负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcalendar | 生产日历 | int8 | 64 |  | √ | 0 | [生产日历 mpdm_calendar](../mpdm_files/mpdm_calendar.md) |
| 5 | fremakes | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fadvanceday | 领料提前期(天数) | int8 | 64 |  | √ | 0 | 领料提前期(天数) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fclasssystem | 班制 | int8 | 64 |  | √ | 0 | [班制 mpdm_classsystem](../mpdm_files/mpdm_classsystem.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fautoday | 自动投放天数 | int8 | 64 |  | √ | 0 | 自动投放天数 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fcreateorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fworkshoporgid | 车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fdepttype | 部门类型 | varchar | 5 |  | √ | ' ' | 部门类型,枚举: A :离散制造 B :重复制造 |
| 20 | fbondedwarehouseid | 保税仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fisprotransferbill | 内协工序启用转移单 | bpchar | 1 |  | √ | '0' | 内协工序启用转移单 |
| 23 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 24 | fbondedlocationid | 保税仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 25 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 26 | fauditer | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fsubmitdate | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 28 | fispropicking | 启用工序领料 | bpchar | 1 |  | √ | '0' | 启用工序领料 |
| 29 | flocationid | 发料仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 30 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 32 | fsubmiter | 提交人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | faduitdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 34 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 36 | fisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_workshopsetup_pkey |  | fid |
| 2 | idx_t_mpdm_workshopsetup_master |  | fmasterid |
| 3 | idx_t_mpdm_workshopsetup_createorg |  | fcreateorgid |
| 4 | idx_mpdm_workshopsetup |  | fnumber,fcreateorgid |

---

## 车间设置-使用范围表 t_mpdm_workshopsetup_u

- **表名称：** 车间设置-使用范围表
- **表名：** t_mpdm_workshopsetup_u

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
| 1 | t_mpdm_workshopsetup_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_mpdm_workshopsetup_u_uo |  | fuseorgid |

---

## 车间设置-多语言表 t_mpdm_workshopsetup_l

- **表名称：** 车间设置-多语言表
- **表名：** t_mpdm_workshopsetup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 225 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_workshopsetup_l_pkey |  | fpkid |
| 2 | idx_mpdm_workshopsetup_l |  | fid,flocaleid |

---

## 车间设置-使用范围位图表 t_mpdm_workshopsetup_m

- **表名称：** 车间设置-使用范围位图表
- **表名：** t_mpdm_workshopsetup_m

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
| 1 | pk_t_mpdm_workshopsetup_m |  | forgid |
