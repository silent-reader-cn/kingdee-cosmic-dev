# 生命周期模板-plm_lc_tmpl

## 源状态-子表 t_plmsm_lc_tmpl_fstatus

- **表名称：** 源状态-子表
- **表名：** t_plmsm_lc_tmpl_fstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffromstatus | 状态配置 | int8 | 64 |  | √ | 0 | 生命周期状态 plm_lc_status |
| 3 | fparentstageid | 阶段id | int8 | 64 |  | √ | 0 | 阶段id |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmsm_lc_tmpl_fstatus |  | fentryid |
| 2 | idx_plmsm_lc_tmpl_fstatus_fk |  | fid |

---

## 阶段信息-子表 t_plmsm_lc_tmpl_stage

- **表名称：** 阶段信息-子表
- **表名：** t_plmsm_lc_tmpl_stage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstage | 阶段配置 | int8 | 64 |  | √ | 0 | 生命周期阶段 plm_lc_stage |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmsm_lc_tmpl_stage |  | fentryid |
| 2 | idx_plmsm_lc_tmpl_stage_fk |  | fid |

---

## 目标状态-子表 t_plmsm_lc_tmpl_tostatus

- **表名称：** 目标状态-子表
- **表名：** t_plmsm_lc_tmpl_tostatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdoupgrade | 升版 | bpchar | 1 |  | √ | '0' | 升版 |
| 2 | fdocreatedchange | 变更（新增对象） | bpchar | 1 |  | √ | '0' | 变更（新增对象） |
| 3 | fdochange | 变更（变更对象） | bpchar | 1 |  | √ | '0' | 变更（变更对象） |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdosetstatus | 设置状态 | bpchar | 1 |  | √ | '0' | 设置状态 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | ftostatus | 目标状态 | int8 | 64 |  | √ | 0 | 生命周期状态 plm_lc_status |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmsm_lc_tmpl_tostatus |  | fdetailid |
| 2 | idx_plmsm_lc_tmpl_tostatus_fk |  | fentryid |

---

## 生命周期模板-主表 t_plmsm_lc_tmpl

- **表名称：** 生命周期模板-主表
- **表名：** t_plmsm_lc_tmpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftitle_op | 操作 | varchar | 50 |  | √ | '操作' | 操作 |
| 3 | ftitle_op_change | 变更 | varchar | 50 |  | √ | '变更' | 变更 |
| 4 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fpreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 14 | ftitle_op_set | 设置状态 | varchar | 50 |  | √ | '设置状态' | 设置状态 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fopconfig | 操作控制 | varchar | 50 |  | √ | '1,1,N' | 操作控制 |
| 20 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 21 | fmodifycontrol | 修改控制 | varchar | 50 |  |  | 'Y' | 修改控制,枚举: Y :可修改 N :不可修改 |
| 22 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | ftitle_op_upgrade | 升版 | varchar | 50 |  | √ | '升版' | 升版 |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 26 | ftmpldesc | 阶段 | varchar | 1000 |  | √ | ' ' | 阶段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plmsm_lc_tmpl_createorg |  | fcreateorgid |
| 2 | idx_t_plmsm_lc_tmpl_master |  | fmasterid |
| 3 | pk_plmsm_lc_tmpl |  | fid |

---

## 生命周期模板-多语言表 t_plmsm_lc_tmpl_l

- **表名称：** 生命周期模板-多语言表
- **表名：** t_plmsm_lc_tmpl_l

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
| 1 | idx_plmsm_lc_tmpl_l_0 |  | fid,flocaleid |
| 2 | pk_plmsm_lc_tmpl_l |  | fpkid |

---

## 生命周期模板-使用范围表 t_plmsm_lc_tmpl_u

- **表名称：** 生命周期模板-使用范围表
- **表名：** t_plmsm_lc_tmpl_u

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
| 1 | pk_t_plmsm_lc_tmpl_u |  | fdataid,fuseorgid |
| 2 | idx_t_plmsm_lc_tmpl_u_uo |  | fuseorgid |
