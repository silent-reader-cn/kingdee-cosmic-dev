# 集成映射配置-gtm_customslinkmap

## 集成映射配置-多语言表 t_gtm_customslinkmap_l

- **表名称：** 集成映射配置-多语言表
- **表名：** t_gtm_customslinkmap_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_customslinkmap_l_id |  | fid,flocaleid |
| 2 | pk_gtm_customslinkmap_l |  | fpkid |

---

## 集成映射配置-使用范围表 t_gtm_customslinkmap_u

- **表名称：** 集成映射配置-使用范围表
- **表名：** t_gtm_customslinkmap_u

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
| 1 | pk_t_gtm_customslinkmap_u |  | fdataid,fuseorgid |
| 2 | idx_t_gtm_customslinkmap_u_uo |  | fuseorgid |

---

## 单据体-子表 t_gtm_customslinkmapety

- **表名称：** 单据体-子表
- **表名：** t_gtm_customslinkmapety

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | 编码 | int8 | 64 |  | √ | 0 | 征免性质 gtm_naturelevy |
| 3 | fthirdnumber | 第三方系统编码 | varchar | 255 |  | √ | ' ' | 第三方系统编码 |
| 4 | fbasedataida | 名称 | int8 | 64 |  | √ | 0 | 征免性质 gtm_naturelevy |
| 5 | fthirdname | 第三方系统名称 | varchar | 512 |  | √ | ' ' | 第三方系统名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_customslinkmapety_bd |  | fbasedataid |
| 2 | idx_gtm_customslinkmapety_id |  | fid |
| 3 | pk_gtm_customslinkmapety |  | fentryid |

---

## 单据体-多语言表 t_gtm_customslinkmapety_l

- **表名称：** 单据体-多语言表
- **表名：** t_gtm_customslinkmapety_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fthirdname | 第三方系统名称 | varchar | 512 |  | √ | ' ' | 第三方系统名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_customslinkmapety_l_id |  | fentryid,flocaleid |
| 2 | pk_gtm_customslinkmapety_l |  | fpkid |

---

## 集成映射配置-主表 t_gtm_customslinkmap

- **表名称：** 集成映射配置-主表
- **表名：** t_gtm_customslinkmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fthirdsystem | 集成系统 | varchar | 50 |  | √ | ' ' | 集成系统,枚举: eptrade :中国数联 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbasedatatype | 基础资料 | varchar | 50 |  | √ | ' ' | 基础资料,枚举: gtm_naturelevy :征免性质 bd_currency :币种 gtm_customsdistrict :海关关区 lgm_shippingpoint :港口 gtm_customsport :海关口岸 bd_country :国家和地区 gtm_tradeterm :贸易术语 gtm_transportmode :运输方式 bd_packagingtype :包装方式 bd_measureunits :计量单位 |
| 18 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 19 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 22 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_customslinkmap |  | fid |
| 2 | idx_gtm_customslinkmap_bt |  | fbasedatatype |
| 3 | idx_t_gtm_customslinkmap_createorg |  | fcreateorgid |
| 4 | idx_t_gtm_customslinkmap_master |  | fmasterid |
