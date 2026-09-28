# 流程管理员-wf_administrator

## 单据体-子表 t_wf_adminsentry

- **表名称：** 单据体-子表
- **表名：** t_wf_adminsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 管辖组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fincludesuborg | 接收其下级组织的异常消息 | bpchar | 1 |  | √ | '0' | 接收其下级组织的异常消息 |
| 6 | forgtype | 职能类型 | varchar | 50 |  | √ | ' ' | 职能类型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_adminsentry_pkey |  | fentryid |
| 2 | idx_wf_adminsentry_fid |  | fid |

---

## 流程管理员-主表 t_wf_admins

- **表名称：** 流程管理员-主表
- **表名：** t_wf_admins

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: global :全局 application :应用 process :流程 |
| 5 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fbusprocessid | 业务流程Id | int8 | 64 |  | √ | 0 | 流程管理 wf_processdefinition |
| 8 | fuserid | 人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fbusappid | 业务应用范围 | int8 | 64 |  | √ | 0 | 流程分类 wf_processcagetory |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_admins_pkey |  | fid |
| 2 | idx_wf_admins_forgid |  | forgid |
| 3 | idx_wf_admins_userid |  | fuserid,fstatus |

---

## 单据体-子表 t_wf_adminsappentry

- **表名称：** 单据体-子表
- **表名：** t_wf_adminsappentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbiztype | 业务云类型 | varchar | 50 |  | √ | ' ' | 业务云类型,枚举: |
| 3 | fappnumbers | 应用标识 | varchar | 500 |  | √ | ' ' | 应用标识 |
| 4 | fappnames | 管辖应用 | varchar | 500 |  | √ | ' ' | 管辖应用 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | freceivemsg | 接收本应用的异常信息 | bpchar | 1 |  | √ | '1' | 接收本应用的异常信息 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fappids | 应用id | varchar | 500 |  | √ | ' ' | 应用id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_adminsappentry |  | fid |
| 2 | pk_t_wf_adminsappentry |  | fentryid |
