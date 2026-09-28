# PII脱敏配置-gai_piisetting

## PII脱敏配置-多语言表 t_gai_piisetting_l

- **表名称：** PII脱敏配置-多语言表
- **表名：** t_gai_piisetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_piisetting_l_id |  | fid |
| 2 | pk_t_gai_piisetting_l |  | fpkid |

---

## PII脱敏配置-使用范围表 t_gai_piisetting_u

- **表名称：** PII脱敏配置-使用范围表
- **表名：** t_gai_piisetting_u

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
| 1 | idx_t_gai_piisetting_u_uo |  | fuseorgid |
| 2 | pk_t_gai_piisetting_u |  | fdataid,fuseorgid |

---

## PII脱敏配置-主表 t_gai_piisetting

- **表名称：** PII脱敏配置-主表
- **表名：** t_gai_piisetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fdescription | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fpiitypes | PII类型 | varchar | 255 |  | √ | ' ' | PII类型,枚举: CREDIT_CARD :国内银行卡号 PHONE_NUMBER :国内电话号码 EMAIL_ADDRESS :邮箱 IDCard :身份证 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_piisetting_master |  | fmasterid |
| 2 | idx_gai_piisettingp_orgid |  | forgid |
| 3 | pk_t_gai_piisetting |  | fid |
| 4 | idx_t_gai_piisetting_createorg |  | fcreateorgid |
| 5 | idx_gai_piisetting_corgid |  | fcreateorgid |
