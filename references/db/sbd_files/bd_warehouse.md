# 仓库-bd_warehouse

## 仓库-多语言表 t_bd_warehouse_l

- **表名称：** 仓库-多语言表
- **表名：** t_bd_warehouse_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_warehouse_l_pkey |  | fpkid |
| 2 | idx_bd_warehouse_l_fid |  | fid,flocaleid |

---

## 仓库-使用范围位图表 t_bd_warehouse_m

- **表名称：** 仓库-使用范围位图表
- **表名：** t_bd_warehouse_m

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
| 1 | pk_t_bd_warehouse_m |  | forgid |

---

## 仓库-使用范围表 t_bd_warehouse_u

- **表名称：** 仓库-使用范围表
- **表名：** t_bd_warehouse_u

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
| 1 | idx_t_bd_warehouse_u_uo |  | fuseorgid |
| 2 | t_bd_warehouse_u_pkey |  | fdataid,fuseorgid |

---

## 仓库-主表 t_bd_warehouse

- **表名称：** 仓库-主表
- **表名：** t_bd_warehouse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [仓库分组 bd_warehousegroup](../sbd_files/bd_warehousegroup.md) |
| 3 | fisallowpartialneginv | 仅允许部分物料负库存 | bpchar | 1 |  | √ | '0' | 仅允许部分物料负库存 |
| 4 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fprincipalid | 仓库负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fisopenlocation | 启用仓位 | bpchar | 1 |  | √ | '0' | 启用仓位 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fisallowallneginv | 允许全部物料负库存 | bpchar | 1 |  | √ | '0' | 允许全部物料负库存 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fdetailaddress | 详细地址 | varchar | 255 |  |  | ' ' | 详细地址 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fisentrustverifyware | 委托代销仓 | bpchar | 1 |  | √ | '0' | 委托代销仓 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fbondedwarehouse | 保税仓 | bpchar | 1 |  | √ | '0' | 保税仓 |
| 24 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 26 | finvorgid | finvorgid | int8 | 64 |  | √ | 0 |  |
| 27 | ftelephone | 联系电话 | varchar | 100 |  | √ | ' ' | 联系电话 |
| 28 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 29 | fadmdivisionid | 仓库地址 | varchar | 100 |  | √ | '0' | 仓库地址 |
| 30 | fk_bj73_checkboxfield | 订单发货 | bpchar | 1 |  | √ | '0' | 订单发货 |
| 31 | fpartiexpectqty | 可发量控制 | bpchar | 1 |  | √ | '1' | 可发量控制 |
| 32 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 33 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 34 | fissuptransvirtualware | 直运虚拟仓 | bpchar | 1 |  | √ | '0' | 直运虚拟仓 |
| 35 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_warehouse_master |  | fmasterid |
| 2 | idx_t_bd_warehouse_createorg |  | fcreateorgid |
| 3 | t_bd_warehouse_pkey |  | fid |
| 4 | idx_bd_warehouse_number |  | fnumber |

---

## 业务员设置-子表 t_bd_warehousesetup_opera

- **表名称：** 业务员设置-子表
- **表名：** t_bd_warehousesetup_opera

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperatoruserid | 业务员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_warehousesetup_opera |  | fentryid |

---

## 仓位单据体-子表 t_bd_warehouseentry

- **表名称：** 仓位单据体-子表
- **表名：** t_bd_warehouseentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 4 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 8 | fisdefaultloc | 默认仓位 | bpchar | 1 |  | √ | '0' | 默认仓位 |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 11 | flocationid | 仓位编码 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 12 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | flocationstatus | 可用 | bpchar | 1 |  |  | '1' | 可用 |
| 15 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 16 | fenbale | fenbale | bpchar | 1 |  | √ | '1' |  |
| 17 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 18 | fenable | fenable | bpchar | 1 |  | √ | '1' |  |
| 19 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_warehouseentry_createorg |  | fcreateorgid |
| 2 | t_bd_warehouseentry_pkey |  | fentryid |
| 3 | idx_bd_warehouseentry_fid |  | fid |
| 4 | idx_t_bd_warehouseentry_master |  | fmasterid |
