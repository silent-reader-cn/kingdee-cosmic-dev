# 资源注册模型-mrp_resourceregister_cf

## 资源注册模型-使用范围表 t_mrp_rsregister_u

- **表名称：** 资源注册模型-使用范围表
- **表名：** t_mrp_rsregister_u

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
| 1 | idx_t_mrp_rsregister_u_uo |  | fuseorgid |
| 2 | t_mrp_rsregister_u_pkey |  | fdataid,fuseorgid |

---

## 资源注册模型-使用范围位图表 t_mrp_rsregister_m

- **表名称：** 资源注册模型-使用范围位图表
- **表名：** t_mrp_rsregister_m

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
| 1 | pk_t_mrp_rsregister_m |  | forgid |

---

## 资源注册模型-多语言表 t_mrp_rsregister_l

- **表名称：** 资源注册模型-多语言表
- **表名：** t_mrp_rsregister_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_rsregister_l |  | fid,flocaleid |
| 2 | pk_t_mrp_rsregister_l |  | fpkid |

---

## 资源注册模型-主表 t_mrp_rsregister

- **表名称：** 资源注册模型-主表
- **表名：** t_mrp_rsregister

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdatabasentity | 表实体 | varchar | 50 |  | √ | ' ' | 表实体 |
| 4 | fbusinesstype | 业务类型 | varchar | 5 |  | √ | ' ' | 业务类型,枚举: 01 :MRP 02 :库存计划 07 :缺料分析 08 :齐套分析 09 :周计划 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fouttosupply | 输出转供应映射 | int8 | 64 |  | √ | 0 | [实体字段映射 mrp_billfieldtransfer](../msplan_files/mrp_billfieldtransfer.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fbusinessentity | 目标实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 14 | foutputmapping | 输出结果映射 | int8 | 64 |  | √ | 0 | [实体字段映射 mrp_billfieldtransfer](../msplan_files/mrp_billfieldtransfer.md) |
| 15 | fversion | 版本 | varchar | 30 |  | √ | ' ' | 版本 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | foutputtype | 输出结果类型 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 19 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | ftype | 模型类型 | varchar | 30 |  | √ | ' ' | 模型类型,枚举: 01 :供应 02 :需求 03 :BOM展开 04 :产线排程 05 :资源计划 06 :资源清单 07 :资源需求 08 :资源供应 |
| 23 | frelativetransfer | BOM匹配维度 | int8 | 64 |  | √ | 0 | [实体字段映射 mrp_billfieldtransfer](../msplan_files/mrp_billfieldtransfer.md) |
| 24 | fdataresolverid | 数据源过滤器 | int8 | 64 |  | √ | 0 | [算法注册配置 mrp_algoregister](../msplan_files/mrp_algoregister.md) |
| 25 | fmatchresolverid | 引擎平衡过滤器 | int8 | 64 |  | √ | 0 | [算法注册配置 mrp_algoregister](../msplan_files/mrp_algoregister.md) |
| 26 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | frelativeresource | BOM资源配置 | int8 | 64 |  | √ | 0 | [资源注册模型 mrp_resourceregister_cf](../msplan_files/mrp_resourceregister_cf.md) |
| 29 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_rsregister |  | fid |
| 2 | idx_mrp_rsregister |  | fnumber,fcreateorgid |
| 3 | idx_t_mrp_rsregister_createorg |  | fcreateorgid |
| 4 | idx_t_mrp_rsregister_master |  | fmasterid |

---

## 资源注册配置分录-子表 t_mrp_rsregisterentry

- **表名称：** 资源注册配置分录-子表
- **表名：** t_mrp_rsregisterentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsignname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 3 | fformuladesc | 计算表达式描述 | varchar | 100 |  | √ | ' ' | 计算表达式描述 |
| 4 | fbizdatatype | 业务数据类型 | varchar | 30 |  | √ | ' ' | 业务数据类型,枚举: A :普通维度 B :主业务组织 C :辅助信息 |
| 5 | fdefaultvalue | 默认值 | varchar | 50 |  | √ | ' ' | 默认值 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fsrctype | 关联类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fsignid | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 10 | fdatatype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_rsregisterentry |  | fid,fseq |
| 2 | pk_t_mrp_rsregisterentry |  | fentryid |
