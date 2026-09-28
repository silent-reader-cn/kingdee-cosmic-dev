# 权限交接-xkperm_handover_bill

## 明细字段子单据体-子表 t_xkperm_hd_feilddsentry

- **表名称：** 明细字段子单据体-子表
- **表名：** t_xkperm_hd_feilddsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldappid | 应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 2 | ffieldentityid | 业务对象 | varchar | 50 |  |  | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentitytypeid | fentitytypeid | varchar | 50 |  |  | ' ' |  |
| 6 | fcontrolmode | 控制模式 | varchar | 50 |  |  | ' ' | 控制模式 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | ffieldkey | 字段编码 | varchar | 50 |  |  | ' ' | 字段编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__xkperm_hd_feildds_id |  | fentryid |
| 2 | pk_xkperm_hd_feilddsentry |  | fdetailid |

---

## 权限交接-多语言表 t_xkperm_handover_bill_l

- **表名称：** 权限交接-多语言表
- **表名：** t_xkperm_handover_bill_l

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
| 1 | pk_xkperm_handover_bill_l |  | fpkid |
| 2 | idx_xkperm_handover_bill_l_fid |  | fid,flocaleid |

---

## 管理员分组-多选基础资料表 t_xkperm_hdbill_admins

- **表名称：** 管理员分组-多选基础资料表
- **表名：** t_xkperm_hdbill_admins

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [管理员分组 perm_admingroup](../base_files/perm_admingroup.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkperm_hdbill_admins |  | fpkid |
| 2 | idx_pk_xkperm_hdbill_admins_id |  | fid,fbasedataid |

---

## 基础资料范围数据规则-子表 t_xkperm_hd_drprsentry

- **表名称：** 基础资料范围数据规则-子表
- **表名：** t_xkperm_hd_drprsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdrfieldkey | 字段标识 | varchar | 50 |  |  | ' ' | 字段标识 |
| 2 | fprdrjson | 数据规则方案内容 | varchar | 255 |  | √ | ' ' | 数据规则方案内容 |
| 3 | fprdrjson_tag | 数据规则方案内容_详情 | text | 0 |  |  | null | 数据规则方案内容_详情 |
| 4 | fprdrentityid | 业务对象 | varchar | 50 |  |  | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdrentitytypeid | 字段类型 | varchar | 50 |  |  | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 7 | fprdrappid | 应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 8 | fprdataruleid | 数据规则方案id | int8 | 64 |  | √ | 0 | 数据规则方案id |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkperm_hd_drprsentry_id |  | fentryid |
| 2 | pk_xkperm_hd_drprsentry |  | fdetailid |

---

## 功能权限子单据体-子表 t_xkperm_hd_funcsentry

- **表名称：** 功能权限子单据体-子表
- **表名：** t_xkperm_hd_funcsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fpermitemid | 权限项 | varchar | 50 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentityid | 业务对象 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fappid | 应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkperm_hd_funcsentry |  | fdetailid |
| 2 | idx_xkperm_hd_funcs_id |  | fentryid |

---

## 原数据规则方案-多选基础资料表 t_xkperm_hd_mulprdr

- **表名称：** 原数据规则方案-多选基础资料表
- **表名：** t_xkperm_hd_mulprdr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [数据规则方案 perm_datarule](../base_files/perm_datarule.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkperm_hd_mulprdr_id |  | fdetailid,fbasedataid |
| 2 | pk_xkperm_hd_mulprdr |  | fpkid |

---

## 权限交接-主表 t_xkperm_handover_bill

- **表名称：** 权限交接-主表
- **表名：** t_xkperm_handover_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fisadminuser | administrator分组 | bpchar | 1 |  | √ | ' ' | administrator分组 |
| 7 | ffromuserid | 姓名 | int8 | 64 |  | √ | 0 | [用户信息 bos_usergroup_user](../base_files/bos_usergroup_user.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | ftouserid | 姓名 | int8 | 64 |  | √ | 0 | [用户信息 bos_usergroup_user](../base_files/bos_usergroup_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fenable | 启用状态 | varchar | 50 |  | √ | ' ' | 启用状态,枚举: A :未启用 B :已启用 |
| 13 | fdesc | 备注 | varchar | 80 |  | √ | ' ' | 备注 |
| 14 | fissuperuser | 全功能用户 | bpchar | 1 |  | √ | ' ' | 全功能用户 |
| 15 | fbillno | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fhandoverstatus | 是否移交 | varchar | 50 |  | √ | ' ' | 是否移交,枚举: A :否 B :是 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkperm_handover_bill |  | fid |
| 2 | idx_handover_rouserid |  | ftouserid,ffromuserid |

---

## 权限数据规则-子表 t_xkperm_hd_drpermsentry

- **表名称：** 权限数据规则-子表
- **表名：** t_xkperm_hd_drpermsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fpermdrappid | 应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 2 | fpermdrjson | 数据规则方案内容 | varchar | 255 |  | √ | ' ' | 数据规则方案内容 |
| 3 | fpermdataruleid | 数据规则方案id | int8 | 64 |  | √ | 0 | 数据规则方案id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fdrpermitemid | 权限项 | varchar | 50 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fpermdrentityid | 业务对象 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 9 | fpermdrjson_tag | 数据规则方案内容_详情 | text | 0 |  |  | null | 数据规则方案内容_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkperm_hd_drpermsentry |  | fdetailid |
| 2 | idx_xkperm_hd_drpermsentry_id |  | fentryid |

---

## 字段方案子单据体-子表 t_xkperm_hd_feildssentry

- **表名称：** 字段方案子单据体-子表
- **表名：** t_xkperm_hd_feildssentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldschemeentityid | 业务对象 | varchar | 50 |  |  | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | ffieldschemeappid | 应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | ffieldschemeid | 方案名称 | varchar | 50 |  |  | ' ' | [属性/明细字段权限方案 perm_fieldscheme](../base_files/perm_fieldscheme.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkperm_hd_feildss_id |  | fentryid |
| 2 | pk_xkperm_hd_feildssentry |  | fdetailid |

---

## 原数据规则方案-多选基础资料表 t_xkperm_hd_mulpermdr

- **表名称：** 原数据规则方案-多选基础资料表
- **表名：** t_xkperm_hd_mulpermdr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [数据规则方案 perm_datarule](../base_files/perm_datarule.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkperm_hd_mulpermdr_id |  | fdetailid,fbasedataid |
| 2 | pk_xkperm_hd_mulpermdr |  | fpkid |

---

## 单据体-子表 t_xkperm_hd_roleentry

- **表名称：** 单据体-子表
- **表名：** t_xkperm_hd_roleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | froleid | 角色id | varchar | 50 |  | √ | ' ' | 角色id |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | frolenumber | 角色编码 | varchar | 80 |  | √ | ' ' | 角色编码 |
| 7 | frolename | 角色名称 | varchar | 80 |  | √ | ' ' | 角色名称 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkperm_hd_roleid |  | froleid |
| 2 | pk_xkperm_hd_roleentry |  | fentryid |
