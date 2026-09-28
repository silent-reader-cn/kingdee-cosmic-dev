# 旅客运输抵扣配置-rim_deduct_config

## 旅客运输抵扣配置-主表 t_rim_deduct_config

- **表名称：** 旅客运输抵扣配置-主表
- **表名：** t_rim_deduct_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbus_company_employee | 是否本企业员工 | varchar | 4 |  | √ | ' ' | 是否本企业员工,枚举: 1 :是 0 :否 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fair_begin_date | 乘机起始日期 | timestamp | 0 |  |  | null | 乘机起始日期 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcustom_config | 个性化配置 | varchar | 255 |  | √ | ' ' | 个性化配置 |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 13 | fair_person_identity | 注明旅客身份信息 | varchar | 4 |  | √ | ' ' | 注明旅客身份信息,枚举: 1 :姓名或身份证 2 :姓名和身份证 |
| 14 | ftrain_person_identity | 注明旅客身份信息 | varchar | 4 |  | √ | ' ' | 注明旅客身份信息,枚举: 1 :姓名或身份证 2 :姓名和身份证 |
| 15 | fboat_person_identity | 注明旅客身份信息 | varchar | 4 |  | √ | ' ' | 注明旅客身份信息,枚举: 1 :姓名或身份证 2 :姓名和身份证 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | ftrain_company_employee | 是否本企业员工 | varchar | 4 |  | √ | ' ' | 是否本企业员工,枚举: 1 :是 0 :否 |
| 21 | fair_company_employee | 是否本企业员工 | varchar | 4 |  | √ | ' ' | 是否本企业员工,枚举: 1 :是 0 :否 |
| 22 | fbus_begin_date | 乘车起始日期 | timestamp | 0 |  |  | null | 乘车起始日期 |
| 23 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fboat_begin_date | 乘船起始日期 | timestamp | 0 |  |  | null | 乘船起始日期 |
| 25 | fcustom_config_tag | 个性化配置_详情 | text | 0 |  |  | null | 个性化配置_详情 |
| 26 | ftrain_begin_date | 乘车起始日期 | timestamp | 0 |  |  | null | 乘车起始日期 |
| 27 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 29 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fboat_company_employee | 是否本企业员工 | varchar | 4 |  | √ | ' ' | 是否本企业员工,枚举: 1 :是 0 :否 |
| 31 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 32 | fbus_person_identity | 注明旅客身份信息 | varchar | 4 |  | √ | ' ' | 注明旅客身份信息,枚举: 1 :姓名或身份证 2 :姓名和身份证 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_deduct_config2 |  | fmasterid |
| 2 | idx_rim_deduct_config1 |  | fcreateorgid |
| 3 | pk_rim_deduct_config |  | fid |
| 4 | idx_t_rim_deduct_config_createorg |  | fcreateorgid |
| 5 | idx_t_rim_deduct_config_master |  | fmasterid |

---

## 旅客运输抵扣配置-多语言表 t_rim_deduct_config_l

- **表名称：** 旅客运输抵扣配置-多语言表
- **表名：** t_rim_deduct_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_deduct_config_l |  | fpkid |
| 2 | idx_rim_deduct_config_l |  | fid,flocaleid |

---

## 旅客运输抵扣配置-使用范围位图表 t_rim_deduct_config_m

- **表名称：** 旅客运输抵扣配置-使用范围位图表
- **表名：** t_rim_deduct_config_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 2 | fidx | fidx | int8 | 64 |  | √ | 0 |  |
| 3 | fdata | fdata | bytea | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_deduct_config_m |  | forgid |

---

## 旅客运输抵扣配置-使用范围表 t_rim_deduct_config_u

- **表名称：** 旅客运输抵扣配置-使用范围表
- **表名：** t_rim_deduct_config_u

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
| 1 | pk_rim_deduct_config_u |  | fdataid,fuseorgid |
| 2 | idx_rim_deduct_config_u |  | fcreateorgid |
