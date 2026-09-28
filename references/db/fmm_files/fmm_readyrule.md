# 资源就绪检查规则-fmm_readyrule

## 资源就绪检查规则-使用范围表 t_fmm_readyrule_u

- **表名称：** 资源就绪检查规则-使用范围表
- **表名：** t_fmm_readyrule_u

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
| 1 | pk_t_fmm_readyrule_u |  | fdataid,fuseorgid |
| 2 | idx_t_fmm_readyrule_u_uo |  | fuseorgid |

---

## 资源就绪检查规则-使用范围位图表 t_fmm_readyrule_m

- **表名称：** 资源就绪检查规则-使用范围位图表
- **表名：** t_fmm_readyrule_m

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
| 1 | pk_t_fmm_readyrule_m |  | forgid |

---

## 资源就绪检查规则-多语言表 t_fmm_readyrule_l

- **表名称：** 资源就绪检查规则-多语言表
- **表名：** t_fmm_readyrule_l

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
| 1 | idx_fmm_readyrule_l |  | fid,flocaleid |
| 2 | pk_fmm_readyrule_l |  | fpkid |

---

## 详细信息-子表 t_fmm_readyruledetail

- **表名称：** 详细信息-子表
- **表名：** t_fmm_readyruledetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrycalculatetext | 计算公式 | varchar | 2000 |  | √ | ' ' | 计算公式 |
| 3 | fentryruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: A :计算公式 B :自定义插件 |
| 4 | fentrysourcefiled | 资源对象标识 | varchar | 255 |  | √ | ' ' | 资源对象标识 |
| 5 | fentrysourcefiledname | 资源对象名称 | varchar | 255 |  | √ | ' ' | 资源对象名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentrycalculateexc_tag | 计算公式_详情 | text | 0 |  |  | null | 计算公式_详情 |
| 8 | fentryalgoregister | 自定义插件 | int8 | 64 |  | √ | 0 | [算法注册配置 mrp_algoregister](../msplan_files/mrp_algoregister.md) |
| 9 | fentrycalculateexc | 计算公式 | varchar | 255 |  | √ | ' ' | 计算公式 |
| 10 | fentrycalcorder | 计算顺序 | int4 | 32 |  | √ | 0 | 计算顺序 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fentryrelationfiledflag | 关联对象标识 | varchar | 255 |  | √ | ' ' | 关联对象标识 |
| 13 | fentryrelationfiledname | 关联对象名称 | varchar | 255 |  | √ | ' ' | 关联对象名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_readyruledetail_fk |  | fid |
| 2 | pk_fmm_readyruledetail |  | fentryid |

---

## 资源就绪检查规则-主表 t_fmm_readyrule

- **表名称：** 资源就绪检查规则-主表
- **表名：** t_fmm_readyrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsrcbillid | 资源对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | freadylevelid | 就绪状态优先级 | int8 | 64 |  | √ | 0 | [就绪状态优先级定义 fmm_readylevel](../fmm_files/fmm_readylevel.md) |
| 15 | fdestbillid | 关联对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbillfieldtransferid | 实体字段映射 | int8 | 64 |  | √ | 0 | [实体字段映射 mrp_billfieldtransfer](../msplan_files/mrp_billfieldtransfer.md) |
| 18 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 19 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fmm_readyrule_createorg |  | fcreateorgid |
| 2 | idx_t_fmm_readyrule_master |  | fmasterid |
| 3 | pk_fmm_readyrule |  | fid |
