# 项目成员变更-src_projectman_chg

## 项目成员变更-主表 t_src_projectmanchg

- **表名称：** 项目成员变更-主表
- **表名：** t_src_projectmanchg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | 寻源项目变更F7 src_bidchangef7 |
| 3 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 4 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 5 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 9 | fprojectcreatorid | 项目创建人(变更前) | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fnewprojectcreatorid | 项目创建人(变更后) | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_projectmanchg_pid |  | fparentid |
| 2 | pk_src_projectmanchg |  | fid |

---

## 项目成员变更分录-子表 t_src_promanchgentry

- **表名称：** 项目成员变更分录-子表
- **表名：** t_src_promanchgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | 原单分录ID | varchar | 50 |  | √ | ' ' | 原单分录ID |
| 3 | fnewbidderid | 姓名(变更后) | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | 业务角色 pds_bizrole |
| 7 | fbidderid | 姓名(变更前) | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_promanchgentry_fid |  | fid |
| 2 | pk_src_promanchgentry |  | fentryid |
