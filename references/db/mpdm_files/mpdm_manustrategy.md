# 制造策略-mpdm_manustrategy

## 制造策略-主表 t_mpdm_manustrategy

- **表名称：** 制造策略-主表
- **表名：** t_mpdm_manustrategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 计划策略分组 | int8 | 64 |  | √ | 0 | [计划策略分组 mpdm_demandmodel_group](../mpdm_files/mpdm_demandmodel_group.md) |
| 3 | fisinway | 考虑在途/在制 | bpchar | 1 |  | √ | ' ' | 考虑在途/在制 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdemandmodel | 计划模式 | varchar | 30 |  | √ | ' ' | 计划模式,枚举: MTS :MTS MTO :MTO ATO :ATO ETO :ETO STO :STO |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fissystemdesign | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | forgdemandtypeid | 组织间需求类型 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fexdemandtypeid | 预测需求类型 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fissafestock | 考虑安全库存 | bpchar | 1 |  | √ | ' ' | 考虑安全库存 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fiscurrentstock | 考虑即时库存 | bpchar | 1 |  | √ | ' ' | 考虑即时库存 |
| 21 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 策略编码 | varchar | 30 |  | √ | ' ' | 策略编码 |
| 24 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 25 | fcusdemandtypeid | 客户需求类型 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_manustrategy |  | fnumber,fcreateorgid |
| 2 | idx_t_mpdm_manustrategy_master |  | fmasterid |
| 3 | t_mpdm_manustrategy_pkey |  | fid |
| 4 | idx_t_mpdm_manustrategy_createorg |  | fcreateorgid |

---

## 制造策略-多语言表 t_mpdm_manustrategy_l

- **表名称：** 制造策略-多语言表
- **表名：** t_mpdm_manustrategy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 策略名称 | varchar | 100 |  | √ | ' ' | 策略名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_manustrategy_l_pkey |  | fpkid |
| 2 | idx_mpdm_manustrategy_l |  | fid,flocaleid |

---

## 制造策略-使用范围位图表 t_mpdm_manustrategy_m

- **表名称：** 制造策略-使用范围位图表
- **表名：** t_mpdm_manustrategy_m

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
| 1 | pk_t_mpdm_manustrategy_m |  | forgid |

---

## 制造策略-使用范围表 t_mpdm_manustrategy_u

- **表名称：** 制造策略-使用范围表
- **表名：** t_mpdm_manustrategy_u

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
| 1 | t_mpdm_manustrategy_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_mpdm_manustrategy_u_uo |  | fuseorgid |
