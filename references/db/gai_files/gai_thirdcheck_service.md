# 机审服务配置-gai_thirdcheck_service

## 机审服务配置-多语言表 t_gai_thirdcheck_service_l

- **表名称：** 机审服务配置-多语言表
- **表名：** t_gai_thirdcheck_service_l

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
| 1 | idx_thirdcheck_service_l_id |  | fid |
| 2 | pk_t_gai_thirdcheck_service_l |  | fpkid |

---

## 机审服务配置-使用范围表 t_gai_thirdcheck_service_u

- **表名称：** 机审服务配置-使用范围表
- **表名：** t_gai_thirdcheck_service_u

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
| 1 | pk_t_gai_thirdcheck_service_u |  | fdataid,fuseorgid |
| 2 | idx_t_gai_thirdcheck_service_u_uo |  | fuseorgid |

---

## 机审服务配置-主表 t_gai_thirdcheck_service

- **表名称：** 机审服务配置-主表
- **表名：** t_gai_thirdcheck_service

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fappid | 应用ID | varchar | 255 |  | √ | ' ' | 应用ID |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fextfield7 | 密钥扩展字段 | varchar | 255 |  | √ | ' ' | 密钥扩展字段 |
| 7 | fextfield8 | 密钥扩展字段 | varchar | 255 |  | √ | ' ' | 密钥扩展字段 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fbusinessid | 业务ID | varchar | 255 |  | √ | ' ' | 业务ID |
| 10 | fextfield9 | 密钥扩展字段 | varchar | 255 |  | √ | ' ' | 密钥扩展字段 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fserver | 服务器地址 | varchar | 255 |  | √ | ' ' | 服务器地址 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fextfield1 | 扩展字段 | varchar | 255 |  | √ | ' ' | 扩展字段 |
| 17 | fextfield2 | 扩展字段 | varchar | 255 |  | √ | ' ' | 扩展字段 |
| 18 | fextfield3 | 扩展字段 | varchar | 255 |  | √ | ' ' | 扩展字段 |
| 19 | fextfield4 | 扩展字段 | varchar | 255 |  | √ | ' ' | 扩展字段 |
| 20 | fextfield5 | 扩展字段 | varchar | 255 |  | √ | ' ' | 扩展字段 |
| 21 | fextfield6 | 密钥扩展字段 | varchar | 255 |  | √ | ' ' | 密钥扩展字段 |
| 22 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 25 | fappkey | 应用密钥 | varchar | 255 |  | √ | ' ' | 应用密钥 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 28 | fprotocol | 协议 | varchar | 50 |  | √ | ' ' | 协议,枚举: http :HTTP https :HTTPS |
| 29 | ftype | 机审类型 | int8 | 64 |  | √ | 0 | [机审类型 gai_thirdcheck_type](../gai_files/gai_thirdcheck_type.md) |
| 30 | fport | 端口 | varchar | 50 |  | √ | ' ' | 端口 |
| 31 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 33 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_thirdcheck_service_master |  | fmasterid |
| 2 | idx_thirdcheck_service_org |  | forgid |
| 3 | pk_t_gai_thirdcheck_service |  | fid |
| 4 | idx_t_gai_thirdcheck_service_createorg |  | fcreateorgid |
| 5 | idx_thirdcheck_service_corg |  | fcreatorid |
