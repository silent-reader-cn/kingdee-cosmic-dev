# 管控归档日志-bdctrl_archivelog

## 操作组织分录-子表 t_bdlog_archiveorgentry

- **表名称：** 操作组织分录-子表
- **表名：** t_bdlog_archiveorgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgentryid | forgentryid | int8 | 64 |  | √ | 0 | id |
| 3 | forgstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :成功 0 :失败 |
| 4 | forgid | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | forgnumber | 组织编码 | varchar | 30 |  | √ | ' ' | 组织编码 |
| 6 | forgname | 组织名称 | varchar | 50 |  | √ | ' ' | 组织名称 |
| 7 | fdetails | 详情 | varchar | 255 |  | √ | ' ' | 详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgentryid | forgentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bdlog_archiveorgentry |  | forgentryid |
| 2 | idx_bdlog_archiveorgentry_id |  | fid |

---

## 操作数据分录-子表 t_bdlog_archivedataentry

- **表名称：** 操作数据分录-子表
- **表名：** t_bdlog_archivedataentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fdatanumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 4 | fdataname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | ffailurecause | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 6 | fcreateorgname | 创建组织名称 | varchar | 255 |  | √ | ' ' | 创建组织名称 |
| 7 | fcreateorgnumber | 创建组织编码 | varchar | 50 |  | √ | ' ' | 创建组织编码 |
| 8 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 1 :逐级分配 2 :自由分配 5 :全局共享 6 :管控范围共享 7 :私有 |
| 9 | fdatastatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :成功 0 :失败 |
| 10 | fdataentryid | fdataentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fnewcreateorgname | 新创建组织名称 | varchar | 255 |  | √ | ' ' | 新创建组织名称 |
| 12 | fnewcreateorgid | 新创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fnewcreateorgnumber | 新创建组织编码 | varchar | 50 |  | √ | ' ' | 新创建组织编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataentryid | fdataentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdlog_archivedataentry_id |  | fid |
| 2 | pk_t_bdlog_archivedataentry |  | fdataentryid |

---

## 失败原因明细-子表 t_bdlog_archivefaildetail

- **表名称：** 失败原因明细-子表
- **表名：** t_bdlog_archivefaildetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgentryid | forgentryid | int8 | 64 |  | √ | 0 |  |
| 2 | ffaildatanumber | 数据编码 | varchar | 50 |  | √ | ' ' | 数据编码 |
| 3 | ffailcreateorgname | 创建组织名称 | varchar | 255 |  | √ | ' ' | 创建组织名称 |
| 4 | ffaildetailid | ffaildetailid | int8 | 64 |  | √ | 0 | id |
| 5 | ffailcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | forgfailurecause | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 7 | ffaildataname | 数据名称 | varchar | 255 |  | √ | ' ' | 数据名称 |
| 8 | ffailcreateorgnumber | 创建组织编码 | varchar | 50 |  | √ | ' ' | 创建组织编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ffaildetailid | ffaildetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdlog_archivefaildetail_id |  | forgentryid |
| 2 | pk_bdlog_archivefaildetail |  | ffaildetailid |

---

## 管控归档日志-主表 t_bdlog_archivelog

- **表名称：** 管控归档日志-主表
- **表名：** t_bdlog_archivelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatorgid | 操作组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | foperatorid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | foperattypename | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型 |
| 5 | fclienttype | 客户端类型 | varchar | 30 |  | √ | ' ' | 客户端类型,枚举: web :PC端 mobile :移动端 api :接口 |
| 6 | foperattypeid | 操作类型 | int8 | 64 |  | √ | 0 | 操作类型 bdlog_optype |
| 7 | foperattypenumber | 操作类型编码 | varchar | 30 |  | √ | ' ' | 操作类型编码 |
| 8 | foperatobj | 操作对象 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 9 | foperatinstruction | 操作说明 | varchar | 255 |  | √ | ' ' | 操作说明 |
| 10 | farchivetime | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 11 | foperatorgname | 操作组织名 | varchar | 50 |  | √ | ' ' | 操作组织名 |
| 12 | foperatorname | 操作人姓名 | varchar | 50 |  | √ | ' ' | 操作人姓名 |
| 13 | fclientip | 客户端IP地址 | varchar | 128 |  | √ | ' ' | 客户端IP地址 |
| 14 | foperatsource | 操作来源 | varchar | 30 |  | √ | ' ' | 操作来源,枚举: 0 :其他 1 :手工界面操作 2 :引入引出 3 :集成方案 4 :API调用 5 :自动分配 |
| 15 | foperatorgnumber | 操作组织编码 | varchar | 30 |  | √ | ' ' | 操作组织编码 |
| 16 | foperattime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 17 | ffrombackup | 是否归档还原而来 | bpchar | 1 |  | √ | '0' | 是否归档还原而来 |
| 18 | foperatobjname | 操作对象 | varchar | 50 |  | √ | ' ' | 操作对象 |
| 19 | foperatsourceid | 操作来源ID | int8 | 64 |  | √ | 0 | 操作来源ID |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | foperatornumber | 操作人工号 | varchar | 30 |  | √ | ' ' | 操作人工号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bdlog_archivelog |  | fid |
| 2 | idx_t_bdlog_archivelog_obj |  | foperatobj |
