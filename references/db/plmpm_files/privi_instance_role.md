# 权限配置-privi_instance_role

## 单据体-子表 t_prijroleinst_entrys

- **表名称：** 单据体-子表
- **表名：** t_prijroleinst_entrys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftextfield1 | 权限包描述 | varchar | 50 |  | √ | ' ' | 权限包描述 |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fprivi_items_id | 权限包ID | int8 | 64 |  | √ | 0 | 权限包ID |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fcheckboxfield |  | bpchar | 1 |  | √ | '0' |  |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | ftextfield | 权限包名称 | varchar | 50 |  | √ | ' ' | 权限包名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_prijroleinst_entrys |  | fentryid |
| 2 | idx_prijroleinst_entrys_fk |  | fid |

---

## 权限配置-主表 t_privi_inst_role

- **表名称：** 权限配置-主表
- **表名：** t_privi_inst_role

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | ftextfield | 当前角色 | varchar | 50 |  | √ | ' ' | 当前角色 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fprjrole_type | 角色类型 | int8 | 64 |  | √ | 0 | [项目角色 prjroletemplate](../plmpm_files/prjroletemplate.md) |
| 11 | fprj_number | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 12 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privi_inst_role |  | fid |
| 2 | idx_privi_inst_role_m0 |  | fbillno |
