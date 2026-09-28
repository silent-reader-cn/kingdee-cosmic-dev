# 资源就绪检查方案-fmm_readyplan

## 计划视角-子表 t_fmm_readyplandetailp

- **表名称：** 计划视角-子表
- **表名：** t_fmm_readyplandetailp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryplanorder | 检查顺序 | int4 | 32 |  | √ | 0 | 检查顺序 |
| 3 | fentryplanreadyrule | 资源就绪检查规则 | int8 | 64 |  | √ | 0 | 资源就绪检查规则 fmm_readyrule |
| 4 | fentryplanrestype | 资源类型 | varchar | 255 |  | √ | ' ' | 资源类型,枚举: 0 :物料 1 :设备 2 :工具 3 :文件 4 :技术支持 5 :工卡 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryplanfieldtransfer | 资源就绪匹配规则 | int8 | 64 |  | √ | 0 | 实体字段映射 mrp_billfieldtransfer |
| 8 | fentryplanresbill | 资源对象 | varchar | 255 |  | √ | ' ' | 业务对象 bos_objecttype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_readyplandetailp |  | fid |
| 2 | pk_fmm_readyplandetailp |  | fentryid |

---

## 执行视角-子表 t_fmm_readyplandetaile

- **表名称：** 执行视角-子表
- **表名：** t_fmm_readyplandetaile

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryexeresbill | 资源对象 | varchar | 255 |  | √ | ' ' | 业务对象 bos_objecttype |
| 3 | fentryexeorder | 检查顺序 | int4 | 32 |  | √ | 0 | 检查顺序 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryexerestype | 资源类型 | varchar | 255 |  | √ | ' ' | 资源类型,枚举: 0 :物料 1 :设备 2 :工具 3 :文件 4 :技术支持 5 :工卡 |
| 6 | fentryexereadyrule | 资源就绪检查规则 | int8 | 64 |  | √ | 0 | 资源就绪检查规则 fmm_readyrule |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryexefieldtransfer | 资源就绪匹配规则 | int8 | 64 |  | √ | 0 | 实体字段映射 mrp_billfieldtransfer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_readyplandetaile |  | fid |
| 2 | pk_fmm_readyplandetaile |  | fentryid |

---

## 资源就绪检查方案-多语言表 t_fmm_readyplan_l

- **表名称：** 资源就绪检查方案-多语言表
- **表名：** t_fmm_readyplan_l

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
| 1 | idx_fmm_readyplan_l |  | fid,flocaleid |
| 2 | pk_fmm_readyplan_l |  | fpkid |

---

## 资源就绪检查方案-使用范围位图表 t_fmm_readyplan_m

- **表名称：** 资源就绪检查方案-使用范围位图表
- **表名：** t_fmm_readyplan_m

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
| 1 | pk_t_fmm_readyplan_m |  | forgid |

---

## 资源就绪检查方案-使用范围表 t_fmm_readyplan_u

- **表名称：** 资源就绪检查方案-使用范围表
- **表名：** t_fmm_readyplan_u

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
| 1 | idx_t_fmm_readyplan_u_uo |  | fuseorgid |
| 2 | pk_t_fmm_readyplan_u |  | fdataid,fuseorgid |

---

## 资源就绪检查方案-主表 t_fmm_readyplan

- **表名称：** 资源就绪检查方案-主表
- **表名：** t_fmm_readyplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fresregisterdemand | 资源需求模型 | int8 | 64 |  | √ | 0 | 资源注册模型 mrp_resourceregister_cf |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fresregistersupply | 资源供应模型 | int8 | 64 |  | √ | 0 | 资源注册模型 mrp_resourceregister_cf |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | freadylevelid | 就绪状态优先级 | int8 | 64 |  | √ | 0 | 就绪状态优先级定义 fmm_readylevel |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 20 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_readyplan |  | fid |
| 2 | idx_pk_fmm_readyplan_number |  | fnumber |
| 3 | idx_t_fmm_readyplan_createorg |  | fcreateorgid |
| 4 | idx_t_fmm_readyplan_master |  | fmasterid |
