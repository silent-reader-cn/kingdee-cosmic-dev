# 供应商角色-scp_suprole

## 授权应用范围-多选基础资料表 t_perm_rolebizapps

- **表名称：** 授权应用范围-多选基础资料表
- **表名：** t_perm_rolebizapps

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_perm_rolebizapps |  | fpkid |
| 2 | idx_t_perm_rolebizapps_fid |  | fid |

---

## 供应商角色-主表 t_perm_role

- **表名称：** 供应商角色-主表
- **表名：** t_perm_role

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fgroupid | 通用角色分组 | varchar | 18 |  | √ | '0' | 通用角色分组 perm_rolegroup |
| 3 | fappusetype | 应用使用权类型 | varchar | 18 |  | √ | 'all' | 应用使用权类型,枚举: all :可以使用所有的表单记录 viewall :可以查看所有记录，只能编辑、删除自己录入的记录 own :可以使用自己录入的表单记录 custom :自定义 |
| 4 | fdimtypeid | 权限控制类型 | varchar | 18 |  | √ | ' ' | 权限控制类型 perm_ctrltype |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | varchar | 18 |  | √ | ' ' | 主数据内码 |
| 10 | fcreateadmingrp | 所属管理员组 | int8 | 64 |  | √ | 0 | 管理员分组 perm_admingroup |
| 11 | frolegroupid | frolegroupid | varchar | 18 |  | √ | '0' |  |
| 12 | fparentroleid | 父角色 | varchar | 18 |  | √ | ' ' | 通用角色 perm_role |
| 13 | fissystem | 系统预置 | bpchar | 1 |  | √ | '1' | 系统预置 |
| 14 | fappmanagetype | 应用管理权类型 | varchar | 18 |  | √ | 'all' | 应用管理权类型,枚举: all :拥有应用的全部管理权 none :无 |
| 15 | fremark | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 18 | fusescope | 公开状态 | bpchar | 1 |  | √ | '2' | 公开状态,枚举: 2 :公开 1 :分配 0 :私有 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | flongnumber | 长编码 | varchar | 1024 |  | √ | ' ' | 长编码 |
| 21 | fsortcode | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 22 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fbizdomainid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 24 | ftype | 适用用户类型 | varchar | 100 |  | √ | ' ' | 适用用户类型,枚举: |
| 25 | fissystemxk | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_role_pkey |  | fid |
| 2 | idx_perm_role |  | fnumber |

---

## 供应商角色-多语言表 t_perm_role_l

- **表名称：** 供应商角色-多语言表
- **表名：** t_perm_role_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' |  |
| 2 | fremark | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_role_l_pkey |  | fpkid |
| 2 | ix_perm_00000015 |  | fid,flocaleid |
