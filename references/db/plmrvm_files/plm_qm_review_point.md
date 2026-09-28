# 评审点-plm_qm_review_point

## 质量目标-多选基础资料表 t_plm_review_obj

- **表名称：** 质量目标-多选基础资料表
- **表名：** t_plm_review_obj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [质量目标 plm_qm_objectives](../plmrvm_files/plm_qm_objectives.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_review_obj_fk |  | fid |
| 2 | pk_plm_review_obj |  | fpkid |

---

## 评审点-使用范围表 t_plm_qm_review_point_u

- **表名称：** 评审点-使用范围表
- **表名：** t_plm_qm_review_point_u

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
| 1 | pk_t_plm_qm_review_point_u |  | fdataid,fuseorgid |
| 2 | idx_t_plm_qm_review_point_u_uo |  | fuseorgid |

---

## 评审点-多语言表 t_plm_qm_review_point_l

- **表名称：** 评审点-多语言表
- **表名：** t_plm_qm_review_point_l

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
| 1 | idx_plm_qm_review_point_l_0 |  | fid,flocaleid |
| 2 | pk_plm_qm_review_point_l |  | fpkid |

---

## 后续活动-多选基础资料表 t_plm_rvm_followup_act

- **表名称：** 后续活动-多选基础资料表
- **表名：** t_plm_rvm_followup_act

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [后续活动 plm_qm_followup_activity](../plmrvm_files/plm_qm_followup_activity.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rvm_followup_act_fk |  | fid |
| 2 | pk_plm_rvm_followup_act |  | fpkid |

---

## 评审点-主表 t_plm_qm_review_point

- **表名称：** 评审点-主表
- **表名：** t_plm_qm_review_point

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fappsign | 应用标识 | varchar | 50 |  | √ | ' ' | 应用标识 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fquality_objectives | fquality_objectives | int8 | 64 |  | √ | 0 |  |
| 7 | freview_type | 评审类型 | varchar | 50 |  | √ | ' ' | 评审类型,枚举: TR :TR DCP :DCP GR :GR |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fpreset | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fpicturefield | 状态图片 | varchar | 255 |  | √ | ' ' | 状态图片 |
| 16 | fsort_num | 排序 | int8 | 64 |  | √ | 0 | 排序 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 20 | fplmrmuse | 需求管理专属 | bpchar | 1 |  | √ | '0' | 需求管理专属 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 23 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fcustomsign | 自定义标识 | varchar | 50 |  | √ | ' ' | 自定义标识 |
| 25 | fbasedatafield | 工作项类型 | int8 | 64 |  | √ | 0 | [工作项类型配置 plm_ipditemgroup](../plmipdsm_files/plm_ipditemgroup.md) |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_qm_review_point |  | fid |
| 2 | idx_plm_qm_review_point_m0 |  | fmasterid |
| 3 | idx_t_plm_qm_review_point_master |  | fmasterid |
| 4 | idx_t_plm_qm_review_point_createorg |  | fcreateorgid |
