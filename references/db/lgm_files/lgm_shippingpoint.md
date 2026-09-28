# 装运点-lgm_shippingpoint

## 装运点-多语言表 t_lgm_shippingpoint_l

- **表名称：** 装运点-多语言表
- **表名：** t_lgm_shippingpoint_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 装运点名称 | varchar | 80 |  | √ | ' ' | 装运点名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lgm_shippingpoint_l |  | fpkid |
| 2 | idx_lgm_shippingpoint_l |  | fid |

---

## 装运点-使用范围表 t_lgm_shippingpoint_u

- **表名称：** 装运点-使用范围表
- **表名：** t_lgm_shippingpoint_u

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
| 1 | pk_t_lgm_shippingpoint_u |  | fdataid,fuseorgid |
| 2 | idx_t_lgm_shippingpoint_u_uo |  | fuseorgid |

---

## 装运点-主表 t_lgm_shippingpoint

- **表名称：** 装运点-主表
- **表名：** t_lgm_shippingpoint

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 装运点分类 | int8 | 64 |  | √ | 0 | [装运点分类 lgm_shippingpointgroup](../lgm_files/lgm_shippingpointgroup.md) |
| 3 | faddress | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |
| 4 | floadduration | 标准装货时长(h) | numeric | 23 | 10 |  | null | 标准装货时长(h) |
| 5 | farriveleadtime | 到达提前期(h) | numeric | 23 | 10 |  | null | 到达提前期(h) |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 12 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  |  | 0 | 主数据内码 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fadmindivision | 行政区划 | varchar | 50 |  | √ | ' ' | 行政区划 |
| 18 | ftimezone | 时区 | int8 | 64 |  | √ | 0 | [时区 inte_timezone](../base_files/inte_timezone.md) |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fname | 装运点名称 | varchar | 80 |  | √ | ' ' | 装运点名称 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fctrlstrategy | 管控策略 | varchar | 5 |  | √ | ' ' | 管控策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | flongitude | 经度 | numeric | 23 | 10 |  | null | 经度 |
| 27 | fnumber | 装运点编码 | varchar | 30 |  | √ | ' ' | 装运点编码 |
| 28 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | funloadduration | 标准卸货时长(h) | numeric | 23 | 10 |  | null | 标准卸货时长(h) |
| 30 | flatitude | 纬度 | numeric | 23 | 10 |  | null | 纬度 |
| 31 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lgm_shippingpoint_master |  | fmasterid |
| 2 | idx_t_lgm_shippingpoint_createorg |  | fcreateorgid |
| 3 | idx_t_lgm_shippingpoint_master |  | fmasterid |
| 4 | pk_lgm_shippingpoint |  | fid |
| 5 | idx_lgm_shippingpoint_crteorg |  | fcreateorgid |
| 6 | idx_lgm_shippingpoint_num |  | fnumber |
