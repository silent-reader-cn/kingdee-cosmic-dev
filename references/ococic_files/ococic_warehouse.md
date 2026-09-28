# 渠道仓库-ococic_warehouse

## 仓位单据体-子表 t_ocdbd_location

- **表名称：** 仓位单据体-子表
- **表名：** t_ocdbd_location

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 6 | fnumber | 仓位编码 | varchar | 80 |  | √ | ' ' | 仓位编码 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ferplocationid | ERP仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 9 | fisdefault | 默认仓位 | bpchar | 1 |  | √ | '0' | 默认仓位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_location_num |  | fnumber |
| 2 | pk_ocdbd_location |  | fentryid |

---

## 渠道仓库-使用范围表 t_ocdbd_warehouse_u

- **表名称：** 渠道仓库-使用范围表
- **表名：** t_ocdbd_warehouse_u

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
| 1 | idx_t_ocdbd_warehouse_u_uo |  | fuseorgid |
| 2 | pk_t_ocdbd_warehouse_u |  | fdataid,fuseorgid |

---

## 渠道仓库-多语言表 t_ocdbd_warehouse_l

- **表名称：** 渠道仓库-多语言表
- **表名：** t_ocdbd_warehouse_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 仓库名称 | varchar | 90 |  | √ | ' ' | 仓库名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_warehouse_l |  | fpkid |
| 2 | idx_ocdbd_warehousel_flid |  | fid,flocaleid |

---

## 仓位单据体-多语言表 t_ocdbd_location_l

- **表名称：** 仓位单据体-多语言表
- **表名：** t_ocdbd_location_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | fname | 仓位名称 | varchar | 80 |  | √ | ' ' | 仓位名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_location_l |  | fpkid |
| 2 | idx_ocdbd_locationl_elid |  | fentryid,flocaleid |

---

## 渠道仓库-主表 t_ocdbd_warehouse

- **表名称：** 渠道仓库-主表
- **表名：** t_ocdbd_warehouse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fiscarwarehouse | 车仓 | bpchar | 1 |  | √ | '0' | 车仓 |
| 3 | fwarehousetype | 仓库类型 | bpchar | 1 |  | √ | '1' | 仓库类型,枚举: 1 :渠道仓库 2 :非渠道仓库 |
| 4 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fconfirmbywarehouse | 退发货需库房确认 | bpchar | 1 |  | √ | '0' | 退发货需库房确认 |
| 6 | fmanager | 仓库负责人 | varchar | 50 |  | √ | ' ' | 仓库负责人 |
| 7 | fprincipalid | 仓库负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | ferpwarehouseid | ERP仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fplatenumber | 车牌号 | varchar | 30 |  | √ | ' ' | 车牌号 |
| 14 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fownerchannelid | 所属渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fisdelivery | 默认发货仓库 | bpchar | 1 |  | √ | '0' | 默认发货仓库 |
| 19 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 20 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 21 | fisreturn | 默认退货仓库 | bpchar | 1 |  | √ | '0' | 默认退货仓库 |
| 22 | fdetailaddress | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |
| 23 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fname | fname | varchar | 90 |  | √ | ' ' |  |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | ferpstockorgid | ERP库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 31 | ftelephone | 联系电话 | varchar | 100 |  | √ | ' ' | 联系电话 |
| 32 | fadmdivisionid | 仓库地址 | varchar | 36 |  | √ | ' ' | 仓库地址 |
| 33 | fdriverid | 司机 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fcarsalerid | 车销员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 36 | fnumber | 仓库编码 | varchar | 80 |  | √ | ' ' | 仓库编码 |
| 37 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 38 | fisdefault | 默认收货仓库 | bpchar | 1 |  | √ | '0' | 默认收货仓库 |
| 39 | fenablelocation | 启用仓位管理 | bpchar | 1 |  | √ | '0' | 启用仓位管理 |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_warehouse_num |  | fnumber |
| 2 | pk_ocdbd_warehouse |  | fid |
| 3 | idx_t_ocdbd_warehouse_master |  | fmasterid |
| 4 | idx_t_ocdbd_warehouse_createorg |  | fcreateorgid |
