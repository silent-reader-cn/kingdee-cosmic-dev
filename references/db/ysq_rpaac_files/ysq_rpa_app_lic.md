# 许可中心-ysq_rpa_app_lic

## 许可中心-多语言表 tk_ysq_rpa_app_lic_l

- **表名称：** 许可中心-多语言表
- **表名：** tk_ysq_rpa_app_lic_l

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
| 1 | pk_tk_ysq_rpa_app_lic_l |  | fpkid |
| 2 | idx__ysq_rpa_app_lic_l_0 |  | fid,flocaleid |

---

## 许可中心-使用范围位图表 tk_ysq_rpa_app_lic_m

- **表名称：** 许可中心-使用范围位图表
- **表名：** tk_ysq_rpa_app_lic_m

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
| 1 | pk_tk_ysq_rpa_app_lic_m |  | forgid |

---

## 许可中心-使用范围表 tk_ysq_rpa_app_lic_u

- **表名称：** 许可中心-使用范围表
- **表名：** tk_ysq_rpa_app_lic_u

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
| 1 | pk_tk_ysq_rpa_app_lic_u |  | fdataid,fuseorgid |
| 2 | idx_tk_ysq_rpa_app_lic_u_uo |  | fuseorgid |

---

## 许可中心-主表 tk_ysq_rpa_app_lic

- **表名称：** 许可中心-主表
- **表名：** tk_ysq_rpa_app_lic

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fk_ysq_lic_count | fk_ysq_lic_count | int8 | 64 |  |  | null |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fk_ysq_start_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 9 | fk_ysq_lic_sn | 许可简码 | varchar | 254 |  | √ | ' ' | 许可简码 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fctrlstrategy | 控制策略 | varchar | 254 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 13 | fk_ysq_end_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  |  | null | 原资料id |
| 18 | fk_ysq_app_useable | 是否可用 | bpchar | 1 |  | √ | '0' | 是否可用 |
| 19 | fbitindex | 位图 | int8 | 64 |  |  | null | 位图 |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fsourcebitindex | 原资料位图 | int8 | 64 |  |  | null | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_ysq_rpa_app_lic |  | fid |
| 2 | idx_tk_ysq_rpa_app_lic_master |  | fmasterid |
| 3 | idx_tk_ysq_rpa_app_lic_createorg |  | fcreateorgid |
