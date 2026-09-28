# 评审要素-plm_qm_review_elements

## 通用角色-多选基础资料表 t_plm_rvm_resp_role

- **表名称：** 通用角色-多选基础资料表
- **表名：** t_plm_rvm_resp_role

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rvm_resp_role |  | fpkid |
| 2 | idx_plm_rvm_resp_role_fk |  | fid |

---

## 评审要素-多语言表 t_plm_qm_review_elements_l

- **表名称：** 评审要素-多语言表
- **表名：** t_plm_qm_review_elements_l

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
| 1 | pk_plm_qm_review_elements_l |  | fpkid |
| 2 | idx_plm_qm_review_elements_l_0 |  | fid,flocaleid |

---

## 评审要素-使用范围表 t_plm_qm_review_elements_u

- **表名称：** 评审要素-使用范围表
- **表名：** t_plm_qm_review_elements_u

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
| 1 | pk_t_plm_qm_review_elements_u |  | fdataid,fuseorgid |
| 2 | idx_t_plm_qm_review_elements_u_uo |  | fuseorgid |

---

## PLM角色-多选基础资料表 t_plm_pri_role

- **表名称：** PLM角色-多选基础资料表
- **表名：** t_plm_pri_role

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [PLM角色 plm_plmsm_role](../plmsm_files/plm_plmsm_role.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pri_role_fk |  | fid |
| 2 | pk_plm_pri_role |  | fpkid |

---

## 评审要素-主表 t_plm_qm_review_elements

- **表名称：** 评审要素-主表
- **表名：** t_plm_qm_review_elements

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | felement_group | 要素分类 | int8 | 64 |  | √ | 0 | [要素分类 plm_qm_element_group](../plmrvm_files/plm_qm_element_group.md) |
| 3 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fappsign | 应用标识 | varchar | 50 |  | √ | ' ' | 应用标识 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fpreset | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fquality_requirement | 质量要求 | varchar | 255 |  | √ | ' ' | 质量要求 |
| 15 | fpicturefield | 状态图片 | varchar | 255 |  | √ | ' ' | 状态图片 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 19 | fplmrmuse | 需求管理专属 | bpchar | 1 |  | √ | '0' | 需求管理专属 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | finstruction | 操作指南 | varchar | 255 |  | √ | ' ' | 操作指南 |
| 22 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 23 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fcustomsign | 自定义标识 | varchar | 50 |  | √ | ' ' | 自定义标识 |
| 25 | freview_ponit | 评审点 | int8 | 64 |  | √ | 0 | [评审点 plm_qm_review_point](../plmrvm_files/plm_qm_review_point.md) |
| 26 | facceptance_criteria | 验收标准 | varchar | 255 |  | √ | ' ' | 验收标准 |
| 27 | fresponsibility_role | fresponsibility_role | varchar | 36 |  | √ | ' ' |  |
| 28 | frole_type | 角色类型 | varchar | 50 |  | √ | ' ' | 角色类型,枚举: A :通用角色 B :PLM角色 |
| 29 | fbasedatafield | 工作项类型 | int8 | 64 |  | √ | 0 | [工作项类型配置 plm_ipditemgroup](../plmipdsm_files/plm_ipditemgroup.md) |
| 30 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 32 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_qm_review_elements_master |  | fmasterid |
| 2 | idx_plm_qm_review_elements_m0 |  | fmasterid |
| 3 | pk_plm_qm_review_elements |  | fid |
| 4 | idx_t_plm_qm_review_elements_createorg |  | fcreateorgid |
