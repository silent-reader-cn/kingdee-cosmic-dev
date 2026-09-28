# 发布单-plm_plmdc_release

## 发布单-主表 t_plmdc_release

- **表名称：** 发布单-主表
- **表名：** t_plmdc_release

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsigninstatus | 签收状态 | varchar | 50 |  | √ | ' ' | 签收状态,枚举: unreceipted :待签收 partreceipted :部分签收 receipted :已签收 rejected :已拒签 noneedreceipted :无需签收 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ftreleaseobject | 发布对象信息 | varchar | 2000 |  | √ | ' ' | 发布对象信息 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | freleasetimefieldfrelease | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 9 | fexpiredatefield | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 10 | freleasestatus | 发布单状态 | varchar | 50 |  | √ | ' ' | 发布单状态,枚举: unpublished :未发布 published :已发布 newpublished :已发布 partrecycled :部分回收 recycled :已回收 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fsource | 来源 | varchar | 50 |  | √ | ' ' | 来源,枚举: A :手工创建 B :流程创建 |
| 13 | fbillname | 发布主题 | varchar | 255 |  | √ | ' ' | 发布主题 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fsignature | 签收情况 | varchar | 255 |  | √ | ' ' | 签收情况 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | freleaseremark | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 18 | fflownodeid | 流程节点 | varchar | 50 |  | √ | ' ' | 流程节点 |
| 19 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fflowid | 流程 | int8 | 64 |  | √ | 0 | [流程管理 wf_processdefinition](../wf_files/wf_processdefinition.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_release |  | fid |
| 2 | idx_plmdc_release_fid |  | fbillno |

---

## 文档对象-子表 t_plmdc_release_objects

- **表名称：** 文档对象-子表
- **表名：** t_plmdc_release_objects

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | freleaseobjectstatus | 发布状态 | varchar | 50 |  | √ | ' ' | 发布状态,枚举: unpublished :未发布 published :已发布 partrecycled :部分回收 recycled :已回收 |
| 4 | frecipientobjids_tag | 已回收的对象_详情 | text | 0 |  |  | ' ' | 已回收的对象_详情 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | frecipientobjids | 已回收的对象 | varchar | 255 |  | √ | ' ' | 已回收的对象 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | freleaseobject | 对象编码 | int8 | 64 |  | √ | 0 | [文档版本 plm_pdm_document_revision](../plmsm_files/plm_pdm_document_revision.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_relobj_fentryid |  | fid |
| 2 | idx_plmdc_relobj_obj |  | freleaseobject |
| 3 | pk_t_plmdc_release_objects |  | fentryid |

---

## 人员对象-子表 t_plmdc_release_users

- **表名称：** 人员对象-子表
- **表名：** t_plmdc_release_users

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frecipienttype | 接收者类型 | varchar | 50 |  | √ | ' ' | 接收者类型,枚举: usergroup :用户组 department :部门 role :角色 user :用户 |
| 3 | fentitysignature | 签收情况 | varchar | 255 |  | √ | ' ' | 签收情况 |
| 4 | fentitysigninstatus | 签收状态 | varchar | 50 |  | √ | ' ' | 签收状态,枚举: unreceipted :待签收 partreceipted :部分签收 receipted :已签收 rejected :已拒签 noneedreceipted :无需签收 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | frecipientobjid | 接收者对象Id | varchar | 255 |  | √ | ' ' | 接收者对象Id |
| 7 | fopendocright | 打开文档 | bpchar | 1 |  | √ | '1' | 打开文档 |
| 8 | fdowloaddocright | 下载文档 | bpchar | 1 |  | √ | '0' | 下载文档 |
| 9 | fviewdocright | 查看文档 | bpchar | 1 |  | √ | '1' | 查看文档 |
| 10 | fviewpdfright | 浏览PDF | bpchar | 1 |  | √ | '0' | 浏览PDF |
| 11 | fviewlightright | 浏览轻量化 | bpchar | 1 |  | √ | '0' | 浏览轻量化 |
| 12 | fsignobject | 签收用户对象 | int8 | 64 |  | √ | 0 | [签收用户组 plm_plmdc_sign_group](../plmdc_files/plm_plmdc_sign_group.md) |
| 13 | fdowloadstepright | 下载STEP | bpchar | 1 |  | √ | '0' | 下载STEP |
| 14 | fsendsubject | 发送主体 | varchar | 50 |  | √ | ' ' | 发送主体,枚举: A :收件人 B :抄送 人 |
| 15 | fsignusers | 接收者 | varchar | 255 |  | √ | ' ' | 接收者 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fdowloadpdfright | 下载PDF | bpchar | 1 |  | √ | '0' | 下载PDF |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_reluser_rec |  | frecipientobjid |
| 2 | pk_t_plmdc_release_users |  | fentryid |
| 3 | idx_plmdc_reluser_entryid |  | fid |

---

## 发布单-多语言表 t_plmdc_release_l

- **表名称：** 发布单-多语言表
- **表名：** t_plmdc_release_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fbillname | 发布主题 | varchar | 255 |  | √ | ' ' | 发布主题 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_release_l |  | fpkid |
| 2 | idx_plmdc_release_l_fpkid |  | fid |
