# 项目设置-状态设置-plm_pm_projectstatusset

## 子单据体-子表 t_plm_pm_statusset_subent

- **表名称：** 子单据体-子表
- **表名：** t_plm_pm_statusset_subent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fieldkey | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_statusset_subent |  | fdetailid |
| 2 | idx_plm_pm_statusset_subent_fk |  | fentryid |

---

## 项目设置-状态设置-主表 t_plm_pm_statussetting

- **表名称：** 项目设置-状态设置-主表
- **表名：** t_plm_pm_statussetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fprojectkind | 项目分类 | varchar | 50 |  | √ | ' ' | 项目分类 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_statussetting_m0 |  | fmasterid |
| 2 | idx_t_plm_pm_statussetting_master |  | fmasterid |
| 3 | idx_t_plm_pm_statussetting_createorg |  | fcreateorgid |
| 4 | pk_plm_pm_statussetting |  | fid |

---

## 单据体-多语言表 t_plm_pm_statusset_entry_l

- **表名称：** 单据体-多语言表
- **表名：** t_plm_pm_statusset_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | foptname | 按钮名称 | varchar | 100 |  | √ | ' ' | 按钮名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_statusset_entry_l |  | fpkid |
| 2 | idx_plm_pm_statusset_entry_l_0 |  | fentryid,flocaleid |

---

## 单据体-子表 t_plm_pm_statusset_entry

- **表名称：** 单据体-子表
- **表名：** t_plm_pm_statusset_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffromstatusseq | 源序号 | int8 | 64 |  | √ | 0 | 源序号 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ftostatusseq | 目标状态序号 | int8 | 64 |  | √ | 0 | 目标状态序号 |
| 5 | ffromstatus | 源状态 | int8 | 64 |  | √ | 0 | [项目状态 plm_pm_projectstatus](../plmpm_files/plm_pm_projectstatus.md) |
| 6 | fbasedatafield | 单据驱动 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 7 | foptname | 按钮名称 | varchar | 100 |  | √ | ' ' | 按钮名称 |
| 8 | ftostatustype | 目标状态类型 | varchar | 50 |  | √ | ' ' | 目标状态类型 |
| 9 | foptmodel | 操作方式 | bpchar | 1 |  | √ | '0' | 操作方式 |
| 10 | fismainline | 是否主线连接点 | bpchar | 1 |  | √ | '0' | 是否主线连接点 |
| 11 | ffromstatustype | 源状态类型 | varchar | 50 |  | √ | ' ' | 源状态类型 |
| 12 | ftostatus | 目标状态 | int8 | 64 |  | √ | 0 | [项目状态 plm_pm_projectstatus](../plmpm_files/plm_pm_projectstatus.md) |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fhasopt | 是否有操作 | bpchar | 1 |  | √ | '0' | 是否有操作 |
| 15 | fischeck | 是否选中 | bpchar | 1 |  | √ | '0' | 是否选中 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_statusset_entry |  | fentryid |
| 2 | idx_plm_pm_statusset_entry_fk |  | fid |

---

## 项目设置-状态设置-使用范围表 t_plm_pm_statussetting_u

- **表名称：** 项目设置-状态设置-使用范围表
- **表名：** t_plm_pm_statussetting_u

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
| 1 | idx_t_plm_pm_statussetting_u_uo |  | fuseorgid |
| 2 | pk_t_plm_pm_statussetting_u |  | fdataid,fuseorgid |

---

## 项目设置-状态设置-多语言表 t_plm_pm_statussetting_l

- **表名称：** 项目设置-状态设置-多语言表
- **表名：** t_plm_pm_statussetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
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
| 1 | idx_plm_pm_statussetting_l_0 |  | fid,flocaleid |
| 2 | pk_plm_pm_statussetting_l |  | fpkid |
