# 状态设置(组织受控)-plm_ipdsm_lc_template_org

## 状态-多选基础资料表 t_plm_ipd_mul_lc

- **表名称：** 状态-多选基础资料表
- **表名：** t_plm_ipd_mul_lc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 状态 plm_ipd_lc_status |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_mul_lc |  | fpkid |
| 2 | idx_plm_ipd_mul_lc_fk |  | fentryid |

---

## 单据体-子表 t_ipd_lc_business_ctrl

- **表名称：** 单据体-子表
- **表名：** t_ipd_lc_business_ctrl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbusinessctrl | 业务控制 | int8 | 64 |  | √ | 0 | 状态设置业务控制 plm_ipdsm_businessctrl |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fbusiness | 业务控制 | varchar | 50 |  | √ | ' ' | 业务控制 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipd_lc_business_ctrl_fk |  | fid |
| 2 | pk_ipd_lc_business_ctrl |  | fentryid |

---

## 源状态单据体-子表 t_ipd_lc_tmpl_fstatus

- **表名称：** 源状态单据体-子表
- **表名：** t_ipd_lc_tmpl_fstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffromstatus | 源状态 | int8 | 64 |  | √ | 0 | 状态 plm_ipd_lc_status |
| 3 | ffromstatusseq | 源序号 | int8 | 64 |  | √ | 0 | 源序号 |
| 4 | fcheckconfig | 多选控制 | varchar | 50 |  | √ | ' ' | 多选控制,枚举: N :多选 1 :单选 0 :不可选 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipd_lc_tmpl_fstatus |  | fentryid |
| 2 | idx_ipd_lc_tmpl_fstatus_fk |  | fid |

---

## 状态设置(组织受控)-使用范围表 t_ipd_lc_template_u

- **表名称：** 状态设置(组织受控)-使用范围表
- **表名：** t_ipd_lc_template_u

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
| 1 | pk_t_ipd_lc_template_u |  | fdataid,fuseorgid |
| 2 | idx_t_ipd_lc_template_u_uo |  | fuseorgid |

---

## 目标状态子单据体-子表 t_ipd_lc_tmpl_tostatus

- **表名称：** 目标状态子单据体-子表
- **表名：** t_ipd_lc_tmpl_tostatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftostatusseq | 目标状态序号 | int8 | 64 |  | √ | 0 | 目标状态序号 |
| 2 | fcheck | 是否选中 | bpchar | 1 |  | √ | '0' | 是否选中 |
| 3 | flocked | 是否锁定 | bpchar | 1 |  | √ | '0' | 是否锁定 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | ftostatus | 目标状态 | int8 | 64 |  | √ | 0 | 状态 plm_ipd_lc_status |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipd_lc_tmpl_tostatus |  | fdetailid |
| 2 | idx_ipd_lc_tmpl_tostatus_fk |  | fentryid |

---

## 状态设置(组织受控)-主表 t_ipd_lc_template

- **表名称：** 状态设置(组织受控)-主表
- **表名：** t_ipd_lc_template

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fjson | JSON | varchar | 255 |  | √ | ' ' | JSON |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fapptype | 所属应用类型 | varchar | 50 |  | √ | ' ' | 所属应用类型 |
| 10 | fentitykey | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 11 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 19 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fjson_tag | JSON_详情 | text | 0 |  |  | null | JSON_详情 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ipd_lc_template_createorg |  | fcreateorgid |
| 2 | idx_t_ipd_lc_template_master |  | fmasterid |
| 3 | pk_ipd_lc_template |  | fid |
| 4 | idx_ipd_lc_template_m0 |  | fmasterid |

---

## 状态设置(组织受控)-多语言表 t_ipd_lc_template_l

- **表名称：** 状态设置(组织受控)-多语言表
- **表名：** t_ipd_lc_template_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipd_lc_template_l |  | fpkid |
| 2 | idx_ipd_lc_template_l_0 |  | fid,flocaleid |
