# 运输路线-lgm_transportroute

## 运输路线-主表 t_lgm_transportroute

- **表名称：** 运输路线-主表
- **表名：** t_lgm_transportroute

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fbeginshippoint | 起始装运点 | int8 | 64 |  | √ | 0 | [装运点 lgm_shippingpoint](../lgm_files/lgm_shippingpoint.md) |
| 8 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  |  | 0 | 主数据内码 |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 13 | fendshippoint | 终止装运点 | int8 | 64 |  | √ | 0 | [装运点 lgm_shippingpoint](../lgm_files/lgm_shippingpoint.md) |
| 14 | fintransittime | 在途时长(h) | numeric | 23 | 10 |  | null | 在途时长(h) |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fname | 路线名称 | varchar | 80 |  | √ | ' ' | 路线名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | ftransportmode | 运输方式 | int8 | 64 |  | √ | 0 | [运输方式 gtm_transportmode](../gtm_files/gtm_transportmode.md) |
| 19 | froutedistance | 路线距离(km) | numeric | 23 | 10 |  | null | 路线距离(km) |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fapproveridtime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 23 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fprepareworktime | 作业准备时间(h) | numeric | 23 | 10 |  | null | 作业准备时间(h) |
| 25 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 路线编码 | varchar | 30 |  | √ | ' ' | 路线编码 |
| 27 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lgm_transportroute_master |  | fmasterid |
| 2 | idx_lgm_transportroute_num |  | fnumber |
| 3 | idx_t_lgm_transportroute_master |  | fmasterid |
| 4 | idx_t_lgm_transportroute_createorg |  | fcreateorgid |
| 5 | pk_lgm_transportroute |  | fid |
| 6 | idx_lgm_transportroute_crteorg |  | fcreateorgid |

---

## 单据体-子表 t_lgm_transportroute_e

- **表名称：** 单据体-子表
- **表名：** t_lgm_transportroute_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrybeginpoint | 启运点 | int8 | 64 |  | √ | 0 | [装运点 lgm_shippingpoint](../lgm_files/lgm_shippingpoint.md) |
| 3 | fentrytransportmode | 运输方式 | int8 | 64 |  | √ | 0 | [运输方式 gtm_transportmode](../gtm_files/gtm_transportmode.md) |
| 4 | fentryintransittime | 时长(h) | numeric | 23 | 10 |  | null | 时长(h) |
| 5 | fentryendpoint | 目的地 | int8 | 64 |  | √ | 0 | [装运点 lgm_shippingpoint](../lgm_files/lgm_shippingpoint.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryroutedistance | 距离(km) | numeric | 23 | 10 |  | null | 距离(km) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lgm_transportroute_e |  | fentryid |
| 2 | idx_lgm_transportroute_e_id |  | fid |

---

## 运输路线-多语言表 t_lgm_transportroute_l

- **表名称：** 运输路线-多语言表
- **表名：** t_lgm_transportroute_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 路线名称 | varchar | 80 |  | √ | ' ' | 路线名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lgm_transportroute_l |  | fpkid |
| 2 | idx_lgm_transportroute_l_id |  | fid |

---

## 运输路线-使用范围表 t_lgm_transportroute_u

- **表名称：** 运输路线-使用范围表
- **表名：** t_lgm_transportroute_u

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
| 1 | pk_t_lgm_transportroute_u |  | fdataid,fuseorgid |
| 2 | idx_t_lgm_transportroute_u_uo |  | fuseorgid |
