# 前置机管理_父类（供查询支付、电子回单继承）-aqap_bank_login_parent

## 前置机管理_父类（供查询支付、电子回单继承）-主表 t_aqap_bank_login

- **表名称：** 前置机管理_父类（供查询支付、电子回单继承）-主表
- **表名：** t_aqap_bank_login

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fremark | fremark | varchar | 255 |  |  | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 4 | fconfig_type | fconfig_type | varchar | 50 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcustom_id | 租户编号 | varchar | 50 |  | √ | ' ' | 租户编号 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 11 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 12 | fbankversion | 银行版本 | int8 | 64 |  |  | null | 银行启用管理 aqap_bank |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 前置机编号 | varchar | 30 |  | √ | ' ' | 前置机编号 |
| 15 | falias | falias | varchar | 255 |  |  | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_bank_login_pkey |  | fid |
| 2 | idx_aqap_bl_fnumber |  | fnumber |

---

## 前置机管理_父类（供查询支付、电子回单继承）-多语言表 t_aqap_bank_login_l

- **表名称：** 前置机管理_父类（供查询支付、电子回单继承）-多语言表
- **表名：** t_aqap_bank_login_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 前置机名称 | varchar | 255 |  | √ | ' ' | 前置机名称 |
| 3 | ftype | ftype | varchar | 100 |  |  | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_bank_login_l_0 |  | fid,flocaleid |
| 2 | t_aqap_bank_login_l_pkey |  | fpkid |
