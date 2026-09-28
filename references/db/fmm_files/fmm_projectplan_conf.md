# 项目计划同步设置-fmm_projectplan_conf

## 项目计划同步设置-主表 t_fmm_projectplanconf

- **表名称：** 项目计划同步设置-主表
- **表名：** t_fmm_projectplanconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 项目组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fsyncobj | 同步对象 | varchar | 50 |  | √ | ' ' | 同步对象,枚举: A :WBS B :里程碑 C :标准任务 |
| 11 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fdefconf | 默认设置 | bpchar | 1 |  | √ | '0' | 默认设置 |
| 15 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fmm_projectplanconf_createorg |  | fcreateorgid |
| 2 | idx_t_fmm_projectplanconf_master |  | fmasterid |
| 3 | idx_fmm_projectplanconf_fnum |  | fnumber |
| 4 | idx_mm_projectplanconf_fcd |  | fcreateorgid |
| 5 | idx_mm_projectplanconf_fct |  | fcreatetime |
| 6 | pk_fmm_projectplanconf |  | fid |

---

## 联动策略-子表 t_fmm_projectplanstra

- **表名称：** 联动策略-子表
- **表名：** t_fmm_projectplanstra

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fsourceplantype1 | 联动项目计划类型 | int8 | 64 |  | √ | 0 | 项目计划类型 fmm_plantype |
| 4 | fsourceplantypeid | 项目计划类型 | int8 | 64 |  | √ | 0 | 项目计划类型 fmm_plantype |
| 5 | feedit | 编辑启用 | bpchar | 1 |  | √ | '0' | 编辑启用 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fedelete | 删除启用 | bpchar | 1 |  | √ | '0' | 删除启用 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fenew | 新增启用 | bpchar | 1 |  | √ | '0' | 新增启用 |
| 10 | fcombofield | 联动节点 | varchar | 50 |  | √ | ' ' | 联动节点,枚举: A :发布前 B :发布后 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_projectplanstra |  | fentryid |
| 2 | idx_fmm_projectplanstra_fseq |  | fid,fseq |

---

## 项目计划同步设置-多语言表 t_fmm_projectplanconf_l

- **表名称：** 项目计划同步设置-多语言表
- **表名：** t_fmm_projectplanconf_l

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
| 1 | pk_fmm_projectplanconf_l |  | fpkid |
| 2 | idx_fmm_projectplanconf_l |  | fid,flocaleid |

---

## 项目计划同步设置-使用范围表 t_fmm_projectplanconf_u

- **表名称：** 项目计划同步设置-使用范围表
- **表名：** t_fmm_projectplanconf_u

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
| 1 | idx_t_fmm_projectplanconf_u_uo |  | fuseorgid |
| 2 | pk_t_fmm_projectplanconf_u |  | fdataid,fuseorgid |
