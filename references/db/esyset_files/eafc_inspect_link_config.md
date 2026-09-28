# 检测环境配置表-eafc_inspect_link_config

## 检测环境配置表-主表 tk_eafc_inspect_config

- **表名称：** 检测环境配置表-主表
- **表名：** tk_eafc_inspect_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_org | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fk_eafc_archive_link | 归档环节 | varchar | 50 |  | √ | ' ' | 归档环节,枚举: 1 :检测不通过不允许编目归档 2 :检测不通过允许手动编目归档 3 :检测不通过可以自动编目归档 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 11 | fk_eafc_transfer_link | 移交与接收环节 | varchar | 50 |  | √ | ' ' | 移交与接收环节,枚举: 1 :检测不通过不允许移交与接收 2 :检测不通过允许手动移交与接收 3 :检测不通过可以自动移交与接收 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fk_eafc_long_save_link | 长期保存环节 | varchar | 50 |  | √ | ' ' | 长期保存环节,枚举: 1 :检测不通过不允许长期保存 2 :检测不通过允许手动长期保存 3 :检测不通过可以自动长期保存 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fname | fname | varchar | 50 |  |  | null |  |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 20 | fk_eafc_inspect_base | fk_eafc_inspect_base | int8 | 64 |  |  | null |  |
| 21 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 24 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 25 | fk_eafc_collect_link | 采集环节 | varchar | 50 |  | √ | ' ' | 采集环节,枚举: 1 :检测不通过不允许编目归档 2 :检测不通过允许手动编目归档 3 :检测不通过可以自动编目归档 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_inspect_config |  | fid |
| 2 | idx_tk_eafc_inspect_config_master |  | fmasterid |
| 3 | idx_tk_eafc_inspect_config_createorg |  | fcreateorgid |

---

## 检测环境配置表-多语言表 tk_eafc_inspect_config_l

- **表名称：** 检测环境配置表-多语言表
- **表名：** tk_eafc_inspect_config_l

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
| 1 | idx_eafc_inspect_config_l_fk |  | fid |
| 2 | pk_eafc_inspect_config_l |  | fpkid |

---

## 检测环境配置表-使用范围表 tk_eafc_inspect_config_u

- **表名称：** 检测环境配置表-使用范围表
- **表名：** tk_eafc_inspect_config_u

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
| 1 | idx_tk_eafc_inspect_config_u_uo |  | fuseorgid |
| 2 | pk_tk_eafc_inspect_config_u |  | fdataid,fuseorgid |
