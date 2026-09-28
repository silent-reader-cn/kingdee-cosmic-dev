# 回收单-plm_plmdc_recycle

## 回收对象-子表 t_plmdc_recovery_objects

- **表名称：** 回收对象-子表
- **表名：** t_plmdc_recovery_objects

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | freleaseversion | 发布版本 | varchar | 255 |  | √ | ' ' | 发布版本 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | freleaseobject | 对象编码 | int8 | 64 |  | √ | 0 | [文档版本 plm_pdm_document_revision](../plmsm_files/plm_pdm_document_revision.md) |
| 8 | fitemmasterid | 主数据 | varchar | 255 |  | √ | ' ' | 主数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_recovery_objects |  | fentryid |
| 2 | idx_plmdc_recobj_fid |  | fid |
| 3 | idx_plmdc_recobj_mast |  | fitemmasterid |

---

## 文档版本对象-多选基础资料表 t_plmdc_recovery_doc

- **表名称：** 文档版本对象-多选基础资料表
- **表名：** t_plmdc_recovery_doc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [文档版本 plm_pdm_document_revision](../plmsm_files/plm_pdm_document_revision.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_rec_doc_eid |  | fentryid |
| 2 | pk_t_plmdc_recovery_doc |  | fpkid |

---

## 回收单-主表 t_plmdc_recycle

- **表名称：** 回收单-主表
- **表名：** t_plmdc_recycle

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frelatedrelease_tag | 关联发布单_详情 | text | 0 |  |  | ' ' | 关联发布单_详情 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 回收主题 | varchar | 200 |  | √ | ' ' | 回收主题 |
| 5 | frecycletime | 回收时间 | timestamp | 0 |  |  | null | 回收时间 |
| 6 | ftreleaseobject | 回收对象信息 | varchar | 2000 |  | √ | ' ' | 回收对象信息 |
| 7 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | frecyclemark | 回收说明 | varchar | 255 |  | √ | ' ' | 回收说明 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | frecyclestatus | 回收状态 | varchar | 50 |  | √ | ' ' | 回收状态,枚举: A :未回收 B :已回收 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | frelatedrelease | 关联发布单 | varchar | 255 |  | √ | ' ' | 关联发布单 |
| 16 | fbillno | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmdc_recycle |  | fid |
| 2 | idx_plmdc_recycle |  | fbillno |

---

## 回收单-多语言表 t_plmdc_recycle_l

- **表名称：** 回收单-多语言表
- **表名：** t_plmdc_recycle_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 回收主题 | varchar | 255 |  | √ | ' ' | 回收主题 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_recycle_l |  | fpkid |
| 2 | idx_plmdc_recycle_l_pkid |  | fid |

---

## 参与人员-子表 t_plmdc_recycle_users

- **表名称：** 参与人员-子表
- **表名：** t_plmdc_recycle_users

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frecipienttype | 参与人类别 | varchar | 50 |  | √ | ' ' | 参与人类别,枚举: usergroup :用户组 department :部门 role :角色 user :用户 |
| 3 | fsignobject | 签收用户对象 | int8 | 64 |  | √ | 0 | [签收用户组 plm_plmdc_sign_group](../plmdc_files/plm_plmdc_sign_group.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | frecipientobjid | 接收者对象Id | varchar | 100 |  | √ | ' ' | 接收者对象Id |
| 6 | fsignusers | 参与人员名称 | varchar | 255 |  | √ | ' ' | 参与人员名称 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_recusers_fentryid |  | fid |
| 2 | pk_plmdc_recycle_users |  | fentryid |
