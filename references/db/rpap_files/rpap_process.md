# 流程-rpap_process

## 流程-使用范围表 t_rpap_process_u

- **表名称：** 流程-使用范围表
- **表名：** t_rpap_process_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | 0 |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rpap_process_u_co |  | fcreateorgid |
| 2 | pk_t_rpap_process_u |  | fdataid,fuseorgid |

---

## 流程-多语言表 t_rpap_process_l

- **表名称：** 流程-多语言表
- **表名：** t_rpap_process_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 流程名称 | varchar | 255 |  |  | ' ' | 流程名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_rpap_process_l_fid |  | fid |
| 2 | pk_t_rpap_process_l |  | fpkid |

---

## 流程-使用范围位图表 t_rpap_process_m

- **表名称：** 流程-使用范围位图表
- **表名：** t_rpap_process_m

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
| 1 | pk_t_rpap_process_m |  | forgid |

---

## 流程-主表 t_rpap_process

- **表名称：** 流程-主表
- **表名：** t_rpap_process

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexternalid | 外部id | varchar | 255 |  |  | ' ' | 外部id |
| 3 | fthirdtypeid | 第三方类型 | int8 | 64 |  | √ | 0 | [第三方类型 rpap_thirdtype](../rpap_files/rpap_thirdtype.md) |
| 4 | forgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fisdelete | 是否已经删除 | varchar | 10 |  | √ | '0' | 是否已经删除,枚举: 1 :已删除 0 :未删除 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fremark | 简介 | varchar | 255 |  |  | ' ' | 简介 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fname | fname | varchar | 255 |  |  | ' ' |  |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fversionid | 流程版本 | int8 | 64 |  | √ | 0 | [流程版本 rpap_processversion](../rpap_files/rpap_processversion.md) |
| 19 | freleasestatus | 发布状态 | varchar | 10 |  | √ | ' ' | 发布状态,枚举: 0 :未发布 1 :已发布 |
| 20 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 21 | fprojectname | 工程名称 | varchar | 100 |  |  | ' ' | 工程名称 |
| 22 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :停用 1 :启用 |
| 23 | fnumber | 流程编号 | varchar | 255 |  |  | ' ' | 流程编号 |
| 24 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_rpap_process_createorg |  | fcreateorgid |
| 2 | pk_t_rpap_process |  | fid |
| 3 | idx_rpap_process_externalid |  | fexternalid,fthirdtypeid |
| 4 | idx_t_rpap_process_master |  | fmasterid |
| 5 | idx_t_rpap_process_orgid |  | forgid |

---

## 单据体-子表 t_rpap_argumententry

- **表名称：** 单据体-子表
- **表名：** t_rpap_argumententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fargumentname | 参数名 | varchar | 255 |  |  | ' ' | 参数名 |
| 3 | fargumentvalue | 参数值 | text | 0 |  |  | null | 参数值 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fargumenttype | 参数类型 | varchar | 255 |  |  | ' ' | 参数类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rpap_argumententry |  | fentryid |
| 2 | idx_t_rpap_argentry_fid |  | fid |
