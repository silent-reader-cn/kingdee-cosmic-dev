# 基础模型版次-plm_pdm_basic_v

## 基础模型版次-多语言表 t_plm_pdm_version_l

- **表名称：** 基础模型版次-多语言表
- **表名：** t_plm_pdm_version_l

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
| 1 | idx_plm_pdm_version_l_0 |  | fid,flocaleid |
| 2 | pk_plm_pdm_version_l |  | fpkid |

---

## 基础模型版次-使用范围表 t_plm_pdm_version_u

- **表名称：** 基础模型版次-使用范围表
- **表名：** t_plm_pdm_version_u

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
| 1 | idx_t_plm_pdm_version_u_uo |  | fuseorgid |
| 2 | pk_t_plm_pdm_version_u |  | fdataid,fuseorgid |

---

## 基础模型版次-主表 t_plm_pdm_version

- **表名称：** 基础模型版次-主表
- **表名：** t_plm_pdm_version

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flcstatusid | flcstatusid | int8 | 64 |  | √ | 0 |  |
| 3 | fcheckoutstatus | fcheckoutstatus | varchar | 50 |  | √ | ' ' |  |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodelid | 业务模型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 6 | frdmversion | 系统版本 | varchar | 10 |  | √ | ' ' | 系统版本 |
| 7 | fconfigcollectid | fconfigcollectid | int8 | 64 |  | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | frevison | frevison | varchar | 50 |  | √ | ' ' |  |
| 11 | fdatastagebit | 数据阶段位 | int8 | 64 |  | √ | 1 | 数据阶段位 |
| 12 | fhasmaterial | fhasmaterial | bpchar | 1 |  | √ | '1' |  |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fmasterbizid | fmasterbizid | int8 | 64 |  | √ | 0 |  |
| 15 | fdomainid | 域 | int8 | 64 |  | √ | 0 | 域 |
| 16 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fcheckouttorid | fcheckouttorid | int8 | 64 |  | √ | 0 |  |
| 20 | fsyncresult | fsyncresult | varchar | 255 |  | √ | ' ' |  |
| 21 | fspecification | fspecification | varchar | 255 |  | √ | ' ' |  |
| 22 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 23 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 24 | fupgradedesc | fupgradedesc | varchar | 255 |  | √ | ' ' |  |
| 25 | fcontainerid | 上下文 | int8 | 64 |  | √ | 0 | [上下文容器 plm_plmsm_container](../plmsm_files/plm_plmsm_container.md) |
| 26 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fbizorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 30 | fdownloadname | fdownloadname | varchar | 1024 |  | √ | ' ' |  |
| 31 | fbranchid | fbranchid | int8 | 64 |  | √ | 0 |  |
| 32 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | fdisplayname | 显示名称 | varchar | 1024 |  | √ | ' ' | 显示名称 |
| 34 | fsummary_tag | 显示名称_作废_详情 | text | 0 |  |  | null | 显示名称_作废_详情 |
| 35 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 36 | flcstatusld | flcstatusld | int8 | 64 |  | √ | 0 |  |
| 37 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 38 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 39 | ffolderdomain | ffolderdomain | int8 | 64 |  | √ | 0 |  |
| 40 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 41 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 42 | fcadeditstatus | fcadeditstatus | bpchar | 1 |  | √ | '0' |  |
| 43 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 44 | fmodelnum | fmodelnum | varchar | 255 |  | √ | ' ' |  |
| 45 | fsummary | 显示名称_作废 | varchar | 255 |  | √ | ' ' | 显示名称_作废 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pdm_version |  | fid |
| 2 | idx_t_plm_pdm_version_createorg |  | fcreateorgid |
| 3 | idx_plm_pdm_version_fnumber |  | fnumber |
| 4 | idx_plm_pdm_version_modelid |  | fmodelid |
| 5 | idx_t_plm_pdm_version_master |  | fmasterid |
