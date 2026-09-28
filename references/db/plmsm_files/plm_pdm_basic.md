# 基础模型-plm_pdm_basic

## 基础模型-使用范围表 t_plm_pdm_basic_u

- **表名称：** 基础模型-使用范围表
- **表名：** t_plm_pdm_basic_u

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
| 1 | idx_t_plm_pdm_basic_u_uo |  | fuseorgid |
| 2 | pk_t_plm_pdm_basic_u |  | fdataid,fuseorgid |

---

## 基础模型-多语言表 t_plm_pdm_basic_l

- **表名称：** 基础模型-多语言表
- **表名：** t_plm_pdm_basic_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fdownloadname | fdownloadname | varchar | 1024 |  | √ | ' ' |  |
| 4 | fsyncresult | fsyncresult | varchar | 500 |  | √ | ' ' |  |
| 5 | fspecification | fspecification | varchar | 255 |  | √ | ' ' |  |
| 6 | fdisplayname | 显示名称 | varchar | 2000 |  | √ | ' ' | 显示名称 |
| 7 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 8 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 9 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 10 | fmodelnum | fmodelnum | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pdm_basic_l |  | fpkid |
| 2 | idx_plm_pdm_basic_l_0 |  | fid,flocaleid |

---

## 基础模型-主表 t_plm_pdm_basic

- **表名称：** 基础模型-主表
- **表名：** t_plm_pdm_basic

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flcstatusid | flcstatusid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fmodelid | 业务模型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 5 | frdmversion | 系统版本 | varchar | 10 |  | √ | ' ' | 系统版本 |
| 6 | fconfigcollectid | fconfigcollectid | int8 | 64 |  | √ | 0 |  |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fdatastagebit | 数据阶段位 | int8 | 64 |  | √ | 1 | 数据阶段位 |
| 10 | fhasmaterial | fhasmaterial | bpchar | 1 |  | √ | '-' |  |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fdomainid | 域 | int8 | 64 |  | √ | 0 | 域 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsyncresult | fsyncresult | varchar | 255 |  | √ | ' ' |  |
| 17 | fspecification | fspecification | varchar | 255 |  | √ | ' ' |  |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 20 | fcontainerid | 上下文 | int8 | 64 |  | √ | 0 | [上下文容器 plm_plmsm_container](../plmsm_files/plm_plmsm_container.md) |
| 21 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fbizorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 25 | fdownloadname | fdownloadname | varchar | 1024 |  | √ | ' ' |  |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fdisplayname | 显示名称 | varchar | 1024 |  | √ | ' ' | 显示名称 |
| 28 | fsummary_tag | 显示名称_作废_详情 | text | 0 |  |  | null | 显示名称_作废_详情 |
| 29 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 30 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 31 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 32 | ffolderdomain | ffolderdomain | int8 | 64 |  | √ | 0 |  |
| 33 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 34 | fnumber | 编码 | varchar | 85 |  | √ | ' ' | 编码 |
| 35 | fcadeditstatus | fcadeditstatus | bpchar | 1 |  | √ | '0' |  |
| 36 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 37 | fmodelnum | fmodelnum | varchar | 255 |  | √ | ' ' |  |
| 38 | fsummary | 显示名称_作废 | varchar | 255 |  | √ | ' ' | 显示名称_作废 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_pdm_basic_createorg |  | fcreateorgid |
| 2 | pk_plm_pdm_basic |  | fid |
| 3 | idx_t_plm_pdm_basic_master |  | fmasterid |
| 4 | idx_plm_pdm_basic_name |  | fname |
| 5 | idx_plm_pdm_basic_modelid |  | fmodelid |
| 6 | idx_plm_pdm_basic_number |  | fnumber |
