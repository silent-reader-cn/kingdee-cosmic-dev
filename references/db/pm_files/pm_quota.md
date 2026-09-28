# 配额方案-pm_quota

## 配额方案-多语言表 t_pm_quota_l

- **表名称：** 配额方案-多语言表
- **表名：** t_pm_quota_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_quota_l_pkey |  | fpkid |
| 2 | idx_pm_quota_l_fid |  | fid,flocaleid |

---

## 配额明细-子表 t_pm_quotasubentry

- **表名称：** 配额明细-子表
- **表名：** t_pm_quotasubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fquotarate | 配额比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 配额比例(%) |
| 2 | fsubentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fsubentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsupplyrank | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 6 | fsubentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 10 | fsubentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_quotasubentry_fentryid |  | fentryid |
| 2 | t_pm_quotasubentry_pkey |  | fdetailid |

---

## 有效期-子表 t_pm_quotaentry

- **表名称：** 有效期-子表
- **表名：** t_pm_quotaentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 4 | fentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fexpirydate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 9 | fentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_quotaentry_pkey |  | fentryid |
| 2 | idx_pm_quotaentry_fid |  | fid |

---

## 配额方案-主表 t_pm_quota

- **表名称：** 配额方案-主表
- **表名：** t_pm_quota

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 适用物料 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fstartdayofweek | 起始日期 | varchar | 5 |  | √ | ' ' | 起始日期,枚举: A :周一 B :周二 C :周三 D :周四 E :周五 F :周六 G :周天 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fstartseasonfourdate | 第四季度 | timestamp | 0 |  |  | null | 第四季度 |
| 12 | fstartdayofmonth | 起始日期 | varchar | 5 |  | √ | ' ' | 起始日期,枚举: A :1号 B :2号 C :3号 D :4号 E :5号 F :6号 G :7号 H :8号 I :9号 J :10号 K :11号 L :12号 M :13号 N :14号 O :15号 P :16号 Q :17号 R :18号 S :19号 T :20号 U :21号 V :22号 W :23号 X :24号 Y :25号 Z :26号 AA :27号 AB :28号 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 15 | fstartotherdate | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fstartseasontwodate | 第二季度 | timestamp | 0 |  |  | null | 第二季度 |
| 19 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 21 | fstartyeardate | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 22 | fcalculatecycle | 计算周期 | varchar | 5 |  | √ | ' ' | 计算周期,枚举: A :日 B :周 C :月 D :季度 E :年 F :其他 |
| 23 | fstartdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 24 | fquotatype | 配额类型 | varchar | 5 |  | √ | ' ' | 配额类型,枚举: A :固定比例 B :最高比例 C :动态比例 |
| 25 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fstartseasonthreedate | 第三季度 | timestamp | 0 |  |  | null | 第三季度 |
| 27 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 28 | fstartseasononedate | 第一季度 | timestamp | 0 |  |  | null | 第一季度 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_quota_pkey |  | fid |
| 2 | idx_pm_quota_fnumber |  | fnumber |
