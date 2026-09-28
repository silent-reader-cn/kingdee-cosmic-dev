# 开发商信息-ysq_rpa_dev_info

## 开发商信息-使用范围表 tk_ysq_rpa_dev_info_u

- **表名称：** 开发商信息-使用范围表
- **表名：** tk_ysq_rpa_dev_info_u

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
| 1 | pk_tk_ysq_rpa_dev_info_u |  | fdataid,fuseorgid |
| 2 | idx_tk_ysq_rpa_dev_info_u_uo |  | fuseorgid |

---

## 开发商信息-使用范围位图表 tk_ysq_rpa_dev_info_m

- **表名称：** 开发商信息-使用范围位图表
- **表名：** tk_ysq_rpa_dev_info_m

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
| 1 | pk_tk_ysq_rpa_dev_info_m |  | forgid |

---

## 开发商信息-多语言表 tk_ysq_rpa_dev_info_l

- **表名称：** 开发商信息-多语言表
- **表名：** tk_ysq_rpa_dev_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
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
| 1 | idx__ysq_rpa_dev_info_l_0 |  | fid,flocaleid |
| 2 | pk_tk_ysq_rpa_dev_info_l |  | fpkid |

---

## 开发商信息-主表 tk_ysq_rpa_dev_info

- **表名称：** 开发商信息-主表
- **表名：** tk_ysq_rpa_dev_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 3 | fk_ysq_dev_name | 开发商名称 | varchar | 256 |  | √ | ' ' | 开发商名称 |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fk_ysq_register_date | 注册日期 | timestamp | 0 |  |  | null | 注册日期 |
| 8 | forgid | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 9 | fk_ysq_dev_code | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 11 | fk_ysq_dev_pwd | 登录密码 | varchar | 256 |  | √ | ' ' | 登录密码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fctrlstrategy | 控制策略 | varchar | 254 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  |  | null | 原资料id |
| 18 | fbitindex | 位图 | int8 | 64 |  |  | null | 位图 |
| 19 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | fsourcebitindex | 原资料位图 | int8 | 64 |  |  | null | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_ysq_rpa_dev_info_master |  | fmasterid |
| 2 | pk_tk_ysq_rpa_dev_info |  | fid |
| 3 | idx_tk_ysq_rpa_dev_info_createorg |  | fcreateorgid |
