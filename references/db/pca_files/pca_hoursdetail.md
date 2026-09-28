# 项目人员工时明细-pca_hoursdetail

## 单据体-多语言表 t_pca_hoursdetailentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_pca_hoursdetailentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | frolename | 项目角色 | varchar | 255 |  | √ | ' ' | 项目角色 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_hoursdetailentry_l |  | fpkid |
| 2 | idx_pca_hoursdetailentry_l_0 |  | fentryid,flocaleid |

---

## 单据体-子表 t_pca_hoursdetailentry

- **表名称：** 单据体-子表
- **表名：** t_pca_hoursdetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 汇报人组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsrcroleid | 项目角色id | int8 | 64 |  | √ | 0 | 项目角色id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fuserid | 姓名 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | freporttime | 汇报工时 | numeric | 23 | 10 | √ | 0 | 汇报工时 |
| 7 | frolename | 项目角色 | varchar | 255 |  | √ | ' ' | 项目角色 |
| 8 | ftaskstatusid | 任务状态 | int8 | 64 |  | √ | 0 | [状态类型 bd_statustype](../basedata_files/bd_statustype.md) |
| 9 | fdptid | 汇报人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fcostobjectid | 项目核算对象 | int8 | 64 |  | √ | 0 | [项目成本核算对象 pca_costobject](../pca_files/pca_costobject.md) |
| 11 | ftaskid | 任务名称 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | funit | 汇报单位 | varchar | 10 |  | √ | ' ' | 汇报单位,枚举: hour :小时 minute :分钟 second :秒 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_hoursdetailentry |  | fentryid |
| 2 | idx_hours_detail_entry |  | fid |

---

## 项目人员工时明细-主表 t_pca_hoursdetail

- **表名称：** 项目人员工时明细-主表
- **表名：** t_pca_hoursdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fsourcetype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: mpm :项目云 manual :手工录入 openapi :API录入 |
| 11 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 12 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_hours_detail |  | fcostaccountid,fperiodid |
| 2 | pk_pca_hoursdetail |  | fid |
