# 库房设置-eafc_store_config_base

## 库房设置-多语言表 tk_eafc_store_config_base_l

- **表名称：** 库房设置-多语言表
- **表名：** tk_eafc_store_config_base_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 库房名称 | varchar | 50 |  | √ | ' ' | 库房名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_store_config_base_l |  | fpkid |
| 2 | idx_eafc_store_config_base_l_fk |  | fid |

---

## 单据体-子表 tk_eafc_store_area_config

- **表名称：** 单据体-子表
- **表名：** tk_eafc_store_area_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_part_num | 单层节数 | int8 | 64 |  |  | null | 单层节数 |
| 3 | fk_eafc_area_name | 区域名称 | varchar | 50 |  | √ | ' ' | 区域名称 |
| 4 | fk_eafc_floor_num | 单面层数 | int8 | 64 |  |  | null | 单面层数 |
| 5 | fk_eafc_part_width | 预设宽度 | numeric | 23 | 10 |  | null | 预设宽度 |
| 6 | fk_eafc_is_pre_box_num | 是否预设装盒数 | bpchar | 1 |  | √ | '0' | 是否预设装盒数 |
| 7 | fk_eafc_right_no | 右侧编码 | varchar | 50 |  | √ | ' ' | 右侧编码 |
| 8 | fk_eafc_area_shelf_num | 放置密集架组数 | int8 | 64 |  |  | null | 放置密集架组数 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fk_eafc_area_no | 区域编码 | varchar | 50 |  | √ | ' ' | 区域编码 |
| 11 | fk_eafc_area_status | 区域状态 | varchar | 50 |  | √ | ' ' | 区域状态,枚举: 0 :未用 1 :在用 |
| 12 | fk_eafc_box_standard | 规格 | varchar | 50 |  | √ | ' ' | 规格,枚举: 20 :20mm 40 :40mm 60 :60mm |
| 13 | fk_eafc_part_box_num | 预设装盒数 | int8 | 64 |  |  | null | 预设装盒数 |
| 14 | fk_eafc_area_area | 区域面积 | numeric | 23 | 2 |  | null | 区域面积 |
| 15 | fk_eafc_left_no | 左侧编码 | varchar | 50 |  | √ | ' ' | 左侧编码 |
| 16 | fk_eafc_shelf_side | 首尾柜子 | varchar | 50 |  | √ | ' ' | 首尾柜子,枚举: 1 :单面 2 :双面 |
| 17 | fk_eafc_one_side | 是否单面 | bpchar | 1 |  | √ | '0' | 是否单面 |
| 18 | fk_eafc_area_desc | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 20 | fk_eafc_shelf_no_end | 密集架编号结束 | int8 | 64 |  |  | null | 密集架编号结束 |
| 21 | fk_eafc_shelf_no_start | 密集架编号开始 | int8 | 64 |  |  | null | 密集架编号开始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_store_area_config |  | fentryid |

---

## 库房设置-主表 tk_eafc_store_config_base

- **表名称：** 库房设置-主表
- **表名：** tk_eafc_store_config_base

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fk_eafc_shelf_serial_bit | 密集架流水号位制 | varchar | 50 |  | √ | ' ' | 密集架流水号位制,枚举: 1 :个位 2 :十位 3 :百位 4 :千位 5 :万位 |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fk_eafc_manager | 管理员 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fk_eafc_shelf_num | 密集架组数 | int8 | 64 |  |  | null | 密集架组数 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fk_eafc_general_org | 全宗 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 12 | fk_eafc_address | 详细地址 | varchar | 50 |  | √ | ' ' | 详细地址 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  |  | null | 原资料id |
| 14 | fbitindex | 位图 | int8 | 64 |  |  | null | 位图 |
| 15 | fk_eafc_store_area | 库房面积 | numeric | 23 | 10 |  | null | 库房面积 |
| 16 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fk_fpy_arctrlstrategy | 档案控制策略 | varchar | 50 |  | √ | ' ' | 档案控制策略,枚举: 1 :全局共享 2 :按组织分配 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fk_eafc_area_config | 是否设置区域 | bpchar | 1 |  | √ | '0' | 是否设置区域 |
| 21 | fname | fname | varchar | 50 |  |  | null |  |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fenable | 库房状态 | varchar | 50 |  | √ | ' ' | 库房状态,枚举: 0 :已禁用 1 :已启用 2 :已保存 3 :已删除 |
| 25 | fk_eafc_useorg | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fk_eafc_telephone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | fk_eafc_desc | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 29 | fk_eafc_area | 行政区划 | varchar | 50 |  | √ | ' ' | 行政区划 |
| 30 | fsourcebitindex | 原资料位图 | int8 | 64 |  |  | null | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_eafc_store_config_base_master |  | fmasterid |
| 2 | idx_tk_eafc_store_config_base_createorg |  | fcreateorgid |
| 3 | pk__eafc_store_config_base |  | fid |

---

## 库房设置-使用范围表 tk_eafc_store_config_base_u

- **表名称：** 库房设置-使用范围表
- **表名：** tk_eafc_store_config_base_u

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
| 1 | pk_tk_eafc_store_config_base_u |  | fdataid,fuseorgid |
