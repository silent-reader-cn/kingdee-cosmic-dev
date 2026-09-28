# 组织变更记录-bos_org_changerecord

## 组织变更记录-多语言表 t_org_changerecord_l

- **表名称：** 组织变更记录-多语言表
- **表名：** t_org_changerecord_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 职能类型 | varchar | 255 |  | √ | ' ' | 职能类型 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_org_changerecord_l |  | fpkid |
| 2 | idx_t_org_changerecord_l |  | fid,flocaleid |

---

## 变更详情-子表 t_org_changeentry

- **表名称：** 变更详情-子表
- **表名：** t_org_changeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foldparentorgid | 原上级组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fparentorgid | 上级组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fhandoverorgid | 交接组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | forgid | 组织名称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fdetailresult | 执行结果 | varchar | 255 |  | √ | ' ' | 执行结果 |
| 7 | fviewid | 视图方案 | int8 | 64 |  | √ | 0 | [组织视图方案 bos_org_viewschema](../base_files/bos_org_viewschema.md) |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fdetailstatus | 状态 | varchar | 30 |  | √ | 'A' | 状态,枚举: A :未执行 D :成功 F :失败 |
| 10 | fbizid | 职能类型 | int8 | 64 |  | √ | 0 | [组织职能类型 bos_org_biz](../base_files/bos_org_biz.md) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_org_changeentry |  | fentryid |
| 2 | idx_t_org_changeentry |  | fid,forgid,fviewid,fbizid |

---

## 检查报告-子表 t_org_changecheckentry

- **表名称：** 检查报告-子表
- **表名：** t_org_changecheckentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feventid | 订阅事件 | int8 | 64 |  | √ | 0 | [事件订阅 evt_subscription](../bec_files/evt_subscription.md) |
| 3 | fcheckresult | 检查情况 | varchar | 255 |  | √ | ' ' | 检查情况 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcheckstatus | 状态 | varchar | 30 |  | √ | 'A' | 状态,枚举: P :通过 W :警告 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_org_changecheckentry |  | fentryid |
| 2 | idx_t_org_changecheckentry |  | fid |

---

## 组织变更记录-主表 t_org_changerecord

- **表名称：** 组织变更记录-主表
- **表名：** t_org_changerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fexecutionstatus | 执行状态 | varchar | 30 |  | √ | 'A' | 执行状态,枚举: A :未执行 B :执行中 C :完成 E :异常 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fresult | 执行结果 | varchar | 255 |  | √ | ' ' | 执行结果 |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fchangetype | 变更类型 | varchar | 30 |  | √ | ' ' | 变更类型,枚举: resetroot :重置根组织 bizfreeze :职能封存 bizunfreeze :职能解封 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | ffailcount | 失败数量 | int4 | 32 |  | √ | 0 | 失败数量 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | fexecutiondate | 执行日期 | timestamp | 0 |  |  | null | 执行日期 |
| 17 | ftotalcount | 总数 | int4 | 32 |  | √ | 0 | 总数 |
| 18 | fsuccesscount | 成功数量 | int4 | 32 |  | √ | 0 | 成功数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_org_changerecord |  | fnumber,fchangetype,fexecutionstatus,fexecutiondate |
| 2 | pk_t_org_changerecord |  | fid |

---

## 子单据体-子表 t_org_changecheckdetail

- **表名称：** 子单据体-子表
- **表名：** t_org_changecheckdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 3 | freason | 错误原因 | varchar | 255 |  | √ | ' ' | 错误原因 |
| 4 | fentityid | 业务对象 | varchar | 30 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fbdnumber | 基础资料编码 | varchar | 255 |  | √ | ' ' | 基础资料编码 |
| 7 | fsolution | 解决方案 | varchar | 255 |  | √ | ' ' | 解决方案 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_org_changecheckdetail |  | fdetailid |
| 2 | idx_t_org_changecheckdetail |  | fentryid,fentityid,fbdnumber |
