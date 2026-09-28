# 四性检测配置-eafc_inspect_config

## 四性检测配置-使用范围表 tk_eafc_inspect_strategy_u

- **表名称：** 四性检测配置-使用范围表
- **表名：** tk_eafc_inspect_strategy_u

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
| 1 | idx_tk_eafc_inspect_strategy_u_uo |  | fuseorgid |
| 2 | pk_tk_eafc_inspect_strategy_u |  | fdataid,fuseorgid |

---

## 单据体-子表 tk_eafc_inspect_config

- **表名称：** 单据体-子表
- **表名：** tk_eafc_inspect_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_org | fk_eafc_org | int8 | 64 |  |  | null |  |
| 3 | forgid | forgid | int8 | 64 |  |  | null |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  |  | null |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fk_eafc_archive_link | 归档环节 | varchar | 50 |  | √ | ' ' | 归档环节 |
| 8 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  |  | null |  |
| 10 | fmasterid | fmasterid | int8 | 64 |  |  | null |  |
| 11 | fk_eafc_transfer_link | 移交与接收环节 | varchar | 50 |  | √ | ' ' | 移交与接收环节 |
| 12 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 13 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 14 | fk_eafc_long_save_link | 长期保存环节 | varchar | 50 |  | √ | ' ' | 长期保存环节 |
| 15 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 16 | fmodifierid | fmodifierid | int8 | 64 |  |  | null |  |
| 17 | fname | fname | varchar | 50 |  |  | null |  |
| 18 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 19 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 20 | fk_eafc_inspect_base | 四性检测项目 | int8 | 64 |  |  | null | [四性检测基础资料 eafc_inspect_base](../esyset_files/eafc_inspect_base.md) |
| 21 | fenable | fenable | varchar | 50 |  | √ | ' ' |  |
| 22 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 25 | fk_eafc_collect_link | 采集环节 | varchar | 50 |  | √ | ' ' | 采集环节 |

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

## 四性检测配置-多语言表 tk_eafc_inspect_strategy_l

- **表名称：** 四性检测配置-多语言表
- **表名：** tk_eafc_inspect_strategy_l

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
| 1 | pk_eafc_inspect_strategy_l |  | fpkid |
| 2 | idx_eafc_inspect_strategy_l_fk |  | fid |

---

## 四性检测配置-主表 tk_eafc_inspect_strategy

- **表名称：** 四性检测配置-主表
- **表名：** tk_eafc_inspect_strategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_strategy_nature | fk_eafc_strategy_nature | varchar | 50 |  | √ | ' ' |  |
| 3 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fk_eafc_strategy_name | fk_eafc_strategy_name | varchar | 150 |  | √ | ' ' |  |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fk_eafc_archive_link | fk_eafc_archive_link | bpchar | 1 |  | √ | '1' |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fk_eafc_strategy_desc | fk_eafc_strategy_desc | varchar | 2000 |  | √ | ' ' |  |
| 12 | fk_eafc_transfer_link | fk_eafc_transfer_link | bpchar | 1 |  | √ | '1' |  |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  |  | null | 原资料id |
| 14 | fbitindex | 位图 | int8 | 64 |  |  | null | 位图 |
| 15 | fk_eafc_org_y | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fk_eafc_strategy_purpose | fk_eafc_strategy_purpose | varchar | 200 |  | √ | ' ' |  |
| 17 | fk_eafc_long_save_link | fk_eafc_long_save_link | bpchar | 1 |  | √ | '1' |  |
| 18 | fk_eafc_strategy_obj | fk_eafc_strategy_obj | varchar | 150 |  | √ | ' ' |  |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fname | fname | varchar | 50 |  |  | null |  |
| 21 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fk_eafc_strategy_code | fk_eafc_strategy_code | varchar | 50 |  | √ | ' ' |  |
| 24 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fk_eafc_strategy_type | fk_eafc_strategy_type | varchar | 200 |  | √ | ' ' |  |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | fsourcebitindex | 原资料位图 | int8 | 64 |  |  | null | 原资料位图 |
| 29 | fk_eafc_collect_link | fk_eafc_collect_link | bpchar | 1 |  | √ | '1' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_eafc_inspect_strategy_master |  | fmasterid |
| 2 | pk__eafc_inspect_strategy |  | fid |
| 3 | idx_tk_eafc_inspect_strategy_createorg |  | fcreateorgid |
